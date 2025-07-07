import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

# Ensure project modules can be imported when running from any location
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# Create argument parser
parser = argparse.ArgumentParser(
    description="Capture raw external data during a stock analysis run"
)
parser.add_argument("stock_symbol", help="Stock symbol to analyze")
args = parser.parse_args()

symbol = args.stock_symbol

# Create output directory relative to the project root so results are stored in
# the repository regardless of the working directory.
output_dir = PROJECT_ROOT / "raw_data_output" / symbol
output_dir.mkdir(parents=True, exist_ok=True)
print(f"Starting data capture for symbol: {symbol}")
print(f"Output directory: {output_dir}/")

# Helper to save data
counter = {"count": 0}


def _save_data(name, data):
    idx = counter["count"]
    counter["count"] += 1
    filename = output_dir / f"{idx}_{name}"
    if isinstance(data, bytes):
        filename = filename.with_suffix(".bin")
        with open(filename, "wb") as f:
            f.write(data)
    elif hasattr(data, "to_csv"):
        filename = filename.with_suffix(".csv")
        data.to_csv(filename, index=False)
    elif isinstance(data, (list, dict)):
        filename = filename.with_suffix(".json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        filename = filename.with_suffix(".txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(data))
    print(f"Intercepted and saved {filename.name}")


# Patch requests to capture all HTTP responses
try:
    import requests

    orig_request = requests.sessions.Session.request

    def request_wrapper(self, method, url, *args, **kwargs):
        response = orig_request(self, method, url, *args, **kwargs)
        parsed = url.split("?")[0].replace("/", "_").replace(":", "_")
        name = f"http_{parsed[-50:]}"
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            _save_data(name + ".json", response.text)
        elif "text" in content_type or "html" in content_type:
            _save_data(name + ".txt", response.text)
        else:
            _save_data(name + ".bin", response.content)
        return response

    requests.sessions.Session.request = request_wrapper
except Exception:
    pass

# Patch Google News scraping function
try:
    from tradingagents.dataflows import googlenews_utils as gnews

    orig_gnews = gnews.getNewsData

    def gnews_wrapper(query, start_date, end_date):
        data = orig_gnews(query, start_date, end_date)
        _save_data("google_news", data)
        return data

    gnews.getNewsData = gnews_wrapper
except Exception:
    pass

# Patch realtime news aggregator methods
try:
    from tradingagents.dataflows.realtime_news_utils import (
        RealtimeNewsAggregator,
        NewsItem,
    )

    def wrap_realtime(method_name, file_tag):
        orig = getattr(RealtimeNewsAggregator, method_name)

        def wrapper(self, *a, **kw):
            data = orig(self, *a, **kw)
            try:
                items = [item.__dict__ for item in data]
            except Exception:
                items = data
            _save_data(file_tag, items)
            return data

        setattr(RealtimeNewsAggregator, method_name, wrapper)

    for m, tag in [
        ("_get_finnhub_realtime_news", "finnhub_realtime_news"),
        ("_get_alpha_vantage_news", "alpha_vantage_news"),
        ("_get_newsapi_news", "newsapi_news"),
        ("_get_chinese_finance_news", "chinese_finance_news"),
    ]:
        if hasattr(RealtimeNewsAggregator, m):
            wrap_realtime(m, tag)
except Exception:
    pass

# Patch YFinanceUtils methods
try:
    from tradingagents.dataflows.yfin_utils import YFinanceUtils
    import pandas as pd

    def wrap_yf(method_name, file_tag):
        orig = getattr(YFinanceUtils, method_name)

        def wrapper(self, *a, **kw):
            data = orig(self, *a, **kw)
            _save_data(file_tag, data)
            return data

        setattr(YFinanceUtils, method_name, wrapper)

    for m, tag in [
        ("get_stock_data", "yfinance_stock_data"),
        ("get_stock_info", "yfinance_stock_info"),
        ("get_company_info", "yfinance_company_info"),
        ("get_stock_dividends", "yfinance_dividends"),
        ("get_income_stmt", "yfinance_income_stmt"),
        ("get_balance_sheet", "yfinance_balance_sheet"),
        ("get_cash_flow", "yfinance_cashflow"),
        ("get_analyst_recommendations", "yfinance_recommendations"),
    ]:
        if hasattr(YFinanceUtils, m):
            wrap_yf(m, tag)
except Exception:
    pass

# Patch TDX utils
try:
    from tradingagents.dataflows import tdx_utils

    if hasattr(tdx_utils, "get_china_stock_data"):
        orig_china = tdx_utils.get_china_stock_data

        def china_wrapper(*a, **kw):
            data = orig_china(*a, **kw)
            _save_data("tdx_china_stock_data", data)
            return data

        tdx_utils.get_china_stock_data = china_wrapper
except Exception:
    pass

# Run analysis
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()

graph = TradingAgentsGraph(debug=False, config=config)

trade_date = datetime.now().strftime("%Y-%m-%d")
try:
    graph.propagate(symbol, trade_date)
except Exception as e:
    print(f"Analysis run encountered an error: {e}")

print("Data capture complete.")
