import os
import json
from datetime import datetime
from functools import wraps
import argparse

import pandas as pd
from dataclasses import asdict, is_dataclass

# Import modules to patch
from tradingagents.dataflows import googlenews_utils
from tradingagents.dataflows.realtime_news_utils import RealtimeNewsAggregator
from tradingagents.dataflows.tdx_utils import TongDaXinDataProvider
from tradingagents.dataflows.yfin_utils import YFinanceUtils
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG


def main():
    parser = argparse.ArgumentParser(
        description="Capture raw external data for a stock analysis"
    )
    parser.add_argument("stock_symbol", help="Stock symbol to analyze")
    args = parser.parse_args()
    symbol = args.stock_symbol

    output_dir = os.path.join(
        "raw_data_output", symbol, datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    os.makedirs(output_dir, exist_ok=True)

    print(f"Starting data capture for symbol: {symbol}")
    print(f"Output directory: {output_dir}")

    def save_data(data, filename):
        path = os.path.join(output_dir, filename)
        if isinstance(data, pd.DataFrame):
            data.to_csv(path, index=False)
        elif isinstance(data, list) and len(data) > 0 and is_dataclass(data[0]):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(
                    [asdict(d) for d in data],
                    f,
                    ensure_ascii=False,
                    indent=2,
                    default=str,
                )
        elif is_dataclass(data):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(asdict(data), f, ensure_ascii=False, indent=2, default=str)
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"Intercepted and saved {filename}")

    def capture(func, filename):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            try:
                save_data(data, filename)
            except Exception as e:
                print(f"Failed to save {filename}: {e}")
            return data

        return wrapper

    # Patch google news
    googlenews_utils.getNewsData = capture(
        googlenews_utils.getNewsData, "google_news.json"
    )

    # Patch realtime news aggregator methods
    RealtimeNewsAggregator._get_finnhub_realtime_news = capture(
        RealtimeNewsAggregator._get_finnhub_realtime_news,
        "finnhub_realtime_news.json",
    )
    RealtimeNewsAggregator._get_alpha_vantage_news = capture(
        RealtimeNewsAggregator._get_alpha_vantage_news,
        "alpha_vantage_news.json",
    )
    RealtimeNewsAggregator._get_newsapi_news = capture(
        RealtimeNewsAggregator._get_newsapi_news,
        "newsapi_news.json",
    )
    RealtimeNewsAggregator._get_chinese_finance_news = capture(
        RealtimeNewsAggregator._get_chinese_finance_news,
        "chinese_finance_news.json",
    )

    # Patch TongDaXin provider methods
    TongDaXinDataProvider.get_real_time_data = capture(
        TongDaXinDataProvider.get_real_time_data,
        "pytdx_real_time.json",
    )
    TongDaXinDataProvider.get_stock_history_data = capture(
        TongDaXinDataProvider.get_stock_history_data,
        "pytdx_historical_klines.csv",
    )
    TongDaXinDataProvider.get_stock_technical_indicators = capture(
        TongDaXinDataProvider.get_stock_technical_indicators,
        "pytdx_technical_indicators.json",
    )

    # Patch yfinance utils
    YFinanceUtils.get_stock_data = capture(
        YFinanceUtils.get_stock_data,
        "yfinance_stock_data.csv",
    )
    YFinanceUtils.get_stock_info = capture(
        YFinanceUtils.get_stock_info,
        "yfinance_stock_info.json",
    )
    YFinanceUtils.get_company_info = capture(
        YFinanceUtils.get_company_info,
        "yfinance_company_info.csv",
    )

    # Run analysis
    config = DEFAULT_CONFIG.copy()
    ta = TradingAgentsGraph(debug=False, config=config)
    analysis_date = datetime.now().strftime("%Y-%m-%d")
    try:
        ta.propagate(symbol, analysis_date)
    except Exception as e:
        print(f"Error during analysis: {e}")

    print("Data capture complete.")


if __name__ == "__main__":
    main()
