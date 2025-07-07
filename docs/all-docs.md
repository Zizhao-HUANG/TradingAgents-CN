# TradingAgents Documentation Combined

<!-- docs/README.md -->

# TradingAgents 文档 (v0.1.4)

欢迎来到 TradingAgents 多智能体金融交易框架的文档中心。本文档适用于中文增强版 v0.1.4，包含完整的A股支持、国产LLM集成和Web界面功能。

## 文档结构

### 📋 概览文档
- [项目概述](./overview/project-overview.md) - 项目的基本介绍和目标
- [快速开始](./overview/quick-start.md) - 快速上手指南
- [安装指南](./overview/installation.md) - 详细的安装说明

### 🏗️ 架构文档
- [系统架构](./architecture/system-architecture.md) - 整体系统架构设计
- [智能体架构](./architecture/agent-architecture.md) - 智能体设计模式
- [数据流架构](./architecture/data-flow-architecture.md) - 数据处理流程
- [图结构设计](./architecture/graph-structure.md) - LangGraph 图结构设计
- [配置优化指南](./architecture/configuration-optimization.md) - v0.1.4架构优化详解 ✨

### 🤖 智能体文档
- [分析师团队](./agents/analysts.md) - 各类分析师智能体详解
- [研究员团队](./agents/researchers.md) - 研究员智能体设计
- [交易员](./agents/trader.md) - 交易决策智能体
- [风险管理](./agents/risk-management.md) - 风险管理智能体
- [管理层](./agents/managers.md) - 管理层智能体

### 📊 数据处理
- [数据源集成](./data/data-sources.md) - 支持的数据源和API (含A股支持) ✨
- [通达信API集成](./data/tongdaxin-api-integration.md) - A股数据源详解 ✨
- [数据处理流程](./data/data-processing.md) - 数据获取和处理
- [缓存机制](./data/caching.md) - 数据缓存策略

### ⚙️ 配置与部署
- [配置说明](./configuration/config-guide.md) - 配置文件详解
- [LLM配置](./configuration/llm-config.md) - 大语言模型配置
- [Google AI配置](./configuration/google-ai-setup.md) - Google AI (Gemini)模型配置指南 ✨
- [Web界面配置](../web/README.md) - Web管理界面使用指南 ✨
- [部署指南](./deployment/deployment-guide.md) - 生产环境部署

### 🔧 开发指南
- [开发环境搭建](./development/dev-setup.md) - 开发环境配置
- [代码结构](./development/code-structure.md) - 代码组织结构
- [扩展开发](./development/extending.md) - 如何扩展框架
- [测试指南](./development/testing.md) - 测试策略和方法

### 📚 API参考
- [核心API](./api/core-api.md) - 核心类和方法
- [智能体API](./api/agents-api.md) - 智能体接口
- [数据API](./api/data-api.md) - 数据处理接口

### 🌐 使用指南
- [Web界面指南](./usage/web-interface-guide.md) - Web界面详细使用指南 ✨
- [投资分析指南](./usage/investment_analysis_guide.md) - 投资分析完整流程
- [A股分析指南](./guides/a-share-analysis-guide.md) - A股市场分析专项指南 ✨

### 💡 示例和教程
- [基础示例](./examples/basic-examples.md) - 基本使用示例
- [高级示例](./examples/advanced-examples.md) - 高级功能示例
- [自定义智能体](./examples/custom-agents.md) - 创建自定义智能体

### ❓ 常见问题
- [FAQ](./faq/faq.md) - 常见问题解答
- [故障排除](./faq/troubleshooting.md) - 问题诊断和解决

## 贡献指南

如果您想为文档做出贡献，请参考 [贡献指南](../CONTRIBUTING.md)。

## 联系我们

- GitHub: [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Discord: [TradingResearch](https://discord.com/invite/hk9PGKShPK)
- 微信: TauricResearch
- Twitter: [@TauricResearch](https://x.com/TauricResearch)


<!-- docs/STRUCTURE.md -->

# 文档目录结构

```
docs/
├── README.md                           # 文档主页和导航
├── STRUCTURE.md                        # 本文件 - 文档结构说明
│
├── overview/                           # 📋 概览文档
│   ├── project-overview.md            # ✅ 项目概述
│   ├── quick-start.md                 # ✅ 快速开始指南
│   └── installation.md                # 🔄 详细安装说明
│
├── architecture/                      # 🏗️ 架构文档
│   ├── system-architecture.md         # ✅ 系统架构设计
│   ├── agent-architecture.md          # ✅ 智能体架构设计
│   ├── data-flow-architecture.md      # ✅ 数据流架构
│   └── graph-structure.md             # ✅ LangGraph 图结构设计
│
├── agents/                            # 🤖 智能体文档
│   ├── analysts.md                    # ✅ 分析师团队详解
│   ├── researchers.md                 # 🔄 研究员团队设计
│   ├── trader.md                      # 🔄 交易员智能体
│   ├── risk-management.md             # 🔄 风险管理智能体
│   └── managers.md                    # 🔄 管理层智能体
│
├── data/                              # 📊 数据处理文档
│   ├── data-sources.md                # 🔄 支持的数据源和API
│   ├── data-processing.md             # 🔄 数据获取和处理
│   └── caching.md                     # 🔄 数据缓存策略
│
├── configuration/                     # ⚙️ 配置与部署
│   ├── config-guide.md               # 🔄 配置文件详解
│   └── llm-config.md                 # 🔄 大语言模型配置
│
├── deployment/                        # 🚀 部署文档
│   └── deployment-guide.md           # 🔄 生产环境部署
│
├── development/                       # 🔧 开发指南
│   ├── dev-setup.md                  # 🔄 开发环境搭建
│   ├── code-structure.md             # 🔄 代码组织结构
│   ├── extending.md                  # 🔄 如何扩展框架
│   └── testing.md                    # 🔄 测试策略和方法
│
├── api/                               # 📚 API参考
│   ├── core-api.md                   # 🔄 核心类和方法
│   ├── agents-api.md                 # 🔄 智能体接口
│   └── data-api.md                   # 🔄 数据处理接口
│
├── examples/                          # 💡 示例和教程
│   ├── basic-examples.md             # 🔄 基本使用示例
│   ├── advanced-examples.md          # 🔄 高级功能示例
│   └── custom-agents.md              # 🔄 创建自定义智能体
│
└── faq/                               # ❓ 常见问题
    ├── faq.md                         # 🔄 常见问题解答
    └── troubleshooting.md             # 🔄 问题诊断和解决
```

## 图例说明

- ✅ **已完成**: 文档已创建并包含完整内容
- 🔄 **待完成**: 文档结构已规划，内容待补充
- 📋 **概览类**: 项目介绍和快速上手
- 🏗️ **架构类**: 系统设计和技术架构
- 🤖 **智能体类**: 各类智能体的详细说明
- 📊 **数据类**: 数据处理和管理
- ⚙️ **配置类**: 系统配置和设置
- 🚀 **部署类**: 部署和运维
- 🔧 **开发类**: 开发和扩展指南
- 📚 **API类**: 接口和方法参考
- 💡 **示例类**: 使用示例和教程
- ❓ **帮助类**: 问题解答和故障排除

## 文档编写规范

### 1. 文件命名
- 使用小写字母和连字符
- 文件名应简洁明了，体现内容主题
- 使用 `.md` 扩展名

### 2. 内容结构
- 每个文档都应包含清晰的标题层次
- 使用适当的Markdown语法
- 包含代码示例和图表说明
- 提供相关链接和参考

### 3. 代码示例
- 提供完整可运行的代码示例
- 包含必要的注释和说明
- 使用一致的代码风格
- 提供预期的输出结果

### 4. 图表和图像
- 使用Mermaid图表展示架构和流程
- 图片应存储在适当的目录中
- 提供图表的文字描述
- 确保图表在不同设备上的可读性

## 维护指南

### 1. 定期更新
- 随着代码更新同步更新文档
- 定期检查链接的有效性
- 更新过时的信息和示例

### 2. 质量控制
- 确保文档的准确性和完整性
- 检查语法和拼写错误
- 验证代码示例的可执行性

### 3. 用户反馈
- 收集用户对文档的反馈
- 根据常见问题完善文档
- 持续改进文档的可读性

## 贡献指南

### 如何贡献文档

1. **Fork 项目**: 在GitHub上fork TradingAgents项目
2. **创建分支**: 为文档更新创建新分支
3. **编写文档**: 按照规范编写或更新文档
4. **提交PR**: 提交Pull Request并描述更改内容
5. **代码审查**: 等待维护者审查和合并

### 文档贡献类型

- **新增文档**: 创建缺失的文档内容
- **内容完善**: 补充现有文档的详细信息
- **错误修正**: 修复文档中的错误和过时信息
- **示例补充**: 添加更多使用示例和教程
- **翻译工作**: 将文档翻译成其他语言

### 贡献者认可

我们会在文档中认可所有贡献者的工作，包括：
- 在README中列出贡献者
- 在相关文档中标注作者信息
- 在发布说明中感谢贡献者

## 联系方式

如果您对文档有任何建议或问题，请通过以下方式联系我们：

- **GitHub Issues**: [提交文档相关问题](https://github.com/TauricResearch/TradingAgents/issues)
- **Discord**: [加入讨论](https://discord.com/invite/hk9PGKShPK)
- **邮箱**: docs@tauric.ai

感谢您对TradingAgents文档建设的关注和支持！


<!-- docs/agents/analysts.md -->

# 分析师团队详解

## 概述

分析师团队是 TradingAgents 框架的核心组成部分，负责从不同维度分析市场数据。每个分析师都专注于特定的分析领域，通过专业化分工确保分析的深度和准确性。

## 分析师架构

### 基础分析师类

```python
class BaseAnalyst:
    """所有分析师的基础类"""
    
    def __init__(self, llm, config, tools=None):
        self.llm = llm
        self.config = config
        self.tools = tools or []
        self.memory = AnalystMemory()
        
    def analyze(self, state: AgentState) -> Dict[str, Any]:
        """执行分析的主要方法"""
        
        # 1. 数据预处理
        processed_data = self.preprocess_data(state)
        
        # 2. 执行专业分析
        analysis_result = self.perform_analysis(processed_data)
        
        # 3. 生成分析报告
        report = self.generate_report(analysis_result)
        
        # 4. 更新记忆
        self.memory.update(state.ticker, report)
        
        return report
    
    def preprocess_data(self, state: AgentState) -> Dict:
        """数据预处理 - 子类可重写"""
        return state
    
    def perform_analysis(self, data: Dict) -> Dict:
        """执行分析 - 子类必须实现"""
        raise NotImplementedError
    
    def generate_report(self, analysis: Dict) -> Dict:
        """生成分析报告 - 子类可重写"""
        return analysis
```

## 1. 基本面分析师 (Fundamentals Analyst)

### 职责与功能
```python
class FundamentalsAnalyst(BaseAnalyst):
    """基本面分析师 - 专注于公司财务和基本面分析"""
    
    专业领域:
    - 财务报表分析
    - 估值模型计算
    - 行业对比分析
    - 盈利能力评估
    - 财务健康度评估
    
    分析维度:
    - 收入增长率
    - 利润率趋势
    - 资产负债比率
    - 现金流状况
    - ROE/ROA 指标
    - P/E, P/B 估值比率
```

### 核心分析方法
```python
def perform_analysis(self, data: Dict) -> Dict:
    """执行基本面分析"""
    
    financial_data = data.get("financial_data", {})
    company_info = data.get("company_info", {})
    
    analysis = {
        "financial_health": self._assess_financial_health(financial_data),
        "valuation": self._calculate_valuation(financial_data),
        "growth_analysis": self._analyze_growth(financial_data),
        "profitability": self._assess_profitability(financial_data),
        "liquidity": self._assess_liquidity(financial_data),
        "leverage": self._assess_leverage(financial_data)
    }
    
    # 综合评分
    analysis["overall_score"] = self._calculate_overall_score(analysis)
    analysis["recommendation"] = self._generate_recommendation(analysis)
    
    return analysis

def _assess_financial_health(self, financial_data: Dict) -> Dict:
    """评估财务健康度"""
    
    # 计算关键财务比率
    current_ratio = financial_data.get("current_assets", 0) / max(
        financial_data.get("current_liabilities", 1), 1
    )
    
    debt_to_equity = financial_data.get("total_debt", 0) / max(
        financial_data.get("shareholders_equity", 1), 1
    )
    
    # 评估财务健康度
    health_score = 0
    if current_ratio > 1.5:
        health_score += 0.3
    if debt_to_equity < 0.5:
        health_score += 0.3
    
    return {
        "current_ratio": current_ratio,
        "debt_to_equity": debt_to_equity,
        "health_score": health_score,
        "assessment": "Strong" if health_score > 0.5 else "Weak"
    }
```

### 分析工具
```python
分析工具集:
- DCF估值模型
- 比较估值法
- 财务比率分析
- 行业基准对比
- 盈利质量评估
- 现金流分析

数据源:
- 财务报表数据
- 行业平均数据
- 宏观经济指标
- 同行业公司数据
```

## 2. 技术分析师 (Market/Technical Analyst)

### 职责与功能
```python
class MarketAnalyst(BaseAnalyst):
    """技术分析师 - 专注于技术指标和价格趋势分析"""
    
    专业领域:
    - 技术指标计算
    - 趋势识别
    - 支撑阻力位分析
    - 交易信号生成
    - 市场情绪分析
    
    技术指标:
    - 移动平均线 (MA, EMA)
    - 相对强弱指数 (RSI)
    - MACD 指标
    - 布林带 (Bollinger Bands)
    - 成交量指标
    - 动量指标
```

### 核心分析方法
```python
def perform_analysis(self, data: Dict) -> Dict:
    """执行技术分析"""
    
    price_data = data.get("price_data", {})
    volume_data = data.get("volume_data", {})
    
    # 计算技术指标
    indicators = self._calculate_indicators(price_data, volume_data)
    
    # 趋势分析
    trend_analysis = self._analyze_trend(price_data, indicators)
    
    # 支撑阻力位
    support_resistance = self._find_support_resistance(price_data)
    
    # 交易信号
    signals = self._generate_signals(indicators, trend_analysis)
    
    analysis = {
        "indicators": indicators,
        "trend": trend_analysis,
        "support_resistance": support_resistance,
        "signals": signals,
        "momentum": self._assess_momentum(indicators),
        "volatility": self._assess_volatility(price_data)
    }
    
    # 综合技术评分
    analysis["technical_score"] = self._calculate_technical_score(analysis)
    analysis["recommendation"] = self._generate_technical_recommendation(analysis)
    
    return analysis

def _calculate_indicators(self, price_data: Dict, volume_data: Dict) -> Dict:
    """计算技术指标"""
    
    prices = price_data.get("close", [])
    volumes = volume_data.get("volume", [])
    
    indicators = {}
    
    # RSI 计算
    indicators["rsi"] = self._calculate_rsi(prices)
    
    # MACD 计算
    indicators["macd"] = self._calculate_macd(prices)
    
    # 移动平均线
    indicators["ma_20"] = self._calculate_ma(prices, 20)
    indicators["ma_50"] = self._calculate_ma(prices, 50)
    
    # 布林带
    indicators["bollinger"] = self._calculate_bollinger_bands(prices)
    
    # 成交量指标
    indicators["volume_ma"] = self._calculate_ma(volumes, 20)
    
    return indicators
```

### 信号生成
```python
def _generate_signals(self, indicators: Dict, trend: Dict) -> Dict:
    """生成交易信号"""
    
    signals = {
        "buy_signals": [],
        "sell_signals": [],
        "neutral_signals": []
    }
    
    # RSI 信号
    rsi = indicators.get("rsi", 50)
    if rsi < 30:
        signals["buy_signals"].append("RSI超卖")
    elif rsi > 70:
        signals["sell_signals"].append("RSI超买")
    
    # MACD 信号
    macd = indicators.get("macd", {})
    if macd.get("signal") == "bullish_crossover":
        signals["buy_signals"].append("MACD金叉")
    elif macd.get("signal") == "bearish_crossover":
        signals["sell_signals"].append("MACD死叉")
    
    # 趋势信号
    if trend.get("direction") == "uptrend":
        signals["buy_signals"].append("上升趋势")
    elif trend.get("direction") == "downtrend":
        signals["sell_signals"].append("下降趋势")
    
    return signals
```

## 3. 新闻分析师 (News Analyst)

### 职责与功能
```python
class NewsAnalyst(BaseAnalyst):
    """新闻分析师 - 专注于新闻事件和宏观因素分析"""
    
    专业领域:
    - 新闻情感分析
    - 事件影响评估
    - 宏观经济分析
    - 政策影响分析
    - 行业动态分析
    
    分析维度:
    - 新闻情感极性
    - 事件重要性评级
    - 影响时间范围
    - 市场反应预期
    - 风险因素识别
```

### 核心分析方法
```python
def perform_analysis(self, data: Dict) -> Dict:
    """执行新闻分析"""
    
    news_data = data.get("news_data", [])
    economic_data = data.get("economic_data", {})
    
    analysis = {
        "sentiment_analysis": self._analyze_sentiment(news_data),
        "event_impact": self._assess_event_impact(news_data),
        "macro_analysis": self._analyze_macro_factors(economic_data),
        "risk_factors": self._identify_risk_factors(news_data),
        "catalysts": self._identify_catalysts(news_data)
    }
    
    # 综合新闻评分
    analysis["news_score"] = self._calculate_news_score(analysis)
    analysis["market_impact"] = self._assess_market_impact(analysis)
    
    return analysis

def _analyze_sentiment(self, news_data: List[Dict]) -> Dict:
    """分析新闻情感"""
    
    sentiments = []
    weighted_sentiment = 0
    total_weight = 0
    
    for news in news_data:
        # 计算单条新闻情感
        sentiment = self._calculate_news_sentiment(news["content"])
        importance = news.get("importance", 1.0)
        
        sentiments.append({
            "title": news["title"],
            "sentiment": sentiment,
            "importance": importance,
            "source": news.get("source", "Unknown")
        })
        
        # 加权平均
        weighted_sentiment += sentiment * importance
        total_weight += importance
    
    overall_sentiment = weighted_sentiment / max(total_weight, 1)
    
    return {
        "individual_sentiments": sentiments,
        "overall_sentiment": overall_sentiment,
        "sentiment_distribution": self._calculate_sentiment_distribution(sentiments),
        "confidence": self._calculate_sentiment_confidence(sentiments)
    }
```

### 事件影响评估
```python
def _assess_event_impact(self, news_data: List[Dict]) -> Dict:
    """评估事件影响"""
    
    impact_assessment = {
        "high_impact_events": [],
        "medium_impact_events": [],
        "low_impact_events": []
    }
    
    for news in news_data:
        impact_score = self._calculate_impact_score(news)
        
        event_info = {
            "title": news["title"],
            "impact_score": impact_score,
            "time_horizon": self._estimate_time_horizon(news),
            "affected_sectors": self._identify_affected_sectors(news)
        }
        
        if impact_score > 0.7:
            impact_assessment["high_impact_events"].append(event_info)
        elif impact_score > 0.4:
            impact_assessment["medium_impact_events"].append(event_info)
        else:
            impact_assessment["low_impact_events"].append(event_info)
    
    return impact_assessment
```

## 4. 社交媒体分析师 (Social Media Analyst)

### 职责与功能
```python
class SocialMediaAnalyst(BaseAnalyst):
    """社交媒体分析师 - 专注于社交媒体情绪和舆论分析"""
    
    专业领域:
    - 社交媒体情感分析
    - 舆论趋势监测
    - 热点话题识别
    - 投资者情绪评估
    - 病毒式传播分析
    
    数据源:
    - Reddit 讨论
    - Twitter 情感
    - 投资论坛
    - 新闻评论
    - 社交媒体提及
```

### 核心分析方法
```python
def perform_analysis(self, data: Dict) -> Dict:
    """执行社交媒体分析"""
    
    social_data = data.get("social_data", {})
    
    analysis = {
        "sentiment_trends": self._analyze_sentiment_trends(social_data),
        "discussion_volume": self._analyze_discussion_volume(social_data),
        "key_topics": self._extract_key_topics(social_data),
        "influencer_sentiment": self._analyze_influencer_sentiment(social_data),
        "viral_content": self._identify_viral_content(social_data)
    }
    
    # 综合社交媒体评分
    analysis["social_score"] = self._calculate_social_score(analysis)
    analysis["crowd_sentiment"] = self._assess_crowd_sentiment(analysis)
    
    return analysis

def _analyze_sentiment_trends(self, social_data: Dict) -> Dict:
    """分析情感趋势"""
    
    reddit_data = social_data.get("reddit", [])
    twitter_data = social_data.get("twitter", [])
    
    # 时间序列情感分析
    sentiment_timeline = self._build_sentiment_timeline(reddit_data, twitter_data)
    
    # 趋势检测
    trend_direction = self._detect_sentiment_trend(sentiment_timeline)
    
    return {
        "timeline": sentiment_timeline,
        "trend_direction": trend_direction,
        "momentum": self._calculate_sentiment_momentum(sentiment_timeline),
        "volatility": self._calculate_sentiment_volatility(sentiment_timeline)
    }
```

## 分析师协作机制

### 1. 分析结果整合
```python
class AnalysisIntegrator:
    """分析结果整合器"""
    
    def integrate_analyses(self, analyst_reports: Dict) -> Dict:
        """整合所有分析师的报告"""
        
        integrated = {
            "fundamental_score": analyst_reports.get("fundamentals", {}).get("overall_score", 0.5),
            "technical_score": analyst_reports.get("technical", {}).get("technical_score", 0.5),
            "news_score": analyst_reports.get("news", {}).get("news_score", 0.5),
            "social_score": analyst_reports.get("social", {}).get("social_score", 0.5)
        }
        
        # 加权综合评分
        weights = self.config.get("analyst_weights", {
            "fundamentals": 0.3,
            "technical": 0.3,
            "news": 0.2,
            "social": 0.2
        })
        
        integrated["composite_score"] = sum(
            integrated[f"{analyst}_score"] * weights[analyst]
            for analyst in weights.keys()
        )
        
        # 一致性分析
        integrated["consensus_level"] = self._calculate_consensus(integrated)
        
        return integrated
```

### 2. 质量控制
```python
class AnalysisQualityControl:
    """分析质量控制"""
    
    def validate_analysis(self, analysis: Dict, analyst_type: str) -> Tuple[bool, List[str]]:
        """验证分析质量"""
        
        errors = []
        
        # 检查必需字段
        required_fields = self._get_required_fields(analyst_type)
        for field in required_fields:
            if field not in analysis:
                errors.append(f"Missing required field: {field}")
        
        # 检查数值范围
        if not self._validate_score_ranges(analysis):
            errors.append("Score values out of valid range")
        
        # 检查逻辑一致性
        if not self._validate_logical_consistency(analysis):
            errors.append("Logical inconsistency detected")
        
        return len(errors) == 0, errors
```

分析师团队通过专业化分工和协作机制，为交易决策提供全面、准确的市场分析，是整个 TradingAgents 系统的重要基础。


<!-- docs/agents/managers.md -->

# 管理层智能体

## 概述

管理层智能体是 TradingAgents 框架的协调和决策中枢，负责统筹各个专业团队的工作，确保整个投资决策流程的有序进行。管理层包括研究经理和风险经理，分别负责研究活动的协调和风险管理的统筹。

## 管理层架构

### 管理层体系设计

```python
class ManagementLayer:
    """管理层系统 - 统筹协调各专业团队"""
    
    def __init__(self, config):
        self.config = config
        self.research_manager = ResearchManager(config)
        self.risk_manager = RiskManager(config)
        self.decision_coordinator = DecisionCoordinator(config)
        
    def orchestrate_decision_process(self, analysis_data: Dict) -> Dict:
        """协调整个决策流程"""
        
        # 1. 研究阶段管理
        research_results = self.research_manager.manage_research_process(analysis_data)
        
        # 2. 风险评估管理
        risk_assessment = self.risk_manager.manage_risk_assessment(
            research_results, analysis_data
        )
        
        # 3. 决策协调
        final_decision = self.decision_coordinator.coordinate_final_decision(
            research_results, risk_assessment
        )
        
        # 4. 质量控制
        quality_check = self._conduct_quality_control(final_decision)
        
        return {
            "research_results": research_results,
            "risk_assessment": risk_assessment,
            "final_decision": final_decision,
            "quality_check": quality_check,
            "management_approval": self._provide_management_approval(final_decision, quality_check)
        }
```

## 1. 研究经理 (Research Manager)

### 职责与功能
```python
class ResearchManager:
    """研究经理 - 协调和管理研究活动"""
    
    def __init__(self, config):
        self.config = config
        self.research_standards = ResearchStandards()
        self.quality_controller = ResearchQualityController()
        self.debate_moderator = DebateModerator()
        
    核心职责:
    - 协调分析师和研究员工作
    - 主持研究员辩论
    - 确保研究质量
    - 形成研究共识
    - 管理研究流程
    
    管理范围:
    - 分析师团队协调
    - 研究员辩论管理
    - 研究质量控制
    - 共识形成机制
    - 研究效率优化
```

### 研究流程管理
```python
def manage_research_process(self, analysis_data: Dict) -> Dict:
    """管理研究流程"""
    
    # 1. 分析师工作协调
    analyst_coordination = self._coordinate_analyst_work(analysis_data)
    
    # 2. 分析质量检查
    analysis_quality = self._check_analysis_quality(analyst_coordination)
    
    # 3. 研究员辩论管理
    debate_results = self._manage_researcher_debate(analyst_coordination)
    
    # 4. 共识形成
    research_consensus = self._facilitate_consensus_formation(debate_results)
    
    # 5. 研究报告生成
    research_report = self._generate_research_report(
        analyst_coordination, debate_results, research_consensus
    )
    
    return {
        "analyst_coordination": analyst_coordination,
        "analysis_quality": analysis_quality,
        "debate_results": debate_results,
        "research_consensus": research_consensus,
        "research_report": research_report,
        "research_confidence": self._assess_research_confidence(research_consensus)
    }

def _coordinate_analyst_work(self, analysis_data: Dict) -> Dict:
    """协调分析师工作"""
    
    analyst_reports = analysis_data.get("analyst_reports", {})
    
    coordination_results = {
        "coverage_completeness": self._assess_coverage_completeness(analyst_reports),
        "analysis_consistency": self._check_analysis_consistency(analyst_reports),
        "data_quality": self._evaluate_data_quality(analyst_reports),
        "methodology_alignment": self._check_methodology_alignment(analyst_reports)
    }
    
    # 识别需要补充的分析
    missing_analysis = self._identify_missing_analysis(analyst_reports)
    
    # 协调补充分析
    if missing_analysis:
        coordination_results["supplementary_analysis"] = self._request_supplementary_analysis(
            missing_analysis
        )
    
    # 分析师工作评估
    coordination_results["analyst_performance"] = self._evaluate_analyst_performance(
        analyst_reports
    )
    
    return coordination_results

def _manage_researcher_debate(self, analyst_coordination: Dict) -> Dict:
    """管理研究员辩论"""
    
    # 设置辩论议题
    debate_agenda = self._set_debate_agenda(analyst_coordination)
    
    # 分配辩论角色
    debate_roles = self._assign_debate_roles()
    
    # 主持辩论过程
    debate_process = self._moderate_debate_process(debate_agenda, debate_roles)
    
    # 评估辩论质量
    debate_quality = self._assess_debate_quality(debate_process)
    
    # 提取关键争议点
    key_disagreements = self._extract_key_disagreements(debate_process)
    
    return {
        "debate_agenda": debate_agenda,
        "debate_roles": debate_roles,
        "debate_process": debate_process,
        "debate_quality": debate_quality,
        "key_disagreements": key_disagreements,
        "debate_effectiveness": self._measure_debate_effectiveness(debate_process)
    }

def _facilitate_consensus_formation(self, debate_results: Dict) -> Dict:
    """促进共识形成"""
    
    # 分析辩论结果
    debate_analysis = self._analyze_debate_outcomes(debate_results)
    
    # 识别共同点
    common_ground = self._identify_common_ground(debate_analysis)
    
    # 调解分歧
    mediated_disagreements = self._mediate_disagreements(
        debate_results["key_disagreements"]
    )
    
    # 权衡不同观点
    balanced_perspective = self._create_balanced_perspective(
        common_ground, mediated_disagreements
    )
    
    # 形成最终共识
    final_consensus = self._formulate_final_consensus(balanced_perspective)
    
    return {
        "common_ground": common_ground,
        "mediated_disagreements": mediated_disagreements,
        "balanced_perspective": balanced_perspective,
        "final_consensus": final_consensus,
        "consensus_strength": self._measure_consensus_strength(final_consensus),
        "remaining_uncertainties": self._identify_remaining_uncertainties(final_consensus)
    }
```

### 研究质量控制
```python
class ResearchQualityController:
    """研究质量控制器"""
    
    def __init__(self):
        self.quality_standards = self._define_quality_standards()
        self.evaluation_metrics = self._setup_evaluation_metrics()
    
    def evaluate_research_quality(self, research_data: Dict) -> Dict:
        """评估研究质量"""
        
        quality_dimensions = {
            "data_quality": self._assess_data_quality(research_data),
            "methodology_rigor": self._assess_methodology_rigor(research_data),
            "analysis_depth": self._assess_analysis_depth(research_data),
            "logical_consistency": self._assess_logical_consistency(research_data),
            "evidence_strength": self._assess_evidence_strength(research_data),
            "bias_control": self._assess_bias_control(research_data)
        }
        
        # 计算综合质量评分
        overall_quality = self._calculate_overall_quality(quality_dimensions)
        
        # 生成改进建议
        improvement_suggestions = self._generate_improvement_suggestions(quality_dimensions)
        
        return {
            "quality_dimensions": quality_dimensions,
            "overall_quality": overall_quality,
            "quality_grade": self._assign_quality_grade(overall_quality),
            "improvement_suggestions": improvement_suggestions,
            "quality_certification": self._provide_quality_certification(overall_quality)
        }
    
    def _assess_data_quality(self, research_data: Dict) -> Dict:
        """评估数据质量"""
        
        data_sources = research_data.get("data_sources", {})
        
        quality_factors = {
            "completeness": self._check_data_completeness(data_sources),
            "accuracy": self._verify_data_accuracy(data_sources),
            "timeliness": self._assess_data_timeliness(data_sources),
            "relevance": self._evaluate_data_relevance(data_sources),
            "reliability": self._assess_source_reliability(data_sources)
        }
        
        data_quality_score = sum(quality_factors.values()) / len(quality_factors)
        
        return {
            "quality_factors": quality_factors,
            "quality_score": data_quality_score,
            "quality_level": "高" if data_quality_score > 0.8 else "中" if data_quality_score > 0.6 else "低"
        }
```

## 2. 风险经理 (Risk Manager)

### 职责与功能
```python
class RiskManager:
    """风险经理 - 统筹风险管理活动"""
    
    def __init__(self, config):
        self.config = config
        self.risk_framework = RiskManagementFramework()
        self.risk_committee = RiskCommittee()
        self.risk_monitor = RiskMonitor()
        
    核心职责:
    - 制定风险管理政策
    - 协调风险评估活动
    - 监督风险控制执行
    - 管理风险委员会
    - 应对风险事件
    
    管理范围:
    - 风险政策制定
    - 风险评估协调
    - 风险控制监督
    - 风险报告管理
    - 危机应对处理
```

### 风险管理流程
```python
def manage_risk_assessment(self, research_results: Dict, market_data: Dict) -> Dict:
    """管理风险评估流程"""
    
    # 1. 风险识别
    risk_identification = self._conduct_risk_identification(research_results, market_data)
    
    # 2. 风险评估协调
    risk_assessment_coordination = self._coordinate_risk_assessments(risk_identification)
    
    # 3. 风险委员会决议
    risk_committee_decision = self._convene_risk_committee(risk_assessment_coordination)
    
    # 4. 风险控制设计
    risk_controls = self._design_risk_controls(risk_committee_decision)
    
    # 5. 风险监控设置
    risk_monitoring = self._setup_risk_monitoring(risk_controls)
    
    return {
        "risk_identification": risk_identification,
        "risk_assessment": risk_assessment_coordination,
        "committee_decision": risk_committee_decision,
        "risk_controls": risk_controls,
        "risk_monitoring": risk_monitoring,
        "risk_approval": self._provide_risk_approval(risk_committee_decision)
    }

def _conduct_risk_identification(self, research_results: Dict, market_data: Dict) -> Dict:
    """进行风险识别"""
    
    # 系统性风险识别
    systematic_risks = self._identify_systematic_risks(market_data)
    
    # 特定风险识别
    specific_risks = self._identify_specific_risks(research_results)
    
    # 操作风险识别
    operational_risks = self._identify_operational_risks()
    
    # 流动性风险识别
    liquidity_risks = self._identify_liquidity_risks(market_data)
    
    # 风险相关性分析
    risk_correlations = self._analyze_risk_correlations(
        systematic_risks, specific_risks, operational_risks, liquidity_risks
    )
    
    return {
        "systematic_risks": systematic_risks,
        "specific_risks": specific_risks,
        "operational_risks": operational_risks,
        "liquidity_risks": liquidity_risks,
        "risk_correlations": risk_correlations,
        "risk_map": self._create_risk_map(systematic_risks, specific_risks, operational_risks)
    }

def _coordinate_risk_assessments(self, risk_identification: Dict) -> Dict:
    """协调风险评估"""
    
    # 分配评估任务
    assessment_assignments = self._assign_assessment_tasks(risk_identification)
    
    # 监督评估过程
    assessment_supervision = self._supervise_assessment_process(assessment_assignments)
    
    # 整合评估结果
    integrated_assessment = self._integrate_assessment_results(assessment_supervision)
    
    # 交叉验证
    cross_validation = self._conduct_cross_validation(integrated_assessment)
    
    # 评估质量控制
    quality_control = self._conduct_assessment_quality_control(integrated_assessment)
    
    return {
        "assignments": assessment_assignments,
        "supervision": assessment_supervision,
        "integrated_results": integrated_assessment,
        "cross_validation": cross_validation,
        "quality_control": quality_control,
        "assessment_confidence": self._calculate_assessment_confidence(integrated_assessment)
    }

def _convene_risk_committee(self, risk_assessment: Dict) -> Dict:
    """召集风险委员会"""
    
    # 准备委员会材料
    committee_materials = self._prepare_committee_materials(risk_assessment)
    
    # 设置议程
    meeting_agenda = self._set_committee_agenda(risk_assessment)
    
    # 主持委员会会议
    committee_meeting = self._chair_committee_meeting(committee_materials, meeting_agenda)
    
    # 促进决策形成
    decision_formation = self._facilitate_committee_decision(committee_meeting)
    
    # 记录决议
    committee_resolution = self._document_committee_resolution(decision_formation)
    
    return {
        "materials": committee_materials,
        "agenda": meeting_agenda,
        "meeting_process": committee_meeting,
        "decision_process": decision_formation,
        "resolution": committee_resolution,
        "decision_rationale": self._document_decision_rationale(committee_resolution)
    }
```

### 风险政策制定
```python
class RiskPolicyFramework:
    """风险政策框架"""
    
    def __init__(self):
        self.policy_templates = self._load_policy_templates()
        self.regulatory_requirements = self._load_regulatory_requirements()
    
    def develop_risk_policies(self, organization_context: Dict) -> Dict:
        """制定风险政策"""
        
        # 风险容忍度政策
        risk_tolerance_policy = self._develop_risk_tolerance_policy(organization_context)
        
        # 风险限额政策
        risk_limits_policy = self._develop_risk_limits_policy(organization_context)
        
        # 风险监控政策
        risk_monitoring_policy = self._develop_risk_monitoring_policy(organization_context)
        
        # 风险报告政策
        risk_reporting_policy = self._develop_risk_reporting_policy(organization_context)
        
        # 应急响应政策
        emergency_response_policy = self._develop_emergency_response_policy(organization_context)
        
        return {
            "risk_tolerance": risk_tolerance_policy,
            "risk_limits": risk_limits_policy,
            "risk_monitoring": risk_monitoring_policy,
            "risk_reporting": risk_reporting_policy,
            "emergency_response": emergency_response_policy,
            "policy_integration": self._integrate_risk_policies([
                risk_tolerance_policy, risk_limits_policy, risk_monitoring_policy,
                risk_reporting_policy, emergency_response_policy
            ])
        }
```

## 3. 决策协调器 (Decision Coordinator)

### 职责与功能
```python
class DecisionCoordinator:
    """决策协调器 - 协调最终投资决策"""
    
    def __init__(self, config):
        self.config = config
        self.decision_framework = DecisionFramework()
        self.stakeholder_manager = StakeholderManager()
        
    def coordinate_final_decision(self, research_results: Dict, risk_assessment: Dict) -> Dict:
        """协调最终决策"""
        
        # 1. 信息整合
        integrated_information = self._integrate_all_information(research_results, risk_assessment)
        
        # 2. 利益相关者协调
        stakeholder_alignment = self._coordinate_stakeholders(integrated_information)
        
        # 3. 决策选项分析
        decision_options = self._analyze_decision_options(integrated_information)
        
        # 4. 决策制定
        final_decision = self._make_final_decision(decision_options, stakeholder_alignment)
        
        # 5. 决策沟通
        decision_communication = self._communicate_decision(final_decision)
        
        return {
            "integrated_information": integrated_information,
            "stakeholder_alignment": stakeholder_alignment,
            "decision_options": decision_options,
            "final_decision": final_decision,
            "communication_plan": decision_communication,
            "implementation_roadmap": self._create_implementation_roadmap(final_decision)
        }

def _integrate_all_information(self, research_results: Dict, risk_assessment: Dict) -> Dict:
    """整合所有信息"""
    
    # 研究信息提取
    research_insights = self._extract_research_insights(research_results)
    
    # 风险信息提取
    risk_insights = self._extract_risk_insights(risk_assessment)
    
    # 信息一致性检查
    consistency_check = self._check_information_consistency(research_insights, risk_insights)
    
    # 信息权重分配
    information_weights = self._assign_information_weights(research_insights, risk_insights)
    
    # 综合信息评分
    integrated_score = self._calculate_integrated_score(
        research_insights, risk_insights, information_weights
    )
    
    return {
        "research_insights": research_insights,
        "risk_insights": risk_insights,
        "consistency_check": consistency_check,
        "information_weights": information_weights,
        "integrated_score": integrated_score,
        "information_quality": self._assess_information_quality(research_insights, risk_insights)
    }

def _analyze_decision_options(self, integrated_information: Dict) -> Dict:
    """分析决策选项"""
    
    # 生成决策选项
    options = self._generate_decision_options(integrated_information)
    
    # 选项评估
    option_evaluations = {}
    for option_name, option_details in options.items():
        option_evaluations[option_name] = self._evaluate_decision_option(
            option_details, integrated_information
        )
    
    # 选项比较
    option_comparison = self._compare_decision_options(option_evaluations)
    
    # 推荐选项
    recommended_option = self._recommend_best_option(option_comparison)
    
    return {
        "available_options": options,
        "option_evaluations": option_evaluations,
        "option_comparison": option_comparison,
        "recommended_option": recommended_option,
        "decision_rationale": self._explain_option_selection(recommended_option, option_comparison)
    }
```

### 管理层监督机制
```python
class ManagementOversight:
    """管理层监督机制"""
    
    def __init__(self):
        self.oversight_standards = self._define_oversight_standards()
        self.performance_metrics = self._setup_performance_metrics()
    
    def conduct_oversight_review(self, decision_process: Dict) -> Dict:
        """进行监督审查"""
        
        # 流程合规性检查
        compliance_check = self._check_process_compliance(decision_process)
        
        # 决策质量评估
        decision_quality = self._assess_decision_quality(decision_process)
        
        # 风险管理有效性评估
        risk_management_effectiveness = self._assess_risk_management_effectiveness(decision_process)
        
        # 团队协作评估
        team_collaboration = self._assess_team_collaboration(decision_process)
        
        # 改进建议
        improvement_recommendations = self._generate_improvement_recommendations(
            compliance_check, decision_quality, risk_management_effectiveness, team_collaboration
        )
        
        return {
            "compliance_check": compliance_check,
            "decision_quality": decision_quality,
            "risk_management_effectiveness": risk_management_effectiveness,
            "team_collaboration": team_collaboration,
            "improvement_recommendations": improvement_recommendations,
            "oversight_rating": self._calculate_oversight_rating(
                compliance_check, decision_quality, risk_management_effectiveness
            )
        }
```

管理层智能体通过有效的协调、监督和决策机制，确保整个投资决策流程的专业性、合规性和有效性，为投资成功提供强有力的管理保障。


<!-- docs/agents/researchers.md -->

# 研究员团队设计

## 概述

研究员团队是 TradingAgents 框架中的关键组件，负责对分析师团队的报告进行深度研究和辩论。通过看涨和看跌研究员之间的结构化辩论，系统能够从多个角度评估投资机会，形成更加平衡和全面的投资观点。

## 研究员架构

### 基础研究员类

```python
class BaseResearcher:
    """所有研究员的基础类"""
    
    def __init__(self, llm, config, stance="neutral"):
        self.llm = llm
        self.config = config
        self.stance = stance  # "bullish", "bearish", "neutral"
        self.memory = ResearcherMemory()
        self.debate_history = []
        
    def research(self, analyst_reports: Dict, context: Dict = None) -> Dict:
        """执行研究分析"""
        
        # 1. 分析师报告解读
        interpretation = self.interpret_reports(analyst_reports)
        
        # 2. 立场分析
        stance_analysis = self.analyze_from_stance(interpretation)
        
        # 3. 生成研究观点
        research_view = self.generate_research_view(stance_analysis)
        
        # 4. 准备辩论要点
        debate_points = self.prepare_debate_points(research_view)
        
        return {
            "interpretation": interpretation,
            "stance_analysis": stance_analysis,
            "research_view": research_view,
            "debate_points": debate_points,
            "confidence": self.calculate_confidence(research_view)
        }
    
    def debate(self, opponent_view: Dict, round_number: int) -> Dict:
        """参与辩论"""
        
        # 1. 分析对手观点
        opponent_analysis = self.analyze_opponent_view(opponent_view)
        
        # 2. 准备反驳
        counter_arguments = self.prepare_counter_arguments(opponent_analysis)
        
        # 3. 强化自己观点
        reinforced_view = self.reinforce_own_view(counter_arguments)
        
        # 4. 生成辩论回应
        debate_response = self.generate_debate_response(
            counter_arguments, reinforced_view, round_number
        )
        
        # 5. 更新辩论历史
        self.debate_history.append({
            "round": round_number,
            "opponent_view": opponent_view,
            "response": debate_response
        })
        
        return debate_response
```

## 1. 看涨研究员 (Bull Researcher)

### 职责与特点
```python
class BullResearcher(BaseResearcher):
    """看涨研究员 - 从乐观角度评估投资机会"""
    
    def __init__(self, llm, config):
        super().__init__(llm, config, stance="bullish")
        
    专业特点:
    - 积极寻找增长机会
    - 强调正面催化剂
    - 关注上涨潜力
    - 挑战悲观观点
    
    分析重点:
    - 收入增长驱动因素
    - 市场扩张机会
    - 竞争优势分析
    - 估值吸引力
    - 技术创新潜力
    - 管理层执行力
```

### 核心研究方法
```python
def analyze_from_stance(self, interpretation: Dict) -> Dict:
    """从看涨角度分析"""
    
    bullish_factors = []
    growth_opportunities = []
    positive_catalysts = []
    
    # 基本面看涨因素
    fundamental_data = interpretation.get("fundamental_analysis", {})
    if fundamental_data.get("revenue_growth", 0) > 0.1:  # 10%以上增长
        bullish_factors.append("强劲的收入增长")
    
    if fundamental_data.get("profit_margin_trend") == "improving":
        bullish_factors.append("利润率改善趋势")
    
    # 技术面看涨信号
    technical_data = interpretation.get("technical_analysis", {})
    if technical_data.get("trend_direction") == "uptrend":
        bullish_factors.append("技术面上升趋势")
    
    if technical_data.get("momentum") == "positive":
        bullish_factors.append("正面动量信号")
    
    # 新闻面积极因素
    news_data = interpretation.get("news_analysis", {})
    if news_data.get("sentiment_score", 0) > 0.6:
        positive_catalysts.append("积极的新闻情绪")
    
    # 识别增长机会
    growth_opportunities = self._identify_growth_opportunities(interpretation)
    
    return {
        "bullish_factors": bullish_factors,
        "growth_opportunities": growth_opportunities,
        "positive_catalysts": positive_catalysts,
        "upside_potential": self._calculate_upside_potential(interpretation),
        "risk_mitigation": self._identify_risk_mitigation_factors(interpretation)
    }

def _identify_growth_opportunities(self, interpretation: Dict) -> List[str]:
    """识别增长机会"""
    
    opportunities = []
    
    # 市场扩张机会
    if interpretation.get("market_size_growth", 0) > 0.05:
        opportunities.append("市场规模持续扩张")
    
    # 新产品/服务机会
    if interpretation.get("new_product_pipeline"):
        opportunities.append("丰富的新产品管线")
    
    # 国际化机会
    if interpretation.get("international_expansion"):
        opportunities.append("国际市场扩张潜力")
    
    # 技术创新机会
    if interpretation.get("innovation_score", 0) > 0.7:
        opportunities.append("技术创新领先优势")
    
    return opportunities

def prepare_debate_points(self, research_view: Dict) -> Dict:
    """准备辩论要点"""
    
    return {
        "main_arguments": [
            "基本面数据显示强劲增长潜力",
            "技术指标支持上涨趋势",
            "市场情绪积极向好",
            "估值仍有上升空间"
        ],
        "supporting_evidence": research_view.get("bullish_factors", []),
        "growth_thesis": research_view.get("growth_opportunities", []),
        "risk_responses": self._prepare_risk_responses(research_view),
        "target_scenarios": self._develop_bull_scenarios(research_view)
    }
```

### 辩论策略
```python
def generate_debate_response(self, counter_args: Dict, reinforced_view: Dict, round_num: int) -> Dict:
    """生成辩论回应"""
    
    response_strategy = self._determine_response_strategy(round_num)
    
    if response_strategy == "aggressive":
        return self._aggressive_response(counter_args, reinforced_view)
    elif response_strategy == "defensive":
        return self._defensive_response(counter_args, reinforced_view)
    else:
        return self._balanced_response(counter_args, reinforced_view)

def _aggressive_response(self, counter_args: Dict, reinforced_view: Dict) -> Dict:
    """积极进攻型回应"""
    
    return {
        "response_type": "aggressive",
        "main_points": [
            "对手过度关注短期风险，忽视长期价值",
            "市场恐慌情绪创造了绝佳买入机会",
            "基本面改善趋势不可逆转",
            "当前估值明显低估真实价值"
        ],
        "evidence_reinforcement": reinforced_view.get("strengthened_evidence", []),
        "opponent_weaknesses": self._identify_opponent_weaknesses(counter_args),
        "confidence_boost": "高度确信看涨观点的正确性"
    }

def _defensive_response(self, counter_args: Dict, reinforced_view: Dict) -> Dict:
    """防守型回应"""
    
    return {
        "response_type": "defensive",
        "risk_acknowledgment": "承认存在一定风险，但风险可控",
        "mitigation_strategies": [
            "分散投资降低单一风险",
            "设置合理止损位",
            "关注基本面变化",
            "动态调整仓位"
        ],
        "qualified_optimism": "在风险可控前提下保持乐观",
        "evidence_reaffirmation": reinforced_view.get("core_evidence", [])
    }
```

## 2. 看跌研究员 (Bear Researcher)

### 职责与特点
```python
class BearResearcher(BaseResearcher):
    """看跌研究员 - 从悲观角度评估投资风险"""
    
    def __init__(self, llm, config):
        super().__init__(llm, config, stance="bearish")
        
    专业特点:
    - 专注风险识别
    - 质疑乐观假设
    - 关注下跌风险
    - 挑战看涨观点
    
    分析重点:
    - 潜在风险因素
    - 估值过高风险
    - 竞争威胁分析
    - 宏观经济风险
    - 行业周期性风险
    - 公司治理问题
```

### 核心研究方法
```python
def analyze_from_stance(self, interpretation: Dict) -> Dict:
    """从看跌角度分析"""
    
    bearish_factors = []
    risk_factors = []
    negative_catalysts = []
    
    # 基本面风险因素
    fundamental_data = interpretation.get("fundamental_analysis", {})
    if fundamental_data.get("debt_to_equity", 0) > 0.6:
        bearish_factors.append("高负债比率风险")
    
    if fundamental_data.get("profit_margin_trend") == "declining":
        bearish_factors.append("利润率下降趋势")
    
    # 技术面看跌信号
    technical_data = interpretation.get("technical_analysis", {})
    if technical_data.get("trend_direction") == "downtrend":
        bearish_factors.append("技术面下降趋势")
    
    if technical_data.get("volume_trend") == "declining":
        bearish_factors.append("成交量萎缩信号")
    
    # 新闻面负面因素
    news_data = interpretation.get("news_analysis", {})
    if news_data.get("sentiment_score", 0) < 0.4:
        negative_catalysts.append("负面新闻情绪")
    
    # 识别风险因素
    risk_factors = self._identify_risk_factors(interpretation)
    
    return {
        "bearish_factors": bearish_factors,
        "risk_factors": risk_factors,
        "negative_catalysts": negative_catalysts,
        "downside_potential": self._calculate_downside_potential(interpretation),
        "valuation_concerns": self._assess_valuation_risks(interpretation)
    }

def _identify_risk_factors(self, interpretation: Dict) -> List[Dict]:
    """识别风险因素"""
    
    risks = []
    
    # 市场风险
    if interpretation.get("market_volatility", 0) > 0.3:
        risks.append({
            "type": "market_risk",
            "description": "市场波动性过高",
            "severity": "high",
            "probability": 0.7
        })
    
    # 行业风险
    if interpretation.get("industry_headwinds"):
        risks.append({
            "type": "industry_risk",
            "description": "行业面临逆风",
            "severity": "medium",
            "probability": 0.6
        })
    
    # 公司特定风险
    if interpretation.get("company_specific_issues"):
        risks.append({
            "type": "company_risk",
            "description": "公司特定问题",
            "severity": "high",
            "probability": 0.8
        })
    
    return risks

def prepare_debate_points(self, research_view: Dict) -> Dict:
    """准备辩论要点"""
    
    return {
        "main_arguments": [
            "估值过高，缺乏安全边际",
            "基本面恶化趋势明显",
            "技术指标显示下跌风险",
            "宏观环境不利于增长"
        ],
        "risk_evidence": research_view.get("risk_factors", []),
        "valuation_concerns": research_view.get("valuation_concerns", []),
        "scenario_analysis": self._develop_bear_scenarios(research_view),
        "contrarian_points": self._prepare_contrarian_arguments(research_view)
    }
```

### 风险评估专长
```python
def _assess_valuation_risks(self, interpretation: Dict) -> Dict:
    """评估估值风险"""
    
    valuation_data = interpretation.get("fundamental_analysis", {})
    
    concerns = []
    
    # P/E 比率分析
    pe_ratio = valuation_data.get("pe_ratio", 0)
    industry_avg_pe = valuation_data.get("industry_avg_pe", 0)
    
    if pe_ratio > industry_avg_pe * 1.5:
        concerns.append("P/E比率显著高于行业平均")
    
    # P/B 比率分析
    pb_ratio = valuation_data.get("pb_ratio", 0)
    if pb_ratio > 3.0:
        concerns.append("P/B比率过高，存在泡沫风险")
    
    # 增长率与估值匹配度
    growth_rate = valuation_data.get("growth_rate", 0)
    peg_ratio = pe_ratio / max(growth_rate * 100, 1)
    
    if peg_ratio > 2.0:
        concerns.append("PEG比率过高，增长不足以支撑估值")
    
    return {
        "concerns": concerns,
        "overvaluation_risk": "high" if len(concerns) >= 2 else "medium",
        "fair_value_estimate": self._calculate_conservative_fair_value(valuation_data),
        "downside_protection": self._assess_downside_protection(valuation_data)
    }
```

## 3. 辩论机制设计

### 辩论管理器
```python
class DebateManager:
    """辩论管理器 - 协调研究员之间的辩论"""
    
    def __init__(self, config):
        self.config = config
        self.max_rounds = config.get("max_debate_rounds", 3)
        self.consensus_threshold = config.get("consensus_threshold", 0.8)
        
    def conduct_debate(self, bull_researcher: BullResearcher, 
                      bear_researcher: BearResearcher,
                      analyst_reports: Dict) -> Dict:
        """主持辩论过程"""
        
        # 初始研究
        bull_initial = bull_researcher.research(analyst_reports)
        bear_initial = bear_researcher.research(analyst_reports)
        
        debate_history = []
        current_round = 1
        
        while current_round <= self.max_rounds:
            print(f"=== 辩论第 {current_round} 轮 ===")
            
            # 看涨方辩论
            bull_response = bull_researcher.debate(bear_initial, current_round)
            
            # 看跌方辩论
            bear_response = bear_researcher.debate(bull_initial, current_round)
            
            # 记录辩论
            round_record = {
                "round": current_round,
                "bull_response": bull_response,
                "bear_response": bear_response,
                "consensus_level": self._calculate_consensus(bull_response, bear_response)
            }
            
            debate_history.append(round_record)
            
            # 检查是否达成共识或需要继续
            if self._should_continue_debate(round_record, current_round):
                current_round += 1
                # 更新观点用于下一轮
                bull_initial = bull_response
                bear_initial = bear_response
            else:
                break
        
        # 生成最终共识
        final_consensus = self._generate_consensus(debate_history, bull_initial, bear_initial)
        
        return {
            "debate_history": debate_history,
            "final_consensus": final_consensus,
            "total_rounds": current_round,
            "consensus_quality": self._assess_consensus_quality(final_consensus)
        }
    
    def _calculate_consensus(self, bull_view: Dict, bear_view: Dict) -> float:
        """计算共识水平"""
        
        # 提取关键观点
        bull_confidence = bull_view.get("confidence", 0.5)
        bear_confidence = bear_view.get("confidence", 0.5)
        
        # 计算观点差异
        confidence_diff = abs(bull_confidence - bear_confidence)
        
        # 共识水平 = 1 - 观点差异
        consensus_level = 1.0 - confidence_diff
        
        return max(0.0, min(1.0, consensus_level))
    
    def _should_continue_debate(self, round_record: Dict, current_round: int) -> bool:
        """判断是否继续辩论"""
        
        # 达到最大轮次
        if current_round >= self.max_rounds:
            return False
        
        # 达成足够共识
        if round_record["consensus_level"] >= self.consensus_threshold:
            return False
        
        # 观点分歧仍然较大，继续辩论
        return True
    
    def _generate_consensus(self, debate_history: List[Dict], 
                          final_bull: Dict, final_bear: Dict) -> Dict:
        """生成最终共识"""
        
        # 综合双方观点
        consensus_points = []
        
        # 提取共同认可的要点
        bull_factors = set(final_bull.get("main_points", []))
        bear_factors = set(final_bear.get("main_points", []))
        
        common_points = bull_factors.intersection(bear_factors)
        consensus_points.extend(list(common_points))
        
        # 平衡风险和机会
        opportunities = final_bull.get("growth_opportunities", [])
        risks = final_bear.get("risk_factors", [])
        
        # 生成平衡的投资建议
        if len(opportunities) > len(risks):
            recommendation = "谨慎乐观"
            confidence = 0.6
        elif len(risks) > len(opportunities):
            recommendation = "谨慎悲观"
            confidence = 0.4
        else:
            recommendation = "中性观望"
            confidence = 0.5
        
        return {
            "consensus_points": consensus_points,
            "balanced_view": {
                "opportunities": opportunities[:3],  # 前3个机会
                "risks": risks[:3],  # 前3个风险
            },
            "recommendation": recommendation,
            "confidence": confidence,
            "key_factors_to_watch": self._identify_key_factors(final_bull, final_bear)
        }
```

### 辩论质量评估
```python
class DebateQualityAssessor:
    """辩论质量评估器"""
    
    def assess_debate_quality(self, debate_result: Dict) -> Dict:
        """评估辩论质量"""
        
        quality_metrics = {
            "depth_score": self._assess_depth(debate_result),
            "balance_score": self._assess_balance(debate_result),
            "evidence_quality": self._assess_evidence_quality(debate_result),
            "logical_consistency": self._assess_logical_consistency(debate_result),
            "consensus_quality": self._assess_consensus_quality(debate_result)
        }
        
        overall_quality = sum(quality_metrics.values()) / len(quality_metrics)
        
        return {
            "quality_metrics": quality_metrics,
            "overall_quality": overall_quality,
            "quality_grade": self._assign_quality_grade(overall_quality),
            "improvement_suggestions": self._generate_improvement_suggestions(quality_metrics)
        }
```

研究员团队通过结构化的辩论机制，确保投资决策考虑了多个角度和潜在风险，提高了决策的质量和可靠性。


<!-- docs/agents/risk-management.md -->

# 风险管理智能体

## 概述

风险管理智能体是 TradingAgents 框架的安全守护者，负责识别、评估和控制投资风险。通过多层次的风险评估机制，确保交易决策在可接受的风险范围内，保护投资组合免受重大损失。

## 风险管理架构

### 风险管理体系

```python
class RiskManagementSystem:
    """风险管理系统 - 统筹所有风险管理活动"""
    
    def __init__(self, config):
        self.config = config
        self.risk_assessors = self._initialize_risk_assessors()
        self.risk_monitor = RiskMonitor()
        self.risk_controller = RiskController()
        
    def _initialize_risk_assessors(self):
        """初始化风险评估智能体"""
        return {
            "aggressive": AggressiveRiskAssessor(self.config),
            "conservative": ConservativeRiskAssessor(self.config),
            "neutral": NeutralRiskAssessor(self.config)
        }
    
    def assess_trading_risk(self, trading_decision: Dict, market_data: Dict) -> Dict:
        """评估交易风险"""
        
        # 1. 多角度风险评估
        risk_assessments = {}
        for assessor_type, assessor in self.risk_assessors.items():
            risk_assessments[assessor_type] = assessor.assess_risk(
                trading_decision, market_data
            )
        
        # 2. 综合风险评估
        consolidated_risk = self._consolidate_risk_assessments(risk_assessments)
        
        # 3. 风险等级分类
        risk_classification = self._classify_risk_level(consolidated_risk)
        
        # 4. 风险控制建议
        control_recommendations = self._generate_control_recommendations(
            consolidated_risk, risk_classification
        )
        
        return {
            "individual_assessments": risk_assessments,
            "consolidated_risk": consolidated_risk,
            "risk_classification": risk_classification,
            "control_recommendations": control_recommendations,
            "approval_status": self._determine_approval_status(risk_classification)
        }
```

## 1. 激进风险评估智能体

### 特点与职责
```python
class AggressiveRiskAssessor:
    """激进风险评估 - 支持高风险高收益策略"""
    
    def __init__(self, config):
        self.config = config
        self.risk_appetite = "high"
        self.return_focus = "high"
        
    专业特点:
    - 高风险容忍度
    - 关注收益最大化
    - 支持杠杆使用
    - 鼓励机会把握
    
    评估重点:
    - 收益潜力分析
    - 机会成本评估
    - 市场时机把握
    - 竞争优势利用
```

### 风险评估方法
```python
def assess_risk(self, trading_decision: Dict, market_data: Dict) -> Dict:
    """激进角度的风险评估"""
    
    # 基础风险指标
    base_risk_metrics = self._calculate_base_risk_metrics(trading_decision, market_data)
    
    # 激进调整因子
    aggressive_adjustments = {
        "volatility_tolerance": 1.5,      # 高波动容忍度
        "drawdown_tolerance": 1.3,        # 高回撤容忍度
        "leverage_acceptance": 1.2,       # 接受适度杠杆
        "opportunity_weight": 1.4         # 高机会权重
    }
    
    # 调整风险评估
    adjusted_risk = self._apply_aggressive_adjustments(
        base_risk_metrics, aggressive_adjustments
    )
    
    # 收益风险比分析
    return_risk_analysis = self._analyze_return_risk_ratio(
        trading_decision, adjusted_risk
    )
    
    # 机会成本评估
    opportunity_cost = self._assess_opportunity_cost(trading_decision, market_data)
    
    return {
        "risk_score": adjusted_risk["overall_risk"],
        "return_potential": return_risk_analysis["return_potential"],
        "risk_adjusted_return": return_risk_analysis["risk_adjusted_return"],
        "opportunity_cost": opportunity_cost,
        "recommendation": self._generate_aggressive_recommendation(
            adjusted_risk, return_risk_analysis, opportunity_cost
        ),
        "key_considerations": [
            "高收益潜力值得承担相应风险",
            "市场机会稍纵即逝，应果断行动",
            "适度风险是获得超额收益的必要条件",
            "风险可通过主动管理得到控制"
        ]
    }

def _analyze_return_risk_ratio(self, decision: Dict, risk_metrics: Dict) -> Dict:
    """分析收益风险比"""
    
    expected_return = decision.get("take_profit", 0.1)
    risk_level = risk_metrics.get("overall_risk", 0.5)
    
    # 激进视角下的收益风险比计算
    # 更看重收益潜力，对风险相对宽容
    risk_adjusted_return = expected_return / max(risk_level * 0.8, 0.1)
    
    return_potential_score = min(expected_return * 10, 1.0)  # 收益潜力评分
    
    return {
        "return_potential": return_potential_score,
        "risk_adjusted_return": risk_adjusted_return,
        "return_risk_ratio": expected_return / max(risk_level, 0.1),
        "attractiveness": "高" if risk_adjusted_return > 1.5 else "中" if risk_adjusted_return > 1.0 else "低"
    }

def _assess_opportunity_cost(self, decision: Dict, market_data: Dict) -> Dict:
    """评估机会成本"""
    
    # 不行动的机会成本
    inaction_cost = self._calculate_inaction_cost(decision, market_data)
    
    # 延迟行动的成本
    delay_cost = self._calculate_delay_cost(decision, market_data)
    
    # 保守策略的机会成本
    conservative_cost = self._calculate_conservative_cost(decision)
    
    total_opportunity_cost = inaction_cost + delay_cost + conservative_cost
    
    return {
        "inaction_cost": inaction_cost,
        "delay_cost": delay_cost,
        "conservative_cost": conservative_cost,
        "total_cost": total_opportunity_cost,
        "urgency_level": "高" if total_opportunity_cost > 0.1 else "中" if total_opportunity_cost > 0.05 else "低"
    }
```

## 2. 保守风险评估智能体

### 特点与职责
```python
class ConservativeRiskAssessor:
    """保守风险评估 - 强调风险控制和资本保护"""
    
    def __init__(self, config):
        self.config = config
        self.risk_appetite = "low"
        self.capital_preservation_focus = True
        
    专业特点:
    - 低风险容忍度
    - 强调资本保护
    - 谨慎的仓位管理
    - 严格的风险控制
    
    评估重点:
    - 下行风险保护
    - 最大回撤控制
    - 流动性风险管理
    - 尾部风险防范
```

### 风险评估方法
```python
def assess_risk(self, trading_decision: Dict, market_data: Dict) -> Dict:
    """保守角度的风险评估"""
    
    # 基础风险指标
    base_risk_metrics = self._calculate_base_risk_metrics(trading_decision, market_data)
    
    # 保守调整因子
    conservative_adjustments = {
        "volatility_penalty": 1.5,        # 高波动惩罚
        "drawdown_penalty": 1.8,          # 高回撤惩罚
        "liquidity_requirement": 1.3,     # 高流动性要求
        "safety_margin": 1.4              # 高安全边际
    }
    
    # 调整风险评估
    adjusted_risk = self._apply_conservative_adjustments(
        base_risk_metrics, conservative_adjustments
    )
    
    # 下行风险分析
    downside_risk = self._analyze_downside_risk(trading_decision, market_data)
    
    # 尾部风险评估
    tail_risk = self._assess_tail_risk(trading_decision, market_data)
    
    # 流动性风险评估
    liquidity_risk = self._assess_liquidity_risk(trading_decision, market_data)
    
    return {
        "risk_score": adjusted_risk["overall_risk"],
        "downside_risk": downside_risk,
        "tail_risk": tail_risk,
        "liquidity_risk": liquidity_risk,
        "capital_at_risk": self._calculate_capital_at_risk(adjusted_risk),
        "recommendation": self._generate_conservative_recommendation(
            adjusted_risk, downside_risk, tail_risk
        ),
        "risk_mitigation_measures": [
            "严格设置止损位，控制最大损失",
            "分散投资，降低单一资产风险",
            "保持充足现金储备",
            "定期重新评估风险状况",
            "避免过度集中和杠杆"
        ]
    }

def _analyze_downside_risk(self, decision: Dict, market_data: Dict) -> Dict:
    """分析下行风险"""
    
    stop_loss = decision.get("stop_loss", 0.05)
    position_size = decision.get("quantity", 0.05)
    
    # 最大可能损失
    max_loss = stop_loss * position_size
    
    # 下行波动率
    downside_volatility = market_data.get("downside_volatility", 0.2)
    
    # VaR 计算 (95% 置信度)
    var_95 = position_size * downside_volatility * 1.65  # 95% VaR
    
    # CVaR 计算 (条件风险价值)
    cvar_95 = var_95 * 1.3  # 估算 CVaR
    
    return {
        "max_loss": max_loss,
        "var_95": var_95,
        "cvar_95": cvar_95,
        "downside_volatility": downside_volatility,
        "risk_level": "高" if max_loss > 0.02 else "中" if max_loss > 0.01 else "低"
    }

def _assess_tail_risk(self, decision: Dict, market_data: Dict) -> Dict:
    """评估尾部风险"""
    
    # 极端市场情况下的风险
    market_stress_scenarios = {
        "market_crash": {"probability": 0.05, "impact": -0.3},
        "liquidity_crisis": {"probability": 0.03, "impact": -0.2},
        "sector_collapse": {"probability": 0.08, "impact": -0.25},
        "black_swan": {"probability": 0.01, "impact": -0.5}
    }
    
    position_size = decision.get("quantity", 0.05)
    
    tail_risk_exposure = 0
    scenario_impacts = {}
    
    for scenario, params in market_stress_scenarios.items():
        scenario_loss = position_size * abs(params["impact"])
        expected_loss = scenario_loss * params["probability"]
        tail_risk_exposure += expected_loss
        
        scenario_impacts[scenario] = {
            "potential_loss": scenario_loss,
            "expected_loss": expected_loss,
            "probability": params["probability"]
        }
    
    return {
        "total_tail_risk": tail_risk_exposure,
        "scenario_impacts": scenario_impacts,
        "tail_risk_level": "高" if tail_risk_exposure > 0.01 else "中" if tail_risk_exposure > 0.005 else "低",
        "mitigation_priority": "高" if tail_risk_exposure > 0.01 else "中"
    }
```

## 3. 中性风险评估智能体

### 特点与职责
```python
class NeutralRiskAssessor:
    """中性风险评估 - 平衡风险和收益"""
    
    def __init__(self, config):
        self.config = config
        self.risk_appetite = "medium"
        self.balanced_approach = True
        
    专业特点:
    - 平衡的风险观
    - 理性的收益预期
    - 适度的风险承担
    - 全面的风险考量
    
    评估重点:
    - 风险收益平衡
    - 多维度风险分析
    - 情景分析
    - 概率加权评估
```

### 风险评估方法
```python
def assess_risk(self, trading_decision: Dict, market_data: Dict) -> Dict:
    """中性角度的风险评估"""
    
    # 全面风险分析
    comprehensive_risk = self._conduct_comprehensive_risk_analysis(
        trading_decision, market_data
    )
    
    # 情景分析
    scenario_analysis = self._conduct_scenario_analysis(trading_decision, market_data)
    
    # 风险收益平衡评估
    risk_return_balance = self._assess_risk_return_balance(
        trading_decision, comprehensive_risk
    )
    
    # 概率加权风险评估
    probability_weighted_risk = self._calculate_probability_weighted_risk(
        scenario_analysis
    )
    
    return {
        "comprehensive_risk": comprehensive_risk,
        "scenario_analysis": scenario_analysis,
        "risk_return_balance": risk_return_balance,
        "probability_weighted_risk": probability_weighted_risk,
        "overall_assessment": self._generate_balanced_assessment(
            comprehensive_risk, scenario_analysis, risk_return_balance
        ),
        "balanced_recommendation": self._generate_balanced_recommendation(
            comprehensive_risk, risk_return_balance
        )
    }

def _conduct_scenario_analysis(self, decision: Dict, market_data: Dict) -> Dict:
    """进行情景分析"""
    
    scenarios = {
        "bull_case": {"probability": 0.3, "return": 0.15, "risk": 0.1},
        "base_case": {"probability": 0.4, "return": 0.08, "risk": 0.15},
        "bear_case": {"probability": 0.3, "return": -0.05, "risk": 0.25}
    }
    
    position_size = decision.get("quantity", 0.05)
    
    scenario_outcomes = {}
    expected_return = 0
    expected_risk = 0
    
    for scenario_name, params in scenarios.items():
        scenario_return = params["return"] * position_size
        scenario_risk = params["risk"] * position_size
        probability = params["probability"]
        
        expected_return += scenario_return * probability
        expected_risk += scenario_risk * probability
        
        scenario_outcomes[scenario_name] = {
            "return": scenario_return,
            "risk": scenario_risk,
            "probability": probability,
            "risk_adjusted_return": scenario_return / max(scenario_risk, 0.01)
        }
    
    return {
        "scenarios": scenario_outcomes,
        "expected_return": expected_return,
        "expected_risk": expected_risk,
        "risk_return_ratio": expected_return / max(expected_risk, 0.01),
        "scenario_dispersion": self._calculate_scenario_dispersion(scenario_outcomes)
    }

def _assess_risk_return_balance(self, decision: Dict, risk_metrics: Dict) -> Dict:
    """评估风险收益平衡"""
    
    expected_return = decision.get("take_profit", 0.1)
    expected_risk = risk_metrics.get("overall_risk", 0.5)
    
    # 夏普比率估算
    risk_free_rate = 0.02  # 假设无风险利率
    excess_return = expected_return - risk_free_rate
    sharpe_ratio = excess_return / max(expected_risk, 0.01)
    
    # 风险调整后收益
    risk_adjusted_return = expected_return / max(expected_risk, 0.01)
    
    # 平衡评分
    balance_score = self._calculate_balance_score(sharpe_ratio, risk_adjusted_return)
    
    return {
        "sharpe_ratio": sharpe_ratio,
        "risk_adjusted_return": risk_adjusted_return,
        "balance_score": balance_score,
        "balance_assessment": self._assess_balance_quality(balance_score),
        "optimization_suggestions": self._suggest_balance_optimization(
            expected_return, expected_risk, balance_score
        )
    }
```

## 4. 风险管理决策

### 风险决策框架
```python
class RiskDecisionFramework:
    """风险决策框架"""
    
    def make_risk_decision(self, risk_assessments: Dict, trading_decision: Dict) -> Dict:
        """制定风险管理决策"""
        
        # 1. 风险共识分析
        risk_consensus = self._analyze_risk_consensus(risk_assessments)
        
        # 2. 风险等级确定
        final_risk_level = self._determine_final_risk_level(risk_assessments, risk_consensus)
        
        # 3. 决策建议生成
        decision_recommendation = self._generate_decision_recommendation(
            final_risk_level, risk_consensus, trading_decision
        )
        
        # 4. 风险控制措施
        risk_controls = self._design_risk_controls(final_risk_level, trading_decision)
        
        # 5. 监控要求
        monitoring_requirements = self._define_monitoring_requirements(
            final_risk_level, trading_decision
        )
        
        return {
            "risk_consensus": risk_consensus,
            "final_risk_level": final_risk_level,
            "decision": decision_recommendation,
            "risk_controls": risk_controls,
            "monitoring": monitoring_requirements,
            "approval_status": self._determine_final_approval(decision_recommendation)
        }
    
    def _analyze_risk_consensus(self, assessments: Dict) -> Dict:
        """分析风险评估共识"""
        
        risk_scores = [
            assessments["aggressive"]["risk_score"],
            assessments["conservative"]["risk_score"],
            assessments["neutral"]["comprehensive_risk"]["overall_risk"]
        ]
        
        # 计算共识指标
        avg_risk = sum(risk_scores) / len(risk_scores)
        risk_std = np.std(risk_scores)
        consensus_level = 1.0 - min(risk_std / avg_risk, 1.0) if avg_risk > 0 else 0.0
        
        # 分析分歧点
        disagreement_areas = self._identify_disagreement_areas(assessments)
        
        return {
            "average_risk_score": avg_risk,
            "risk_score_std": risk_std,
            "consensus_level": consensus_level,
            "disagreement_areas": disagreement_areas,
            "consensus_quality": "高" if consensus_level > 0.8 else "中" if consensus_level > 0.6 else "低"
        }
    
    def _generate_decision_recommendation(self, risk_level: str, consensus: Dict, decision: Dict) -> Dict:
        """生成决策建议"""
        
        consensus_level = consensus["consensus_level"]
        avg_risk = consensus["average_risk_score"]
        
        if risk_level == "low" and consensus_level > 0.7:
            recommendation = "approve"
            confidence = 0.9
        elif risk_level == "medium" and consensus_level > 0.6:
            recommendation = "approve_with_conditions"
            confidence = 0.7
        elif risk_level == "high" and consensus_level > 0.8:
            recommendation = "approve_with_strict_controls"
            confidence = 0.6
        else:
            recommendation = "reject"
            confidence = 0.8
        
        return {
            "recommendation": recommendation,
            "confidence": confidence,
            "reasoning": self._explain_recommendation_reasoning(
                risk_level, consensus_level, avg_risk, recommendation
            ),
            "conditions": self._define_approval_conditions(recommendation, risk_level)
        }
```

### 风险监控系统
```python
class RiskMonitor:
    """风险监控系统"""
    
    def __init__(self):
        self.active_positions = {}
        self.risk_alerts = []
        self.monitoring_rules = self._setup_monitoring_rules()
    
    def monitor_position_risk(self, position_id: str, current_data: Dict) -> Dict:
        """监控仓位风险"""
        
        position = self.active_positions.get(position_id)
        if not position:
            return {"status": "position_not_found"}
        
        # 实时风险计算
        current_risk = self._calculate_current_risk(position, current_data)
        
        # 风险阈值检查
        risk_alerts = self._check_risk_thresholds(position, current_risk)
        
        # 止损止盈检查
        exit_signals = self._check_exit_conditions(position, current_data)
        
        # 更新监控状态
        monitoring_status = self._update_monitoring_status(
            position, current_risk, risk_alerts, exit_signals
        )
        
        return {
            "position_id": position_id,
            "current_risk": current_risk,
            "risk_alerts": risk_alerts,
            "exit_signals": exit_signals,
            "monitoring_status": monitoring_status,
            "recommended_actions": self._recommend_risk_actions(
                current_risk, risk_alerts, exit_signals
            )
        }
```

风险管理智能体通过多角度评估、严格控制和持续监控，确保交易活动在可控的风险范围内进行，保护投资组合的安全。


<!-- docs/agents/trader.md -->

# 交易员智能体

## 概述

交易员智能体是 TradingAgents 框架的核心决策组件，负责综合分析师报告和研究员辩论结果，制定最终的交易决策。交易员智能体具备专业的交易知识和风险意识，能够在复杂的市场环境中做出明智的投资决策。

## 交易员架构

### 基础交易员类

```python
class Trader:
    """交易员智能体 - 负责最终交易决策"""
    
    def __init__(self, llm, config):
        self.llm = llm
        self.config = config
        self.trading_style = config.get("trading_style", "balanced")
        self.risk_tolerance = config.get("risk_tolerance", "medium")
        self.memory = TradingMemory()
        self.position_manager = PositionManager()
        
    def make_decision(self, analysis_data: Dict) -> Dict:
        """制定交易决策"""
        
        # 1. 综合分析所有输入
        comprehensive_analysis = self.synthesize_analysis(analysis_data)
        
        # 2. 评估市场条件
        market_assessment = self.assess_market_conditions(analysis_data)
        
        # 3. 制定交易策略
        trading_strategy = self.develop_trading_strategy(
            comprehensive_analysis, market_assessment
        )
        
        # 4. 确定仓位大小
        position_size = self.calculate_position_size(trading_strategy)
        
        # 5. 设置风险管理参数
        risk_parameters = self.set_risk_parameters(trading_strategy)
        
        # 6. 生成最终决策
        final_decision = self.generate_final_decision(
            trading_strategy, position_size, risk_parameters
        )
        
        # 7. 更新交易记忆
        self.memory.update_decision(final_decision)
        
        return final_decision
```

## 核心功能模块

### 1. 分析综合模块

```python
def synthesize_analysis(self, analysis_data: Dict) -> Dict:
    """综合分析所有输入数据"""
    
    # 提取各类分析结果
    analyst_reports = analysis_data.get("analyst_reports", {})
    research_consensus = analysis_data.get("research_consensus", {})
    market_data = analysis_data.get("market_data", {})
    
    # 分析师报告权重
    analyst_weights = self.config.get("analyst_weights", {
        "fundamentals": 0.3,
        "technical": 0.3,
        "news": 0.2,
        "social": 0.2
    })
    
    # 计算加权分析评分
    weighted_scores = {}
    total_score = 0
    
    for analyst_type, weight in analyst_weights.items():
        if analyst_type in analyst_reports:
            score = analyst_reports[analyst_type].get("overall_score", 0.5)
            weighted_scores[analyst_type] = score * weight
            total_score += weighted_scores[analyst_type]
    
    # 研究员共识影响
    consensus_impact = self._assess_consensus_impact(research_consensus)
    
    # 综合评估
    synthesis = {
        "analyst_scores": weighted_scores,
        "total_analyst_score": total_score,
        "consensus_impact": consensus_impact,
        "adjusted_score": self._adjust_score_with_consensus(total_score, consensus_impact),
        "confidence_level": self._calculate_overall_confidence(analyst_reports, research_consensus),
        "key_factors": self._extract_key_factors(analyst_reports, research_consensus)
    }
    
    return synthesis

def _assess_consensus_impact(self, research_consensus: Dict) -> Dict:
    """评估研究员共识的影响"""
    
    consensus_strength = research_consensus.get("consensus_level", 0.5)
    recommendation = research_consensus.get("recommendation", "neutral")
    
    # 共识强度影响权重
    if consensus_strength > 0.8:
        impact_weight = 0.3  # 高共识，高影响
    elif consensus_strength > 0.6:
        impact_weight = 0.2  # 中等共识，中等影响
    else:
        impact_weight = 0.1  # 低共识，低影响
    
    # 推荐方向影响
    direction_impact = {
        "谨慎乐观": 0.15,
        "谨慎悲观": -0.15,
        "中性观望": 0.0
    }.get(recommendation, 0.0)
    
    return {
        "strength": consensus_strength,
        "weight": impact_weight,
        "direction": direction_impact,
        "net_impact": direction_impact * impact_weight
    }
```

### 2. 市场条件评估

```python
def assess_market_conditions(self, analysis_data: Dict) -> Dict:
    """评估当前市场条件"""
    
    market_indicators = {
        "volatility": self._assess_volatility(analysis_data),
        "liquidity": self._assess_liquidity(analysis_data),
        "sentiment": self._assess_market_sentiment(analysis_data),
        "trend": self._assess_market_trend(analysis_data),
        "correlation": self._assess_market_correlation(analysis_data)
    }
    
    # 市场环境分类
    market_regime = self._classify_market_regime(market_indicators)
    
    # 交易适宜性评估
    trading_suitability = self._assess_trading_suitability(market_indicators)
    
    return {
        "indicators": market_indicators,
        "regime": market_regime,
        "suitability": trading_suitability,
        "risk_level": self._calculate_market_risk_level(market_indicators)
    }

def _classify_market_regime(self, indicators: Dict) -> str:
    """分类市场环境"""
    
    volatility = indicators["volatility"]["level"]
    trend = indicators["trend"]["direction"]
    sentiment = indicators["sentiment"]["score"]
    
    if volatility == "low" and trend == "uptrend" and sentiment > 0.6:
        return "bull_market"
    elif volatility == "high" and trend == "downtrend" and sentiment < 0.4:
        return "bear_market"
    elif volatility == "high":
        return "volatile_market"
    else:
        return "sideways_market"

def _assess_trading_suitability(self, indicators: Dict) -> Dict:
    """评估交易适宜性"""
    
    suitability_score = 0.5
    factors = []
    
    # 波动性影响
    if indicators["volatility"]["level"] == "low":
        suitability_score += 0.1
        factors.append("低波动性有利于交易")
    elif indicators["volatility"]["level"] == "high":
        suitability_score -= 0.1
        factors.append("高波动性增加交易风险")
    
    # 流动性影响
    if indicators["liquidity"]["level"] == "high":
        suitability_score += 0.1
        factors.append("高流动性便于进出")
    
    # 趋势明确性影响
    if indicators["trend"]["strength"] > 0.7:
        suitability_score += 0.1
        factors.append("趋势明确有利于交易")
    
    return {
        "score": max(0.0, min(1.0, suitability_score)),
        "factors": factors,
        "recommendation": "适宜" if suitability_score > 0.6 else "谨慎" if suitability_score > 0.4 else "不适宜"
    }
```

### 3. 交易策略制定

```python
def develop_trading_strategy(self, analysis: Dict, market_conditions: Dict) -> Dict:
    """制定交易策略"""
    
    # 基于分析结果确定基本方向
    base_signal = self._determine_base_signal(analysis)
    
    # 根据市场条件调整策略
    adjusted_strategy = self._adjust_for_market_conditions(base_signal, market_conditions)
    
    # 选择交易类型
    trade_type = self._select_trade_type(adjusted_strategy, market_conditions)
    
    # 设定时间框架
    time_horizon = self._determine_time_horizon(adjusted_strategy, market_conditions)
    
    # 制定进出场策略
    entry_exit_strategy = self._develop_entry_exit_strategy(adjusted_strategy)
    
    return {
        "base_signal": base_signal,
        "adjusted_signal": adjusted_strategy,
        "trade_type": trade_type,
        "time_horizon": time_horizon,
        "entry_strategy": entry_exit_strategy["entry"],
        "exit_strategy": entry_exit_strategy["exit"],
        "confidence": self._calculate_strategy_confidence(analysis, market_conditions)
    }

def _determine_base_signal(self, analysis: Dict) -> Dict:
    """确定基本交易信号"""
    
    adjusted_score = analysis.get("adjusted_score", 0.5)
    confidence = analysis.get("confidence_level", 0.5)
    
    # 信号强度阈值
    strong_buy_threshold = 0.7
    buy_threshold = 0.6
    sell_threshold = 0.4
    strong_sell_threshold = 0.3
    
    if adjusted_score >= strong_buy_threshold and confidence > 0.7:
        signal = "strong_buy"
    elif adjusted_score >= buy_threshold:
        signal = "buy"
    elif adjusted_score <= strong_sell_threshold and confidence > 0.7:
        signal = "strong_sell"
    elif adjusted_score <= sell_threshold:
        signal = "sell"
    else:
        signal = "hold"
    
    return {
        "action": signal,
        "strength": abs(adjusted_score - 0.5) * 2,  # 0-1 scale
        "confidence": confidence,
        "score": adjusted_score
    }

def _select_trade_type(self, strategy: Dict, market_conditions: Dict) -> str:
    """选择交易类型"""
    
    signal_strength = strategy.get("strength", 0.5)
    market_regime = market_conditions.get("regime", "sideways_market")
    volatility = market_conditions["indicators"]["volatility"]["level"]
    
    # 根据信号强度和市场条件选择交易类型
    if signal_strength > 0.8 and market_regime in ["bull_market", "bear_market"]:
        return "momentum_trade"  # 动量交易
    elif signal_strength > 0.6 and volatility == "low":
        return "swing_trade"     # 波段交易
    elif market_regime == "sideways_market":
        return "range_trade"     # 区间交易
    else:
        return "position_trade"  # 仓位交易
```

### 4. 仓位管理

```python
def calculate_position_size(self, strategy: Dict) -> Dict:
    """计算仓位大小"""
    
    # 基础仓位大小 (基于信号强度)
    signal_strength = strategy.get("strength", 0.5)
    base_position = signal_strength * self.config.get("max_position_size", 0.1)
    
    # 风险调整
    risk_adjustment = self._calculate_risk_adjustment(strategy)
    
    # 市场条件调整
    market_adjustment = self._calculate_market_adjustment(strategy)
    
    # 最终仓位大小
    final_position = base_position * risk_adjustment * market_adjustment
    
    # 确保在限制范围内
    max_position = self.config.get("max_position_size", 0.1)
    min_position = self.config.get("min_position_size", 0.01)
    
    final_position = max(min_position, min(max_position, final_position))
    
    return {
        "base_size": base_position,
        "risk_adjustment": risk_adjustment,
        "market_adjustment": market_adjustment,
        "final_size": final_position,
        "size_rationale": self._explain_position_sizing(
            base_position, risk_adjustment, market_adjustment
        )
    }

def _calculate_risk_adjustment(self, strategy: Dict) -> float:
    """计算风险调整系数"""
    
    confidence = strategy.get("confidence", 0.5)
    trade_type = strategy.get("trade_type", "position_trade")
    
    # 基于置信度的调整
    confidence_adjustment = 0.5 + (confidence - 0.5)
    
    # 基于交易类型的调整
    type_adjustments = {
        "momentum_trade": 1.2,    # 动量交易可以稍大仓位
        "swing_trade": 1.0,       # 波段交易标准仓位
        "range_trade": 0.8,       # 区间交易较小仓位
        "position_trade": 0.9     # 仓位交易中等仓位
    }
    
    type_adjustment = type_adjustments.get(trade_type, 1.0)
    
    return confidence_adjustment * type_adjustment
```

### 5. 风险管理参数

```python
def set_risk_parameters(self, strategy: Dict) -> Dict:
    """设置风险管理参数"""
    
    trade_type = strategy.get("trade_type", "position_trade")
    signal_strength = strategy.get("strength", 0.5)
    time_horizon = strategy.get("time_horizon", "medium")
    
    # 止损设置
    stop_loss = self._calculate_stop_loss(trade_type, signal_strength)
    
    # 止盈设置
    take_profit = self._calculate_take_profit(trade_type, signal_strength)
    
    # 风险收益比
    risk_reward_ratio = take_profit / stop_loss if stop_loss > 0 else 0
    
    # 最大持有时间
    max_holding_period = self._determine_max_holding_period(time_horizon)
    
    return {
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risk_reward_ratio": risk_reward_ratio,
        "max_holding_period": max_holding_period,
        "position_monitoring": self._setup_position_monitoring(strategy),
        "exit_conditions": self._define_exit_conditions(strategy)
    }

def _calculate_stop_loss(self, trade_type: str, signal_strength: float) -> float:
    """计算止损水平"""
    
    base_stop_loss = {
        "momentum_trade": 0.03,   # 3% 止损
        "swing_trade": 0.05,      # 5% 止损
        "range_trade": 0.02,      # 2% 止损
        "position_trade": 0.08    # 8% 止损
    }.get(trade_type, 0.05)
    
    # 根据信号强度调整
    # 信号越强，可以容忍更大的回撤
    strength_adjustment = 1.0 + (signal_strength - 0.5) * 0.5
    
    return base_stop_loss * strength_adjustment

def _calculate_take_profit(self, trade_type: str, signal_strength: float) -> float:
    """计算止盈水平"""
    
    base_take_profit = {
        "momentum_trade": 0.08,   # 8% 止盈
        "swing_trade": 0.12,      # 12% 止盈
        "range_trade": 0.04,      # 4% 止盈
        "position_trade": 0.20    # 20% 止盈
    }.get(trade_type, 0.10)
    
    # 根据信号强度调整
    strength_adjustment = 1.0 + signal_strength * 0.5
    
    return base_take_profit * strength_adjustment
```

### 6. 最终决策生成

```python
def generate_final_decision(self, strategy: Dict, position: Dict, risk_params: Dict) -> Dict:
    """生成最终交易决策"""
    
    action = strategy["adjusted_signal"]["action"]
    
    # 构建决策结构
    decision = {
        "action": action,
        "quantity": position["final_size"],
        "confidence": strategy["confidence"],
        "strategy_type": strategy["trade_type"],
        "time_horizon": strategy["time_horizon"],
        
        # 风险管理
        "stop_loss": risk_params["stop_loss"],
        "take_profit": risk_params["take_profit"],
        "risk_reward_ratio": risk_params["risk_reward_ratio"],
        
        # 执行细节
        "entry_strategy": strategy["entry_strategy"],
        "exit_strategy": strategy["exit_strategy"],
        "max_holding_period": risk_params["max_holding_period"],
        
        # 决策依据
        "reasoning": self._generate_decision_reasoning(strategy, position, risk_params),
        "key_factors": strategy.get("key_factors", []),
        
        # 监控要求
        "monitoring_requirements": risk_params["position_monitoring"],
        "exit_conditions": risk_params["exit_conditions"],
        
        # 元数据
        "decision_timestamp": datetime.now().isoformat(),
        "decision_id": self._generate_decision_id(),
        "trader_style": self.trading_style,
        "risk_tolerance": self.risk_tolerance
    }
    
    return decision

def _generate_decision_reasoning(self, strategy: Dict, position: Dict, risk_params: Dict) -> str:
    """生成决策推理说明"""
    
    action = strategy["adjusted_signal"]["action"]
    confidence = strategy["confidence"]
    trade_type = strategy["trade_type"]
    
    reasoning_parts = []
    
    # 基本决策逻辑
    if action in ["buy", "strong_buy"]:
        reasoning_parts.append(f"基于综合分析，建议{action}该股票")
    elif action in ["sell", "strong_sell"]:
        reasoning_parts.append(f"基于综合分析，建议{action}该股票")
    else:
        reasoning_parts.append("当前分析结果建议持有观望")
    
    # 置信度说明
    if confidence > 0.8:
        reasoning_parts.append(f"决策置信度很高({confidence:.1%})")
    elif confidence > 0.6:
        reasoning_parts.append(f"决策置信度较高({confidence:.1%})")
    else:
        reasoning_parts.append(f"决策置信度中等({confidence:.1%})，建议谨慎操作")
    
    # 交易类型说明
    reasoning_parts.append(f"采用{trade_type}策略")
    
    # 风险管理说明
    reasoning_parts.append(
        f"设置{risk_params['stop_loss']:.1%}止损和{risk_params['take_profit']:.1%}止盈"
    )
    
    # 仓位说明
    reasoning_parts.append(f"建议仓位大小为{position['final_size']:.1%}")
    
    return "。".join(reasoning_parts) + "。"
```

### 7. 交易记忆管理

```python
class TradingMemory:
    """交易记忆管理"""
    
    def __init__(self):
        self.decision_history = []
        self.performance_metrics = {}
        self.learning_insights = []
    
    def update_decision(self, decision: Dict):
        """更新决策记录"""
        self.decision_history.append(decision)
        
        # 保持最近100个决策
        if len(self.decision_history) > 100:
            self.decision_history = self.decision_history[-100:]
    
    def learn_from_outcomes(self, decision_id: str, outcome: Dict):
        """从交易结果中学习"""
        
        # 找到对应的决策
        decision = self._find_decision(decision_id)
        if not decision:
            return
        
        # 分析决策质量
        decision_quality = self._analyze_decision_quality(decision, outcome)
        
        # 提取学习要点
        insights = self._extract_learning_insights(decision, outcome, decision_quality)
        
        # 更新学习记录
        self.learning_insights.extend(insights)
        
        # 更新性能指标
        self._update_performance_metrics(decision, outcome)
    
    def get_relevant_experience(self, current_situation: Dict) -> List[Dict]:
        """获取相关的历史经验"""
        
        relevant_decisions = []
        
        for decision in self.decision_history:
            similarity = self._calculate_situation_similarity(
                current_situation, decision
            )
            
            if similarity > 0.7:  # 相似度阈值
                relevant_decisions.append({
                    "decision": decision,
                    "similarity": similarity
                })
        
        # 按相似度排序
        relevant_decisions.sort(key=lambda x: x["similarity"], reverse=True)
        
        return relevant_decisions[:5]  # 返回最相似的5个决策
```

交易员智能体通过综合分析、策略制定、风险管理和持续学习，确保在复杂的市场环境中做出明智的投资决策。


<!-- docs/architecture/agent-architecture.md -->

# 智能体架构设计

## 概述

TradingAgents 框架采用专业化的多智能体架构，每个智能体都有明确的职责和专业领域。智能体之间通过结构化的通信协议进行协作，形成一个完整的金融决策系统。

## 智能体设计模式

### 基础智能体类

```python
class BaseAgent:
    """所有智能体的基础类"""
    
    def __init__(self, llm, config):
        self.llm = llm
        self.config = config
        self.memory = AgentMemory()
        self.tools = self._initialize_tools()
    
    def process(self, state: AgentState) -> AgentState:
        """处理输入状态并返回更新后的状态"""
        pass
    
    def _initialize_tools(self):
        """初始化智能体专用工具"""
        pass
```

### 智能体状态管理

```python
class AgentState:
    """智能体状态数据结构"""
    
    ticker: str                    # 股票代码
    date: str                     # 分析日期
    analyst_reports: Dict         # 分析师报告
    research_reports: Dict        # 研究员报告
    trader_decision: Dict         # 交易决策
    risk_assessment: Dict         # 风险评估
    portfolio_decision: Dict      # 投资组合决策
    messages: List[BaseMessage]   # 消息历史
```

## 智能体分类与职责

### 1. 分析师团队 (Analysts)

#### 基本面分析师 (Fundamentals Analyst)
```python
class FundamentalsAnalyst(BaseAgent):
    """基本面分析师 - 分析公司财务和基本面数据"""
    
    专业领域:
    - 财务报表分析
    - 估值模型计算
    - 行业对比分析
    - 盈利能力评估
    
    输入数据:
    - 财务报表数据
    - 行业数据
    - 宏观经济指标
    
    输出结果:
    - 基本面评分
    - 估值建议
    - 财务健康度评估
```

#### 技术分析师 (Market Analyst)
```python
class MarketAnalyst(BaseAgent):
    """技术分析师 - 分析技术指标和价格趋势"""
    
    专业领域:
    - 技术指标计算 (RSI, MACD, 布林带等)
    - 趋势分析
    - 支撑阻力位识别
    - 交易信号生成
    
    输入数据:
    - 历史价格数据
    - 交易量数据
    - 技术指标数据
    
    输出结果:
    - 技术分析评分
    - 趋势方向判断
    - 关键价位识别
```

#### 新闻分析师 (News Analyst)
```python
class NewsAnalyst(BaseAgent):
    """新闻分析师 - 分析新闻事件和宏观因素"""
    
    专业领域:
    - 新闻情感分析
    - 事件影响评估
    - 宏观经济分析
    - 政策影响分析
    
    输入数据:
    - 新闻文章
    - 经济数据发布
    - 政策公告
    
    输出结果:
    - 新闻情感评分
    - 事件影响评估
    - 宏观趋势判断
```

#### 社交媒体分析师 (Social Media Analyst)
```python
class SocialMediaAnalyst(BaseAgent):
    """社交媒体分析师 - 分析社交媒体情绪"""
    
    专业领域:
    - 社交媒体情感分析
    - 舆论趋势监测
    - 热点话题识别
    - 投资者情绪评估
    
    输入数据:
    - Reddit 讨论数据
    - Twitter 情感数据
    - 论坛讨论内容
    
    输出结果:
    - 社交情感评分
    - 舆论趋势分析
    - 投资者情绪指标
```

### 2. 研究员团队 (Researchers)

#### 看涨研究员 (Bull Researcher)
```python
class BullResearcher(BaseAgent):
    """看涨研究员 - 从乐观角度评估投资机会"""
    
    职责:
    - 识别积极因素
    - 评估上涨潜力
    - 提供乐观预期
    - 挑战悲观观点
    
    分析重点:
    - 增长机会
    - 市场优势
    - 正面催化剂
    - 估值吸引力
```

#### 看跌研究员 (Bear Researcher)
```python
class BearResearcher(BaseAgent):
    """看跌研究员 - 从悲观角度评估投资风险"""
    
    职责:
    - 识别风险因素
    - 评估下跌风险
    - 提供谨慎预期
    - 挑战乐观观点
    
    分析重点:
    - 潜在风险
    - 市场威胁
    - 负面催化剂
    - 估值过高风险
```

### 3. 交易执行 (Trader)

#### 交易员 (Trader)
```python
class Trader(BaseAgent):
    """交易员 - 制定最终交易决策"""
    
    职责:
    - 综合各方分析
    - 制定交易策略
    - 确定仓位大小
    - 设置止损止盈
    
    决策因素:
    - 分析师报告
    - 研究员辩论结果
    - 风险评估
    - 市场条件
```

### 4. 风险管理团队 (Risk Management)

#### 风险评估智能体
```python
class RiskDebator(BaseAgent):
    """风险评估智能体基类"""
    
    风险评估维度:
    - 市场风险
    - 流动性风险
    - 信用风险
    - 操作风险
    
    评估方法:
    - VaR 计算
    - 压力测试
    - 情景分析
    - 相关性分析
```

- **激进风险评估**: 支持高风险高收益策略
- **保守风险评估**: 强调风险控制和资本保护
- **中性风险评估**: 平衡风险和收益

### 5. 管理层 (Managers)

#### 研究经理 (Research Manager)
```python
class ResearchManager(BaseAgent):
    """研究经理 - 协调研究员团队工作"""
    
    职责:
    - 组织研究员辩论
    - 平衡不同观点
    - 形成研究共识
    - 质量控制
```

#### 风险经理 (Risk Manager)
```python
class RiskManager(BaseAgent):
    """风险经理 - 管理整体风险控制"""
    
    职责:
    - 协调风险评估
    - 制定风险政策
    - 监控风险指标
    - 最终风险决策
```

## 智能体交互模式

### 1. 并行分析阶段
```mermaid
graph LR
    Input[市场数据] --> FA[基本面分析师]
    Input --> MA[技术分析师]
    Input --> NA[新闻分析师]
    Input --> SA[社交媒体分析师]
    
    FA --> Reports[分析报告]
    MA --> Reports
    NA --> Reports
    SA --> Reports
```

### 2. 研究辩论阶段
```mermaid
graph TB
    Reports[分析报告] --> RM[研究经理]
    RM --> BR[看涨研究员]
    RM --> BEAR[看跌研究员]
    
    BR --> Debate[结构化辩论]
    BEAR --> Debate
    
    Debate --> Consensus[研究共识]
```

### 3. 交易决策阶段
```mermaid
graph TB
    Consensus[研究共识] --> Trader[交易员]
    Trader --> Decision[交易决策]
    
    Decision --> RiskTeam[风险管理团队]
    RiskTeam --> RiskManager[风险经理]
    RiskManager --> FinalDecision[最终决策]
```

## 智能体通信协议

### 消息格式
```python
class AgentMessage:
    sender: str           # 发送者ID
    receiver: str         # 接收者ID
    message_type: str     # 消息类型
    content: Dict         # 消息内容
    timestamp: datetime   # 时间戳
    priority: int         # 优先级
```

### 通信类型
1. **分析报告**: 分析师向系统提交分析结果
2. **辩论消息**: 研究员之间的观点交换
3. **决策请求**: 请求其他智能体提供意见
4. **风险警告**: 风险管理团队的风险提醒
5. **最终决策**: 最终的交易决策通知

## 智能体配置

### 配置参数
```python
agent_config = {
    "llm_model": "gpt-4o",           # 使用的LLM模型
    "temperature": 0.1,              # 生成温度
    "max_tokens": 2000,              # 最大token数
    "tools_enabled": True,           # 是否启用工具
    "memory_enabled": True,          # 是否启用记忆
    "debate_rounds": 3,              # 辩论轮数
    "confidence_threshold": 0.7,     # 置信度阈值
}
```

### 专业化配置
每个智能体都有特定的配置参数，以优化其专业领域的表现：

- **分析师**: 专注于数据分析和模式识别
- **研究员**: 优化辩论和批判性思维
- **交易员**: 强化决策制定和风险评估
- **风险管理**: 专注于风险识别和量化

这种专业化的智能体架构确保了系统能够从多个角度全面分析市场，并通过协作机制形成高质量的投资决策。


<!-- docs/architecture/configuration-optimization.md -->

# 配置管理和数据库架构优化指南

## 📋 概述

本文档详细说明了TradingAgents项目在v0.1.2版本中进行的重大架构优化，主要解决了配置管理混乱和数据库管理器重复的问题。

## 🎯 优化目标

### 解决的问题
1. **配置管理混乱**：多个配置源（.env、default_config.py、JSON文件）导致配置冲突
2. **数据库管理器重复**：两个功能重叠的数据库管理器造成维护困难
3. **启用开关失效**：数据库启用开关不生效，即使禁用仍会连接
4. **布尔值判断错误**：MongoDB对象布尔值判断导致运行时错误

### 优化成果
- ✅ **配置管理统一**：只使用.env文件管理数据库配置
- ✅ **数据库管理器统一**：移除重复组件，使用单一管理器
- ✅ **启用开关生效**：正确遵守MONGODB_ENABLED和REDIS_ENABLED设置
- ✅ **错误修复**：解决所有MongoDB布尔值判断错误

## 🏗️ 架构变更

### 优化前的架构问题

```
配置管理混乱：
.env文件 ──┐
           ├─→ 配置冲突和优先级不明
default_config.py ──┘

数据库管理器重复：
tradingagents.config.database_manager ──┐
                                        ├─→ 功能重叠
tradingagents.dataflows.database_manager ──┘
```

### 优化后的清晰架构

```
统一配置管理：
.env文件 (唯一配置源)
    ↓
tradingagents.config.database_manager (统一管理器)
    ↓
自动检测 + 智能降级
    ↓
文件缓存 / MongoDB / Redis
```

## 📝 配置管理优化

### 1. 移除default_config.py中的数据库配置

**优化前**：
```python
# tradingagents/default_config.py
"database": {
    "mongodb": {
        "enabled": True,  # 硬编码，无法通过.env控制
        "host": os.getenv("MONGODB_HOST", "localhost"),
        # ...
    }
}
```

**优化后**：
```python
# tradingagents/default_config.py
# Note: Database configuration is now managed by .env file and config.database_manager
# No database settings in default config to avoid configuration conflicts
```

### 2. 统一使用.env文件管理数据库配置

**配置示例**：
```env
# 数据库启用开关 (默认禁用)
MONGODB_ENABLED=false
REDIS_ENABLED=false

# MongoDB配置
MONGODB_HOST=localhost
MONGODB_PORT=27018
MONGODB_USERNAME=admin
MONGODB_PASSWORD=tradingagents123
MONGODB_DATABASE=tradingagents
MONGODB_AUTH_SOURCE=admin

# Redis配置
REDIS_HOST=localhost
REDIS_PORT=6380
REDIS_PASSWORD=tradingagents123
REDIS_DB=0
```

## 🔧 数据库管理器统一

### 1. 移除旧的数据库管理器

**删除的文件**：
- `tradingagents/dataflows/database_manager.py`

**保留的统一管理器**：
- `tradingagents/config/database_manager.py`

### 2. 更新所有引用

**更新的文件**：
```
tradingagents/dataflows/tdx_utils.py
tradingagents/dataflows/stock_data_service.py
scripts/setup/setup_databases.py
scripts/setup/init_database.py
tests/test_database_fix.py
docs/database_setup.md
```

**导入更改**：
```python
# 修改前
from tradingagents.dataflows.database_manager import get_database_manager

# 修改后
from tradingagents.config.database_manager import get_database_manager
```

## 🛠️ 布尔值判断错误修复

### 问题说明
PyMongo的数据库对象重写了`__bool__`方法，直接进行布尔值判断会抛出`NotImplementedError`。

### 修复方案

**错误的判断方式**：
```python
if mongodb_db:  # ❌ 会抛出NotImplementedError
    # 执行操作
```

**正确的判断方式**：
```python
# 方式1：使用is not None
if mongodb_db is not None:  # ✅ 安全
    # 执行操作

# 方式2：使用专门的方法
if db_manager.is_mongodb_available():  # ✅ 推荐
    # 执行操作
```

## 📋 使用指南

### 1. 基本配置

编辑项目根目录的`.env`文件：

```env
# 禁用所有数据库（默认配置）
MONGODB_ENABLED=false
REDIS_ENABLED=false

# 启用MongoDB
MONGODB_ENABLED=true
MONGODB_HOST=localhost
MONGODB_PORT=27018
# ... 其他MongoDB配置

# 启用Redis
REDIS_ENABLED=true
REDIS_HOST=localhost
REDIS_PORT=6380
# ... 其他Redis配置
```

### 2. 代码使用

```python
from tradingagents.config.database_manager import get_database_manager

# 获取统一数据库管理器
db_manager = get_database_manager()

# 检查数据库可用性
if db_manager.is_mongodb_available():
    print("MongoDB可用")

if db_manager.is_redis_available():
    print("Redis可用")

# 获取缓存后端信息
backend = db_manager.get_cache_backend()  # "file", "mongodb", "redis"

# 获取数据库客户端
mongodb_client = db_manager.get_mongodb_client()
redis_client = db_manager.get_redis_client()
```

### 3. 系统行为

**当数据库禁用时**：
- ✅ 系统不会尝试连接数据库
- ✅ 自动使用文件缓存
- ✅ 不会出现连接错误消息
- ✅ 所有功能正常工作

**当数据库启用但不可用时**：
- ✅ 系统自动检测连接失败
- ✅ 自动降级到文件缓存
- ✅ 记录警告日志但不影响功能

## 🔍 验证优化效果

### 1. 检查配置生效

```bash
# 设置禁用数据库
echo "MONGODB_ENABLED=false" >> .env
echo "REDIS_ENABLED=false" >> .env

# 运行系统，应该看到：
# - 没有数据库连接消息
# - 使用文件缓存
# - 没有布尔值判断错误
```

### 2. 检查启用开关

```python
import os
from tradingagents.config.database_manager import get_database_manager

# 检查环境变量
print(f"MONGODB_ENABLED: {os.getenv('MONGODB_ENABLED', 'false')}")
print(f"REDIS_ENABLED: {os.getenv('REDIS_ENABLED', 'false')}")

# 检查管理器状态
db_manager = get_database_manager()
print(f"MongoDB可用: {db_manager.is_mongodb_available()}")
print(f"Redis可用: {db_manager.is_redis_available()}")

# 两者应该一致
```

## 📚 相关文档

- [数据库配置指南](../database_setup.md)
- [环境配置说明](../configuration/environment-setup.md)
- [缓存系统文档](../caching/cache-system.md)

## 🎉 总结

本次架构优化显著提升了项目的可维护性和用户体验：

1. **配置更简单**：只需编辑.env文件
2. **行为更可预测**：启用开关真正生效
3. **架构更清晰**：移除重复组件
4. **错误更少**：修复了所有已知的布尔值判断问题

这些改进为项目的后续发展奠定了更加稳固的基础。


<!-- docs/architecture/data-flow-architecture.md -->

# 数据流架构

## 概述

TradingAgents 的数据流架构设计用于高效地获取、处理和分发金融数据。系统支持多种数据源，实现了统一的数据接口，并提供了强大的缓存和处理机制。

## 数据流架构图

```mermaid
graph TB
    subgraph "外部数据源"
        FINNHUB[FinnHub API<br/>实时金融数据]
        YAHOO[Yahoo Finance<br/>历史价格数据]
        REDDIT[Reddit API<br/>社交媒体数据]
        GNEWS[Google News<br/>新闻数据]
        CUSTOM[自定义数据源<br/>扩展接口]
    end
    
    subgraph "数据获取层"
        FUTILS[FinnHub Utils]
        YUTILS[YFinance Utils]
        RUTILS[Reddit Utils]
        NUTILS[News Utils]
        SUTILS[StockStats Utils]
    end
    
    subgraph "数据处理层"
        INTERFACE[Data Interface]
        PROCESSOR[Data Processor]
        VALIDATOR[Data Validator]
        TRANSFORMER[Data Transformer]
    end
    
    subgraph "缓存层"
        CACHE[Data Cache]
        REDIS[Redis Cache]
        LOCAL[Local Cache]
        MEMORY[Memory Cache]
    end
    
    subgraph "数据分发层"
        DISPATCHER[Data Dispatcher]
        ROUTER[Data Router]
        FORMATTER[Data Formatter]
    end
    
    subgraph "智能体消费层"
        ANALYSTS[分析师团队]
        RESEARCHERS[研究员团队]
        TRADER[交易员]
        RISK[风险管理]
    end
    
    FINNHUB --> FUTILS
    YAHOO --> YUTILS
    REDDIT --> RUTILS
    GNEWS --> NUTILS
    CUSTOM --> SUTILS
    
    FUTILS --> INTERFACE
    YUTILS --> INTERFACE
    RUTILS --> INTERFACE
    NUTILS --> INTERFACE
    SUTILS --> INTERFACE
    
    INTERFACE --> PROCESSOR
    PROCESSOR --> VALIDATOR
    VALIDATOR --> TRANSFORMER
    
    TRANSFORMER --> CACHE
    CACHE --> REDIS
    CACHE --> LOCAL
    CACHE --> MEMORY
    
    CACHE --> DISPATCHER
    DISPATCHER --> ROUTER
    ROUTER --> FORMATTER
    
    FORMATTER --> ANALYSTS
    FORMATTER --> RESEARCHERS
    FORMATTER --> TRADER
    FORMATTER --> RISK
```

## 数据源详解

### 1. FinnHub API
```python
class FinnHubUtils:
    """FinnHub 数据获取工具"""
    
    支持的数据类型:
    - 实时股价数据
    - 公司基本信息
    - 财务报表数据
    - 新闻和公告
    - 技术指标
    - 市场情绪指标
    
    API限制:
    - 免费版: 60 calls/minute
    - 付费版: 更高频率限制
    
    数据格式:
    {
        "symbol": "AAPL",
        "price": 150.25,
        "change": 2.15,
        "changePercent": 1.45,
        "timestamp": 1640995200
    }
```

### 2. Yahoo Finance
```python
class YFinanceUtils:
    """Yahoo Finance 数据获取工具"""
    
    支持的数据类型:
    - 历史价格数据
    - 股票分割信息
    - 股息数据
    - 期权数据
    - 财务指标
    
    优势:
    - 免费使用
    - 数据覆盖面广
    - 历史数据丰富
    
    数据格式:
    {
        "Date": "2024-01-01",
        "Open": 148.50,
        "High": 152.30,
        "Low": 147.80,
        "Close": 150.25,
        "Volume": 45678900
    }
```

### 3. Reddit API
```python
class RedditUtils:
    """Reddit 社交媒体数据获取工具"""
    
    支持的数据类型:
    - 热门帖子
    - 评论情感
    - 用户讨论热度
    - 关键词提及频率
    
    分析维度:
    - 情感极性 (正面/负面/中性)
    - 讨论热度
    - 用户参与度
    - 话题趋势
    
    数据格式:
    {
        "post_id": "abc123",
        "title": "AAPL earnings discussion",
        "score": 1250,
        "comments": 89,
        "sentiment": 0.65,
        "timestamp": 1640995200
    }
```

### 4. Google News
```python
class GoogleNewsUtils:
    """Google News 新闻数据获取工具"""
    
    支持的数据类型:
    - 相关新闻文章
    - 新闻情感分析
    - 事件时间线
    - 影响力评估
    
    处理流程:
    1. 关键词搜索
    2. 新闻筛选
    3. 内容提取
    4. 情感分析
    5. 影响力评估
    
    数据格式:
    {
        "title": "Apple reports strong Q4 earnings",
        "source": "Reuters",
        "published": "2024-01-01T10:00:00Z",
        "sentiment": 0.8,
        "relevance": 0.95,
        "impact_score": 0.7
    }
```

## 数据处理流程

### 1. 数据获取阶段
```python
class DataAcquisition:
    """数据获取协调器"""
    
    def fetch_data(self, symbol: str, date: str) -> Dict:
        """获取指定股票和日期的所有数据"""
        
        # 并行获取各类数据
        tasks = [
            self.fetch_price_data(symbol, date),
            self.fetch_fundamental_data(symbol),
            self.fetch_news_data(symbol, date),
            self.fetch_social_data(symbol, date),
            self.fetch_technical_data(symbol, date)
        ]
        
        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        
        # 整合数据
        return self.integrate_data(results)
```

### 2. 数据验证阶段
```python
class DataValidator:
    """数据验证器"""
    
    验证规则:
    - 数据完整性检查
    - 数据类型验证
    - 数值范围检查
    - 时间戳验证
    - 异常值检测
    
    def validate(self, data: Dict) -> Tuple[bool, List[str]]:
        """验证数据质量"""
        errors = []
        
        # 检查必需字段
        if not self.check_required_fields(data):
            errors.append("Missing required fields")
        
        # 检查数据类型
        if not self.check_data_types(data):
            errors.append("Invalid data types")
        
        # 检查数值范围
        if not self.check_value_ranges(data):
            errors.append("Values out of range")
        
        return len(errors) == 0, errors
```

### 3. 数据转换阶段
```python
class DataTransformer:
    """数据转换器"""
    
    转换功能:
    - 数据标准化
    - 单位统一
    - 格式转换
    - 特征工程
    - 数据聚合
    
    def transform(self, raw_data: Dict) -> Dict:
        """转换原始数据为标准格式"""
        
        transformed = {}
        
        # 价格数据标准化
        transformed['price_data'] = self.normalize_prices(
            raw_data['price_data']
        )
        
        # 财务数据转换
        transformed['financial_data'] = self.convert_financials(
            raw_data['financial_data']
        )
        
        # 情感数据聚合
        transformed['sentiment_data'] = self.aggregate_sentiment(
            raw_data['news_data'],
            raw_data['social_data']
        )
        
        return transformed
```

## 缓存策略

### 1. 多层缓存架构
```python
class CacheManager:
    """缓存管理器"""
    
    缓存层次:
    1. 内存缓存 (最快访问)
    2. 本地文件缓存 (持久化)
    3. Redis缓存 (分布式)
    4. 数据库缓存 (长期存储)
    
    def get_data(self, key: str) -> Optional[Dict]:
        """按优先级获取缓存数据"""
        
        # 1. 检查内存缓存
        if data := self.memory_cache.get(key):
            return data
        
        # 2. 检查本地缓存
        if data := self.local_cache.get(key):
            self.memory_cache.set(key, data)
            return data
        
        # 3. 检查Redis缓存
        if data := self.redis_cache.get(key):
            self.local_cache.set(key, data)
            self.memory_cache.set(key, data)
            return data
        
        return None
```

### 2. 缓存策略
```python
缓存配置:
{
    "price_data": {
        "ttl": 300,        # 5分钟过期
        "refresh": "auto"   # 自动刷新
    },
    "fundamental_data": {
        "ttl": 86400,      # 24小时过期
        "refresh": "manual" # 手动刷新
    },
    "news_data": {
        "ttl": 3600,       # 1小时过期
        "refresh": "auto"   # 自动刷新
    },
    "social_data": {
        "ttl": 1800,       # 30分钟过期
        "refresh": "auto"   # 自动刷新
    }
}
```

## 数据分发机制

### 1. 数据路由
```python
class DataRouter:
    """数据路由器"""
    
    路由规则:
    - 基本面数据 → 基本面分析师
    - 技术数据 → 技术分析师
    - 新闻数据 → 新闻分析师
    - 社交数据 → 社交媒体分析师
    - 综合数据 → 所有智能体
    
    def route_data(self, data: Dict, agents: List[str]) -> Dict:
        """根据智能体类型分发相应数据"""
        
        routed_data = {}
        
        for agent in agents:
            if agent == "fundamentals_analyst":
                routed_data[agent] = {
                    "financial_data": data["financial_data"],
                    "company_info": data["company_info"],
                    "industry_data": data["industry_data"]
                }
            elif agent == "technical_analyst":
                routed_data[agent] = {
                    "price_data": data["price_data"],
                    "volume_data": data["volume_data"],
                    "technical_indicators": data["technical_indicators"]
                }
            # ... 其他智能体的路由规则
        
        return routed_data
```

### 2. 数据格式化
```python
class DataFormatter:
    """数据格式化器"""
    
    def format_for_agent(self, data: Dict, agent_type: str) -> Dict:
        """为特定智能体格式化数据"""
        
        if agent_type == "fundamentals_analyst":
            return self.format_fundamental_data(data)
        elif agent_type == "technical_analyst":
            return self.format_technical_data(data)
        elif agent_type == "news_analyst":
            return self.format_news_data(data)
        elif agent_type == "social_analyst":
            return self.format_social_data(data)
        
        return data
```

## 性能优化

### 1. 并行处理
- 多线程数据获取
- 异步API调用
- 并行数据处理

### 2. 智能缓存
- 预测性缓存
- 热数据预加载
- 缓存命中率优化

### 3. 数据压缩
- 数据压缩存储
- 增量数据传输
- 数据去重

### 4. 错误处理
- 数据源故障转移
- 重试机制
- 降级策略

这种数据流架构确保了系统能够高效、可靠地处理大量金融数据，为智能体提供高质量的数据支持。


<!-- docs/architecture/database-architecture.md -->

# TradingAgents-CN 数据库架构设计

## 1. 概述

本文档详细描述了 TradingAgents-CN 项目的数据库架构设计，包括 MongoDB 和 Redis 的集成方案。该架构旨在提供高性能、可扩展、高可用的数据管理解决方案，以支持多智能体交易系统的数据需求。

## 2. 架构概览

TradingAgents-CN 采用多层数据架构：

```mermaid
graph TD
    A[应用层] --> B[数据访问抽象层]
    B --> C[Redis 缓存层]
    B --> D[MongoDB 持久层]
    B --> E[文件存储层]
    C -.-> D
    D -.-> E
```

### 2.1 核心组件

| 组件 | 角色 | 主要职责 |
|-----|-----|---------|
| **Redis** | 缓存层 | 提供高速数据访问，减轻数据库负担 |
| **MongoDB** | 持久层 | 存储结构化和半结构化数据 |
| **文件存储** | 备份层 | 提供数据备份和历史归档 |
| **数据访问抽象层** | 中间层 | 统一数据访问接口，管理缓存策略 |

## 3. MongoDB 数据模型

### 3.1 数据库结构

```
mongodb://localhost:27017/tradingagents
├── market_data                # 集合：市场数据
│   ├── { symbol: "AAPL", date: "2023-05-15", open: 150.25, ... }
│   └── { symbol: "GOOGL", date: "2023-05-15", open: 2500.10, ... }
├── fundamental_data          # 集合：基本面数据
│   ├── { symbol: "AAPL", period: "2023Q1", revenue: 94.8, ... }
│   └── { symbol: "GOOGL", period: "2023Q1", revenue: 69.8, ... }
├── news_data                 # 集合：新闻数据
│   ├── { symbol: "AAPL", timestamp: "2023-05-15T08:30:00", title: "...", ... }
│   └── { symbol: "MARKET", timestamp: "2023-05-15T09:15:00", title: "...", ... }
├── social_data               # 集合：社交媒体数据
│   └── { symbol: "AAPL", source: "reddit", timestamp: "...", sentiment: 0.75, ... }
├── analysis_results          # 集合：分析结果
│   └── { symbol: "AAPL", date: "2023-05-15", analyst: "market", decision: "BUY", ... }
└── metadata                  # 集合：元数据
    ├── { type: "sync_status", last_update: "2023-05-15T10:00:00", ... }
    └── { type: "data_catalog", schema_version: "1.0", ... }
```

### 3.2 索引策略

| 集合 | 索引 | 类型 | 目的 |
|-----|-----|------|-----|
| **market_data** | `{ symbol: 1, date: 1 }` | 复合索引 | 快速查询特定股票的历史数据 |
| **market_data** | `{ date: 1 }` | 单字段索引 | 按日期查询市场数据 |
| **fundamental_data** | `{ symbol: 1, period: 1 }` | 复合索引 | 快速查询特定股票的财务数据 |
| **news_data** | `{ symbol: 1, timestamp: -1 }` | 复合索引 | 按时间倒序查询新闻 |
| **news_data** | `{ timestamp: -1 }` | 单字段索引 | 获取最新新闻 |
| **social_data** | `{ symbol: 1, timestamp: -1 }` | 复合索引 | 按时间倒序查询社交数据 |
| **analysis_results** | `{ symbol: 1, date: -1 }` | 复合索引 | 查询最新分析结果 |

### 3.3 文档模型示例

```json
// market_data 集合文档示例
{
  "_id": ObjectId("..."),
  "symbol": "AAPL",
  "market": "us",
  "date": "2023-05-15",
  "open": 150.25,
  "high": 152.30,
  "low": 149.80,
  "close": 151.75,
  "volume": 75482365,
  "adjusted_close": 151.75,
  "source": "finnhub",
  "created_at": ISODate("2023-05-15T20:00:00Z"),
  "updated_at": ISODate("2023-05-15T20:00:00Z")
}

// fundamental_data 集合文档示例
{
  "_id": ObjectId("..."),
  "symbol": "AAPL",
  "period": "2023Q1",
  "report_type": "income_statement",
  "currency": "USD",
  "revenue": 94800000000,
  "gross_profit": 41500000000,
  "net_income": 24160000000,
  "eps": 1.52,
  "source": "simfin",
  "filing_date": "2023-04-28",
  "created_at": ISODate("2023-04-28T18:30:00Z"),
  "updated_at": ISODate("2023-04-28T18:30:00Z")
}
```

## 4. Redis 缓存设计

### 4.1 键空间设计

```
Redis 实例 (localhost:6379)
├── ta:price:{symbol}:{timeframe}     # 价格数据缓存
├── ta:quote:{symbol}                 # 实时报价缓存
├── ta:news:{symbol}                  # 新闻数据缓存
├── ta:social:{symbol}                # 社交媒体数据缓存
├── ta:analysis:{symbol}:{analyst}    # 分析结果缓存
├── ta:stats:{symbol}                 # 统计数据缓存
├── ta:locks:{resource}               # 分布式锁
└── ta:jobs:{job_id}                  # 后台任务状态
```

### 4.2 数据结构与TTL策略

| 缓存键模式 | 数据类型 | TTL | 用途 |
|-----------|---------|-----|-----|
| `ta:price:{symbol}:daily` | Hash | 1天 | 日线价格数据 |
| `ta:price:{symbol}:intraday` | Hash | 5分钟 | 分钟级价格数据 |
| `ta:quote:{symbol}` | Hash | 1分钟 | 实时报价 |
| `ta:news:{symbol}` | List | 15分钟 | 最新新闻 |
| `ta:news:market` | List | 10分钟 | 市场新闻 |
| `ta:social:{symbol}` | Sorted Set | 5分钟 | 社交媒体情绪 |
| `ta:analysis:{symbol}:{date}` | Hash | 1小时 | 分析结果 |
| `ta:stats:{symbol}` | Hash | 1天 | 统计数据 |

### 4.3 数据结构示例

```
# 价格数据 (Hash)
HSET ta:price:AAPL:daily 2023-05-15 "{'open':150.25,'high':152.30,'low':149.80,'close':151.75,'volume':75482365}"
EXPIRE ta:price:AAPL:daily 86400

# 实时报价 (Hash)
HSET ta:quote:AAPL price 151.75 change 1.25 percent 0.83 volume 75482365 updated_at 1684180800
EXPIRE ta:quote:AAPL 60

# 新闻数据 (List)
LPUSH ta:news:AAPL "{'id':'n12345','title':'Apple Announces New iPhone','timestamp':'2023-05-15T14:30:00Z','source':'reuters'}"
EXPIRE ta:news:AAPL 900

# 社交媒体情绪 (Sorted Set，按时间戳排序)
ZADD ta:social:AAPL 1684180800 "{'source':'reddit','sentiment':0.75,'mentions':120,'timestamp':1684180800}"
EXPIRE ta:social:AAPL 300
```

## 5. 数据流设计

### 5.1 读取流程

```mermaid
graph TD
    A[请求数据] --> B{Redis缓存?}
    B -->|是| C[返回缓存数据]
    B -->|否| D{MongoDB?}
    D -->|是| E[查询MongoDB]
    D -->|否| F{文件存储?}
    F -->|是| G[读取文件]
    F -->|否| H[API获取]
    
    E --> I[更新Redis缓存]
    G --> I
    H --> J[写入MongoDB]
    J --> I
    
    I --> C
```

### 5.2 写入流程

```mermaid
graph TD
    A[新数据] --> B[数据验证]
    B --> C[写入MongoDB]
    C --> D[更新Redis缓存]
    C --> E{需要备份?}
    E -->|是| F[写入文件存储]
    E -->|否| G[完成]
    D --> G
    F --> G
```

### 5.3 缓存同步策略

| 同步类型 | 触发条件 | 同步方向 | 实现方式 |
|---------|---------|---------|---------|
| **写入同步** | 数据更新 | API → MongoDB → Redis | 写入管道 |
| **缓存失效** | TTL过期 | MongoDB → Redis | 按需加载 |
| **定期同步** | 定时任务 | MongoDB → Redis | 后台任务 |
| **全量同步** | 系统启动 | MongoDB → Redis | 启动脚本 |

## 6. 数据访问层设计

### 6.1 抽象接口

```python
class DataAccess:
    """数据访问抽象层，统一管理MongoDB和Redis访问"""
    
    def __init__(self, config=None):
        self.config = config or DATABASE_CONFIG
        self.mongo_client = pymongo.MongoClient(self.config["mongodb"]["uri"])
        self.db = self.mongo_client[self.config["mongodb"]["db_name"]]
        self.redis_client = redis.Redis(
            host=self.config["redis"]["host"],
            port=self.config["redis"]["port"],
            db=self.config["redis"]["db"],
            password=self.config["redis"]["password"]
        )
        
    def get_price_data(self, symbol, start_date, end_date=None, timeframe="daily"):
        """获取价格数据，优先从缓存获取"""
        # 实现代码...
        
    def get_fundamental_data(self, symbol, period=None, report_type=None):
        """获取基本面数据"""
        # 实现代码...
        
    def get_news_data(self, symbol=None, start_time=None, limit=20):
        """获取新闻数据"""
        # 实现代码...
        
    def get_social_data(self, symbol, start_time=None, limit=20):
        """获取社交媒体数据"""
        # 实现代码...
        
    def get_analysis_results(self, symbol, date=None, analyst=None):
        """获取分析结果"""
        # 实现代码...
        
    def save_price_data(self, symbol, data, timeframe="daily"):
        """保存价格数据"""
        # 实现代码...
        
    # 其他数据访问方法...
```

### 6.2 分布式锁实现

```python
def acquire_lock(resource_name, timeout=10):
    """获取分布式锁"""
    lock_key = f"ta:locks:{resource_name}"
    lock_value = str(uuid.uuid4())
    
    # 尝试获取锁，设置过期时间防止死锁
    acquired = redis_client.set(lock_key, lock_value, nx=True, ex=timeout)
    
    if acquired:
        return lock_value
    return None

def release_lock(resource_name, lock_value):
    """释放分布式锁"""
    lock_key = f"ta:locks:{resource_name}"
    
    # 使用Lua脚本确保原子性操作
    script = """
    if redis.call('get', KEYS[1]) == ARGV[1] then
        return redis.call('del', KEYS[1])
    else
        return 0
    end
    """
    redis_client.eval(script, 1, lock_key, lock_value)
```

## 7. 配置设计

### 7.1 MongoDB 配置

```yaml
# MongoDB 配置文件
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
  directoryPerDB: true
  wiredTiger:
    engineConfig:
      cacheSizeGB: 2
      journalCompressor: snappy

systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true

net:
  port: 27017
  bindIp: 127.0.0.1

security:
  authorization: enabled

processManagement:
  timeZoneInfo: /usr/share/zoneinfo
```

### 7.2 Redis 配置

```
# Redis 配置文件
port 6379
bind 127.0.0.1
protected-mode yes

# 内存配置
maxmemory 1gb
maxmemory-policy allkeys-lru

# 持久化配置
appendonly yes
appendfsync everysec

# 超时配置
timeout 0

# 日志配置
loglevel notice
logfile /var/log/redis/redis-server.log

# 数据库数量
databases 16

# 性能优化
tcp-keepalive 300
```

### 7.3 应用配置

```python
DATABASE_CONFIG = {
    "mongodb": {
        "uri": "mongodb://localhost:27017/",
        "db_name": "tradingagents",
        "options": {
            "connectTimeoutMS": 5000,
            "socketTimeoutMS": 30000,
            "maxPoolSize": 50,
            "minPoolSize": 5
        },
        "collections": {
            "market_data": "market_data",
            "fundamental_data": "fundamental_data",
            "news_data": "news_data",
            "social_data": "social_data",
            "analysis_results": "analysis_results",
            "metadata": "metadata"
        }
    },
    "redis": {
        "host": "localhost",
        "port": 6379,
        "db": 0,
        "password": None,
        "key_prefix": "ta:",
        "ttl": {
            "price_data": 86400,      # 1天
            "quote_data": 60,         # 1分钟
            "news_data": 900,         # 15分钟
            "social_data": 300,       # 5分钟
            "analysis_results": 3600  # 1小时
        }
    },
    "file_storage": {
        "enabled": True,              # 是否保留文件存储
        "base_dir": "./data",
        "backup_frequency": "daily"   # 文件备份频率
    }
}
```

## 8. 性能优化

### 8.1 MongoDB 性能优化

1. **索引优化**
   - 为常用查询创建适当索引
   - 定期分析慢查询并优化
   - 避免过多索引导致写入性能下降

2. **文档设计优化**
   - 避免过大文档（保持<16MB）
   - 合理设计嵌套结构
   - 适当反规范化以减少查询次数

3. **查询优化**
   - 使用投影限制返回字段
   - 利用聚合管道减少数据传输
   - 批量操作减少网络往返

4. **连接池管理**
   - 配置适当的连接池大小
   - 监控连接使用情况
   - 及时释放不需要的连接

### 8.2 Redis 性能优化

1. **内存管理**
   - 设置合理的maxmemory
   - 选择适当的淘汰策略
   - 监控内存使用率

2. **数据结构选择**
   - 为不同数据选择最合适的数据结构
   - 使用Hash存储对象而非多个String
   - 利用Sorted Set实现时间序列数据

3. **批量操作**
   - 使用pipeline减少网络往返
   - 使用mget/mset代替多次get/set
   - 合理使用Lua脚本实现原子操作

4. **键设计**
   - 避免过长的键名
   - 使用一致的命名规范
   - 合理设置TTL避免内存泄漏

## 9. 高可用设计

### 9.1 MongoDB 集群设计

```
MongoDB 集群
├── 配置服务器 (3节点)
│   ├── configsvr1: 27019
│   ├── configsvr2: 27019
│   └── configsvr3: 27019
├── 分片服务器 (2分片)
│   ├── shard1 (3节点副本集)
│   │   ├── shard1svr1: 27018 (Primary)
│   │   ├── shard1svr2: 27018 (Secondary)
│   │   └── shard1svr3: 27018 (Secondary)
│   └── shard2 (3节点副本集)
│       ├── shard2svr1: 27018 (Primary)
│       ├── shard2svr2: 27018 (Secondary)
│       └── shard2svr3: 27018 (Secondary)
└── 路由服务器 (2节点)
    ├── mongos1: 27017
    └── mongos2: 27017
```

### 9.2 Redis 集群设计

```
Redis 集群
├── 主从复制 (3组)
│   ├── 组1
│   │   ├── master1: 6379
│   │   └── slave1: 6380
│   ├── 组2
│   │   ├── master2: 6381
│   │   └── slave2: 6382
│   └── 组3
│       ├── master3: 6383
│       └── slave3: 6384
└── Sentinel (3节点)
    ├── sentinel1: 26379
    ├── sentinel2: 26380
    └── sentinel3: 26381
```

### 9.3 故障转移策略

1. **MongoDB 故障转移**
   - 副本集自动选举新主节点
   - 应用层自动重连到新主节点
   - 监控系统发送故障通知

2. **Redis 故障转移**
   - Sentinel自动监测主节点故障
   - 自动选举新主节点
   - 客户端通过Sentinel发现新主节点

3. **应用层故障处理**
   - 连接池自动重连
   - 指数退避重试策略
   - 降级服务机制

## 10. 监控与运维

### 10.1 监控指标

| 监控类别 | 监控指标 | 告警阈值 | 处理策略 |
|---------|---------|---------|---------|
| **MongoDB** | 查询延迟 | >100ms | 优化索引或查询 |
| **MongoDB** | 连接数 | >80% | 增加连接池 |
| **MongoDB** | 内存使用 | >80% | 增加内存或优化查询 |
| **Redis** | 内存使用 | >80% | 调整淘汰策略或增加内存 |
| **Redis** | 命中率 | <80% | 调整缓存策略 |
| **Redis** | 延迟 | >10ms | 检查网络或命令复杂度 |

### 10.2 备份策略

1. **MongoDB 备份**
   - 每日全量备份
   - 每小时增量备份
   - 跨区域备份存储

2. **Redis 备份**
   - RDB定时快照
   - AOF持久化
   - 主从复制作为实时备份

3. **文件备份**
   - 关键数据定期归档
   - 增量备份策略
   - 多副本存储

### 10.3 运维工具

1. **监控工具**
   - Prometheus + Grafana
   - MongoDB Atlas监控
   - Redis Insight

2. **运维脚本**
   - 自动备份脚本
   - 数据完整性检查
   - 性能诊断工具

## 11. 实施路线图

### 11.1 第一阶段：基础整合（1-2周）

1. 安装配置MongoDB和Redis
2. 开发数据访问抽象层
3. 迁移核心数据到MongoDB
4. 实现基本缓存策略

### 11.2 第二阶段：功能完善（2-3周）

1. 完善所有数据类型的存储和缓存
2. 实现分布式锁和任务队列
3. 开发数据同步和一致性管理
4. 添加基本监控和告警

### 11.3 第三阶段：性能优化（2周）

1. 优化索引和查询性能
2. 实现高级缓存策略
3. 添加数据压缩和分区
4. 完善监控和性能分析

### 11.4 第四阶段：高可用部署（2-3周）

1. 部署MongoDB副本集或分片集群
2. 配置Redis主从复制和哨兵
3. 实现自动故障转移
4. 开发完整的运维工具

## 12. 总结

TradingAgents-CN 的数据库架构设计基于 MongoDB 和 Redis，提供了高性能、可扩展、高可用的数据管理解决方案。该架构具有以下核心优势：

1. **高性能数据访问**：Redis提供毫秒级的数据读取，MongoDB提供灵活的查询能力
2. **可扩展性**：支持数据量增长和用户并发访问
3. **数据一致性**：自动化的数据同步和缓存管理
4. **高可用性**：支持故障转移和负载均衡
5. **运维简化**：标准化的数据管理和监控

这种架构不仅满足当前需求，还为未来的功能扩展和性能优化提供了坚实基础，使TradingAgents-CN能够处理更大规模的数据和更复杂的分析任务。

<!-- docs/architecture/graph-structure.md -->

# LangGraph 图结构设计

## 概述

TradingAgents 基于 LangGraph 框架构建，采用有向无环图（DAG）结构来组织智能体的工作流程。这种设计确保了智能体之间的有序协作和信息的正确流转。

## 图结构架构

### 整体工作流图

```mermaid
graph TD
    START([开始]) --> INIT[初始化状态]
    INIT --> PARALLEL_ANALYSIS{并行分析阶段}
    
    PARALLEL_ANALYSIS --> FA[基本面分析师]
    PARALLEL_ANALYSIS --> TA[技术分析师]
    PARALLEL_ANALYSIS --> NA[新闻分析师]
    PARALLEL_ANALYSIS --> SA[社交媒体分析师]
    
    FA --> COLLECT_ANALYSIS[收集分析结果]
    TA --> COLLECT_ANALYSIS
    NA --> COLLECT_ANALYSIS
    SA --> COLLECT_ANALYSIS
    
    COLLECT_ANALYSIS --> RESEARCH_MANAGER[研究经理]
    RESEARCH_MANAGER --> DEBATE_INIT[初始化辩论]
    
    DEBATE_INIT --> BULL_RESEARCHER[看涨研究员]
    DEBATE_INIT --> BEAR_RESEARCHER[看跌研究员]
    
    BULL_RESEARCHER --> DEBATE_ROUND{辩论轮次}
    BEAR_RESEARCHER --> DEBATE_ROUND
    
    DEBATE_ROUND -->|继续辩论| BULL_RESEARCHER
    DEBATE_ROUND -->|辩论结束| RESEARCH_CONSENSUS[研究共识]
    
    RESEARCH_CONSENSUS --> TRADER[交易员]
    TRADER --> TRADING_DECISION[交易决策]
    
    TRADING_DECISION --> RISK_PARALLEL{并行风险评估}
    
    RISK_PARALLEL --> AGGRESSIVE_RISK[激进风险评估]
    RISK_PARALLEL --> CONSERVATIVE_RISK[保守风险评估]
    RISK_PARALLEL --> NEUTRAL_RISK[中性风险评估]
    
    AGGRESSIVE_RISK --> RISK_DEBATE[风险辩论]
    CONSERVATIVE_RISK --> RISK_DEBATE
    NEUTRAL_RISK --> RISK_DEBATE
    
    RISK_DEBATE --> RISK_MANAGER[风险经理]
    RISK_MANAGER --> PORTFOLIO_DECISION[投资组合决策]
    
    PORTFOLIO_DECISION --> END([结束])
```

## 核心组件设计

### 1. 图构建器 (GraphSetup)

```python
class GraphSetup:
    """LangGraph 图结构设置"""
    
    def build_graph(self) -> StateGraph:
        """构建完整的交易决策图"""
        
        # 创建状态图
        workflow = StateGraph(AgentState)
        
        # 添加节点
        self._add_analysis_nodes(workflow)
        self._add_research_nodes(workflow)
        self._add_trading_nodes(workflow)
        self._add_risk_nodes(workflow)
        
        # 添加边和条件逻辑
        self._add_edges(workflow)
        self._add_conditional_edges(workflow)
        
        # 设置入口和出口
        workflow.set_entry_point("initialize")
        workflow.set_finish_point("portfolio_decision")
        
        return workflow.compile()
    
    def _add_analysis_nodes(self, workflow: StateGraph):
        """添加分析师节点"""
        workflow.add_node("fundamentals_analyst", self.fundamentals_analyst)
        workflow.add_node("technical_analyst", self.technical_analyst)
        workflow.add_node("news_analyst", self.news_analyst)
        workflow.add_node("social_analyst", self.social_analyst)
    
    def _add_research_nodes(self, workflow: StateGraph):
        """添加研究员节点"""
        workflow.add_node("research_manager", self.research_manager)
        workflow.add_node("bull_researcher", self.bull_researcher)
        workflow.add_node("bear_researcher", self.bear_researcher)
    
    def _add_trading_nodes(self, workflow: StateGraph):
        """添加交易节点"""
        workflow.add_node("trader", self.trader)
    
    def _add_risk_nodes(self, workflow: StateGraph):
        """添加风险管理节点"""
        workflow.add_node("aggressive_risk", self.aggressive_risk)
        workflow.add_node("conservative_risk", self.conservative_risk)
        workflow.add_node("neutral_risk", self.neutral_risk)
        workflow.add_node("risk_manager", self.risk_manager)
```

### 2. 条件逻辑 (ConditionalLogic)

```python
class ConditionalLogic:
    """图的条件逻辑控制"""
    
    def should_continue_debate(self, state: AgentState) -> str:
        """判断是否继续研究员辩论"""
        
        current_round = state.get("debate_round", 0)
        max_rounds = self.config.get("max_debate_rounds", 3)
        
        # 检查辩论轮次
        if current_round >= max_rounds:
            return "end_debate"
        
        # 检查是否达成共识
        if self._has_consensus(state):
            return "end_debate"
        
        # 检查分歧是否足够大
        if self._has_significant_disagreement(state):
            return "continue_debate"
        
        return "end_debate"
    
    def route_to_risk_assessment(self, state: AgentState) -> List[str]:
        """路由到风险评估节点"""
        
        trading_decision = state.get("trader_decision", {})
        risk_level = trading_decision.get("risk_level", "medium")
        
        # 根据风险级别决定评估路径
        if risk_level == "high":
            return ["aggressive_risk", "conservative_risk", "neutral_risk"]
        elif risk_level == "low":
            return ["conservative_risk", "neutral_risk"]
        else:
            return ["neutral_risk"]
    
    def should_approve_trade(self, state: AgentState) -> str:
        """判断是否批准交易"""
        
        risk_assessment = state.get("risk_assessment", {})
        risk_score = risk_assessment.get("overall_risk_score", 0.5)
        
        # 风险阈值检查
        if risk_score > self.config.get("risk_threshold", 0.8):
            return "reject_trade"
        
        # 一致性检查
        if self._risk_assessments_consistent(state):
            return "approve_trade"
        
        return "request_review"
```

### 3. 状态传播 (Propagator)

```python
class Propagator:
    """状态传播管理器"""
    
    def propagate(self, symbol: str, date: str) -> Tuple[AgentState, Dict]:
        """执行完整的传播流程"""
        
        # 初始化状态
        initial_state = self._initialize_state(symbol, date)
        
        # 执行图传播
        final_state = self.graph.invoke(initial_state)
        
        # 提取决策结果
        decision = self._extract_decision(final_state)
        
        return final_state, decision
    
    def _initialize_state(self, symbol: str, date: str) -> AgentState:
        """初始化智能体状态"""
        return AgentState(
            ticker=symbol,
            date=date,
            analyst_reports={},
            research_reports={},
            trader_decision={},
            risk_assessment={},
            portfolio_decision={},
            messages=[],
            metadata={}
        )
    
    def _extract_decision(self, state: AgentState) -> Dict:
        """从最终状态提取决策信息"""
        return {
            "action": state.portfolio_decision.get("action", "hold"),
            "quantity": state.portfolio_decision.get("quantity", 0),
            "confidence": state.portfolio_decision.get("confidence", 0.5),
            "reasoning": state.portfolio_decision.get("reasoning", ""),
            "risk_score": state.risk_assessment.get("overall_risk_score", 0.5)
        }
```

## 节点类型详解

### 1. 分析节点 (Analysis Nodes)
```python
def fundamentals_analyst_node(state: AgentState) -> AgentState:
    """基本面分析师节点"""
    
    # 获取数据
    data = get_fundamental_data(state.ticker, state.date)
    
    # 执行分析
    analysis = fundamentals_analyst.analyze(data)
    
    # 更新状态
    state.analyst_reports["fundamentals"] = analysis
    
    return state
```

### 2. 决策节点 (Decision Nodes)
```python
def trader_node(state: AgentState) -> AgentState:
    """交易员决策节点"""
    
    # 收集所有分析报告
    all_reports = {
        **state.analyst_reports,
        **state.research_reports
    }
    
    # 制定交易决策
    decision = trader.make_decision(all_reports)
    
    # 更新状态
    state.trader_decision = decision
    
    return state
```

### 3. 并行节点 (Parallel Nodes)
```python
def parallel_analysis_node(state: AgentState) -> AgentState:
    """并行分析节点"""
    
    # 并行执行多个分析师
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(fundamentals_analyst.analyze, state): "fundamentals",
            executor.submit(technical_analyst.analyze, state): "technical",
            executor.submit(news_analyst.analyze, state): "news",
            executor.submit(social_analyst.analyze, state): "social"
        }
        
        # 收集结果
        for future in as_completed(futures):
            analyst_type = futures[future]
            result = future.result()
            state.analyst_reports[analyst_type] = result
    
    return state
```

## 边和路由设计

### 1. 顺序边 (Sequential Edges)
```python
# 简单的顺序连接
workflow.add_edge("initialize", "parallel_analysis")
workflow.add_edge("parallel_analysis", "research_manager")
workflow.add_edge("research_manager", "trader")
```

### 2. 条件边 (Conditional Edges)
```python
# 基于条件的路由
workflow.add_conditional_edges(
    "debate_round",
    conditional_logic.should_continue_debate,
    {
        "continue_debate": "bull_researcher",
        "end_debate": "research_consensus"
    }
)
```

### 3. 并行边 (Parallel Edges)
```python
# 并行执行多个节点
workflow.add_conditional_edges(
    "trading_decision",
    conditional_logic.route_to_risk_assessment,
    {
        "aggressive_risk": "aggressive_risk_node",
        "conservative_risk": "conservative_risk_node",
        "neutral_risk": "neutral_risk_node"
    }
)
```

## 状态管理

### 1. 状态结构
```python
@dataclass
class AgentState:
    """智能体状态数据结构"""
    
    # 基本信息
    ticker: str
    date: str
    
    # 分析结果
    analyst_reports: Dict[str, Any]
    research_reports: Dict[str, Any]
    
    # 决策信息
    trader_decision: Dict[str, Any]
    risk_assessment: Dict[str, Any]
    portfolio_decision: Dict[str, Any]
    
    # 通信记录
    messages: List[BaseMessage]
    
    # 元数据
    metadata: Dict[str, Any]
    
    # 控制信息
    debate_round: int = 0
    risk_round: int = 0
```

### 2. 状态更新
```python
class StateManager:
    """状态管理器"""
    
    def update_state(self, state: AgentState, updates: Dict) -> AgentState:
        """安全地更新状态"""
        
        # 深拷贝状态
        new_state = copy.deepcopy(state)
        
        # 应用更新
        for key, value in updates.items():
            if hasattr(new_state, key):
                setattr(new_state, key, value)
        
        # 验证状态一致性
        self._validate_state(new_state)
        
        return new_state
    
    def _validate_state(self, state: AgentState):
        """验证状态一致性"""
        
        # 检查必需字段
        required_fields = ["ticker", "date"]
        for field in required_fields:
            if not getattr(state, field):
                raise ValueError(f"Required field {field} is missing")
        
        # 检查数据类型
        if not isinstance(state.analyst_reports, dict):
            raise TypeError("analyst_reports must be a dictionary")
```

## 错误处理和恢复

### 1. 节点级错误处理
```python
def safe_node_execution(node_func):
    """节点执行的安全包装器"""
    
    def wrapper(state: AgentState) -> AgentState:
        try:
            return node_func(state)
        except Exception as e:
            # 记录错误
            logger.error(f"Node {node_func.__name__} failed: {e}")
            
            # 添加错误信息到状态
            state.metadata["errors"] = state.metadata.get("errors", [])
            state.metadata["errors"].append({
                "node": node_func.__name__,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
            
            return state
    
    return wrapper
```

### 2. 图级错误恢复
```python
class GraphRecovery:
    """图执行恢复机制"""
    
    def execute_with_recovery(self, graph, initial_state):
        """带恢复机制的图执行"""
        
        try:
            return graph.invoke(initial_state)
        except Exception as e:
            # 尝试从检查点恢复
            if checkpoint := self._find_last_checkpoint(initial_state):
                logger.info("Recovering from checkpoint")
                return self._recover_from_checkpoint(graph, checkpoint)
            
            # 降级执行
            logger.warning("Falling back to degraded execution")
            return self._degraded_execution(initial_state)
```

这种图结构设计确保了智能体工作流的清晰性、可维护性和容错性，同时提供了灵活的扩展机制。


<!-- docs/architecture/system-architecture.md -->

# 系统架构

## 概述

TradingAgents 是一个基于多智能体的金融交易框架，采用分层架构设计，模拟真实世界交易公司的运作模式。系统通过多个专业化的AI智能体协作，实现从市场分析到交易执行的完整流程。

## 整体架构图

```mermaid
graph TB
    subgraph "用户接口层"
        CLI[命令行界面]
        API[Python API]
        WEB[Web界面]
    end
    
    subgraph "核心框架层"
        TG[TradingAgentsGraph]
        CL[ConditionalLogic]
        PROP[Propagator]
        REF[Reflector]
        SP[SignalProcessor]
    end
    
    subgraph "智能体层"
        subgraph "分析师团队"
            FA[基本面分析师]
            MA[市场分析师]
            NA[新闻分析师]
            SA[社交媒体分析师]
        end
        
        subgraph "研究员团队"
            BR[看涨研究员]
            BEAR[看跌研究员]
        end
        
        subgraph "交易执行"
            TRADER[交易员]
        end
        
        subgraph "风险管理"
            AGG[激进风险评估]
            CON[保守风险评估]
            NEU[中性风险评估]
        end
        
        subgraph "管理层"
            RM[研究经理]
            RISKM[风险经理]
        end
    end
    
    subgraph "数据层"
        subgraph "外部数据源"
            FINN[FinnHub API]
            YF[Yahoo Finance]
            REDDIT[Reddit API]
            NEWS[Google News]
        end
        
        subgraph "数据处理"
            CACHE[数据缓存]
            PROC[数据处理器]
        end
    end
    
    subgraph "LLM层"
        OPENAI[OpenAI]
        ANTHROPIC[Anthropic]
        GOOGLE[Google AI]
    end
    
    CLI --> TG
    API --> TG
    WEB --> TG
    
    TG --> CL
    TG --> PROP
    TG --> REF
    TG --> SP
    
    CL --> FA
    CL --> MA
    CL --> NA
    CL --> SA
    CL --> BR
    CL --> BEAR
    CL --> TRADER
    CL --> AGG
    CL --> CON
    CL --> NEU
    CL --> RM
    CL --> RISKM
    
    FA --> PROC
    MA --> PROC
    NA --> PROC
    SA --> PROC
    
    PROC --> FINN
    PROC --> YF
    PROC --> REDDIT
    PROC --> NEWS
    
    PROC --> CACHE
    
    FA --> OPENAI
    MA --> ANTHROPIC
    NA --> GOOGLE
    SA --> OPENAI
    BR --> OPENAI
    BEAR --> OPENAI
    TRADER --> OPENAI
    AGG --> OPENAI
    CON --> OPENAI
    NEU --> OPENAI
    RM --> OPENAI
    RISKM --> OPENAI
```

## 架构层次

### 1. 用户接口层
- **命令行界面 (CLI)**: 提供交互式命令行工具
- **Python API**: 程序化接口，支持集成到其他系统
- **Web界面**: 基于Chainlit的Web用户界面

### 2. 核心框架层
- **TradingAgentsGraph**: 主要的编排类，管理整个交易流程
- **ConditionalLogic**: 条件逻辑处理，控制智能体间的交互流程
- **Propagator**: 信息传播机制，管理智能体间的信息流
- **Reflector**: 反思机制，支持从历史决策中学习
- **SignalProcessor**: 信号处理，整合各智能体的输出

### 3. 智能体层
采用专业化分工的多智能体架构：

#### 分析师团队
- **基本面分析师**: 分析公司财务数据和基本面指标
- **市场分析师**: 分析技术指标和市场趋势
- **新闻分析师**: 处理新闻事件和宏观经济数据
- **社交媒体分析师**: 分析社交媒体情绪和舆论

#### 研究员团队
- **看涨研究员**: 从乐观角度评估投资机会
- **看跌研究员**: 从悲观角度评估投资风险

#### 交易执行
- **交易员**: 综合各方信息做出最终交易决策

#### 风险管理
- **激进风险评估**: 评估高风险高收益策略
- **保守风险评估**: 评估低风险稳健策略
- **中性风险评估**: 平衡风险收益的中性评估

#### 管理层
- **研究经理**: 协调研究员团队的工作
- **风险经理**: 管理整体风险控制流程

### 4. 数据层
#### 外部数据源
- **FinnHub API**: 实时金融数据
- **Yahoo Finance**: 历史价格和财务数据
- **Reddit API**: 社交媒体情绪数据
- **Google News**: 新闻和事件数据

#### 数据处理
- **数据缓存**: 本地缓存机制，提高性能
- **数据处理器**: 统一的数据处理接口

### 5. LLM层
支持多种大语言模型提供商：
- **OpenAI**: GPT系列模型
- **Anthropic**: Claude系列模型
- **Google AI**: Gemini系列模型

## 核心设计原则

### 1. 模块化设计
- 每个智能体都是独立的模块
- 支持插件式扩展
- 松耦合的组件设计

### 2. 可扩展性
- 支持添加新的智能体类型
- 支持新的数据源集成
- 支持新的LLM提供商

### 3. 容错性
- 智能体故障隔离
- 数据源故障转移
- 优雅的错误处理

### 4. 性能优化
- 数据缓存机制
- 并行处理能力
- 智能的API调用管理

## 数据流向

1. **数据获取**: 从多个外部数据源获取实时和历史数据
2. **数据处理**: 清洗、标准化和缓存数据
3. **智能体分析**: 各专业智能体并行分析数据
4. **信息整合**: 整合各智能体的分析结果
5. **决策制定**: 通过辩论和协商机制形成最终决策
6. **风险评估**: 风险管理团队评估决策风险
7. **交易执行**: 执行最终的交易决策

## 技术栈

- **框架**: LangGraph (基于LangChain)
- **编程语言**: Python 3.10+
- **数据处理**: Pandas, NumPy
- **API集成**: requests, finnhub-python, yfinance
- **缓存**: Redis (可选)
- **UI**: Chainlit, Rich (CLI)
- **配置管理**: YAML/JSON配置文件

这种架构设计确保了系统的可扩展性、可维护性和高性能，同时保持了各组件间的清晰职责分工。


<!-- docs/configuration/config-guide.md -->

# 配置指南 (v0.1.4)

## 概述

TradingAgents 中文增强版提供了统一的配置系统，所有配置通过 `.env` 文件管理。本指南详细介绍了所有可用的配置选项和最佳实践。

## 🎯 v0.1.4 配置优化

### 统一配置管理
- ✅ **单一配置源**: 只使用 `.env` 文件
- ✅ **启用开关生效**: 数据库启用开关完全生效
- ✅ **智能降级**: 自动检测并降级到可用的数据源
- ✅ **Web界面管理**: 通过Web界面管理配置

## 配置文件结构

### .env 配置文件 (推荐)
```bash
# ===========================================
# TradingAgents 中文增强版配置文件 (v0.1.4)
# ===========================================

# 🧠 LLM 配置 (推荐阿里百炼)
DASHSCOPE_API_KEY=your_dashscope_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# 📊 数据源配置
FINNHUB_API_KEY=your_finnhub_api_key_here

# 🗄️ 数据库配置 (默认禁用)
MONGODB_ENABLED=false
REDIS_ENABLED=false
MONGODB_HOST=localhost
MONGODB_PORT=27018
REDIS_HOST=localhost
REDIS_PORT=6380

# 📁 路径配置
TRADINGAGENTS_RESULTS_DIR=./results
TRADINGAGENTS_DATA_DIR=./data
```

## 配置选项详解

### 1. 路径配置

#### project_dir
- **类型**: `str`
- **默认值**: 项目根目录
- **说明**: 项目根目录路径，用于定位其他相对路径

#### results_dir
- **类型**: `str`
- **默认值**: `"./results"`
- **环境变量**: `TRADINGAGENTS_RESULTS_DIR`
- **说明**: 分析结果存储目录

```python
config = {
    "results_dir": "/path/to/custom/results",  # 自定义结果目录
}
```

#### data_cache_dir
- **类型**: `str`
- **默认值**: `"tradingagents/dataflows/data_cache"`
- **说明**: 数据缓存目录

### 2. LLM 配置

#### llm_provider
- **类型**: `str`
- **可选值**: `"openai"`, `"anthropic"`, `"google"`
- **默认值**: `"openai"`
- **说明**: 大语言模型提供商

```python
# OpenAI 配置
config = {
    "llm_provider": "openai",
    "backend_url": "https://api.openai.com/v1",
    "deep_think_llm": "gpt-4o",
    "quick_think_llm": "gpt-4o-mini",
}

# Anthropic 配置
config = {
    "llm_provider": "anthropic",
    "backend_url": "https://api.anthropic.com",
    "deep_think_llm": "claude-3-opus-20240229",
    "quick_think_llm": "claude-3-haiku-20240307",
}

# Google 配置
config = {
    "llm_provider": "google",
    "backend_url": "https://generativelanguage.googleapis.com/v1",
    "deep_think_llm": "gemini-pro",
    "quick_think_llm": "gemini-pro",
}
```

#### deep_think_llm
- **类型**: `str`
- **默认值**: `"o4-mini"`
- **说明**: 用于深度思考任务的模型（如复杂分析、辩论）

**推荐模型**:
- **高性能**: `"gpt-4o"`, `"claude-3-opus-20240229"`
- **平衡**: `"gpt-4o-mini"`, `"claude-3-sonnet-20240229"`
- **经济**: `"gpt-3.5-turbo"`, `"claude-3-haiku-20240307"`

#### quick_think_llm
- **类型**: `str`
- **默认值**: `"gpt-4o-mini"`
- **说明**: 用于快速任务的模型（如数据处理、格式化）

### 3. 辩论和讨论配置

#### max_debate_rounds
- **类型**: `int`
- **默认值**: `1`
- **范围**: `1-10`
- **说明**: 研究员辩论的最大轮次

```python
# 不同场景的推荐配置
config_scenarios = {
    "quick_analysis": {"max_debate_rounds": 1},      # 快速分析
    "standard": {"max_debate_rounds": 2},            # 标准分析
    "thorough": {"max_debate_rounds": 3},            # 深度分析
    "comprehensive": {"max_debate_rounds": 5},       # 全面分析
}
```

#### max_risk_discuss_rounds
- **类型**: `int`
- **默认值**: `1`
- **范围**: `1-5`
- **说明**: 风险管理讨论的最大轮次

#### max_recur_limit
- **类型**: `int`
- **默认值**: `100`
- **说明**: 递归调用的最大限制，防止无限循环

### 4. 工具配置

#### online_tools
- **类型**: `bool`
- **默认值**: `True`
- **说明**: 是否使用在线数据工具

```python
# 在线模式 - 获取实时数据
config = {"online_tools": True}

# 离线模式 - 使用缓存数据
config = {"online_tools": False}
```

## 高级配置选项

### 1. 智能体权重配置
```python
config = {
    "analyst_weights": {
        "fundamentals": 0.3,    # 基本面分析权重
        "technical": 0.3,       # 技术分析权重
        "news": 0.2,           # 新闻分析权重
        "social": 0.2,         # 社交媒体分析权重
    }
}
```

### 2. 风险管理配置
```python
config = {
    "risk_management": {
        "risk_threshold": 0.8,           # 风险阈值
        "max_position_size": 0.1,        # 最大仓位比例
        "stop_loss_threshold": 0.05,     # 止损阈值
        "take_profit_threshold": 0.15,   # 止盈阈值
    }
}
```

### 3. 数据源配置
```python
config = {
    "data_sources": {
        "primary": "finnhub",            # 主要数据源
        "fallback": ["yahoo", "alpha_vantage"],  # 备用数据源
        "cache_ttl": {
            "price_data": 300,           # 价格数据缓存5分钟
            "fundamental_data": 86400,   # 基本面数据缓存24小时
            "news_data": 3600,          # 新闻数据缓存1小时
        }
    }
}
```

### 4. 性能优化配置
```python
config = {
    "performance": {
        "parallel_analysis": True,       # 并行分析
        "max_workers": 4,               # 最大工作线程数
        "timeout": 300,                 # 超时时间（秒）
        "retry_attempts": 3,            # 重试次数
        "batch_size": 10,               # 批处理大小
    }
}
```

## 环境变量配置

### 必需的环境变量
```bash
# OpenAI API
export OPENAI_API_KEY="your_openai_api_key"

# FinnHub API
export FINNHUB_API_KEY="your_finnhub_api_key"

# 可选的环境变量
export ANTHROPIC_API_KEY="your_anthropic_api_key"
export GOOGLE_API_KEY="your_google_api_key"
export TRADINGAGENTS_RESULTS_DIR="/custom/results/path"
```

### .env 文件配置
```bash
# .env 文件
OPENAI_API_KEY=your_openai_api_key
FINNHUB_API_KEY=your_finnhub_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
TRADINGAGENTS_RESULTS_DIR=./custom_results
TRADINGAGENTS_LOG_LEVEL=INFO
```

## 配置最佳实践

### 1. 成本优化配置
```python
# 低成本配置
cost_optimized_config = {
    "llm_provider": "openai",
    "deep_think_llm": "gpt-4o-mini",
    "quick_think_llm": "gpt-4o-mini",
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "online_tools": False,  # 使用缓存数据
}
```

### 2. 高性能配置
```python
# 高性能配置
high_performance_config = {
    "llm_provider": "openai",
    "deep_think_llm": "gpt-4o",
    "quick_think_llm": "gpt-4o",
    "max_debate_rounds": 3,
    "max_risk_discuss_rounds": 2,
    "online_tools": True,
    "performance": {
        "parallel_analysis": True,
        "max_workers": 8,
    }
}
```

### 3. 开发环境配置
```python
# 开发环境配置
dev_config = {
    "llm_provider": "openai",
    "deep_think_llm": "gpt-4o-mini",
    "quick_think_llm": "gpt-4o-mini",
    "max_debate_rounds": 1,
    "online_tools": True,
    "debug": True,
    "log_level": "DEBUG",
}
```

### 4. 生产环境配置
```python
# 生产环境配置
prod_config = {
    "llm_provider": "openai",
    "deep_think_llm": "gpt-4o",
    "quick_think_llm": "gpt-4o-mini",
    "max_debate_rounds": 2,
    "max_risk_discuss_rounds": 1,
    "online_tools": True,
    "performance": {
        "parallel_analysis": True,
        "max_workers": 4,
        "timeout": 600,
        "retry_attempts": 3,
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/tradingagents.log",
    }
}
```

## 配置验证

### 配置验证器
```python
class ConfigValidator:
    """配置验证器"""
    
    def validate(self, config: Dict) -> Tuple[bool, List[str]]:
        """验证配置的有效性"""
        errors = []
        
        # 检查必需字段
        required_fields = ["llm_provider", "deep_think_llm", "quick_think_llm"]
        for field in required_fields:
            if field not in config:
                errors.append(f"Missing required field: {field}")
        
        # 检查LLM提供商
        valid_providers = ["openai", "anthropic", "google"]
        if config.get("llm_provider") not in valid_providers:
            errors.append(f"Invalid llm_provider. Must be one of: {valid_providers}")
        
        # 检查数值范围
        if config.get("max_debate_rounds", 1) < 1:
            errors.append("max_debate_rounds must be >= 1")
        
        return len(errors) == 0, errors

# 使用示例
validator = ConfigValidator()
is_valid, errors = validator.validate(config)
if not is_valid:
    print("Configuration errors:", errors)
```

## 动态配置更新

### 运行时配置更新
```python
class TradingAgentsGraph:
    def update_config(self, new_config: Dict):
        """运行时更新配置"""
        
        # 验证新配置
        validator = ConfigValidator()
        is_valid, errors = validator.validate(new_config)
        
        if not is_valid:
            raise ValueError(f"Invalid configuration: {errors}")
        
        # 更新配置
        self.config.update(new_config)
        
        # 重新初始化受影响的组件
        self._reinitialize_components()
    
    def _reinitialize_components(self):
        """重新初始化组件"""
        # 重新初始化LLM
        self._setup_llms()
        
        # 重新初始化智能体
        self._setup_agents()
```

通过合理的配置，您可以根据不同的使用场景优化 TradingAgents 的性能和成本。


<!-- docs/configuration/dashscope-config.md -->

# 阿里百炼大模型配置指南

## 概述

阿里百炼（DashScope）是阿里云推出的大模型服务平台，提供通义千问系列模型。本指南详细介绍如何在 TradingAgents 中配置和使用阿里百炼大模型。

## 为什么选择阿里百炼？

### 🇨🇳 **国产化优势**
- **无需翻墙**: 国内直接访问，网络稳定
- **中文优化**: 专门针对中文场景优化
- **合规安全**: 符合国内数据安全要求
- **本土化服务**: 中文客服和技术支持

### 💰 **成本优势**
- **价格透明**: 按量计费，价格公开透明
- **免费额度**: 新用户有免费试用额度
- **性价比高**: 相比国外模型成本更低

### 🧠 **技术优势**
- **中文理解**: 在中文理解和生成方面表现优秀
- **金融知识**: 对中国金融市场有更好的理解
- **推理能力**: 通义千问系列在推理任务上表现出色

## 快速开始

### 1. 获取API密钥

#### 步骤1: 注册阿里云账号
1. 访问 [阿里云官网](https://www.aliyun.com/)
2. 点击"免费注册"
3. 完成账号注册和实名认证

#### 步骤2: 开通百炼服务
1. 访问 [百炼控制台](https://dashscope.console.aliyun.com/)
2. 点击"立即开通"
3. 选择合适的套餐（建议先选择按量付费）

#### 步骤3: 获取API密钥
1. 在百炼控制台中，点击"API-KEY管理"
2. 点击"创建新的API-KEY"
3. 复制生成的API密钥

### 2. 配置环境变量

#### 方法1: 使用环境变量
```bash
# Windows
set DASHSCOPE_API_KEY=your_dashscope_api_key_here
set FINNHUB_API_KEY=your_finnhub_api_key_here

# Linux/macOS
export DASHSCOPE_API_KEY=your_dashscope_api_key_here
export FINNHUB_API_KEY=your_finnhub_api_key_here
```

#### 方法2: 使用 .env 文件
```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件，填入真实的API密钥
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
FINNHUB_API_KEY=your_finnhub_api_key_here
```

### 3. 运行演示

```bash
# 使用专门的阿里百炼演示脚本
python demo_dashscope.py
```

## 支持的模型

### 通义千问系列模型

| 模型名称 | 模型ID | 特点 | 适用场景 |
|---------|--------|------|----------|
| **通义千问 Turbo** | `qwen-turbo` | 快速响应，成本低 | 快速任务、日常对话 |
| **通义千问 Plus** | `qwen-plus-latest` | 平衡性能和成本 | 复杂分析、专业任务 |
| **通义千问 Max** | `qwen-max` | 最强性能 | 最复杂任务、高质量输出 |
| **通义千问 Max 长文本** | `qwen-max-longcontext` | 超长上下文 | 长文档分析、大量数据处理 |

### 推荐配置

#### 经济型配置（成本优先）
```python
config = {
    "llm_provider": "dashscope",
    "deep_think_llm": "qwen-plus-latest",      # 深度思考使用Plus
    "quick_think_llm": "qwen-turbo",    # 快速任务使用Turbo
    "max_debate_rounds": 1,             # 减少辩论轮次
}
```

#### 性能型配置（质量优先）
```python
config = {
    "llm_provider": "dashscope", 
    "deep_think_llm": "qwen-max",       # 深度思考使用Max
    "quick_think_llm": "qwen-plus",     # 快速任务使用Plus
    "max_debate_rounds": 2,             # 增加辩论轮次
}
```

#### 长文本配置（处理大量数据）
```python
config = {
    "llm_provider": "dashscope",
    "deep_think_llm": "qwen-max-longcontext",  # 使用长文本版本
    "quick_think_llm": "qwen-plus",
    "max_debate_rounds": 1,
}
```

## 配置示例

### 基础配置
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 创建阿里百炼配置
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "dashscope"
config["deep_think_llm"] = "qwen-plus-latest"
config["quick_think_llm"] = "qwen-turbo"

# 初始化
ta = TradingAgentsGraph(debug=True, config=config)

# 运行分析
state, decision = ta.propagate("AAPL", "2024-05-10")
print(decision)
```

### 高级配置
```python
# 自定义模型参数
config = DEFAULT_CONFIG.copy()
config.update({
    "llm_provider": "dashscope",
    "deep_think_llm": "qwen-max",
    "quick_think_llm": "qwen-plus-latest",
    "max_debate_rounds": 2,
    "max_risk_discuss_rounds": 2,
    "online_tools": True,
})

# 使用自定义参数创建LLM
from tradingagents.llm_adapters import ChatDashScope

custom_llm = ChatDashScope(
    model="qwen-max",
    temperature=0.1,
    max_tokens=3000,
    top_p=0.9
)
```

## 成本控制

### 典型使用成本
- **经济模式**: ¥0.01-0.05/次分析 (使用 qwen-turbo)
- **标准模式**: ¥0.05-0.15/次分析 (使用 qwen-plus)
- **高精度模式**: ¥0.10-0.30/次分析 (使用 qwen-max)

### 成本优化建议
1. **合理选择模型**: 根据任务复杂度选择合适的模型
2. **控制辩论轮次**: 减少 `max_debate_rounds` 参数
3. **使用缓存**: 启用数据缓存减少重复调用
4. **监控使用量**: 定期检查API调用量和费用

## 故障排除

### 常见问题

#### 1. API密钥错误
```
Error: Invalid API key
```
**解决方案**: 检查API密钥是否正确，确认已开通百炼服务

#### 2. 额度不足
```
Error: Insufficient quota
```
**解决方案**: 在百炼控制台充值或升级套餐

#### 3. 网络连接问题
```
Error: Connection timeout
```
**解决方案**: 检查网络连接，确认可以访问阿里云服务

#### 4. 模型不存在
```
Error: Model not found
```
**解决方案**: 检查模型名称是否正确，确认模型已开通

### 调试技巧

1. **启用调试模式**:
   ```python
   ta = TradingAgentsGraph(debug=True, config=config)
   ```

2. **检查API连接**:
   ```python
   import dashscope
   dashscope.api_key = "your_api_key"
   
   from dashscope import Generation
   response = Generation.call(
       model="qwen-turbo",
       messages=[{"role": "user", "content": "Hello"}]
   )
   print(response)
   ```

## 最佳实践

1. **模型选择**: 根据任务复杂度选择合适的模型
2. **参数调优**: 根据具体需求调整温度、最大token数等参数
3. **错误处理**: 实现适当的错误处理和重试机制
4. **监控使用**: 定期监控API使用量和成本
5. **缓存策略**: 合理使用缓存减少API调用

## 相关链接

- [阿里百炼官网](https://dashscope.aliyun.com/)
- [百炼控制台](https://dashscope.console.aliyun.com/)
- [API文档](https://help.aliyun.com/zh/dashscope/)
- [价格说明](https://help.aliyun.com/zh/dashscope/product-overview/billing-overview)


<!-- docs/configuration/data-directory-configuration.md -->

# 数据目录配置指南 | Data Directory Configuration Guide

本指南详细说明如何在TradingAgents中配置数据目录路径，解决路径相关问题，并提供多种配置方式。

This guide explains how to configure data directory paths in TradingAgents, resolve path-related issues, and provides multiple configuration methods.

## 概述 | Overview

TradingAgents支持灵活的数据目录配置，允许用户：
- 自定义数据存储位置
- 通过环境变量配置
- 使用CLI命令管理
- 自动创建必要的目录结构

TradingAgents supports flexible data directory configuration, allowing users to:
- Customize data storage locations
- Configure via environment variables
- Manage through CLI commands
- Automatically create necessary directory structures

## 配置方法 | Configuration Methods

### 1. CLI命令配置 | CLI Command Configuration

#### 查看当前配置 | View Current Configuration
```bash
# 显示当前数据目录配置
python -m cli.main data-config
python -m cli.main data-config --show
```

#### 设置自定义数据目录 | Set Custom Data Directory
```bash
# Windows
python -m cli.main data-config --set "C:\MyTradingData"

# Linux/macOS
python -m cli.main data-config --set "/home/user/trading-data"
```

#### 重置为默认配置 | Reset to Default Configuration
```bash
python -m cli.main data-config --reset
```

### 2. 环境变量配置 | Environment Variable Configuration

#### Windows
```cmd
# 设置数据目录
set TRADINGAGENTS_DATA_DIR=C:\MyTradingData

# 设置缓存目录
set TRADINGAGENTS_CACHE_DIR=C:\MyTradingData\cache

# 设置结果目录
set TRADINGAGENTS_RESULTS_DIR=C:\MyTradingData\results
```

#### Linux/macOS
```bash
# 设置数据目录
export TRADINGAGENTS_DATA_DIR="/home/user/trading-data"

# 设置缓存目录
export TRADINGAGENTS_CACHE_DIR="/home/user/trading-data/cache"

# 设置结果目录
export TRADINGAGENTS_RESULTS_DIR="/home/user/trading-data/results"
```

#### .env文件配置 | .env File Configuration
```env
# 在项目根目录创建.env文件
TRADINGAGENTS_DATA_DIR=/path/to/your/data
TRADINGAGENTS_CACHE_DIR=/path/to/your/cache
TRADINGAGENTS_RESULTS_DIR=/path/to/your/results
```

### 3. 程序化配置 | Programmatic Configuration

```python
from tradingagents.dataflows.config import set_data_dir, get_data_dir
from tradingagents.config.config_manager import config_manager

# 设置数据目录
set_data_dir("/path/to/custom/data")

# 获取当前数据目录
current_dir = get_data_dir()
print(f"当前数据目录: {current_dir}")

# 确保目录存在
config_manager.ensure_directories_exist()
```

## 目录结构 | Directory Structure

配置数据目录后，系统会自动创建以下目录结构：

After configuring the data directory, the system automatically creates the following directory structure:

```
data/
├── cache/                          # 缓存目录 | Cache directory
├── finnhub_data/                   # Finnhub数据目录 | Finnhub data directory
│   ├── news_data/                  # 新闻数据 | News data
│   ├── insider_sentiment/          # 内部人情绪数据 | Insider sentiment data
│   └── insider_transactions/       # 内部人交易数据 | Insider transaction data
└── results/                        # 分析结果 | Analysis results
```

## 配置优先级 | Configuration Priority

配置的优先级从高到低：

Configuration priority from high to low:

1. **环境变量** | Environment Variables
2. **CLI设置** | CLI Settings
3. **默认配置** | Default Configuration

## 默认配置 | Default Configuration

如果没有自定义配置，系统使用以下默认路径：

If no custom configuration is provided, the system uses the following default paths:

- **Windows**: `C:\Users\{username}\Documents\TradingAgents\data`
- **Linux/macOS**: `~/Documents/TradingAgents/data`

## 常见问题解决 | Troubleshooting

### 问题1：路径不存在错误 | Issue 1: Path Not Found Error

**错误信息** | Error Message:
```
No such file or directory: '/data/finnhub_data/news_data'
```

**解决方案** | Solution:
```bash
# 使用CLI重新配置数据目录
python -m cli.main data-config --set "C:\YourDataPath"

# 或重置为默认配置
python -m cli.main data-config --reset
```

### 问题2：权限不足 | Issue 2: Permission Denied

**解决方案** | Solution:
1. 确保对目标目录有写权限
2. 选择用户目录下的路径
3. 在Windows上以管理员身份运行

### 问题3：跨平台路径问题 | Issue 3: Cross-Platform Path Issues

**解决方案** | Solution:
- 使用正斜杠 `/` 或双反斜杠 `\\` 在Windows上
- 避免硬编码路径分隔符
- 使用环境变量进行跨平台配置

## 验证配置 | Verify Configuration

### 1. 使用CLI验证 | Verify Using CLI
```bash
python -m cli.main data-config --show
```

### 2. 使用测试脚本验证 | Verify Using Test Script
```bash
python test_data_config_cli.py
```

### 3. 使用演示脚本验证 | Verify Using Demo Script
```bash
python examples/data_dir_config_demo.py
```

## 最佳实践 | Best Practices

1. **使用绝对路径** | Use Absolute Paths
   - 避免相对路径可能导致的问题
   - Avoid issues that relative paths might cause

2. **定期备份数据** | Regular Data Backup
   - 重要的分析结果应定期备份
   - Important analysis results should be backed up regularly

3. **环境隔离** | Environment Isolation
   - 不同项目使用不同的数据目录
   - Use different data directories for different projects

4. **权限管理** | Permission Management
   - 确保应用程序对数据目录有适当权限
   - Ensure the application has appropriate permissions to the data directory

## 高级配置 | Advanced Configuration

### 自定义子目录结构 | Custom Subdirectory Structure

```python
from tradingagents.config.config_manager import config_manager

# 自定义目录结构
custom_dirs = {
    'custom_data': 'my_custom_data',
    'reports': 'analysis_reports',
    'logs': 'application_logs'
}

# 创建自定义目录
for dir_name, dir_path in custom_dirs.items():
    full_path = os.path.join(config_manager.get_data_dir(), dir_path)
    os.makedirs(full_path, exist_ok=True)
```

### 动态配置更新 | Dynamic Configuration Updates

```python
# 运行时更新配置
config_manager.set_data_dir('/new/data/path')
config_manager.ensure_directories_exist()

# 验证更新
print(f"新数据目录: {config_manager.get_data_dir()}")
```

## 相关文件 | Related Files

- `tradingagents/config/config_manager.py` - 配置管理器
- `tradingagents/dataflows/config.py` - 数据流配置
- `cli/main.py` - CLI命令实现
- `examples/data_dir_config_demo.py` - 配置演示脚本
- `test_data_config_cli.py` - 配置测试脚本

## 技术支持 | Technical Support

如果遇到配置问题，请：
1. 查看错误日志
2. 运行诊断脚本
3. 检查权限设置
4. 参考故障排除指南

If you encounter configuration issues, please:
1. Check error logs
2. Run diagnostic scripts
3. Check permission settings
4. Refer to the troubleshooting guide

<!-- docs/configuration/google-ai-setup.md -->

# Google AI 配置指南

本指南将帮助您配置Google AI (Gemini)模型，以便在TradingAgents-CN中使用Google的强大AI能力进行股票分析。

## 🎯 概述

TradingAgents-CN v0.1.2新增了对Google AI的完整支持，包括：

- **Gemini 2.0 Flash** - 最新模型，推荐使用
- **Gemini 1.5 Pro** - 强大性能，适合深度分析  
- **Gemini 1.5 Flash** - 快速响应，适合简单分析
- **智能混合嵌入** - Google AI推理 + 阿里百炼嵌入

## 🔑 获取Google AI API密钥

### 1. 访问Google AI Studio

1. 打开 [Google AI Studio](https://aistudio.google.com/)
2. 使用您的Google账号登录
3. 如果是首次使用，需要同意服务条款

### 2. 创建API密钥

1. 在左侧导航栏中点击 **"API keys"**
2. 点击 **"Create API key"** 按钮
3. 选择一个Google Cloud项目（或创建新项目）
4. 复制生成的API密钥

### 3. 配置API密钥

在项目根目录的 `.env` 文件中添加：

```env
# Google AI API密钥
GOOGLE_API_KEY=your_google_api_key_here
```

## 🤖 支持的模型

### Gemini 2.0 Flash (推荐)
- **模型名称**: `gemini-2.0-flash`
- **特点**: 最新版本，性能优秀，LangChain集成稳定
- **适用场景**: 日常股票分析，推荐首选
- **优势**: 
  - 🧠 优秀的推理能力
  - 🌍 完美的中文支持
  - 🔧 稳定的LangChain集成
  - 💾 完整的内存学习功能

### Gemini 1.5 Pro
- **模型名称**: `gemini-1.5-pro`
- **特点**: 强大性能，适合复杂分析
- **适用场景**: 深度分析，重要投资决策
- **优势**: 功能强大，分析深度高

### Gemini 1.5 Flash  
- **模型名称**: `gemini-1.5-flash`
- **特点**: 快速响应，成本较低
- **适用场景**: 快速查询，批量分析
- **优势**: 响应速度快，适合高频使用

## 🔧 配置方法

### 1. Web界面配置

1. **启动Web界面**:
   ```bash
   python -m streamlit run web/app.py
   ```

2. **在左侧边栏中**:
   - 选择 **"Google AI - Gemini模型"** 作为LLM提供商
   - 选择具体的Gemini模型
   - 启用记忆功能获得更好效果

3. **开始分析**:
   - 输入股票代码
   - 选择分析师
   - 点击"开始分析"

### 2. CLI配置

```bash
# 使用Gemini 2.0 Flash模型
python -m cli.main --llm-provider google --model gemini-2.0-flash --stock AAPL

# 使用Gemini 1.5 Pro进行深度分析
python -m cli.main --llm-provider google --model gemini-1.5-pro --stock TSLA --analysts market fundamentals news
```

### 3. Python API配置

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 配置Google AI
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "google"
config["deep_think_llm"] = "gemini-2.0-flash"
config["quick_think_llm"] = "gemini-2.0-flash"
config["memory_enabled"] = True

# 创建分析图
graph = TradingAgentsGraph(["market", "fundamentals"], config=config)

# 执行分析
state, decision = graph.propagate("AAPL", "2025-06-27")
```

## 🔄 智能混合嵌入

TradingAgents-CN的一个独特功能是智能混合嵌入服务：

### 工作原理
```
🧠 Google Gemini (主要推理)
    ↓
🔍 阿里百炼嵌入 (向量化和记忆)
    ↓  
💾 ChromaDB (向量数据库)
    ↓
🎯 中文股票分析结果
```

### 优势
- **最佳性能**: Google AI的强大推理能力
- **中文优化**: 阿里百炼的中文嵌入优势
- **成本控制**: 合理的API调用成本
- **稳定可靠**: 经过充分测试的集成方案

## 🧪 测试配置

### 1. 运行测试脚本

```bash
# 测试Google AI连接
python tests/test_gemini_correct.py

# 测试Web界面Google模型功能
python tests/test_web_interface.py

# 完整的Gemini功能测试
python tests/final_gemini_test.py
```

### 2. 验证配置

```bash
# 检查API密钥配置
python tests/test_all_apis.py

# 测试中文输出功能
python tests/test_chinese_output.py
```

## 💡 使用建议

### 模型选择建议

1. **日常使用**: 推荐 `gemini-2.0-flash`
   - 性能优秀，成本合理
   - LangChain集成稳定
   - 中文支持完美

2. **深度分析**: 使用 `gemini-1.5-pro`
   - 适合重要投资决策
   - 分析深度更高
   - 推理能力更强

3. **快速查询**: 使用 `gemini-1.5-flash`
   - 响应速度快
   - 适合批量分析
   - 成本较低

### 最佳实践

1. **启用内存功能**: 让AI学习您的分析偏好
2. **合理选择分析师**: 根据需要选择相关的分析师
3. **设置适当的研究深度**: 平衡分析质量和时间成本
4. **定期检查API额度**: 确保有足够的API调用额度

## ⚠️ 注意事项

### API限制
- Google AI有API调用频率限制
- 建议合理控制分析频率
- 监控API使用量和成本

### 网络要求
- 需要稳定的网络连接
- 某些地区可能需要特殊网络配置
- 建议使用稳定的网络环境

### 数据安全
- API密钥仅在本地使用
- 不会上传到任何服务器
- 建议定期更换API密钥

## 🔧 故障排除

### 常见问题

#### 1. API密钥无效
```bash
# 检查API密钥格式
echo $GOOGLE_API_KEY

# 验证API密钥有效性
python tests/test_correct_apis.py
```

#### 2. 模型调用失败
- 检查网络连接
- 验证API额度是否充足
- 确认模型名称正确

#### 3. 中文输出异常
- 检查字符编码设置
- 验证模型配置
- 运行中文输出测试

### 获取帮助

如果遇到问题：

1. 📖 查看 [完整文档](../README.md)
2. 🧪 运行 [测试程序](../../tests/)
3. 💬 提交 [GitHub Issue](https://github.com/hsliuping/TradingAgents-CN/issues)

## 🎉 开始使用

现在您已经完成了Google AI的配置，可以开始享受Gemini模型的强大分析能力了！

```bash
# 启动Web界面
python -m streamlit run web/app.py

# 或使用CLI
python -m cli.main --llm-provider google --model gemini-2.0-flash --stock AAPL
```

祝您投资分析愉快！🚀


<!-- docs/configuration/llm-config.md -->

# 大语言模型配置

## 概述

TradingAgents 框架支持多种大语言模型提供商，包括 OpenAI、Anthropic 和 Google AI。本文档详细介绍了如何配置和优化不同的 LLM 以获得最佳性能。

## 支持的 LLM 提供商

### 1. OpenAI

#### 支持的模型
```python
openai_models = {
    "gpt-4o": {
        "description": "最新的 GPT-4 优化版本",
        "context_length": 128000,
        "cost_per_1k_tokens": {"input": 0.005, "output": 0.015},
        "recommended_for": ["深度分析", "复杂推理", "高质量输出"]
    },
    "gpt-4o-mini": {
        "description": "轻量级 GPT-4 版本",
        "context_length": 128000,
        "cost_per_1k_tokens": {"input": 0.00015, "output": 0.0006},
        "recommended_for": ["快速任务", "成本敏感场景", "大量API调用"]
    },
    "gpt-4-turbo": {
        "description": "GPT-4 Turbo 版本",
        "context_length": 128000,
        "cost_per_1k_tokens": {"input": 0.01, "output": 0.03},
        "recommended_for": ["平衡性能和成本", "标准分析任务"]
    },
    "gpt-3.5-turbo": {
        "description": "经济实用的选择",
        "context_length": 16385,
        "cost_per_1k_tokens": {"input": 0.0005, "output": 0.0015},
        "recommended_for": ["简单任务", "预算有限", "快速响应"]
    }
}
```

#### 配置示例
```python
# OpenAI 配置
openai_config = {
    "llm_provider": "openai",
    "backend_url": "https://api.openai.com/v1",
    "deep_think_llm": "gpt-4o",           # 用于复杂分析
    "quick_think_llm": "gpt-4o-mini",     # 用于简单任务
    "api_key": os.getenv("OPENAI_API_KEY"),
    
    # 模型参数
    "model_params": {
        "temperature": 0.1,               # 低温度保证一致性
        "max_tokens": 2000,               # 最大输出长度
        "top_p": 0.9,                     # 核采样参数
        "frequency_penalty": 0.0,         # 频率惩罚
        "presence_penalty": 0.0,          # 存在惩罚
    },
    
    # 速率限制
    "rate_limits": {
        "requests_per_minute": 3500,      # 每分钟请求数
        "tokens_per_minute": 90000,       # 每分钟token数
    },
    
    # 重试配置
    "retry_config": {
        "max_retries": 3,
        "backoff_factor": 2,
        "timeout": 60
    }
}
```

### 2. Anthropic Claude

#### 支持的模型
```python
anthropic_models = {
    "claude-3-opus-20240229": {
        "description": "最强大的 Claude 模型",
        "context_length": 200000,
        "cost_per_1k_tokens": {"input": 0.015, "output": 0.075},
        "recommended_for": ["最复杂的分析", "高质量推理", "创意任务"]
    },
    "claude-3-sonnet-20240229": {
        "description": "平衡性能和成本",
        "context_length": 200000,
        "cost_per_1k_tokens": {"input": 0.003, "output": 0.015},
        "recommended_for": ["标准分析任务", "平衡使用场景"]
    },
    "claude-3-haiku-20240307": {
        "description": "快速且经济的选择",
        "context_length": 200000,
        "cost_per_1k_tokens": {"input": 0.00025, "output": 0.00125},
        "recommended_for": ["快速任务", "大量调用", "成本优化"]
    }
}
```

#### 配置示例
```python
# Anthropic 配置
anthropic_config = {
    "llm_provider": "anthropic",
    "backend_url": "https://api.anthropic.com",
    "deep_think_llm": "claude-3-opus-20240229",
    "quick_think_llm": "claude-3-haiku-20240307",
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    
    # 模型参数
    "model_params": {
        "temperature": 0.1,
        "max_tokens": 2000,
        "top_p": 0.9,
        "top_k": 40,
    },
    
    # 速率限制
    "rate_limits": {
        "requests_per_minute": 1000,
        "tokens_per_minute": 40000,
    }
}
```

### 3. Google AI (Gemini)

#### 支持的模型
```python
google_models = {
    "gemini-pro": {
        "description": "Google 的主力模型",
        "context_length": 32768,
        "cost_per_1k_tokens": {"input": 0.0005, "output": 0.0015},
        "recommended_for": ["多模态任务", "代码分析", "推理任务"]
    },
    "gemini-pro-vision": {
        "description": "支持图像的 Gemini 版本",
        "context_length": 16384,
        "cost_per_1k_tokens": {"input": 0.0005, "output": 0.0015},
        "recommended_for": ["图表分析", "多模态输入"]
    },
    "gemini-2.0-flash": {
        "description": "最新的快速版本",
        "context_length": 32768,
        "cost_per_1k_tokens": {"input": 0.0002, "output": 0.0008},
        "recommended_for": ["快速响应", "实时分析"]
    }
}
```

#### 配置示例
```python
# Google AI 配置
google_config = {
    "llm_provider": "google",
    "backend_url": "https://generativelanguage.googleapis.com/v1",
    "deep_think_llm": "gemini-pro",
    "quick_think_llm": "gemini-2.0-flash",
    "api_key": os.getenv("GOOGLE_API_KEY"),
    
    # 模型参数
    "model_params": {
        "temperature": 0.1,
        "max_output_tokens": 2000,
        "top_p": 0.9,
        "top_k": 40,
    }
}
```

## LLM 选择策略

### 基于任务类型的选择
```python
class LLMSelector:
    """LLM 选择器 - 根据任务选择最适合的模型"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.task_model_mapping = self._initialize_task_mapping()
        
    def select_model(self, task_type: str, complexity: str = "medium") -> str:
        """根据任务类型和复杂度选择模型"""
        
        task_config = self.task_model_mapping.get(task_type, {})
        
        if complexity == "high":
            return task_config.get("high_complexity", self.config["deep_think_llm"])
        elif complexity == "low":
            return task_config.get("low_complexity", self.config["quick_think_llm"])
        else:
            return task_config.get("medium_complexity", self.config["deep_think_llm"])
    
    def _initialize_task_mapping(self) -> Dict:
        """初始化任务-模型映射"""
        return {
            "fundamental_analysis": {
                "high_complexity": "gpt-4o",
                "medium_complexity": "gpt-4o-mini",
                "low_complexity": "gpt-3.5-turbo"
            },
            "technical_analysis": {
                "high_complexity": "claude-3-opus-20240229",
                "medium_complexity": "claude-3-sonnet-20240229",
                "low_complexity": "claude-3-haiku-20240307"
            },
            "news_analysis": {
                "high_complexity": "gpt-4o",
                "medium_complexity": "gpt-4o-mini",
                "low_complexity": "gemini-pro"
            },
            "social_sentiment": {
                "high_complexity": "claude-3-sonnet-20240229",
                "medium_complexity": "gpt-4o-mini",
                "low_complexity": "gemini-2.0-flash"
            },
            "risk_assessment": {
                "high_complexity": "gpt-4o",
                "medium_complexity": "claude-3-sonnet-20240229",
                "low_complexity": "gpt-4o-mini"
            },
            "trading_decision": {
                "high_complexity": "gpt-4o",
                "medium_complexity": "gpt-4o",
                "low_complexity": "claude-3-sonnet-20240229"
            }
        }
```

### 成本优化策略
```python
class CostOptimizer:
    """成本优化器 - 在性能和成本间找到平衡"""
    
    def __init__(self, budget_config: Dict):
        self.daily_budget = budget_config.get("daily_budget", 100)  # 美元
        self.cost_tracking = {}
        self.model_costs = self._load_model_costs()
        
    def get_cost_optimized_config(self, current_usage: Dict) -> Dict:
        """获取成本优化的配置"""
        
        remaining_budget = self._calculate_remaining_budget(current_usage)
        
        if remaining_budget > 50:  # 预算充足
            return {
                "deep_think_llm": "gpt-4o",
                "quick_think_llm": "gpt-4o-mini",
                "max_debate_rounds": 3
            }
        elif remaining_budget > 20:  # 预算中等
            return {
                "deep_think_llm": "gpt-4o-mini",
                "quick_think_llm": "gpt-4o-mini",
                "max_debate_rounds": 2
            }
        else:  # 预算紧张
            return {
                "deep_think_llm": "gpt-3.5-turbo",
                "quick_think_llm": "gpt-3.5-turbo",
                "max_debate_rounds": 1
            }
    
    def estimate_request_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """估算请求成本"""
        
        model_cost = self.model_costs.get(model, {"input": 0.001, "output": 0.002})
        
        input_cost = (input_tokens / 1000) * model_cost["input"]
        output_cost = (output_tokens / 1000) * model_cost["output"]
        
        return input_cost + output_cost
```

## 性能优化

### 提示词优化
```python
class PromptOptimizer:
    """提示词优化器"""
    
    def __init__(self):
        self.prompt_templates = self._load_prompt_templates()
        
    def optimize_prompt(self, task_type: str, model: str, context: Dict) -> str:
        """优化提示词"""
        
        base_prompt = self.prompt_templates[task_type]["base"]
        
        # 根据模型特点调整提示词
        if "gpt" in model.lower():
            optimized_prompt = self._optimize_for_gpt(base_prompt, context)
        elif "claude" in model.lower():
            optimized_prompt = self._optimize_for_claude(base_prompt, context)
        elif "gemini" in model.lower():
            optimized_prompt = self._optimize_for_gemini(base_prompt, context)
        else:
            optimized_prompt = base_prompt
        
        return optimized_prompt
    
    def _optimize_for_gpt(self, prompt: str, context: Dict) -> str:
        """为 GPT 模型优化提示词"""
        
        # GPT 喜欢结构化的指令
        structured_prompt = f"""
任务: {context.get('task_description', '')}

指令:
1. 仔细分析提供的数据
2. 应用相关的金融分析方法
3. 提供清晰的结论和建议
4. 包含置信度评估

数据:
{context.get('data', '')}

请按照以下格式回答:
- 分析结果: [你的分析]
- 结论: [主要结论]
- 建议: [具体建议]
- 置信度: [0-1之间的数值]
"""
        return structured_prompt
    
    def _optimize_for_claude(self, prompt: str, context: Dict) -> str:
        """为 Claude 模型优化提示词"""
        
        # Claude 喜欢对话式的提示
        conversational_prompt = f"""
我需要你作为一个专业的金融分析师来帮助我分析以下数据。

{context.get('data', '')}

请你:
1. 深入分析这些数据的含义
2. 识别关键的趋势和模式
3. 评估潜在的风险和机会
4. 给出你的专业建议

请用专业但易懂的语言回答，并解释你的推理过程。
"""
        return conversational_prompt
```

### 并发控制
```python
class LLMConcurrencyManager:
    """LLM 并发管理器"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.semaphores = self._initialize_semaphores()
        self.rate_limiters = self._initialize_rate_limiters()
        
    def _initialize_semaphores(self) -> Dict:
        """初始化信号量控制并发"""
        return {
            "openai": asyncio.Semaphore(10),      # OpenAI 最多10个并发
            "anthropic": asyncio.Semaphore(5),    # Anthropic 最多5个并发
            "google": asyncio.Semaphore(8)        # Google 最多8个并发
        }
    
    async def execute_with_concurrency_control(self, provider: str, llm_call: callable) -> Any:
        """在并发控制下执行LLM调用"""
        
        semaphore = self.semaphores.get(provider)
        rate_limiter = self.rate_limiters.get(provider)
        
        async with semaphore:
            await rate_limiter.acquire()
            try:
                result = await llm_call()
                return result
            except Exception as e:
                # 处理速率限制错误
                if "rate_limit" in str(e).lower():
                    await asyncio.sleep(60)  # 等待1分钟
                    return await llm_call()
                else:
                    raise e
```

## 监控和调试

### LLM 性能监控
```python
class LLMMonitor:
    """LLM 性能监控"""
    
    def __init__(self):
        self.metrics = {
            "request_count": defaultdict(int),
            "response_times": defaultdict(list),
            "token_usage": defaultdict(dict),
            "error_rates": defaultdict(float),
            "costs": defaultdict(float)
        }
    
    def record_request(self, model: str, response_time: float, 
                      input_tokens: int, output_tokens: int, cost: float):
        """记录请求指标"""
        
        self.metrics["request_count"][model] += 1
        self.metrics["response_times"][model].append(response_time)
        
        if model not in self.metrics["token_usage"]:
            self.metrics["token_usage"][model] = {"input": 0, "output": 0}
        
        self.metrics["token_usage"][model]["input"] += input_tokens
        self.metrics["token_usage"][model]["output"] += output_tokens
        self.metrics["costs"][model] += cost
    
    def get_performance_report(self) -> Dict:
        """获取性能报告"""
        
        report = {}
        
        for model in self.metrics["request_count"]:
            response_times = self.metrics["response_times"][model]
            
            report[model] = {
                "total_requests": self.metrics["request_count"][model],
                "avg_response_time": sum(response_times) / len(response_times) if response_times else 0,
                "total_input_tokens": self.metrics["token_usage"][model].get("input", 0),
                "total_output_tokens": self.metrics["token_usage"][model].get("output", 0),
                "total_cost": self.metrics["costs"][model],
                "avg_cost_per_request": self.metrics["costs"][model] / self.metrics["request_count"][model] if self.metrics["request_count"][model] > 0 else 0
            }
        
        return report
```

## 最佳实践

### 1. 模型选择建议
- **高精度任务**: 使用 GPT-4o 或 Claude-3-Opus
- **平衡场景**: 使用 GPT-4o-mini 或 Claude-3-Sonnet  
- **成本敏感**: 使用 GPT-3.5-turbo 或 Claude-3-Haiku
- **快速响应**: 使用 Gemini-2.0-flash

### 2. 成本控制策略
- 设置每日预算限制
- 使用较小模型处理简单任务
- 实施智能缓存减少重复调用
- 监控token使用量

### 3. 性能优化技巧
- 优化提示词长度和结构
- 使用适当的温度参数
- 实施并发控制避免速率限制
- 定期监控和调整配置

通过合理的LLM配置和优化，可以在保证分析质量的同时控制成本并提高系统性能。


<!-- docs/configuration/token-tracking-guide.md -->

# Token使用统计和成本跟踪指南

本指南介绍如何配置和使用TradingAgents的Token使用统计和成本跟踪功能。

## 功能概述

TradingAgents提供了完整的Token使用统计和成本跟踪功能，包括：

- **实时Token统计**: 自动记录每次LLM调用的输入和输出token数量
- **成本计算**: 根据不同供应商的定价自动计算使用成本
- **多存储支持**: 支持JSON文件存储和MongoDB数据库存储
- **统计分析**: 提供详细的使用统计和成本分析
- **成本警告**: 当使用成本超过阈值时自动提醒

## 支持的LLM供应商

目前支持以下LLM供应商的Token统计：

- ✅ **DashScope (阿里百炼)**: 完全支持，自动提取API响应中的token使用量
- 🔄 **OpenAI**: 计划支持
- 🔄 **Google AI**: 计划支持
- 🔄 **Anthropic**: 计划支持

## 配置方法

### 1. 基础配置

在项目根目录创建或编辑 `.env` 文件：

```bash
# 启用成本跟踪（默认启用）
ENABLE_COST_TRACKING=true

# 成本警告阈值（人民币）
COST_ALERT_THRESHOLD=100.0

# DashScope API密钥
DASHSCOPE_API_KEY=your_dashscope_api_key_here
```

### 2. 存储配置

#### 选项1: JSON文件存储（默认）

默认情况下，Token使用记录保存在 `config/usage.json` 文件中。

```bash
# 最大记录数量（默认10000）
MAX_USAGE_RECORDS=10000

# 自动保存使用记录（默认启用）
AUTO_SAVE_USAGE=true
```

#### 选项2: MongoDB存储（推荐用于生产环境）

对于大量数据和高性能需求，推荐使用MongoDB存储：

```bash
# 启用MongoDB存储
USE_MONGODB_STORAGE=true

# MongoDB连接字符串
# 本地MongoDB
MONGODB_CONNECTION_STRING=mongodb://localhost:27017/

# 或云MongoDB（如MongoDB Atlas）
# MONGODB_CONNECTION_STRING=mongodb+srv://username:password@cluster.mongodb.net/

# 数据库名称
MONGODB_DATABASE_NAME=tradingagents
```

### 3. 安装MongoDB依赖（如果使用MongoDB存储）

```bash
pip install pymongo
```

## 使用方法

### 1. 自动Token统计

当使用DashScope适配器时，Token统计会自动进行：

```python
from tradingagents.llm_adapters.dashscope_adapter import ChatDashScope
from langchain_core.messages import HumanMessage

# 初始化LLM
llm = ChatDashScope(
    model="qwen-turbo",
    temperature=0.7
)

# 发送消息（自动记录token使用）
response = llm.invoke([
    HumanMessage(content="分析一下苹果公司的股票")
], session_id="my_session", analysis_type="stock_analysis")
```

### 2. 查看使用统计

```python
from tradingagents.config.config_manager import config_manager

# 获取最近30天的统计
stats = config_manager.get_usage_statistics(30)

print(f"总成本: ¥{stats['total_cost']:.4f}")
print(f"总请求数: {stats['total_requests']}")
print(f"输入tokens: {stats['total_input_tokens']}")
print(f"输出tokens: {stats['total_output_tokens']}")

# 按供应商查看统计
for provider, provider_stats in stats['provider_stats'].items():
    print(f"{provider}: ¥{provider_stats['cost']:.4f}")
```

### 3. 查看会话成本

```python
from tradingagents.config.config_manager import token_tracker

# 查看特定会话的成本
session_cost = token_tracker.get_session_cost("my_session")
print(f"会话成本: ¥{session_cost:.4f}")
```

### 4. 估算成本

```python
# 估算成本（用于预算规划）
estimated_cost = token_tracker.estimate_cost(
    provider="dashscope",
    model_name="qwen-turbo",
    estimated_input_tokens=1000,
    estimated_output_tokens=500
)
print(f"估算成本: ¥{estimated_cost:.4f}")
```

## 定价配置

系统内置了主要LLM供应商的定价信息，也可以自定义定价：

```python
from tradingagents.config.config_manager import config_manager, PricingConfig

# 添加自定义定价
custom_pricing = PricingConfig(
    provider="dashscope",
    model_name="qwen-max",
    input_price_per_1k=0.02,   # 每1000个输入token的价格（人民币）
    output_price_per_1k=0.06,  # 每1000个输出token的价格（人民币）
    currency="CNY"
)

pricing_list = config_manager.load_pricing()
pricing_list.append(custom_pricing)
config_manager.save_pricing(pricing_list)
```

## 内置定价表

### DashScope (阿里百炼)

| 模型 | 输入价格 (¥/1K tokens) | 输出价格 (¥/1K tokens) |
|------|----------------------|----------------------|
| qwen-turbo | 0.002 | 0.006 |
| qwen-plus-latest | 0.004 | 0.012 |
| qwen-max | 0.02 | 0.06 |

### OpenAI

| 模型 | 输入价格 ($/1K tokens) | 输出价格 ($/1K tokens) |
|------|----------------------|----------------------|
| gpt-3.5-turbo | 0.0015 | 0.002 |
| gpt-4 | 0.03 | 0.06 |
| gpt-4-turbo | 0.01 | 0.03 |

## 测试Token统计功能

运行测试脚本验证功能：

```bash
# 测试DashScope token统计
python tests/test_dashscope_token_tracking.py
```

## MongoDB存储优势

使用MongoDB存储相比JSON文件存储有以下优势：

1. **高性能**: 支持大量数据的高效查询和聚合
2. **可扩展性**: 支持分布式部署和水平扩展
3. **数据安全**: 支持备份、复制和故障恢复
4. **高级查询**: 支持复杂的聚合查询和统计分析
5. **并发支持**: 支持多用户并发访问

### MongoDB索引优化

系统会自动创建以下索引以提高查询性能：

- 复合索引：`(timestamp, provider, model_name)`
- 单字段索引：`session_id`, `analysis_type`

## 成本控制建议

1. **设置合理的成本警告阈值**
2. **定期查看使用统计，优化使用模式**
3. **根据需求选择合适的模型（平衡成本和性能）**
4. **使用会话ID跟踪特定分析的成本**
5. **定期清理旧的使用记录（MongoDB支持自动清理）**

## 故障排除

### 1. Token统计不工作

- 检查API密钥是否正确配置
- 确认 `ENABLE_COST_TRACKING=true`
- 查看控制台是否有错误信息

### 2. MongoDB连接失败

- 检查MongoDB服务是否运行
- 验证连接字符串格式
- 确认网络连接和防火墙设置
- 检查用户权限

### 3. 成本计算不准确

- 检查定价配置是否正确
- 确认模型名称匹配
- 验证token提取逻辑

## 最佳实践

1. **生产环境使用MongoDB存储**
2. **定期备份使用数据**
3. **监控成本趋势，及时调整策略**
4. **使用有意义的会话ID和分析类型**
5. **定期更新定价信息**

## 未来计划

- [ ] 支持更多LLM供应商的Token统计
- [ ] 添加可视化仪表板
- [ ] 支持成本预算和限制
- [ ] 添加使用报告导出功能
- [ ] 支持团队和用户级别的成本跟踪

<!-- docs/data/caching.md -->

# 数据缓存策略

## 概述

TradingAgents 框架采用多层次的缓存策略来优化数据访问性能，减少API调用成本，并提高系统响应速度。本文档详细介绍了缓存架构、策略、实现和最佳实践。

## 缓存架构

### 多层缓存设计

```mermaid
graph TB
    subgraph "应用层"
        AGENT1[分析师智能体]
        AGENT2[研究员智能体]
        AGENT3[交易员智能体]
    end
    
    subgraph "缓存层次"
        L1[L1: 内存缓存<br/>最快访问]
        L2[L2: 本地文件缓存<br/>持久化存储]
        L3[L3: Redis缓存<br/>分布式共享]
        L4[L4: 数据库缓存<br/>长期存储]
    end
    
    subgraph "数据源"
        API1[FinnHub API]
        API2[Yahoo Finance]
        API3[Reddit API]
        API4[Google News]
    end
    
    AGENT1 --> L1
    AGENT2 --> L1
    AGENT3 --> L1
    
    L1 --> L2
    L2 --> L3
    L3 --> L4
    
    L4 --> API1
    L4 --> API2
    L4 --> API3
    L4 --> API4
```

## 1. 缓存管理器

### 核心缓存类
```python
class CacheManager:
    """缓存管理器 - 统一管理多层缓存"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.memory_cache = MemoryCache(config.get("memory_cache", {}))
        self.file_cache = FileCache(config.get("file_cache", {}))
        self.redis_cache = RedisCache(config.get("redis_cache", {})) if config.get("redis_enabled") else None
        self.db_cache = DatabaseCache(config.get("db_cache", {})) if config.get("db_enabled") else None
        
        # 缓存策略配置
        self.cache_strategies = self._load_cache_strategies()
        self.ttl_config = self._load_ttl_config()
        
    def get(self, key: str, data_type: str = "default") -> Optional[Any]:
        """获取缓存数据 - 按层次查找"""
        
        # L1: 内存缓存
        data = self.memory_cache.get(key)
        if data is not None:
            self._record_cache_hit("memory", key, data_type)
            return data
        
        # L2: 文件缓存
        data = self.file_cache.get(key)
        if data is not None:
            # 回填到内存缓存
            self.memory_cache.set(key, data, self._get_ttl(data_type))
            self._record_cache_hit("file", key, data_type)
            return data
        
        # L3: Redis缓存
        if self.redis_cache:
            data = self.redis_cache.get(key)
            if data is not None:
                # 回填到上层缓存
                self.file_cache.set(key, data, self._get_ttl(data_type))
                self.memory_cache.set(key, data, self._get_ttl(data_type))
                self._record_cache_hit("redis", key, data_type)
                return data
        
        # L4: 数据库缓存
        if self.db_cache:
            data = self.db_cache.get(key)
            if data is not None:
                # 回填到所有上层缓存
                if self.redis_cache:
                    self.redis_cache.set(key, data, self._get_ttl(data_type))
                self.file_cache.set(key, data, self._get_ttl(data_type))
                self.memory_cache.set(key, data, self._get_ttl(data_type))
                self._record_cache_hit("database", key, data_type)
                return data
        
        # 缓存未命中
        self._record_cache_miss(key, data_type)
        return None
    
    def set(self, key: str, data: Any, data_type: str = "default", ttl: Optional[int] = None) -> None:
        """设置缓存数据 - 写入所有层次"""
        
        if ttl is None:
            ttl = self._get_ttl(data_type)
        
        # 根据数据类型和大小决定缓存策略
        cache_strategy = self._determine_cache_strategy(data, data_type)
        
        # L1: 内存缓存 (总是缓存小数据)
        if cache_strategy["memory"]:
            self.memory_cache.set(key, data, ttl)
        
        # L2: 文件缓存 (缓存中等大小数据)
        if cache_strategy["file"]:
            self.file_cache.set(key, data, ttl)
        
        # L3: Redis缓存 (缓存共享数据)
        if cache_strategy["redis"] and self.redis_cache:
            self.redis_cache.set(key, data, ttl)
        
        # L4: 数据库缓存 (缓存重要数据)
        if cache_strategy["database"] and self.db_cache:
            self.db_cache.set(key, data, ttl)
    
    def _determine_cache_strategy(self, data: Any, data_type: str) -> Dict[str, bool]:
        """确定缓存策略"""
        
        data_size = self._estimate_data_size(data)
        data_importance = self._assess_data_importance(data_type)
        
        strategy = {
            "memory": data_size < 1024 * 1024,  # 小于1MB
            "file": data_size < 10 * 1024 * 1024,  # 小于10MB
            "redis": data_importance >= 0.7,  # 重要数据
            "database": data_importance >= 0.8 or data_type in ["fundamental_data", "company_profile"]
        }
        
        return strategy
    
    def _get_ttl(self, data_type: str) -> int:
        """获取数据类型的TTL"""
        return self.ttl_config.get(data_type, self.ttl_config["default"])
```

## 2. 内存缓存 (L1)

### 高速内存缓存
```python
class MemoryCache:
    """内存缓存 - 最快的缓存层"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.cache = {}
        self.access_times = {}
        self.max_size = config.get("max_size", 1000)
        self.cleanup_threshold = config.get("cleanup_threshold", 0.8)
        
    def get(self, key: str) -> Optional[Any]:
        """获取缓存项"""
        if key in self.cache:
            item = self.cache[key]
            
            # 检查是否过期
            if self._is_expired(item):
                del self.cache[key]
                if key in self.access_times:
                    del self.access_times[key]
                return None
            
            # 更新访问时间
            self.access_times[key] = time.time()
            return item["data"]
        
        return None
    
    def set(self, key: str, data: Any, ttl: int) -> None:
        """设置缓存项"""
        
        # 检查是否需要清理
        if len(self.cache) >= self.max_size * self.cleanup_threshold:
            self._cleanup_cache()
        
        # 存储数据
        self.cache[key] = {
            "data": data,
            "timestamp": time.time(),
            "ttl": ttl
        }
        self.access_times[key] = time.time()
    
    def _cleanup_cache(self) -> None:
        """清理过期和最少使用的缓存项"""
        
        current_time = time.time()
        
        # 首先清理过期项
        expired_keys = []
        for key, item in self.cache.items():
            if self._is_expired(item):
                expired_keys.append(key)
        
        for key in expired_keys:
            del self.cache[key]
            if key in self.access_times:
                del self.access_times[key]
        
        # 如果还是太多，使用LRU策略清理
        if len(self.cache) >= self.max_size * self.cleanup_threshold:
            # 按访问时间排序，删除最少使用的
            sorted_keys = sorted(self.access_times.keys(), key=lambda k: self.access_times[k])
            keys_to_remove = sorted_keys[:len(sorted_keys) // 4]  # 删除25%
            
            for key in keys_to_remove:
                if key in self.cache:
                    del self.cache[key]
                if key in self.access_times:
                    del self.access_times[key]
    
    def _is_expired(self, item: Dict) -> bool:
        """检查缓存项是否过期"""
        return time.time() - item["timestamp"] > item["ttl"]
```

## 3. 文件缓存 (L2)

### 持久化文件缓存
```python
class FileCache:
    """文件缓存 - 持久化存储"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.cache_dir = Path(config.get("cache_dir", "./cache"))
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.compression_enabled = config.get("compression", True)
        self.max_file_size = config.get("max_file_size", 50 * 1024 * 1024)  # 50MB
        
    def get(self, key: str) -> Optional[Any]:
        """从文件获取缓存数据"""
        
        cache_file = self._get_cache_file_path(key)
        
        if not cache_file.exists():
            return None
        
        try:
            # 检查文件修改时间
            if self._is_file_expired(cache_file, key):
                cache_file.unlink()  # 删除过期文件
                return None
            
            # 读取数据
            with open(cache_file, 'rb') as f:
                if self.compression_enabled:
                    compressed_data = f.read()
                    data = self._decompress_data(compressed_data)
                else:
                    data = pickle.load(f)
            
            return data
            
        except Exception as e:
            print(f"Error reading cache file {cache_file}: {e}")
            # 删除损坏的缓存文件
            if cache_file.exists():
                cache_file.unlink()
            return None
    
    def set(self, key: str, data: Any, ttl: int) -> None:
        """将数据写入文件缓存"""
        
        cache_file = self._get_cache_file_path(key)
        
        try:
            # 检查数据大小
            data_size = self._estimate_data_size(data)
            if data_size > self.max_file_size:
                print(f"Data too large for file cache: {data_size} bytes")
                return
            
            # 创建缓存元数据
            cache_data = {
                "data": data,
                "timestamp": time.time(),
                "ttl": ttl,
                "key": key
            }
            
            # 写入文件
            with open(cache_file, 'wb') as f:
                if self.compression_enabled:
                    compressed_data = self._compress_data(cache_data)
                    f.write(compressed_data)
                else:
                    pickle.dump(cache_data, f)
            
        except Exception as e:
            print(f"Error writing cache file {cache_file}: {e}")
    
    def _get_cache_file_path(self, key: str) -> Path:
        """获取缓存文件路径"""
        # 使用哈希避免文件名过长或包含特殊字符
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.cache"
    
    def _is_file_expired(self, cache_file: Path, key: str) -> bool:
        """检查缓存文件是否过期"""
        try:
            with open(cache_file, 'rb') as f:
                if self.compression_enabled:
                    compressed_data = f.read()
                    cache_data = self._decompress_data(compressed_data)
                else:
                    cache_data = pickle.load(f)
            
            return time.time() - cache_data["timestamp"] > cache_data["ttl"]
            
        except Exception:
            return True  # 如果无法读取，认为已过期
    
    def _compress_data(self, data: Any) -> bytes:
        """压缩数据"""
        import gzip
        pickled_data = pickle.dumps(data)
        return gzip.compress(pickled_data)
    
    def _decompress_data(self, compressed_data: bytes) -> Any:
        """解压数据"""
        import gzip
        pickled_data = gzip.decompress(compressed_data)
        return pickle.loads(pickled_data)
    
    def cleanup_expired_files(self) -> None:
        """清理过期的缓存文件"""
        for cache_file in self.cache_dir.glob("*.cache"):
            try:
                if self._is_file_expired(cache_file, ""):
                    cache_file.unlink()
            except Exception as e:
                print(f"Error checking cache file {cache_file}: {e}")
```

## 4. Redis缓存 (L3)

### 分布式共享缓存
```python
class RedisCache:
    """Redis缓存 - 分布式共享缓存"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.redis_client = self._initialize_redis_client()
        self.key_prefix = config.get("key_prefix", "tradingagents:")
        self.serialization_format = config.get("serialization", "pickle")  # pickle, json, msgpack
        
    def _initialize_redis_client(self):
        """初始化Redis客户端"""
        try:
            import redis
            
            redis_config = {
                "host": self.config.get("host", "localhost"),
                "port": self.config.get("port", 6379),
                "db": self.config.get("db", 0),
                "password": self.config.get("password"),
                "socket_timeout": self.config.get("timeout", 5),
                "socket_connect_timeout": self.config.get("connect_timeout", 5),
                "retry_on_timeout": True,
                "health_check_interval": 30
            }
            
            # 移除None值
            redis_config = {k: v for k, v in redis_config.items() if v is not None}
            
            client = redis.Redis(**redis_config)
            
            # 测试连接
            client.ping()
            print("Redis connection established")
            
            return client
            
        except Exception as e:
            print(f"Failed to connect to Redis: {e}")
            return None
    
    def get(self, key: str) -> Optional[Any]:
        """从Redis获取数据"""
        if not self.redis_client:
            return None
        
        try:
            full_key = self.key_prefix + key
            data = self.redis_client.get(full_key)
            
            if data is None:
                return None
            
            # 反序列化数据
            return self._deserialize_data(data)
            
        except Exception as e:
            print(f"Error getting data from Redis: {e}")
            return None
    
    def set(self, key: str, data: Any, ttl: int) -> None:
        """向Redis设置数据"""
        if not self.redis_client:
            return
        
        try:
            full_key = self.key_prefix + key
            
            # 序列化数据
            serialized_data = self._serialize_data(data)
            
            # 设置数据和TTL
            self.redis_client.setex(full_key, ttl, serialized_data)
            
        except Exception as e:
            print(f"Error setting data to Redis: {e}")
    
    def _serialize_data(self, data: Any) -> bytes:
        """序列化数据"""
        if self.serialization_format == "pickle":
            return pickle.dumps(data)
        elif self.serialization_format == "json":
            import json
            return json.dumps(data, default=str).encode('utf-8')
        elif self.serialization_format == "msgpack":
            import msgpack
            return msgpack.packb(data, default=str)
        else:
            raise ValueError(f"Unsupported serialization format: {self.serialization_format}")
    
    def _deserialize_data(self, data: bytes) -> Any:
        """反序列化数据"""
        if self.serialization_format == "pickle":
            return pickle.loads(data)
        elif self.serialization_format == "json":
            import json
            return json.loads(data.decode('utf-8'))
        elif self.serialization_format == "msgpack":
            import msgpack
            return msgpack.unpackb(data, raw=False)
        else:
            raise ValueError(f"Unsupported serialization format: {self.serialization_format}")
    
    def delete(self, key: str) -> None:
        """删除Redis中的数据"""
        if not self.redis_client:
            return
        
        try:
            full_key = self.key_prefix + key
            self.redis_client.delete(full_key)
        except Exception as e:
            print(f"Error deleting data from Redis: {e}")
    
    def clear_expired(self) -> None:
        """清理过期的键（Redis自动处理TTL）"""
        # Redis会自动清理过期键，这里可以添加额外的清理逻辑
        pass
```

## 5. 缓存策略配置

### TTL配置
```python
# 不同数据类型的TTL配置
TTL_CONFIG = {
    "price_data": 60,           # 1分钟 - 价格数据变化快
    "fundamental_data": 3600,   # 1小时 - 基本面数据相对稳定
    "company_profile": 86400,   # 24小时 - 公司信息变化很少
    "news_data": 1800,          # 30分钟 - 新闻数据中等频率
    "social_data": 900,         # 15分钟 - 社交媒体数据变化较快
    "technical_indicators": 300, # 5分钟 - 技术指标需要较新数据
    "market_data": 600,         # 10分钟 - 市场数据中等频率
    "historical_data": 7200,    # 2小时 - 历史数据相对稳定
    "default": 1800             # 30分钟 - 默认TTL
}

# 缓存重要性评分
DATA_IMPORTANCE = {
    "price_data": 0.9,          # 高重要性
    "fundamental_data": 0.8,    # 高重要性
    "company_profile": 0.7,     # 中高重要性
    "news_data": 0.6,           # 中等重要性
    "social_data": 0.5,         # 中等重要性
    "technical_indicators": 0.7, # 中高重要性
    "market_data": 0.6,         # 中等重要性
    "historical_data": 0.8,     # 高重要性
}
```

## 6. 缓存监控和优化

### 缓存性能监控
```python
class CacheMonitor:
    """缓存性能监控"""
    
    def __init__(self):
        self.metrics = {
            "hits": defaultdict(int),
            "misses": defaultdict(int),
            "hit_rates": defaultdict(float),
            "response_times": defaultdict(list),
            "cache_sizes": defaultdict(int)
        }
        
    def record_hit(self, cache_level: str, key: str, data_type: str, response_time: float = None):
        """记录缓存命中"""
        self.metrics["hits"][cache_level] += 1
        if response_time:
            self.metrics["response_times"][cache_level].append(response_time)
        
        self._update_hit_rate(cache_level)
    
    def record_miss(self, key: str, data_type: str):
        """记录缓存未命中"""
        self.metrics["misses"]["total"] += 1
        self._update_hit_rate("total")
    
    def _update_hit_rate(self, cache_level: str):
        """更新命中率"""
        hits = self.metrics["hits"][cache_level]
        misses = self.metrics["misses"].get(cache_level, 0)
        total = hits + misses
        
        if total > 0:
            self.metrics["hit_rates"][cache_level] = hits / total
    
    def get_performance_report(self) -> Dict:
        """获取性能报告"""
        return {
            "hit_rates": dict(self.metrics["hit_rates"]),
            "total_hits": sum(self.metrics["hits"].values()),
            "total_misses": sum(self.metrics["misses"].values()),
            "avg_response_times": {
                level: sum(times) / len(times) if times else 0
                for level, times in self.metrics["response_times"].items()
            },
            "cache_efficiency": self._calculate_cache_efficiency()
        }
    
    def _calculate_cache_efficiency(self) -> float:
        """计算缓存效率"""
        total_hits = sum(self.metrics["hits"].values())
        total_requests = total_hits + sum(self.metrics["misses"].values())
        
        return total_hits / total_requests if total_requests > 0 else 0.0
```

## 7. 缓存最佳实践

### 使用建议
```python
class CacheBestPractices:
    """缓存最佳实践指南"""
    
    @staticmethod
    def generate_cache_key(symbol: str, data_type: str, date: str = None, **kwargs) -> str:
        """生成标准化的缓存键"""
        
        key_parts = [symbol.upper(), data_type]
        
        if date:
            key_parts.append(date)
        
        # 添加其他参数
        for k, v in sorted(kwargs.items()):
            key_parts.append(f"{k}:{v}")
        
        return ":".join(key_parts)
    
    @staticmethod
    def should_cache_data(data: Any, data_type: str) -> bool:
        """判断是否应该缓存数据"""
        
        # 不缓存空数据
        if not data:
            return False
        
        # 不缓存错误数据
        if isinstance(data, dict) and "error" in data:
            return False
        
        # 不缓存过大的数据
        data_size = CacheBestPractices._estimate_size(data)
        if data_size > 100 * 1024 * 1024:  # 100MB
            return False
        
        return True
    
    @staticmethod
    def _estimate_size(obj: Any) -> int:
        """估算对象大小"""
        try:
            return len(pickle.dumps(obj))
        except:
            return 0
```

通过这套完整的缓存策略，TradingAgents 能够显著提高数据访问性能，减少API调用成本，并提供更好的用户体验。


<!-- docs/data/data-processing.md -->

# 数据处理流程

## 概述

TradingAgents 框架的数据处理系统负责将来自多个数据源的原始数据转换为智能体可以使用的标准化、高质量信息。本文档详细介绍了数据获取、清洗、转换、验证和分发的完整流程。

## 数据处理架构

### 数据处理管道

```mermaid
graph TB
    subgraph "数据获取层"
        API1[FinnHub API]
        API2[Yahoo Finance]
        API3[Reddit API]
        API4[Google News]
    end
    
    subgraph "数据预处理层"
        COLLECT[数据收集器]
        VALIDATE[数据验证器]
        CLEAN[数据清洗器]
        NORMALIZE[数据标准化器]
    end
    
    subgraph "数据转换层"
        TRANSFORM[数据转换器]
        ENRICH[数据增强器]
        AGGREGATE[数据聚合器]
        FEATURE[特征工程器]
    end
    
    subgraph "数据存储层"
        CACHE[缓存系统]
        DATABASE[数据库]
        MEMORY[内存存储]
    end
    
    subgraph "数据分发层"
        ROUTER[数据路由器]
        FORMATTER[格式化器]
        DISPATCHER[分发器]
    end
    
    API1 --> COLLECT
    API2 --> COLLECT
    API3 --> COLLECT
    API4 --> COLLECT
    
    COLLECT --> VALIDATE
    VALIDATE --> CLEAN
    CLEAN --> NORMALIZE
    
    NORMALIZE --> TRANSFORM
    TRANSFORM --> ENRICH
    ENRICH --> AGGREGATE
    AGGREGATE --> FEATURE
    
    FEATURE --> CACHE
    FEATURE --> DATABASE
    FEATURE --> MEMORY
    
    CACHE --> ROUTER
    DATABASE --> ROUTER
    MEMORY --> ROUTER
    
    ROUTER --> FORMATTER
    FORMATTER --> DISPATCHER
```

## 1. 数据收集器

### 核心功能
```python
class DataCollector:
    """数据收集器 - 统一收集各数据源的数据"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.data_sources = self._initialize_data_sources()
        self.collection_scheduler = CollectionScheduler()
        self.error_handler = DataErrorHandler()
        
    def collect_comprehensive_data(self, symbol: str, date: str = None) -> Dict:
        """收集综合数据"""
        
        collection_tasks = {
            "price_data": self._collect_price_data,
            "fundamental_data": self._collect_fundamental_data,
            "technical_data": self._collect_technical_data,
            "news_data": self._collect_news_data,
            "social_data": self._collect_social_data,
            "market_data": self._collect_market_data
        }
        
        collected_data = {}
        collection_metadata = {}
        
        # 并行收集数据
        with ThreadPoolExecutor(max_workers=6) as executor:
            future_to_task = {
                executor.submit(task_func, symbol, date): task_name
                for task_name, task_func in collection_tasks.items()
            }
            
            for future in as_completed(future_to_task):
                task_name = future_to_task[future]
                try:
                    result = future.result(timeout=30)  # 30秒超时
                    collected_data[task_name] = result["data"]
                    collection_metadata[task_name] = result["metadata"]
                except Exception as e:
                    self.error_handler.handle_collection_error(task_name, e)
                    collected_data[task_name] = {}
                    collection_metadata[task_name] = {"error": str(e)}
        
        return {
            "data": collected_data,
            "metadata": collection_metadata,
            "collection_timestamp": datetime.now().isoformat(),
            "symbol": symbol,
            "date": date
        }
    
    def _collect_price_data(self, symbol: str, date: str = None) -> Dict:
        """收集价格数据"""
        
        price_sources = ["finnhub", "yahoo_finance"]
        price_data = {}
        
        for source in price_sources:
            try:
                if source == "finnhub" and "finnhub" in self.data_sources:
                    data = self.data_sources["finnhub"].get_stock_price(symbol)
                    price_data["finnhub"] = data
                    break  # 优先使用 FinnHub
                elif source == "yahoo_finance":
                    data = self.data_sources["yahoo"].get_current_price(symbol)
                    price_data["yahoo"] = data
            except Exception as e:
                print(f"Error collecting price data from {source}: {e}")
        
        # 选择最佳数据源
        best_price_data = self._select_best_price_data(price_data)
        
        return {
            "data": best_price_data,
            "metadata": {
                "sources_attempted": price_sources,
                "sources_successful": list(price_data.keys()),
                "primary_source": self._identify_primary_source(price_data)
            }
        }
    
    def _collect_fundamental_data(self, symbol: str, date: str = None) -> Dict:
        """收集基本面数据"""
        
        fundamental_data = {}
        
        # 财务报表数据
        try:
            if "finnhub" in self.data_sources:
                financials = self.data_sources["finnhub"].get_financial_statements(symbol)
                fundamental_data["financials"] = financials
        except Exception as e:
            print(f"Error collecting financial statements: {e}")
        
        # 公司概况
        try:
            if "finnhub" in self.data_sources:
                profile = self.data_sources["finnhub"].get_company_profile(symbol)
                fundamental_data["profile"] = profile
        except Exception as e:
            print(f"Error collecting company profile: {e}")
        
        # 估值指标
        try:
            if "yahoo" in self.data_sources:
                valuation = self.data_sources["yahoo"].get_valuation_metrics(symbol)
                fundamental_data["valuation"] = valuation
        except Exception as e:
            print(f"Error collecting valuation metrics: {e}")
        
        return {
            "data": fundamental_data,
            "metadata": {
                "data_completeness": self._assess_fundamental_completeness(fundamental_data),
                "data_freshness": self._assess_data_freshness(fundamental_data)
            }
        }
```

## 2. 数据验证器

### 数据质量检查
```python
class DataValidator:
    """数据验证器 - 确保数据质量和完整性"""
    
    def __init__(self):
        self.validation_rules = self._load_validation_rules()
        self.quality_metrics = QualityMetrics()
        
    def validate_collected_data(self, collected_data: Dict) -> Dict:
        """验证收集的数据"""
        
        validation_results = {}
        
        for data_type, data in collected_data["data"].items():
            validation_result = self._validate_data_type(data_type, data)
            validation_results[data_type] = validation_result
        
        # 计算整体数据质量评分
        overall_quality = self._calculate_overall_quality(validation_results)
        
        return {
            "validation_results": validation_results,
            "overall_quality": overall_quality,
            "quality_grade": self._assign_quality_grade(overall_quality),
            "issues_found": self._extract_issues(validation_results),
            "recommendations": self._generate_quality_recommendations(validation_results)
        }
    
    def _validate_data_type(self, data_type: str, data: Dict) -> Dict:
        """验证特定类型的数据"""
        
        validation_checks = {
            "completeness": self._check_completeness(data_type, data),
            "accuracy": self._check_accuracy(data_type, data),
            "consistency": self._check_consistency(data_type, data),
            "timeliness": self._check_timeliness(data_type, data),
            "format": self._check_format(data_type, data)
        }
        
        # 计算验证评分
        validation_score = sum(check["score"] for check in validation_checks.values()) / len(validation_checks)
        
        return {
            "checks": validation_checks,
            "validation_score": validation_score,
            "status": "passed" if validation_score > 0.8 else "warning" if validation_score > 0.6 else "failed",
            "critical_issues": [check["issue"] for check in validation_checks.values() if check.get("critical")]
        }
    
    def _check_completeness(self, data_type: str, data: Dict) -> Dict:
        """检查数据完整性"""
        
        required_fields = self.validation_rules[data_type]["required_fields"]
        missing_fields = [field for field in required_fields if field not in data]
        
        completeness_score = 1.0 - (len(missing_fields) / len(required_fields))
        
        return {
            "score": completeness_score,
            "missing_fields": missing_fields,
            "critical": len(missing_fields) > len(required_fields) * 0.5,
            "issue": f"Missing {len(missing_fields)} required fields" if missing_fields else None
        }
    
    def _check_accuracy(self, data_type: str, data: Dict) -> Dict:
        """检查数据准确性"""
        
        accuracy_issues = []
        
        if data_type == "price_data":
            # 价格合理性检查
            if "current_price" in data:
                price = data["current_price"]
                if not isinstance(price, (int, float)) or price <= 0:
                    accuracy_issues.append("Invalid price value")
                elif price > 10000:  # 异常高价格
                    accuracy_issues.append("Unusually high price")
        
        elif data_type == "fundamental_data":
            # 财务数据合理性检查
            if "market_cap" in data:
                market_cap = data["market_cap"]
                if market_cap and market_cap < 0:
                    accuracy_issues.append("Negative market cap")
        
        accuracy_score = 1.0 if not accuracy_issues else 0.5
        
        return {
            "score": accuracy_score,
            "issues": accuracy_issues,
            "critical": len(accuracy_issues) > 0,
            "issue": "; ".join(accuracy_issues) if accuracy_issues else None
        }
```

## 3. 数据清洗器

### 数据清洗流程
```python
class DataCleaner:
    """数据清洗器 - 清理和修复数据问题"""
    
    def __init__(self):
        self.cleaning_strategies = self._initialize_cleaning_strategies()
        self.outlier_detector = OutlierDetector()
        
    def clean_data(self, validated_data: Dict) -> Dict:
        """清洗数据"""
        
        cleaned_data = {}
        cleaning_log = {}
        
        for data_type, data in validated_data["data"].items():
            cleaning_result = self._clean_data_type(data_type, data)
            cleaned_data[data_type] = cleaning_result["cleaned_data"]
            cleaning_log[data_type] = cleaning_result["cleaning_log"]
        
        return {
            "cleaned_data": cleaned_data,
            "cleaning_log": cleaning_log,
            "cleaning_summary": self._generate_cleaning_summary(cleaning_log)
        }
    
    def _clean_data_type(self, data_type: str, data: Dict) -> Dict:
        """清洗特定类型的数据"""
        
        cleaned_data = data.copy()
        cleaning_operations = []
        
        # 处理缺失值
        missing_value_result = self._handle_missing_values(data_type, cleaned_data)
        cleaned_data.update(missing_value_result["data"])
        cleaning_operations.extend(missing_value_result["operations"])
        
        # 处理异常值
        outlier_result = self._handle_outliers(data_type, cleaned_data)
        cleaned_data.update(outlier_result["data"])
        cleaning_operations.extend(outlier_result["operations"])
        
        # 数据类型转换
        type_conversion_result = self._convert_data_types(data_type, cleaned_data)
        cleaned_data.update(type_conversion_result["data"])
        cleaning_operations.extend(type_conversion_result["operations"])
        
        # 数据格式标准化
        standardization_result = self._standardize_formats(data_type, cleaned_data)
        cleaned_data.update(standardization_result["data"])
        cleaning_operations.extend(standardization_result["operations"])
        
        return {
            "cleaned_data": cleaned_data,
            "cleaning_log": {
                "operations": cleaning_operations,
                "data_quality_improvement": self._measure_quality_improvement(data, cleaned_data)
            }
        }
    
    def _handle_missing_values(self, data_type: str, data: Dict) -> Dict:
        """处理缺失值"""
        
        operations = []
        updated_data = {}
        
        if data_type == "price_data":
            # 价格数据的缺失值处理
            if "current_price" not in data or data["current_price"] is None:
                # 尝试从历史数据推断
                if "previous_close" in data and data["previous_close"]:
                    updated_data["current_price"] = data["previous_close"]
                    operations.append("Imputed current_price from previous_close")
        
        elif data_type == "fundamental_data":
            # 基本面数据的缺失值处理
            if "market_cap" not in data or data["market_cap"] is None:
                # 尝试计算市值
                if "shares_outstanding" in data and "current_price" in data:
                    if data["shares_outstanding"] and data["current_price"]:
                        updated_data["market_cap"] = data["shares_outstanding"] * data["current_price"]
                        operations.append("Calculated market_cap from shares and price")
        
        return {
            "data": updated_data,
            "operations": operations
        }
    
    def _handle_outliers(self, data_type: str, data: Dict) -> Dict:
        """处理异常值"""
        
        operations = []
        updated_data = {}
        
        if data_type == "price_data":
            # 检查价格异常值
            if "current_price" in data:
                price = data["current_price"]
                if isinstance(price, (int, float)):
                    # 使用历史价格范围检查异常值
                    if self._is_price_outlier(price, data):
                        # 使用前一交易日收盘价替代
                        if "previous_close" in data:
                            updated_data["current_price"] = data["previous_close"]
                            operations.append(f"Replaced outlier price {price} with previous_close")
        
        return {
            "data": updated_data,
            "operations": operations
        }
```

## 4. 数据转换器

### 数据标准化和转换
```python
class DataTransformer:
    """数据转换器 - 标准化和转换数据格式"""
    
    def __init__(self):
        self.transformation_rules = self._load_transformation_rules()
        self.unit_converter = UnitConverter()
        
    def transform_data(self, cleaned_data: Dict) -> Dict:
        """转换数据"""
        
        transformed_data = {}
        transformation_log = {}
        
        for data_type, data in cleaned_data["cleaned_data"].items():
            transformation_result = self._transform_data_type(data_type, data)
            transformed_data[data_type] = transformation_result["transformed_data"]
            transformation_log[data_type] = transformation_result["transformation_log"]
        
        return {
            "transformed_data": transformed_data,
            "transformation_log": transformation_log,
            "transformation_summary": self._generate_transformation_summary(transformation_log)
        }
    
    def _transform_data_type(self, data_type: str, data: Dict) -> Dict:
        """转换特定类型的数据"""
        
        transformed_data = {}
        transformations = []
        
        if data_type == "price_data":
            transformed_data = self._transform_price_data(data)
            transformations.append("Price data standardization")
            
        elif data_type == "fundamental_data":
            transformed_data = self._transform_fundamental_data(data)
            transformations.append("Fundamental data normalization")
            
        elif data_type == "news_data":
            transformed_data = self._transform_news_data(data)
            transformations.append("News data processing")
            
        elif data_type == "social_data":
            transformed_data = self._transform_social_data(data)
            transformations.append("Social data analysis")
        
        return {
            "transformed_data": transformed_data,
            "transformation_log": {
                "transformations": transformations,
                "data_schema": self._generate_data_schema(transformed_data)
            }
        }
    
    def _transform_price_data(self, data: Dict) -> Dict:
        """转换价格数据"""
        
        transformed = {
            "symbol": data.get("symbol"),
            "price": {
                "current": float(data.get("current_price", 0)),
                "open": float(data.get("open", 0)),
                "high": float(data.get("high", 0)),
                "low": float(data.get("low", 0)),
                "previous_close": float(data.get("previous_close", 0))
            },
            "change": {
                "absolute": float(data.get("change", 0)),
                "percentage": float(data.get("change_percent", 0))
            },
            "volume": int(data.get("volume", 0)),
            "timestamp": self._standardize_timestamp(data.get("timestamp"))
        }
        
        # 计算额外指标
        if transformed["price"]["current"] and transformed["price"]["previous_close"]:
            transformed["metrics"] = {
                "daily_return": (transformed["price"]["current"] - transformed["price"]["previous_close"]) / transformed["price"]["previous_close"],
                "volatility_indicator": abs(transformed["price"]["high"] - transformed["price"]["low"]) / transformed["price"]["current"] if transformed["price"]["current"] else 0
            }
        
        return transformed
    
    def _transform_fundamental_data(self, data: Dict) -> Dict:
        """转换基本面数据"""
        
        transformed = {
            "company_info": {
                "symbol": data.get("symbol"),
                "name": data.get("name"),
                "sector": data.get("sector"),
                "industry": data.get("industry"),
                "market_cap": self._normalize_market_cap(data.get("market_cap"))
            },
            "valuation_metrics": {
                "pe_ratio": float(data.get("pe_ratio", 0)) if data.get("pe_ratio") else None,
                "pb_ratio": float(data.get("pb_ratio", 0)) if data.get("pb_ratio") else None,
                "ps_ratio": float(data.get("ps_ratio", 0)) if data.get("ps_ratio") else None,
                "ev_ebitda": float(data.get("ev_ebitda", 0)) if data.get("ev_ebitda") else None
            },
            "financial_health": {
                "debt_to_equity": float(data.get("debt_to_equity", 0)) if data.get("debt_to_equity") else None,
                "current_ratio": float(data.get("current_ratio", 0)) if data.get("current_ratio") else None,
                "roe": float(data.get("roe", 0)) if data.get("roe") else None,
                "roa": float(data.get("roa", 0)) if data.get("roa") else None
            },
            "growth_metrics": {
                "revenue_growth": float(data.get("revenue_growth", 0)) if data.get("revenue_growth") else None,
                "earnings_growth": float(data.get("earnings_growth", 0)) if data.get("earnings_growth") else None,
                "book_value_growth": float(data.get("book_value_growth", 0)) if data.get("book_value_growth") else None
            }
        }
        
        return transformed
```

## 5. 特征工程器

### 特征提取和生成
```python
class FeatureEngineer:
    """特征工程器 - 生成分析特征"""
    
    def __init__(self):
        self.feature_generators = self._initialize_feature_generators()
        
    def engineer_features(self, transformed_data: Dict) -> Dict:
        """工程化特征"""
        
        features = {}
        
        # 价格特征
        if "price_data" in transformed_data:
            features["price_features"] = self._generate_price_features(transformed_data["price_data"])
        
        # 基本面特征
        if "fundamental_data" in transformed_data:
            features["fundamental_features"] = self._generate_fundamental_features(transformed_data["fundamental_data"])
        
        # 技术特征
        if "technical_data" in transformed_data:
            features["technical_features"] = self._generate_technical_features(transformed_data["technical_data"])
        
        # 情感特征
        sentiment_data = {}
        if "news_data" in transformed_data:
            sentiment_data["news"] = transformed_data["news_data"]
        if "social_data" in transformed_data:
            sentiment_data["social"] = transformed_data["social_data"]
        
        if sentiment_data:
            features["sentiment_features"] = self._generate_sentiment_features(sentiment_data)
        
        # 综合特征
        features["composite_features"] = self._generate_composite_features(features)
        
        return {
            "features": features,
            "feature_metadata": self._generate_feature_metadata(features)
        }
    
    def _generate_price_features(self, price_data: Dict) -> Dict:
        """生成价格特征"""
        
        price_info = price_data.get("price", {})
        
        features = {
            "price_momentum": self._calculate_price_momentum(price_info),
            "price_volatility": self._calculate_price_volatility(price_info),
            "price_trend": self._identify_price_trend(price_info),
            "support_resistance": self._identify_support_resistance(price_info),
            "volume_profile": self._analyze_volume_profile(price_data.get("volume", 0))
        }
        
        return features
    
    def _generate_fundamental_features(self, fundamental_data: Dict) -> Dict:
        """生成基本面特征"""
        
        valuation = fundamental_data.get("valuation_metrics", {})
        health = fundamental_data.get("financial_health", {})
        growth = fundamental_data.get("growth_metrics", {})
        
        features = {
            "valuation_score": self._calculate_valuation_score(valuation),
            "financial_strength": self._calculate_financial_strength(health),
            "growth_quality": self._assess_growth_quality(growth),
            "profitability_trend": self._analyze_profitability_trend(fundamental_data),
            "competitive_position": self._assess_competitive_position(fundamental_data)
        }
        
        return features
```

## 6. 数据分发器

### 智能数据路由
```python
class DataDispatcher:
    """数据分发器 - 将处理后的数据分发给智能体"""
    
    def __init__(self):
        self.routing_rules = self._load_routing_rules()
        self.agent_requirements = self._load_agent_requirements()
        
    def dispatch_data(self, engineered_data: Dict, target_agents: List[str]) -> Dict:
        """分发数据给目标智能体"""
        
        dispatched_data = {}
        
        for agent in target_agents:
            agent_data = self._prepare_agent_data(agent, engineered_data)
            dispatched_data[agent] = agent_data
        
        return {
            "agent_data": dispatched_data,
            "dispatch_metadata": {
                "target_agents": target_agents,
                "dispatch_timestamp": datetime.now().isoformat(),
                "data_completeness": self._assess_dispatch_completeness(dispatched_data)
            }
        }
    
    def _prepare_agent_data(self, agent: str, data: Dict) -> Dict:
        """为特定智能体准备数据"""
        
        agent_requirements = self.agent_requirements.get(agent, {})
        required_features = agent_requirements.get("required_features", [])
        
        agent_data = {}
        
        # 根据智能体需求筛选数据
        for feature_category in required_features:
            if feature_category in data["features"]:
                agent_data[feature_category] = data["features"][feature_category]
        
        # 添加智能体特定的数据格式化
        formatted_data = self._format_for_agent(agent, agent_data)
        
        return {
            "data": formatted_data,
            "metadata": {
                "agent": agent,
                "data_version": data.get("feature_metadata", {}).get("version"),
                "completeness_score": self._calculate_completeness_score(agent_data, required_features)
            }
        }
```

通过这个完整的数据处理流程，TradingAgents 确保智能体获得高质量、标准化、相关的数据，为准确的分析和决策提供坚实基础。


<!-- docs/data/data-sources.md -->

# 数据源集成 (v0.1.4)

## 概述

TradingAgents 中文增强版集成了多种金融数据源，特别加强了对中国A股市场的支持。为智能体提供全面、准确、实时的市场信息。本文档详细介绍了支持的数据源、API集成方法、数据格式和使用指南。

## 🎯 v0.1.4 数据源状态

| 数据源 | 市场 | 状态 | 说明 |
|--------|------|------|------|
| 🇨🇳 **通达信API** | A股 | ✅ 完整支持 | 实时行情、历史数据、技术指标 |
| **FinnHub** | 美股 | ✅ 完整支持 | 实时数据、基本面、新闻 |
| **Google News** | 全球 | ✅ 完整支持 | 财经新闻、市场资讯 |
| **Reddit** | 全球 | ✅ 完整支持 | 社交媒体情绪分析 |
| **MongoDB** | 缓存 | ✅ 完整支持 | 数据持久化存储 |
| **Redis** | 缓存 | ✅ 完整支持 | 高速数据缓存 |

## 支持的数据源

### 🇨🇳 1. 通达信API (新增 v0.1.3)

#### 简介
通达信API是中国领先的股票数据提供商，为A股市场提供实时行情和历史数据。

#### 数据类型
```python
tdx_data_types = {
    "实时数据": [
        "A股实时行情",
        "成交量",
        "涨跌幅",
        "换手率"
    ],
    "历史数据": [
        "日K线数据",
        "分钟级数据",
        "复权数据",
        "除权除息"
    ],
    "技术指标": [
        "MA移动平均",
        "MACD",
        "RSI",
        "KDJ"
    ],
    "市场数据": [
        "板块分类",
        "概念股",
        "龙虎榜",
        "资金流向"
    ]
}
```

#### 使用示例
```python
from tradingagents.dataflows.tdx_utils import get_stock_data

# 获取A股数据
data = get_stock_data(
    stock_code="000001",  # 平安银行
    start_date="2024-01-01",
    end_date="2024-12-31"
)
```

### 1. FinnHub API

#### 简介
FinnHub 是领先的金融数据提供商，提供实时股票价格、公司基本面数据、新闻和市场指标。

#### 数据类型
```python
finnhub_data_types = {
    "实时数据": [
        "股票价格",
        "交易量",
        "市场深度",
        "实时新闻"
    ],
    "基本面数据": [
        "财务报表",
        "公司概况",
        "分析师评级",
        "盈利预测"
    ],
    "技术指标": [
        "RSI",
        "MACD",
        "布林带",
        "移动平均线"
    ],
    "市场数据": [
        "IPO日历",
        "分红信息",
        "股票分割",
        "期权数据"
    ]
}
```

#### API 配置
```python
# finnhub_utils.py
import finnhub

class FinnHubDataProvider:
    """FinnHub 数据提供器"""
    
    def __init__(self, api_key: str):
        self.client = finnhub.Client(api_key=api_key)
        self.rate_limiter = RateLimiter(calls_per_minute=60)  # 免费版限制
    
    def get_stock_price(self, symbol: str) -> Dict:
        """获取股票价格"""
        with self.rate_limiter:
            quote = self.client.quote(symbol)
            return {
                "symbol": symbol,
                "current_price": quote.get("c"),
                "change": quote.get("d"),
                "change_percent": quote.get("dp"),
                "high": quote.get("h"),
                "low": quote.get("l"),
                "open": quote.get("o"),
                "previous_close": quote.get("pc"),
                "timestamp": quote.get("t")
            }
    
    def get_company_profile(self, symbol: str) -> Dict:
        """获取公司概况"""
        with self.rate_limiter:
            profile = self.client.company_profile2(symbol=symbol)
            return {
                "symbol": symbol,
                "name": profile.get("name"),
                "industry": profile.get("finnhubIndustry"),
                "sector": profile.get("gsubind"),
                "market_cap": profile.get("marketCapitalization"),
                "shares_outstanding": profile.get("shareOutstanding"),
                "website": profile.get("weburl"),
                "logo": profile.get("logo"),
                "exchange": profile.get("exchange")
            }
    
    def get_financial_statements(self, symbol: str, statement_type: str = "ic") -> Dict:
        """获取财务报表"""
        with self.rate_limiter:
            financials = self.client.financials(symbol, statement_type, "annual")
            return {
                "symbol": symbol,
                "statement_type": statement_type,
                "data": financials.get("financials", []),
                "currency": financials.get("currency"),
                "last_updated": financials.get("cik")
            }
```

#### 使用示例
```python
# 初始化 FinnHub 客户端
finnhub_provider = FinnHubDataProvider(api_key=os.getenv("FINNHUB_API_KEY"))

# 获取股票价格
price_data = finnhub_provider.get_stock_price("AAPL")
print(f"AAPL 当前价格: ${price_data['current_price']}")

# 获取公司信息
company_info = finnhub_provider.get_company_profile("AAPL")
print(f"公司名称: {company_info['name']}")
```

### 2. Yahoo Finance

#### 简介
Yahoo Finance 提供免费的历史股票数据、财务信息和市场指标，是获取历史数据的优秀选择。

#### 数据类型
```python
yahoo_finance_data_types = {
    "历史数据": [
        "股票价格历史",
        "交易量历史",
        "调整后价格",
        "股息历史"
    ],
    "财务数据": [
        "损益表",
        "资产负债表",
        "现金流量表",
        "关键指标"
    ],
    "市场数据": [
        "期权链",
        "分析师建议",
        "机构持股",
        "内部人交易"
    ]
}
```

#### API 集成
```python
# yfin_utils.py
import yfinance as yf
import pandas as pd

class YahooFinanceProvider:
    """Yahoo Finance 数据提供器"""
    
    def __init__(self):
        self.cache = {}
        self.cache_duration = 300  # 5分钟缓存
    
    def get_historical_data(self, symbol: str, period: str = "1y") -> pd.DataFrame:
        """获取历史数据"""
        cache_key = f"{symbol}_{period}"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]["data"]
        
        ticker = yf.Ticker(symbol)
        hist_data = ticker.history(period=period)
        
        # 缓存数据
        self.cache[cache_key] = {
            "data": hist_data,
            "timestamp": time.time()
        }
        
        return hist_data
    
    def get_financial_info(self, symbol: str) -> Dict:
        """获取财务信息"""
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        return {
            "symbol": symbol,
            "market_cap": info.get("marketCap"),
            "enterprise_value": info.get("enterpriseValue"),
            "pe_ratio": info.get("trailingPE"),
            "pb_ratio": info.get("priceToBook"),
            "debt_to_equity": info.get("debtToEquity"),
            "roe": info.get("returnOnEquity"),
            "revenue_growth": info.get("revenueGrowth"),
            "profit_margins": info.get("profitMargins"),
            "beta": info.get("beta")
        }
    
    def get_technical_indicators(self, symbol: str, period: str = "1y") -> Dict:
        """计算技术指标"""
        hist_data = self.get_historical_data(symbol, period)
        
        # 计算移动平均线
        hist_data["MA_20"] = hist_data["Close"].rolling(window=20).mean()
        hist_data["MA_50"] = hist_data["Close"].rolling(window=50).mean()
        
        # 计算 RSI
        hist_data["RSI"] = self._calculate_rsi(hist_data["Close"])
        
        # 计算 MACD
        macd_data = self._calculate_macd(hist_data["Close"])
        hist_data = pd.concat([hist_data, macd_data], axis=1)
        
        return {
            "symbol": symbol,
            "indicators": hist_data.tail(1).to_dict("records")[0],
            "trend_analysis": self._analyze_trend(hist_data),
            "support_resistance": self._find_support_resistance(hist_data)
        }
```

### 3. Reddit API

#### 简介
Reddit API 提供社交媒体讨论数据，用于分析投资者情绪和市场热点。

#### 数据类型
```python
reddit_data_types = {
    "讨论数据": [
        "热门帖子",
        "评论内容",
        "用户互动",
        "话题趋势"
    ],
    "情感数据": [
        "情感极性",
        "情感强度",
        "情感分布",
        "情感变化"
    ],
    "热度指标": [
        "提及频率",
        "讨论热度",
        "用户参与度",
        "传播速度"
    ]
}
```

#### API 集成
```python
# reddit_utils.py
import praw
from textblob import TextBlob

class RedditDataProvider:
    """Reddit 数据提供器"""
    
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def get_stock_discussions(self, symbol: str, subreddit: str = "stocks", limit: int = 100) -> List[Dict]:
        """获取股票讨论"""
        discussions = []
        
        # 搜索相关帖子
        for submission in self.reddit.subreddit(subreddit).search(symbol, limit=limit):
            # 分析情感
            sentiment = self.sentiment_analyzer.analyze(submission.title + " " + submission.selftext)
            
            discussions.append({
                "id": submission.id,
                "title": submission.title,
                "content": submission.selftext,
                "score": submission.score,
                "num_comments": submission.num_comments,
                "created_utc": submission.created_utc,
                "author": str(submission.author),
                "url": submission.url,
                "sentiment": sentiment
            })
        
        return discussions
    
    def analyze_sentiment_trends(self, discussions: List[Dict]) -> Dict:
        """分析情感趋势"""
        if not discussions:
            return {"error": "No discussions found"}
        
        # 计算整体情感
        sentiments = [d["sentiment"]["polarity"] for d in discussions]
        avg_sentiment = sum(sentiments) / len(sentiments)
        
        # 时间序列分析
        time_series = self._create_sentiment_time_series(discussions)
        
        # 热度分析
        engagement_metrics = self._calculate_engagement_metrics(discussions)
        
        return {
            "overall_sentiment": avg_sentiment,
            "sentiment_distribution": self._calculate_sentiment_distribution(sentiments),
            "time_series": time_series,
            "engagement_metrics": engagement_metrics,
            "trending_topics": self._extract_trending_topics(discussions)
        }
```

### 4. Google News

#### 简介
Google News API 提供实时新闻数据，用于分析市场事件和新闻对股价的影响。

#### 数据类型
```python
google_news_data_types = {
    "新闻内容": [
        "新闻标题",
        "新闻正文",
        "发布时间",
        "新闻来源"
    ],
    "影响分析": [
        "新闻情感",
        "影响程度",
        "相关性评分",
        "时效性分析"
    ],
    "事件追踪": [
        "事件时间线",
        "关联事件",
        "影响范围",
        "后续发展"
    ]
}
```

#### API 集成
```python
# googlenews_utils.py
from GoogleNews import GoogleNews
import requests
from bs4 import BeautifulSoup

class GoogleNewsProvider:
    """Google News 数据提供器"""
    
    def __init__(self):
        self.googlenews = GoogleNews()
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def get_stock_news(self, symbol: str, days: int = 7) -> List[Dict]:
        """获取股票相关新闻"""
        # 设置搜索参数
        self.googlenews.clear()
        self.googlenews.set_time_range(f"{days}d")
        self.googlenews.set_lang("en")
        
        # 搜索新闻
        search_terms = [symbol, f"{symbol} stock", f"{symbol} earnings"]
        all_news = []
        
        for term in search_terms:
            self.googlenews.search(term)
            news_results = self.googlenews.results()
            
            for news in news_results:
                # 获取新闻详情
                news_detail = self._get_news_detail(news)
                if news_detail:
                    all_news.append(news_detail)
        
        # 去重和排序
        unique_news = self._deduplicate_news(all_news)
        return sorted(unique_news, key=lambda x: x["published_date"], reverse=True)
    
    def _get_news_detail(self, news_item: Dict) -> Dict:
        """获取新闻详情"""
        try:
            # 分析新闻情感
            sentiment = self.sentiment_analyzer.analyze(news_item.get("title", ""))
            
            # 评估新闻重要性
            importance = self._assess_news_importance(news_item)
            
            return {
                "title": news_item.get("title"),
                "link": news_item.get("link"),
                "published_date": news_item.get("date"),
                "source": news_item.get("media"),
                "sentiment": sentiment,
                "importance": importance,
                "relevance_score": self._calculate_relevance_score(news_item)
            }
        except Exception as e:
            print(f"Error processing news item: {e}")
            return None
    
    def analyze_news_impact(self, news_list: List[Dict], symbol: str) -> Dict:
        """分析新闻影响"""
        if not news_list:
            return {"error": "No news found"}
        
        # 情感分析
        sentiment_analysis = self._analyze_news_sentiment(news_list)
        
        # 影响评估
        impact_assessment = self._assess_news_impact(news_list, symbol)
        
        # 时间线分析
        timeline_analysis = self._create_news_timeline(news_list)
        
        return {
            "sentiment_analysis": sentiment_analysis,
            "impact_assessment": impact_assessment,
            "timeline_analysis": timeline_analysis,
            "key_events": self._identify_key_events(news_list),
            "market_implications": self._analyze_market_implications(news_list, symbol)
        }
```

## 数据集成接口

### 统一数据接口
```python
# interface.py
class DataInterface:
    """统一数据接口"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.providers = self._initialize_providers()
        self.cache_manager = CacheManager()
        
    def _initialize_providers(self) -> Dict:
        """初始化数据提供器"""
        providers = {}
        
        # FinnHub
        if self.config.get("finnhub_api_key"):
            providers["finnhub"] = FinnHubDataProvider(self.config["finnhub_api_key"])
        
        # Yahoo Finance
        providers["yahoo"] = YahooFinanceProvider()
        
        # Reddit
        if self.config.get("reddit_credentials"):
            providers["reddit"] = RedditDataProvider(**self.config["reddit_credentials"])
        
        # Google News
        providers["google_news"] = GoogleNewsProvider()
        
        return providers
    
    def get_comprehensive_data(self, symbol: str, date: str = None) -> Dict:
        """获取综合数据"""
        data = {}
        
        # 并行获取数据
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(self._get_price_data, symbol): "price_data",
                executor.submit(self._get_fundamental_data, symbol): "fundamental_data",
                executor.submit(self._get_news_data, symbol): "news_data",
                executor.submit(self._get_social_data, symbol): "social_data"
            }
            
            for future in as_completed(futures):
                data_type = futures[future]
                try:
                    data[data_type] = future.result()
                except Exception as e:
                    print(f"Error fetching {data_type}: {e}")
                    data[data_type] = {}
        
        return data
    
    def _get_price_data(self, symbol: str) -> Dict:
        """获取价格数据"""
        # 优先使用 FinnHub，备用 Yahoo Finance
        if "finnhub" in self.providers:
            try:
                return self.providers["finnhub"].get_stock_price(symbol)
            except Exception:
                pass
        
        if "yahoo" in self.providers:
            hist_data = self.providers["yahoo"].get_historical_data(symbol, "5d")
            latest = hist_data.iloc[-1]
            return {
                "symbol": symbol,
                "current_price": latest["Close"],
                "change": latest["Close"] - latest["Open"],
                "high": latest["High"],
                "low": latest["Low"],
                "volume": latest["Volume"]
            }
        
        return {}
```

## 数据质量控制

### 数据验证
```python
class DataValidator:
    """数据验证器"""
    
    def validate_data(self, data: Dict, data_type: str) -> Tuple[bool, List[str]]:
        """验证数据质量"""
        errors = []
        
        # 基本完整性检查
        if not data:
            errors.append("Data is empty")
            return False, errors
        
        # 特定类型验证
        if data_type == "price_data":
            errors.extend(self._validate_price_data(data))
        elif data_type == "fundamental_data":
            errors.extend(self._validate_fundamental_data(data))
        elif data_type == "news_data":
            errors.extend(self._validate_news_data(data))
        elif data_type == "social_data":
            errors.extend(self._validate_social_data(data))
        
        return len(errors) == 0, errors
    
    def _validate_price_data(self, data: Dict) -> List[str]:
        """验证价格数据"""
        errors = []
        
        required_fields = ["symbol", "current_price"]
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        # 价格合理性检查
        if "current_price" in data:
            price = data["current_price"]
            if not isinstance(price, (int, float)) or price <= 0:
                errors.append("Invalid price value")
        
        return errors
```

## 使用最佳实践

### 1. API 限制管理
```python
class RateLimiter:
    """API 限制管理器"""
    
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.calls = []
    
    def __enter__(self):
        current_time = time.time()
        
        # 清理过期的调用记录
        self.calls = [call_time for call_time in self.calls if current_time - call_time < 60]
        
        # 检查是否超过限制
        if len(self.calls) >= self.calls_per_minute:
            sleep_time = 60 - (current_time - self.calls[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.calls.append(current_time)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

### 2. 错误处理和重试
```python
def with_retry(max_retries: int = 3, delay: float = 1.0):
    """重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay * (2 ** attempt))  # 指数退避
            return None
        return wrapper
    return decorator
```

### 3. 数据缓存策略
```python
class CacheManager:
    """缓存管理器"""
    
    def __init__(self):
        self.cache = {}
        self.cache_ttl = {
            "price_data": 60,      # 1分钟
            "fundamental_data": 3600,  # 1小时
            "news_data": 1800,     # 30分钟
            "social_data": 900     # 15分钟
        }
    
    def get(self, key: str, data_type: str) -> Optional[Dict]:
        """获取缓存数据"""
        if key in self.cache:
            cached_item = self.cache[key]
            ttl = self.cache_ttl.get(data_type, 3600)
            
            if time.time() - cached_item["timestamp"] < ttl:
                return cached_item["data"]
            else:
                del self.cache[key]
        
        return None
    
    def set(self, key: str, data: Dict, data_type: str):
        """设置缓存数据"""
        self.cache[key] = {
            "data": data,
            "timestamp": time.time(),
            "type": data_type
        }
```

通过这些数据源的集成，TradingAgents 能够获得全面、实时、高质量的市场数据，为智能体的分析和决策提供坚实的数据基础。


<!-- docs/data/tongdaxin-api-integration.md -->

# 通达信API集成指南

## 🎯 概述

通达信API为TradingAgents-CN提供了高质量的中国股票数据，包括A股、深股、创业板、科创板等所有板块的实时行情和历史数据。

## 🌟 优势对比

### 📊 数据覆盖对比

| 数据类型 | 通达信API | Yahoo Finance | 优势 |
|----------|-----------|---------------|------|
| **A股实时数据** | ✅ 完整覆盖 | ❌ 不支持 | 🟢 独有优势 |
| **港股数据** | ✅ 实时数据 | ⚠️ 部分支持 | 🟢 更全面 |
| **数据实时性** | ✅ 秒级更新 | ⚠️ 15分钟延迟 | 🟢 实时性强 |
| **技术指标** | ✅ 丰富指标 | ✅ 基础指标 | 🟡 相当 |
| **历史数据** | ✅ 完整历史 | ✅ 完整历史 | 🟡 相当 |
| **中文支持** | ✅ 原生支持 | ❌ 不支持 | 🟢 本土化 |

### 🇨🇳 本土化优势

- **数据源权威**: 直接对接交易所数据
- **更新及时**: 实时行情，无延迟
- **中文支持**: 股票名称、板块分类等
- **本土特色**: 涨跌停、ST股票等特殊标记
- **免费使用**: 无需API密钥，免费获取数据

## 🔧 安装和配置

### 1. 安装依赖

```bash
# 方法1: 使用安装脚本
python install_tdx.py

# 方法2: 手动安装
pip install pytdx
```

### 2. 验证安装

```bash
# 运行测试脚本
python test_tdx_integration.py
```

### 3. 无需额外配置

通达信API使用免费的公共服务器，无需申请API密钥或进行额外配置。

## 📊 支持的数据类型

### 1. 实时行情数据

```python
# 获取实时数据
realtime_data = {
    'code': '000001',
    'name': '平安银行',
    'price': 12.34,
    'change_percent': 2.15,
    'volume': 1234567,
    'amount': 15234567.89,
    'bid_prices': [12.33, 12.32, 12.31, 12.30, 12.29],
    'ask_prices': [12.34, 12.35, 12.36, 12.37, 12.38],
    'update_time': '2024-01-01 15:00:00'
}
```

### 2. 历史K线数据

```python
# 支持的周期
periods = {
    'D': '日线',
    'W': '周线', 
    'M': '月线'
}

# 数据格式 (兼容Yahoo Finance)
columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Amount']
```

### 3. 技术指标

```python
# 支持的技术指标
indicators = {
    'MA5': '5日移动平均',
    'MA10': '10日移动平均',
    'MA20': '20日移动平均',
    'RSI': '相对强弱指数',
    'MACD': 'MACD指标',
    'BB_Upper': '布林带上轨',
    'BB_Lower': '布林带下轨'
}
```

### 4. 市场概览

```python
# 主要指数
indices = {
    '上证指数': '000001',
    '深证成指': '399001', 
    '创业板指': '399006',
    '科创50': '000688'
}
```

## 🎯 使用方法

### 1. Web界面使用

1. **启动Web界面**:
   ```bash
   python -m streamlit run web/app.py
   ```

2. **选择A股市场**:
   - 在"选择市场"下拉框中选择"A股"

3. **输入股票代码**:
   ```
   000001  # 平安银行
   600519  # 贵州茅台
   000858  # 五粮液
   300750  # 宁德时代
   ```

4. **开始分析**:
   - 系统将自动使用通达信API获取实时数据

### 2. 编程接口使用

```python
from tradingagents.dataflows.tdx_utils import get_china_stock_data, get_china_market_overview

# 获取股票数据
stock_data = get_china_stock_data('000001', '2024-01-01', '2024-01-31')
print(stock_data)

# 获取市场概览
market_overview = get_china_market_overview()
print(market_overview)
```

### 3. 在分析师中使用

```python
# 新增的工具函数
toolkit.get_china_stock_data('000001', '2024-01-01', '2024-01-31')
toolkit.get_china_market_overview('2024-01-31')
```

## 📈 支持的股票代码格式

### A股代码规则

| 代码前缀 | 市场 | 示例 | 说明 |
|----------|------|------|------|
| **000xxx** | 深圳主板 | 000001 | 平安银行 |
| **002xxx** | 深圳中小板 | 002415 | 海康威视 |
| **003xxx** | 深圳主板 | 003816 | 中国广核 |
| **300xxx** | 创业板 | 300750 | 宁德时代 |
| **600xxx** | 上海主板 | 600519 | 贵州茅台 |
| **601xxx** | 上海主板 | 601318 | 中国平安 |
| **603xxx** | 上海主板 | 603259 | 药明康德 |
| **688xxx** | 科创板 | 688981 | 中芯国际 |

### 常用股票代码

```python
popular_stocks = {
    # 银行股
    '000001': '平安银行',
    '600036': '招商银行',
    '601398': '工商银行',
    
    # 白酒股
    '600519': '贵州茅台',
    '000858': '五粮液',
    '000568': '泸州老窖',
    
    # 科技股
    '000002': '万科A',
    '000651': '格力电器',
    '300750': '宁德时代',
    
    # 新能源
    '002594': '比亚迪',
    '300274': '阳光电源'
}
```

## 🔍 技术实现细节

### 1. 连接机制

```python
# 使用免费的通达信服务器
servers = [
    ('119.147.212.81', 7709),  # 主服务器
    ('119.147.212.81', 7721)   # 扩展服务器
]
```

### 2. 数据获取流程

```mermaid
graph TD
    A[用户输入股票代码] --> B[连接通达信服务器]
    B --> C[获取实时数据]
    B --> D[获取历史数据]
    B --> E[计算技术指标]
    C --> F[格式化数据]
    D --> F
    E --> F
    F --> G[返回分析报告]
```

### 3. 错误处理

```python
# 自动重连机制
if not connected:
    success = connect()
    if not success:
        return fallback_data

# 数据验证
if not data or len(data) == 0:
    return empty_result_with_message
```

## 🚨 注意事项

### 1. 网络要求

- **需要网络连接**: 通达信API需要连接到通达信服务器
- **服务器稳定性**: 依赖通达信免费服务器的可用性
- **连接超时**: 网络不稳定时可能出现连接超时

### 2. 数据限制

- **历史数据**: 单次最多获取800条K线数据
- **实时数据**: 交易时间内数据更新频率最高
- **技术指标**: 需要足够的历史数据进行计算

### 3. 使用建议

- **备用方案**: 建议同时配置Yahoo Finance作为备用数据源
- **数据验证**: 重要决策前建议交叉验证数据
- **交易时间**: 非交易时间获取的是最后交易日数据

## 🔧 故障排除

### 常见问题

#### 1. 连接失败

```bash
❌ 通达信API连接失败: [Errno 11001] getaddrinfo failed
```

**解决方案**:
- 检查网络连接
- 尝试重新运行程序
- 检查防火墙设置

#### 2. 数据获取失败

```bash
⚠️ 未获取到股票数据
```

**解决方案**:
- 确认股票代码格式正确
- 检查股票是否存在
- 尝试其他股票代码

#### 3. pytdx安装失败

```bash
❌ pytdx库安装失败
```

**解决方案**:
```bash
# 升级pip
python -m pip install --upgrade pip

# 重新安装
pip install pytdx --no-cache-dir

# 或使用国内镜像
pip install pytdx -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 🎯 最佳实践

### 1. 性能优化

```python
# 复用连接
provider = get_tdx_provider()  # 全局实例

# 批量获取数据
stocks = ['000001', '600519', '000858']
for stock in stocks:
    data = provider.get_real_time_data(stock)
```

### 2. 错误处理

```python
try:
    data = get_china_stock_data(stock_code, start_date, end_date)
    if "获取失败" in data:
        # 使用备用数据源
        fallback_data = get_yahoo_finance_data(stock_code)
except Exception as e:
    # 记录错误并提供用户友好的消息
    logger.error(f"数据获取失败: {e}")
    return "数据暂时不可用，请稍后重试"
```

### 3. 数据缓存

```python
# 实现简单的数据缓存
cache = {}
cache_key = f"{stock_code}_{date}"

if cache_key in cache:
    return cache[cache_key]
else:
    data = fetch_data(stock_code, date)
    cache[cache_key] = data
    return data
```

## 📊 性能基准

### 数据获取速度

| 操作 | 平均耗时 | 说明 |
|------|----------|------|
| **连接服务器** | 1-3秒 | 首次连接 |
| **实时数据** | 0.5-1秒 | 单只股票 |
| **历史数据** | 2-5秒 | 30天数据 |
| **技术指标** | 1-2秒 | 基础指标 |
| **市场概览** | 3-5秒 | 主要指数 |

### 数据准确性

- **实时数据**: 与交易所数据一致
- **历史数据**: 复权处理准确
- **技术指标**: 计算方法标准
- **中文名称**: 官方标准名称

## 🎉 总结

通达信API的集成为TradingAgents-CN带来了以下价值：

1. **🇨🇳 本土化优势**: 完整的A股数据覆盖
2. **⚡ 实时性**: 秒级数据更新
3. **💰 成本优势**: 免费使用，无API限制
4. **🔧 易用性**: 无需复杂配置
5. **📊 专业性**: 丰富的技术指标

现在您可以在TradingAgents-CN中无缝分析中国股票，享受专业级的本土化股票分析体验！


<!-- docs/database_setup.md -->

# TradingAgents 数据库配置指南

## 📋 概述

TradingAgents现在支持MongoDB和Redis数据库，提供数据持久化存储和高性能缓存功能。

## 🚀 快速启动

### 1. 启动Docker服务

```bash
# Windows
scripts\start_services_alt_ports.bat

# Linux/Mac
scripts/start_services_alt_ports.sh
```

### 2. 安装Python依赖

```bash
pip install pymongo redis
```

### 3. 初始化数据库

```bash
python scripts/init_database.py
```

### 4. 启动Web应用

```bash
cd web
python -m streamlit run app.py
```

## 🔧 服务配置

### Docker服务端口

由于本地环境端口冲突，使用了替代端口：

| 服务 | 默认端口 | 实际端口 | 访问地址 |
|------|----------|----------|----------|
| MongoDB | 27017 | **27018** | localhost:27018 |
| Redis | 6379 | **6380** | localhost:6380 |
| Redis Commander | 8081 | **8082** | http://localhost:8082 |

### 认证信息

- **用户名**: admin
- **密码**: tradingagents123
- **数据库**: tradingagents

## 📊 数据库结构

### MongoDB集合

1. **stock_data** - 股票历史数据
   - 索引: (symbol, market_type), created_at, updated_at
   
2. **analysis_results** - 分析结果
   - 索引: (symbol, analysis_type), created_at
   
3. **user_sessions** - 用户会话
   - 索引: session_id, created_at, last_activity
   
4. **configurations** - 系统配置
   - 索引: (config_type, config_name), updated_at

### Redis缓存结构

- **键前缀**: `tradingagents:`
- **TTL配置**:
  - 美股数据: 2小时
  - A股数据: 1小时
  - 新闻数据: 4-6小时
  - 基本面数据: 12-24小时

## 🛠️ 管理工具

### Redis Commander
- 访问地址: http://localhost:8082
- 功能: Redis数据可视化管理

### 缓存管理页面
- 访问地址: http://localhost:8501 -> 缓存管理
- 功能: 缓存统计、清理、测试

## 📝 配置文件

### 环境变量 (.env)

```bash
# MongoDB配置
MONGODB_HOST=localhost
MONGODB_PORT=27018
MONGODB_USERNAME=admin
MONGODB_PASSWORD=tradingagents123
MONGODB_DATABASE=tradingagents

# Redis配置
REDIS_HOST=localhost
REDIS_PORT=6380
REDIS_PASSWORD=tradingagents123
REDIS_DB=0
```

### 默认配置 (default_config.py)

数据库配置已集成到默认配置中，支持环境变量覆盖。

## 🔍 故障排除

### 常见问题

1. **端口冲突**
   ```bash
   # 检查端口占用
   netstat -an | findstr :27018
   netstat -an | findstr :6380
   ```

2. **连接失败**
   ```bash
   # 检查Docker容器状态
   docker ps --filter "name=tradingagents-"
   
   # 查看容器日志
   docker logs tradingagents-mongodb
   docker logs tradingagents-redis
   ```

3. **权限问题**
   ```bash
   # 重启容器
   docker restart tradingagents-mongodb tradingagents-redis
   ```

### 重置数据库

```bash
# 停止并删除容器
docker stop tradingagents-mongodb tradingagents-redis tradingagents-redis-commander
docker rm tradingagents-mongodb tradingagents-redis tradingagents-redis-commander

# 删除数据卷（可选，会丢失所有数据）
docker volume rm tradingagents_mongodb_data tradingagents_redis_data

# 重新启动
scripts\start_services_alt_ports.bat
python scripts/init_database.py
```

## 📈 性能优化

### 缓存策略

1. **分层缓存**: Redis + 文件缓存
2. **智能TTL**: 根据数据类型设置不同过期时间
3. **压缩存储**: 大数据自动压缩（可配置）
4. **批量操作**: 支持批量读写

### 监控指标

- 缓存命中率
- 数据库连接数
- 内存使用量
- 响应时间

## 🔐 安全配置

### 生产环境建议

1. **修改默认密码**
2. **启用SSL/TLS**
3. **配置防火墙规则**
4. **定期备份数据**
5. **监控异常访问**

## 📚 API使用示例

### Python代码示例

```python
from tradingagents.config.database_manager import get_database_manager

# 获取数据库管理器
db_manager = get_database_manager()

# 检查数据库可用性
if db_manager.is_mongodb_available():
    print("MongoDB可用")

if db_manager.is_redis_available():
    print("Redis可用")

# 获取数据库客户端
mongodb_client = db_manager.get_mongodb_client()
redis_client = db_manager.get_redis_client()

# 获取缓存统计
stats = db_manager.get_cache_stats()
```

## 🎯 下一步计划

1. **数据同步**: 实现多实例数据同步
2. **备份策略**: 自动备份和恢复
3. **性能监控**: 集成监控仪表板
4. **集群支持**: MongoDB和Redis集群配置
5. **数据分析**: 内置数据分析工具

---

**注意**: 本配置适用于开发和测试环境。生产环境请参考安全配置章节进行相应调整。


<!-- docs/development/branch-strategy.md -->

# 分支管理策略

## 🌿 分支架构设计

### 主要分支

```
main (生产分支)
├── develop (开发主分支)
├── feature/* (功能开发分支)
├── enhancement/* (中文增强分支)
├── hotfix/* (紧急修复分支)
├── release/* (发布准备分支)
└── upstream-sync/* (上游同步分支)
```

### 分支说明

#### 🏠 **main** - 生产主分支
- **用途**: 稳定的生产版本
- **保护**: 受保护，只能通过PR合并
- **来源**: develop、hotfix、upstream-sync
- **特点**: 始终保持可发布状态

#### 🚀 **develop** - 开发主分支
- **用途**: 集成所有功能开发
- **保护**: 受保护，通过PR合并
- **来源**: feature、enhancement分支
- **特点**: 最新的开发进度

#### ✨ **feature/** - 功能开发分支
- **命名**: `feature/功能名称`
- **用途**: 开发新功能
- **生命周期**: 短期（1-2周）
- **示例**: `feature/portfolio-optimization`

#### 🇨🇳 **enhancement/** - 中文增强分支
- **命名**: `enhancement/增强名称`
- **用途**: 中文本地化和增强功能
- **生命周期**: 中期（2-4周）
- **示例**: `enhancement/chinese-llm-integration`

#### 🚨 **hotfix/** - 紧急修复分支
- **命名**: `hotfix/修复描述`
- **用途**: 紧急Bug修复
- **生命周期**: 短期（1-3天）
- **示例**: `hotfix/api-timeout-fix`

#### 📦 **release/** - 发布准备分支
- **命名**: `release/版本号`
- **用途**: 发布前的最后准备
- **生命周期**: 短期（3-7天）
- **示例**: `release/v1.1.0-cn`

#### 🔄 **upstream-sync/** - 上游同步分支
- **命名**: `upstream-sync/日期`
- **用途**: 同步上游更新
- **生命周期**: 临时（1天）
- **示例**: `upstream-sync/20240115`

## 🔄 工作流程

### 功能开发流程

```mermaid
graph LR
    A[main] --> B[develop]
    B --> C[feature/new-feature]
    C --> D[开发和测试]
    D --> E[PR to develop]
    E --> F[代码审查]
    F --> G[合并到develop]
    G --> H[测试集成]
    H --> I[PR to main]
    I --> J[发布]
```

### 中文增强流程

```mermaid
graph LR
    A[develop] --> B[enhancement/chinese-feature]
    B --> C[本地化开发]
    C --> D[中文测试]
    D --> E[文档更新]
    E --> F[PR to develop]
    F --> G[审查和合并]
```

### 紧急修复流程

```mermaid
graph LR
    A[main] --> B[hotfix/urgent-fix]
    B --> C[快速修复]
    C --> D[测试验证]
    D --> E[PR to main]
    E --> F[立即发布]
    F --> G[合并到develop]
```

## 📋 分支操作指南

### 创建功能分支

```bash
# 从develop创建功能分支
git checkout develop
git pull origin develop
git checkout -b feature/portfolio-analysis

# 开发完成后推送
git push -u origin feature/portfolio-analysis
```

### 创建中文增强分支

```bash
# 从develop创建增强分支
git checkout develop
git pull origin develop
git checkout -b enhancement/tushare-integration

# 推送分支
git push -u origin enhancement/tushare-integration
```

### 创建紧急修复分支

```bash
# 从main创建修复分支
git checkout main
git pull origin main
git checkout -b hotfix/api-error-fix

# 推送分支
git push -u origin hotfix/api-error-fix
```

## 🔒 分支保护规则

### main分支保护
- ✅ 要求PR审查
- ✅ 要求状态检查通过
- ✅ 要求分支为最新
- ✅ 限制推送权限
- ✅ 限制强制推送

### develop分支保护
- ✅ 要求PR审查
- ✅ 要求CI通过
- ✅ 允许管理员绕过

### 功能分支
- ❌ 无特殊保护
- ✅ 自动删除已合并分支

## 🏷️ 命名规范

### 分支命名

```bash
# 功能开发
feature/功能名称-简短描述
feature/chinese-data-source
feature/risk-management-enhancement

# 中文增强
enhancement/增强类型-具体内容
enhancement/llm-baidu-integration
enhancement/chinese-financial-terms

# Bug修复
hotfix/问题描述
hotfix/memory-leak-fix
hotfix/config-loading-error

# 发布准备
release/版本号
release/v1.1.0-cn
release/v1.2.0-cn-beta
```

### 提交信息规范

```bash
# 功能开发
feat(agents): 添加量化分析师智能体
feat(data): 集成Tushare数据源

# 中文增强
enhance(llm): 集成文心一言API
enhance(docs): 完善中文文档体系

# Bug修复
fix(api): 修复API超时问题
fix(config): 解决配置文件加载错误

# 文档更新
docs(readme): 更新安装指南
docs(api): 添加API使用示例
```

## 🧪 测试策略

### 分支测试要求

#### feature分支
- ✅ 单元测试覆盖率 > 80%
- ✅ 功能测试通过
- ✅ 代码风格检查

#### enhancement分支
- ✅ 中文功能测试
- ✅ 兼容性测试
- ✅ 文档完整性检查

#### develop分支
- ✅ 完整测试套件
- ✅ 集成测试
- ✅ 性能测试

#### main分支
- ✅ 生产环境测试
- ✅ 端到端测试
- ✅ 安全扫描

## 📊 分支监控

### 分支健康度指标

```bash
# 检查分支状态
git branch -a --merged    # 已合并分支
git branch -a --no-merged # 未合并分支

# 检查分支差异
git log develop..main --oneline
git log feature/branch..develop --oneline

# 检查分支大小
git rev-list --count develop..feature/branch
```

### 定期清理

```bash
# 删除已合并的本地分支
git branch --merged develop | grep -v "develop\|main" | xargs -n 1 git branch -d

# 删除远程跟踪分支
git remote prune origin

# 清理过期分支
git for-each-ref --format='%(refname:short) %(committerdate)' refs/heads | awk '$2 <= "'$(date -d '30 days ago' '+%Y-%m-%d')'"' | cut -d' ' -f1
```

## 🚀 发布流程

### 版本发布步骤

1. **创建发布分支**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/v1.1.0-cn
   ```

2. **版本准备**
   ```bash
   # 更新版本号
   # 更新CHANGELOG.md
   # 最后测试
   ```

3. **合并到main**
   ```bash
   git checkout main
   git merge release/v1.1.0-cn
   git tag v1.1.0-cn
   git push origin main --tags
   ```

4. **回合并到develop**
   ```bash
   git checkout develop
   git merge main
   git push origin develop
   ```

## 🔧 自动化工具

### Git Hooks

```bash
# pre-commit hook
#!/bin/sh
# 运行代码风格检查
black --check .
flake8 .

# pre-push hook
#!/bin/sh
# 运行测试
python -m pytest tests/
```

### GitHub Actions

```yaml
# 分支保护检查
on:
  pull_request:
    branches: [main, develop]
    
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: python -m pytest
```

## 🚀 推荐的开发工作流

### 1. 日常功能开发流程

#### 标准功能开发
```bash
# 步骤1: 创建功能分支
python scripts/branch_manager.py create feature portfolio-optimization -d "投资组合优化功能"

# 步骤2: 开发功能
# 编写代码...
git add .
git commit -m "feat: 添加投资组合优化算法"

# 步骤3: 定期同步develop分支
git fetch origin
git merge origin/develop  # 或使用 git rebase origin/develop

# 步骤4: 推送到远程
git push origin feature/portfolio-optimization

# 步骤5: 创建Pull Request
# 在GitHub上创建PR: feature/portfolio-optimization -> develop
# 填写PR模板，包含功能描述、测试说明等

# 步骤6: 代码审查
# 等待团队成员审查，根据反馈修改代码

# 步骤7: 合并和清理
# PR合并后，删除本地和远程分支
python scripts/branch_manager.py delete feature/portfolio-optimization
```

#### 功能开发检查清单
- [ ] 功能需求明确，有详细的设计文档
- [ ] 创建了合适的分支名称和描述
- [ ] 编写了完整的单元测试
- [ ] 代码符合项目编码规范
- [ ] 更新了相关文档
- [ ] 通过了所有自动化测试
- [ ] 进行了代码审查
- [ ] 测试了与现有功能的兼容性

### 2. 中文增强开发流程

#### 本地化功能开发
```bash
# 步骤1: 创建增强分支
python scripts/branch_manager.py create enhancement tushare-integration -d "集成Tushare A股数据源"

# 步骤2: 开发中文功能
# 集成中文数据源
git add tradingagents/data/tushare_source.py
git commit -m "enhance(data): 添加Tushare数据源适配器"

# 添加中文配置
git add config/chinese_config.yaml
git commit -m "enhance(config): 添加中文市场配置"

# 步骤3: 更新中文文档
git add docs/data/tushare-integration.md
git commit -m "docs: 添加Tushare集成文档"

# 步骤4: 中文功能测试
python -m pytest tests/test_tushare_integration.py
git add tests/test_tushare_integration.py
git commit -m "test: 添加Tushare集成测试"

# 步骤5: 推送和合并
git push origin enhancement/tushare-integration
# 创建PR到develop分支
```

#### 中文增强检查清单
- [ ] 功能适配中国金融市场特点
- [ ] 添加了完整的中文文档
- [ ] 支持中文金融术语
- [ ] 兼容现有的国际化功能
- [ ] 测试了中文数据处理
- [ ] 更新了配置文件和示例

### 3. 紧急修复流程

#### 生产环境Bug修复
```bash
# 步骤1: 从main创建修复分支
python scripts/branch_manager.py create hotfix api-timeout-fix -d "修复API请求超时问题"

# 步骤2: 快速定位和修复
# 分析问题根因
# 实施最小化修复
git add tradingagents/api/client.py
git commit -m "fix: 增加API请求超时重试机制"

# 步骤3: 紧急测试
python -m pytest tests/test_api_client.py -v
# 手动测试关键路径

# 步骤4: 立即部署到main
git push origin hotfix/api-timeout-fix
# 创建PR到main，标记为紧急修复

# 步骤5: 同步到develop
git checkout develop
git merge main
git push origin develop
```

#### 紧急修复检查清单
- [ ] 问题影响评估和优先级确认
- [ ] 实施最小化修复方案
- [ ] 通过了关键路径测试
- [ ] 有回滚计划
- [ ] 同步到所有相关分支
- [ ] 通知相关团队成员

### 4. 版本发布流程

#### 正式版本发布
```bash
# 步骤1: 创建发布分支
python scripts/branch_manager.py create release v1.1.0-cn -d "v1.1.0中文增强版发布"

# 步骤2: 版本准备
# 更新版本号
echo "1.1.0-cn" > VERSION
git add VERSION
git commit -m "bump: 版本号更新到v1.1.0-cn"

# 更新变更日志
git add CHANGELOG.md
git commit -m "docs: 更新v1.1.0-cn变更日志"

# 最终测试
python -m pytest tests/ --cov=tradingagents
python examples/full_test.py

# 步骤3: 合并到main
git checkout main
git merge release/v1.1.0-cn
git tag v1.1.0-cn
git push origin main --tags

# 步骤4: 回合并到develop
git checkout develop
git merge main
git push origin develop

# 步骤5: 清理发布分支
python scripts/branch_manager.py delete release/v1.1.0-cn
```

#### 版本发布检查清单
- [ ] 所有计划功能已完成并合并
- [ ] 通过了完整的测试套件
- [ ] 更新了版本号和变更日志
- [ ] 创建了版本标签
- [ ] 准备了发布说明
- [ ] 通知了用户和社区

### 5. 上游同步集成流程

#### 与原项目保持同步
```bash
# 步骤1: 检查上游更新
python scripts/sync_upstream.py

# 步骤2: 如果有更新，会自动创建同步分支
# upstream-sync/20240115

# 步骤3: 解决可能的冲突
# 保护我们的中文文档和增强功能
# 采用上游的核心代码更新

# 步骤4: 测试同步结果
python -m pytest tests/
python examples/basic_example.py

# 步骤5: 合并到主分支
git checkout main
git merge upstream-sync/20240115
git push origin main

# 步骤6: 同步到develop
git checkout develop
git merge main
git push origin develop
```

## 📈 最佳实践

### 开发建议

1. **小而频繁的提交** - 每个提交解决一个具体问题
2. **描述性分支名** - 清楚表达分支用途
3. **及时同步** - 定期从develop拉取最新更改
4. **完整测试** - 合并前确保所有测试通过
5. **文档同步** - 功能开发同时更新文档

### 协作规范

1. **PR模板** - 使用标准的PR描述模板
2. **代码审查** - 至少一人审查后合并
3. **冲突解决** - 及时解决合并冲突
4. **分支清理** - 及时删除已合并分支
5. **版本标记** - 重要节点创建版本标签

### 质量保证

1. **自动化测试** - 每个PR都要通过CI测试
2. **代码覆盖率** - 保持80%以上的测试覆盖率
3. **性能测试** - 重要功能要进行性能测试
4. **安全扫描** - 定期进行安全漏洞扫描
5. **文档更新** - 功能变更同步更新文档

通过这套完整的分支管理策略和开发工作流，我们可以确保项目开发的有序进行，同时保持代码质量和发布稳定性。


<!-- docs/development/development-workflow.md -->

# 开发工作流指南

## 🎯 概述

本文档详细说明 TradingAgents 中文增强版的标准开发工作流程，确保团队协作的一致性和代码质量。

## 🔄 核心工作流程

### 工作流程图

```mermaid
graph TD
    A[需求分析] --> B[创建分支]
    B --> C[功能开发]
    C --> D[编写测试]
    D --> E[更新文档]
    E --> F[代码审查]
    F --> G{审查通过?}
    G -->|否| C
    G -->|是| H[合并到develop]
    H --> I[集成测试]
    I --> J{测试通过?}
    J -->|否| K[修复问题]
    K --> C
    J -->|是| L[发布准备]
    L --> M[合并到main]
    M --> N[版本发布]
```

## 🚀 详细工作流程

### 1. 功能开发工作流

#### 1.1 需求分析阶段
```bash
# 确认开发需求
# 1. 阅读需求文档或Issue描述
# 2. 确认技术方案和实现路径
# 3. 评估开发时间和资源需求
# 4. 与团队讨论技术细节
```

#### 1.2 分支创建阶段
```bash
# 确保本地develop分支是最新的
git checkout develop
git pull origin develop

# 创建功能分支
python scripts/branch_manager.py create feature risk-management-v2 -d "风险管理模块重构"

# 验证分支创建
git branch --show-current
# 应该显示: feature/risk-management-v2
```

#### 1.3 功能开发阶段
```bash
# 开发核心功能
# 1. 实现主要功能逻辑
git add tradingagents/risk/manager_v2.py
git commit -m "feat(risk): 实现新版风险管理器核心逻辑"

# 2. 添加配置支持
git add config/risk_management_v2.yaml
git commit -m "feat(config): 添加风险管理v2配置文件"

# 3. 集成到主框架
git add tradingagents/graph/trading_graph.py
git commit -m "feat(graph): 集成风险管理v2到交易图"

# 定期同步develop分支
git fetch origin
git rebase origin/develop  # 或使用 merge
```

#### 1.4 测试开发阶段
```bash
# 编写单元测试
git add tests/risk/test_manager_v2.py
git commit -m "test(risk): 添加风险管理v2单元测试"

# 编写集成测试
git add tests/integration/test_risk_integration.py
git commit -m "test(integration): 添加风险管理集成测试"

# 运行测试确保通过
python -m pytest tests/risk/ -v
python -m pytest tests/integration/test_risk_integration.py -v
```

#### 1.5 文档更新阶段
```bash
# 更新API文档
git add docs/api/risk-management.md
git commit -m "docs(api): 更新风险管理API文档"

# 添加使用示例
git add examples/risk_management_example.py
git commit -m "docs(examples): 添加风险管理使用示例"

# 更新配置文档
git add docs/configuration/risk-config.md
git commit -m "docs(config): 更新风险管理配置文档"
```

#### 1.6 代码审查阶段
```bash
# 推送分支到远程
git push origin feature/risk-management-v2

# 创建Pull Request
# 1. 访问GitHub仓库
# 2. 创建PR: feature/risk-management-v2 -> develop
# 3. 填写PR模板
# 4. 添加审查者
# 5. 等待审查反馈

# 根据审查意见修改代码
git add .
git commit -m "fix(risk): 根据审查意见修复代码风格问题"
git push origin feature/risk-management-v2
```

### 2. 中文增强开发工作流

#### 2.1 中文功能开发
```bash
# 创建中文增强分支
python scripts/branch_manager.py create enhancement akshare-integration -d "集成AkShare数据源"

# 开发中文数据源适配器
git add tradingagents/data/akshare_adapter.py
git commit -m "enhance(data): 添加AkShare数据源适配器"

# 添加中文金融术语支持
git add tradingagents/utils/chinese_terms.py
git commit -m "enhance(utils): 添加中文金融术语映射"

# 配置中文市场参数
git add config/chinese_markets/
git commit -m "enhance(config): 添加中国金融市场配置"
```

#### 2.2 中文文档开发
```bash
# 添加中文使用指南
git add docs/data/akshare-integration.md
git commit -m "docs: 添加AkShare集成中文指南"

# 更新中文示例
git add examples/chinese_market_analysis.py
git commit -m "examples: 添加中国市场分析示例"

# 更新中文FAQ
git add docs/faq/chinese-features-faq.md
git commit -m "docs: 添加中文功能常见问题"
```

### 3. 紧急修复工作流

#### 3.1 问题识别和评估
```bash
# 1. 确认问题严重程度
# 2. 评估影响范围
# 3. 制定修复方案
# 4. 确定修复时间线
```

#### 3.2 紧急修复开发
```bash
# 从main分支创建修复分支
git checkout main
git pull origin main
python scripts/branch_manager.py create hotfix memory-leak-fix -d "修复内存泄漏问题"

# 实施最小化修复
git add tradingagents/core/memory_manager.py
git commit -m "fix: 修复智能体内存泄漏问题"

# 紧急测试
python -m pytest tests/core/test_memory_manager.py -v
python tests/manual/memory_leak_test.py
```

#### 3.3 快速部署
```bash
# 推送修复
git push origin hotfix/memory-leak-fix

# 创建紧急PR到main
# 标记为紧急修复，跳过常规审查流程

# 合并后立即同步到develop
git checkout develop
git merge main
git push origin develop
```

### 4. 版本发布工作流

#### 4.1 发布准备
```bash
# 创建发布分支
python scripts/branch_manager.py create release v1.2.0-cn -d "v1.2.0中文增强版发布"

# 版本号更新
echo "1.2.0-cn" > VERSION
git add VERSION
git commit -m "bump: 版本更新到v1.2.0-cn"

# 更新变更日志
# 编辑CHANGELOG.md，添加新版本的变更内容
git add CHANGELOG.md
git commit -m "docs: 更新v1.2.0-cn变更日志"
```

#### 4.2 发布测试
```bash
# 完整测试套件
python -m pytest tests/ --cov=tradingagents --cov-report=html

# 性能测试
python tests/performance/benchmark_test.py

# 集成测试
python examples/full_integration_test.py

# 文档测试
# 验证所有文档链接和示例代码
```

#### 4.3 正式发布
```bash
# 合并到main
git checkout main
git merge release/v1.2.0-cn

# 创建版本标签
git tag -a v1.2.0-cn -m "TradingAgents中文增强版 v1.2.0"
git push origin main --tags

# 同步到develop
git checkout develop
git merge main
git push origin develop

# 清理发布分支
python scripts/branch_manager.py delete release/v1.2.0-cn
```

## 📋 工作流检查清单

### 功能开发检查清单
- [ ] **需求明确**: 功能需求和验收标准清晰
- [ ] **设计文档**: 有详细的技术设计文档
- [ ] **分支命名**: 使用规范的分支命名
- [ ] **代码质量**: 通过代码风格检查
- [ ] **单元测试**: 测试覆盖率达到80%以上
- [ ] **集成测试**: 通过集成测试
- [ ] **文档更新**: 更新相关API和使用文档
- [ ] **示例代码**: 提供使用示例
- [ ] **代码审查**: 至少一人审查通过
- [ ] **向后兼容**: 确保向后兼容性

### 中文增强检查清单
- [ ] **市场适配**: 适配中国金融市场特点
- [ ] **术语支持**: 支持中文金融术语
- [ ] **数据源**: 集成中文数据源
- [ ] **配置文件**: 添加中文市场配置
- [ ] **中文文档**: 完整的中文使用文档
- [ ] **示例代码**: 中文市场分析示例
- [ ] **测试用例**: 中文功能测试用例
- [ ] **兼容性**: 与国际化功能兼容

### 发布检查清单
- [ ] **功能完整**: 所有计划功能已实现
- [ ] **测试通过**: 完整测试套件通过
- [ ] **性能验证**: 性能测试达标
- [ ] **文档完整**: 所有文档已更新
- [ ] **版本标记**: 正确的版本号和标签
- [ ] **变更日志**: 详细的变更记录
- [ ] **发布说明**: 准备发布公告
- [ ] **回滚计划**: 有应急回滚方案

## 🔧 工具和自动化

### 开发工具
```bash
# 分支管理
python scripts/branch_manager.py

# 上游同步
python scripts/sync_upstream.py

# 代码质量检查
black tradingagents/
flake8 tradingagents/
mypy tradingagents/

# 测试运行
python -m pytest tests/ -v --cov=tradingagents
```

### CI/CD集成
- **GitHub Actions**: 自动化测试和部署
- **代码质量**: 自动代码风格和质量检查
- **测试覆盖**: 自动生成测试覆盖率报告
- **文档构建**: 自动构建和部署文档

## 📞 获取帮助

### 文档资源
- [分支管理策略](branch-strategy.md)
- [分支快速指南](../../BRANCH_GUIDE.md)
- [上游同步指南](../maintenance/upstream-sync.md)

### 联系方式
- **GitHub Issues**: [提交问题](https://github.com/hsliuping/TradingAgents-CN/issues)
- **邮箱**: hsliup@163.com

通过遵循这套标准化的开发工作流程，我们可以确保项目的高质量开发和稳定发布。


<!-- docs/development/project-structure.md -->

# 项目结构规范

## 📁 目录组织原则

TradingAgents-CN 项目遵循清晰的目录结构规范，确保代码组织有序、易于维护。

## 🏗️ 项目根目录结构

```
TradingAgentsCN/
├── 📁 tradingagents/          # 核心代码包
├── 📁 web/                    # Web界面代码
├── 📁 docs/                   # 项目文档
├── 📁 tests/                  # 所有测试文件
├── 📁 scripts/                # 工具脚本
├── 📁 env/                    # Python虚拟环境
├── 📄 README.md               # 项目说明
├── 📄 requirements.txt        # 依赖列表
├── 📄 .env.example           # 环境变量模板
├── 📄 VERSION                 # 版本号
└── 📄 CHANGELOG.md           # 更新日志
```

## 📋 目录职责说明

### 🧪 tests/ - 测试目录
**规则**: 所有测试相关的文件必须放在此目录下

#### 允许的文件类型：
- ✅ `test_*.py` - 单元测试文件
- ✅ `*_test.py` - 快速测试脚本
- ✅ `test_*_integration.py` - 集成测试
- ✅ `test_*_performance.py` - 性能测试
- ✅ `check_*.py` - 检查脚本
- ✅ `debug_*.py` - 调试脚本

#### 子目录组织：
```
tests/
├── 📄 README.md                    # 测试说明文档
├── 📄 __init__.py                  # Python包初始化
├── 📁 integration/                 # 集成测试
├── 📄 test_*.py                   # 单元测试
├── 📄 *_test.py                   # 快速测试
└── 📄 test_*_performance.py       # 性能测试
```

#### 示例文件：
- `test_analysis.py` - 分析功能单元测试
- `fast_tdx_test.py` - 通达信API快速测试
- `test_tdx_integration.py` - 通达信API集成测试
- `test_redis_performance.py` - Redis性能测试

### 🔧 scripts/ - 工具脚本目录
**规则**: 仅放置非测试的工具脚本

#### 允许的文件类型：
- ✅ `release_*.py` - 发布脚本
- ✅ `setup_*.py` - 安装配置脚本
- ✅ `deploy_*.py` - 部署脚本
- ✅ `migrate_*.py` - 数据迁移脚本
- ✅ `backup_*.py` - 备份脚本

#### 不允许的文件：
- ❌ `test_*.py` - 测试文件应放在tests/
- ❌ `*_test.py` - 测试脚本应放在tests/
- ❌ `check_*.py` - 检查脚本应放在tests/

### 📚 docs/ - 文档目录
**规则**: 所有项目文档按类型组织

#### 目录结构：
```
docs/
├── 📁 guides/                     # 使用指南
├── 📁 development/                # 开发文档
├── 📁 data/                       # 数据源文档
├── 📁 api/                        # API文档
└── 📁 localization/               # 本土化文档
```

### 🌐 web/ - Web界面目录
**规则**: Web相关代码统一管理

#### 目录结构：
```
web/
├── 📄 app.py                      # 主应用入口
├── 📁 components/                 # UI组件
├── 📁 utils/                      # Web工具函数
├── 📁 static/                     # 静态资源
└── 📁 templates/                  # 模板文件
```

### 🧠 tradingagents/ - 核心代码包
**规则**: 核心业务逻辑代码

#### 目录结构：
```
tradingagents/
├── 📁 agents/                     # 智能体代码
├── 📁 dataflows/                  # 数据流处理
├── 📁 tools/                      # 工具函数
└── 📁 utils/                      # 通用工具
```

## 🚫 禁止的文件位置

### 根目录禁止项：
- ❌ `test_*.py` - 必须放在tests/
- ❌ `*_test.py` - 必须放在tests/
- ❌ `debug_*.py` - 必须放在tests/
- ❌ `check_*.py` - 必须放在tests/
- ❌ 临时文件和调试文件
- ❌ IDE配置文件（应在.gitignore中）

### scripts/目录禁止项：
- ❌ 任何测试相关文件
- ❌ 调试脚本
- ❌ 检查脚本

## ✅ 文件命名规范

### 测试文件命名：
- **单元测试**: `test_<module_name>.py`
- **集成测试**: `test_<feature>_integration.py`
- **性能测试**: `test_<component>_performance.py`
- **快速测试**: `<component>_test.py`
- **检查脚本**: `check_<feature>.py`
- **调试脚本**: `debug_<issue>.py`

### 工具脚本命名：
- **发布脚本**: `release_v<version>.py`
- **安装脚本**: `setup_<component>.py`
- **部署脚本**: `deploy_<environment>.py`

### 文档文件命名：
- **使用指南**: `<feature>-guide.md`
- **技术文档**: `<component>-integration.md`
- **API文档**: `<api>-api.md`

## 🔍 项目结构检查

### 自动检查脚本
创建 `tests/check_project_structure.py` 来验证项目结构：

```python
def check_no_tests_in_root():
    """检查根目录没有测试文件"""
    
def check_no_tests_in_scripts():
    """检查scripts目录没有测试文件"""
    
def check_all_tests_in_tests_dir():
    """检查所有测试文件都在tests目录"""
```

### 手动检查清单
发布前检查：
- [ ] 根目录没有test_*.py文件
- [ ] 根目录没有*_test.py文件
- [ ] scripts/目录没有测试文件
- [ ] 所有测试文件都在tests/目录
- [ ] tests/README.md已更新
- [ ] 文档中的路径引用正确

## 📝 最佳实践

### 1. 新增测试文件
```bash
# ✅ 正确：在tests目录创建
touch tests/test_new_feature.py

# ❌ 错误：在根目录创建
touch test_new_feature.py
```

### 2. 运行测试
```bash
# ✅ 正确：指定tests目录
python tests/fast_tdx_test.py
python -m pytest tests/

# ❌ 错误：从根目录运行
python fast_tdx_test.py
```

### 3. 文档引用
```markdown
<!-- ✅ 正确：使用完整路径 -->
运行测试：`python tests/fast_tdx_test.py`

<!-- ❌ 错误：使用相对路径 -->
运行测试：`python fast_tdx_test.py`
```

## 🔧 迁移现有文件

如果发现文件位置不符合规范：

### 移动测试文件到tests目录：
```bash
# Windows
move test_*.py tests\
move *_test.py tests\

# Linux/macOS
mv test_*.py tests/
mv *_test.py tests/
```

### 更新引用：
1. 更新文档中的路径引用
2. 更新脚本中的import路径
3. 更新CI/CD配置中的测试路径

## 🎯 遵循规范的好处

1. **清晰的项目结构** - 新开发者容易理解
2. **便于维护** - 文件位置可预测
3. **自动化友好** - CI/CD脚本更简单
4. **避免混乱** - 测试和业务代码分离
5. **专业形象** - 符合开源项目标准

---

**请严格遵循此项目结构规范，确保代码库的整洁和专业性！** 📁✨


<!-- docs/examples/advanced-examples.md -->

# 高级使用示例

## 概述

本文档提供了 TradingAgents 框架的高级使用示例，包括自定义智能体开发、复杂策略实现、性能优化和生产环境部署等高级功能。

## 示例 1: 自定义分析师智能体

### 创建量化分析师
```python
from tradingagents.agents.analysts.base_analyst import BaseAnalyst
import numpy as np
import pandas as pd

class QuantitativeAnalyst(BaseAnalyst):
    """量化分析师 - 基于数学模型的分析"""

    def __init__(self, llm, config):
        super().__init__(llm, config)
        self.models = self._initialize_quant_models()

    def _initialize_quant_models(self):
        """初始化量化模型"""
        return {
            "mean_reversion": MeanReversionModel(),
            "momentum": MomentumModel(),
            "volatility": VolatilityModel(),
            "correlation": CorrelationModel()
        }

    def perform_analysis(self, data: Dict) -> Dict:
        """执行量化分析"""

        price_data = data.get("price_data", {})
        historical_data = data.get("historical_data", pd.DataFrame())

        if historical_data.empty:
            return {"error": "No historical data available"}

        # 1. 统计套利分析
        stat_arb_signals = self._statistical_arbitrage_analysis(historical_data)

        # 2. 动量因子分析
        momentum_signals = self._momentum_factor_analysis(historical_data)

        # 3. 均值回归分析
        mean_reversion_signals = self._mean_reversion_analysis(historical_data)

        # 4. 波动率分析
        volatility_analysis = self._volatility_analysis(historical_data)

        # 5. 风险调整收益分析
        risk_adjusted_metrics = self._risk_adjusted_analysis(historical_data)

        # 6. 综合量化评分
        quant_score = self._calculate_quant_score({
            "stat_arb": stat_arb_signals,
            "momentum": momentum_signals,
            "mean_reversion": mean_reversion_signals,
            "volatility": volatility_analysis,
            "risk_adjusted": risk_adjusted_metrics
        })

        return {
            "statistical_arbitrage": stat_arb_signals,
            "momentum_analysis": momentum_signals,
            "mean_reversion": mean_reversion_signals,
            "volatility_analysis": volatility_analysis,
            "risk_metrics": risk_adjusted_metrics,
            "quantitative_score": quant_score,
            "model_confidence": self._calculate_model_confidence(quant_score),
            "trading_signals": self._generate_trading_signals(quant_score)
        }

    def _statistical_arbitrage_analysis(self, data: pd.DataFrame) -> Dict:
        """统计套利分析"""

        returns = data['Close'].pct_change().dropna()

        # Z-Score 计算
        rolling_mean = returns.rolling(window=20).mean()
        rolling_std = returns.rolling(window=20).std()
        z_score = (returns - rolling_mean) / rolling_std

        # 协整性检验
        adf_statistic, adf_pvalue = self._adf_test(data['Close'])

        # 半衰期计算
        half_life = self._calculate_half_life(returns)

        return {
            "current_z_score": z_score.iloc[-1] if not z_score.empty else 0,
            "z_score_percentile": self._calculate_percentile(z_score.iloc[-1], z_score),
            "adf_statistic": adf_statistic,
            "adf_pvalue": adf_pvalue,
            "is_stationary": adf_pvalue < 0.05,
            "half_life_days": half_life,
            "signal_strength": abs(z_score.iloc[-1]) if not z_score.empty else 0
        }

    def _momentum_factor_analysis(self, data: pd.DataFrame) -> Dict:
        """动量因子分析"""

        # 多时间框架动量
        momentum_1m = self._calculate_momentum(data, 21)    # 1个月
        momentum_3m = self._calculate_momentum(data, 63)    # 3个月
        momentum_6m = self._calculate_momentum(data, 126)   # 6个月
        momentum_12m = self._calculate_momentum(data, 252)  # 12个月

        # 动量强度
        momentum_strength = self._calculate_momentum_strength(data)

        # 动量持续性
        momentum_persistence = self._calculate_momentum_persistence(data)

        return {
            "momentum_1m": momentum_1m,
            "momentum_3m": momentum_3m,
            "momentum_6m": momentum_6m,
            "momentum_12m": momentum_12m,
            "momentum_strength": momentum_strength,
            "momentum_persistence": momentum_persistence,
            "momentum_score": (momentum_1m + momentum_3m + momentum_6m) / 3,
            "momentum_trend": "bullish" if momentum_3m > 0.05 else "bearish" if momentum_3m < -0.05 else "neutral"
        }
```

## 示例 2: 多资产组合分析

### 投资组合优化器
```python
class PortfolioOptimizer:
    """投资组合优化器 - 多资产配置优化"""

    def __init__(self, config: Dict):
        self.config = config
        self.risk_models = self._initialize_risk_models()
        self.optimization_methods = self._initialize_optimization_methods()

    def optimize_portfolio(self, symbols: List[str], target_date: str,
                          constraints: Dict = None) -> Dict:
        """优化投资组合配置"""

        # 1. 收集所有资产数据
        assets_data = self._collect_multi_asset_data(symbols, target_date)

        # 2. 计算预期收益
        expected_returns = self._calculate_expected_returns(assets_data)

        # 3. 构建协方差矩阵
        covariance_matrix = self._build_covariance_matrix(assets_data)

        # 4. 风险模型分析
        risk_analysis = self._analyze_portfolio_risk(assets_data, covariance_matrix)

        # 5. 多目标优化
        optimization_results = self._multi_objective_optimization(
            expected_returns, covariance_matrix, constraints
        )

        # 6. 情景分析
        scenario_analysis = self._perform_scenario_analysis(
            optimization_results, assets_data
        )

        return {
            "assets_analysis": assets_data,
            "expected_returns": expected_returns,
            "risk_analysis": risk_analysis,
            "optimal_weights": optimization_results["weights"],
            "portfolio_metrics": optimization_results["metrics"],
            "scenario_analysis": scenario_analysis,
            "rebalancing_schedule": self._generate_rebalancing_schedule(optimization_results)
        }

    def _collect_multi_asset_data(self, symbols: List[str], target_date: str) -> Dict:
        """收集多资产数据"""

        assets_data = {}

        # 并行分析所有资产
        with ThreadPoolExecutor(max_workers=len(symbols)) as executor:
            future_to_symbol = {
                executor.submit(self._analyze_single_asset, symbol, target_date): symbol
                for symbol in symbols
            }

            for future in as_completed(future_to_symbol):
                symbol = future_to_symbol[future]
                try:
                    asset_analysis = future.result()
                    assets_data[symbol] = asset_analysis
                except Exception as e:
                    print(f"Error analyzing {symbol}: {e}")
                    assets_data[symbol] = {"error": str(e)}

        return assets_data

    def _analyze_single_asset(self, symbol: str, target_date: str) -> Dict:
        """分析单个资产"""

        # 使用 TradingAgents 分析单个资产
        ta = TradingAgentsGraph(debug=False, config=self.config)
        state, decision = ta.propagate(symbol, target_date)

        # 提取关键指标
        return {
            "symbol": symbol,
            "decision": decision,
            "fundamental_score": state.analyst_reports.get("fundamentals", {}).get("overall_score", 0.5),
            "technical_score": state.analyst_reports.get("technical", {}).get("technical_score", 0.5),
            "sentiment_score": (
                state.analyst_reports.get("news", {}).get("news_score", 0.5) +
                state.analyst_reports.get("social", {}).get("social_score", 0.5)
            ) / 2,
            "risk_score": decision.get("risk_score", 0.5),
            "confidence": decision.get("confidence", 0.5)
        }

    def _multi_objective_optimization(self, expected_returns: np.ndarray,
                                    cov_matrix: np.ndarray, constraints: Dict) -> Dict:
        """多目标优化"""

        from scipy.optimize import minimize

        n_assets = len(expected_returns)

        # 目标函数：最大化夏普比率
        def objective(weights):
            portfolio_return = np.sum(weights * expected_returns)
            portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            sharpe_ratio = portfolio_return / portfolio_risk if portfolio_risk > 0 else 0
            return -sharpe_ratio  # 最小化负夏普比率

        # 约束条件
        constraints_list = [
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # 权重和为1
        ]

        # 添加自定义约束
        if constraints:
            if 'max_weight' in constraints:
                for i in range(n_assets):
                    constraints_list.append({
                        'type': 'ineq',
                        'fun': lambda x, i=i: constraints['max_weight'] - x[i]
                    })

            if 'min_weight' in constraints:
                for i in range(n_assets):
                    constraints_list.append({
                        'type': 'ineq',
                        'fun': lambda x, i=i: x[i] - constraints['min_weight']
                    })

        # 边界条件
        bounds = tuple((0, 1) for _ in range(n_assets))

        # 初始猜测
        x0 = np.array([1/n_assets] * n_assets)

        # 优化
        result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints_list)

        if result.success:
            optimal_weights = result.x
            portfolio_return = np.sum(optimal_weights * expected_returns)
            portfolio_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(cov_matrix, optimal_weights)))
            sharpe_ratio = portfolio_return / portfolio_risk if portfolio_risk > 0 else 0

            return {
                "weights": optimal_weights,
                "metrics": {
                    "expected_return": portfolio_return,
                    "expected_risk": portfolio_risk,
                    "sharpe_ratio": sharpe_ratio,
                    "optimization_success": True
                }
            }
        else:
            # 如果优化失败，使用等权重
            equal_weights = np.array([1/n_assets] * n_assets)
            return {
                "weights": equal_weights,
                "metrics": {
                    "expected_return": np.sum(equal_weights * expected_returns),
                    "expected_risk": np.sqrt(np.dot(equal_weights.T, np.dot(cov_matrix, equal_weights))),
                    "sharpe_ratio": 0,
                    "optimization_success": False,
                    "error": result.message
                }
            }
```

## 示例 3: 实时交易系统

### 实时监控和执行系统
```python
class RealTimeTradingSystem:
    """实时交易系统"""

    def __init__(self, config: Dict):
        self.config = config
        self.trading_agents = {}
        self.position_manager = PositionManager()
        self.risk_monitor = RealTimeRiskMonitor()
        self.execution_engine = ExecutionEngine()
        self.market_data_feed = MarketDataFeed()

    async def start_real_time_trading(self, watchlist: List[str]):
        """启动实时交易"""

        print(f"启动实时交易系统，监控 {len(watchlist)} 只股票...")

        # 初始化每只股票的交易智能体
        for symbol in watchlist:
            self.trading_agents[symbol] = TradingAgentsGraph(
                debug=False,
                config=self.config
            )

        # 启动市场数据订阅
        await self.market_data_feed.subscribe(watchlist)

        # 启动主交易循环
        await self._main_trading_loop(watchlist)

    async def _main_trading_loop(self, watchlist: List[str]):
        """主交易循环"""

        while True:
            try:
                # 获取最新市场数据
                market_updates = await self.market_data_feed.get_updates()

                # 并行处理所有股票
                tasks = []
                for symbol in watchlist:
                    if symbol in market_updates:
                        task = self._process_symbol_update(symbol, market_updates[symbol])
                        tasks.append(task)

                if tasks:
                    await asyncio.gather(*tasks, return_exceptions=True)

                # 风险检查
                await self._perform_risk_checks()

                # 短暂休眠
                await asyncio.sleep(1)

            except Exception as e:
                print(f"交易循环错误: {e}")
                await asyncio.sleep(5)

    async def _process_symbol_update(self, symbol: str, market_data: Dict):
        """处理单个股票的市场更新"""

        try:
            # 检查是否需要重新分析
            if self._should_reanalyze(symbol, market_data):

                # 执行快速分析
                analysis_result = await self._quick_analysis(symbol, market_data)

                # 检查交易信号
                trading_signals = self._extract_trading_signals(analysis_result)

                # 执行交易决策
                if trading_signals["action"] != "hold":
                    await self._execute_trading_decision(symbol, trading_signals)

                # 更新仓位监控
                await self._update_position_monitoring(symbol, analysis_result)

        except Exception as e:
            print(f"处理 {symbol} 更新时出错: {e}")

    def _should_reanalyze(self, symbol: str, market_data: Dict) -> bool:
        """判断是否需要重新分析"""

        # 价格变动阈值
        price_change_threshold = 0.02  # 2%

        current_price = market_data.get("price", 0)
        last_analysis_price = self.trading_agents[symbol].last_analysis_price if hasattr(self.trading_agents[symbol], 'last_analysis_price') else 0

        if last_analysis_price == 0:
            return True

        price_change = abs(current_price - last_analysis_price) / last_analysis_price

        # 如果价格变动超过阈值，或者距离上次分析超过一定时间
        time_threshold = 300  # 5分钟
        last_analysis_time = getattr(self.trading_agents[symbol], 'last_analysis_time', 0)
        time_since_last = time.time() - last_analysis_time

        return price_change > price_change_threshold or time_since_last > time_threshold

    async def _quick_analysis(self, symbol: str, market_data: Dict) -> Dict:
        """快速分析"""

        # 使用简化配置进行快速分析
        quick_config = self.config.copy()
        quick_config.update({
            "max_debate_rounds": 1,
            "max_risk_discuss_rounds": 1,
            "quick_think_llm": "gpt-4o-mini"  # 使用快速模型
        })

        # 创建快速分析智能体
        quick_agent = TradingAgentsGraph(
            selected_analysts=["market", "news"],  # 只使用关键分析师
            debug=False,
            config=quick_config
        )

        # 执行分析
        current_date = datetime.now().strftime("%Y-%m-%d")
        state, decision = quick_agent.propagate(symbol, current_date)

        # 记录分析时间和价格
        self.trading_agents[symbol].last_analysis_time = time.time()
        self.trading_agents[symbol].last_analysis_price = market_data.get("price", 0)

        return {
            "state": state,
            "decision": decision,
            "market_data": market_data,
            "analysis_timestamp": time.time()
        }
```

## 示例 4: 策略回测框架

### 高级回测系统
```python
class AdvancedBacktester:
    """高级回测系统"""

    def __init__(self, config: Dict):
        self.config = config
        self.performance_analyzer = PerformanceAnalyzer()
        self.risk_analyzer = RiskAnalyzer()
        self.transaction_cost_model = TransactionCostModel()

    def run_comprehensive_backtest(self, strategy_config: Dict,
                                 start_date: str, end_date: str,
                                 universe: List[str]) -> Dict:
        """运行综合回测"""

        print(f"开始回测: {start_date} 到 {end_date}, 股票池: {len(universe)} 只")

        # 1. 数据准备
        historical_data = self._prepare_historical_data(universe, start_date, end_date)

        # 2. 策略执行
        trading_history = self._execute_strategy(strategy_config, historical_data)

        # 3. 性能分析
        performance_metrics = self._analyze_performance(trading_history)

        # 4. 风险分析
        risk_metrics = self._analyze_risk(trading_history)

        # 5. 归因分析
        attribution_analysis = self._perform_attribution_analysis(trading_history)

        # 6. 敏感性分析
        sensitivity_analysis = self._perform_sensitivity_analysis(strategy_config, historical_data)

        return {
            "strategy_config": strategy_config,
            "backtest_period": {"start": start_date, "end": end_date},
            "universe": universe,
            "trading_history": trading_history,
            "performance_metrics": performance_metrics,
            "risk_metrics": risk_metrics,
            "attribution_analysis": attribution_analysis,
            "sensitivity_analysis": sensitivity_analysis,
            "summary": self._generate_backtest_summary(performance_metrics, risk_metrics)
        }

    def _execute_strategy(self, strategy_config: Dict, historical_data: Dict) -> List[Dict]:
        """执行策略"""

        trading_history = []
        portfolio = Portfolio(initial_capital=strategy_config.get("initial_capital", 1000000))

        # 按日期顺序执行
        dates = sorted(historical_data.keys())

        for date in dates:
            daily_data = historical_data[date]

            # 为每只股票生成交易信号
            daily_signals = {}
            for symbol in daily_data:
                try:
                    # 使用 TradingAgents 生成信号
                    signal = self._generate_trading_signal(symbol, date, daily_data[symbol])
                    daily_signals[symbol] = signal
                except Exception as e:
                    print(f"生成 {symbol} 信号时出错: {e}")
                    continue

            # 执行投资组合重平衡
            portfolio_changes = self._rebalance_portfolio(
                portfolio, daily_signals, daily_data, strategy_config
            )

            # 记录交易历史
            if portfolio_changes:
                trading_history.extend(portfolio_changes)

            # 更新投资组合价值
            portfolio.update_value(daily_data)

        return trading_history

    def _analyze_performance(self, trading_history: List[Dict]) -> Dict:
        """分析策略性能"""

        # 计算收益序列
        returns = self._calculate_returns(trading_history)

        # 基础性能指标
        total_return = self._calculate_total_return(returns)
        annualized_return = self._calculate_annualized_return(returns)
        volatility = self._calculate_volatility(returns)
        sharpe_ratio = self._calculate_sharpe_ratio(returns)

        # 高级性能指标
        sortino_ratio = self._calculate_sortino_ratio(returns)
        calmar_ratio = self._calculate_calmar_ratio(returns)
        max_drawdown = self._calculate_max_drawdown(returns)

        # 胜率分析
        win_rate = self._calculate_win_rate(trading_history)
        profit_factor = self._calculate_profit_factor(trading_history)

        return {
            "total_return": total_return,
            "annualized_return": annualized_return,
            "volatility": volatility,
            "sharpe_ratio": sharpe_ratio,
            "sortino_ratio": sortino_ratio,
            "calmar_ratio": calmar_ratio,
            "max_drawdown": max_drawdown,
            "win_rate": win_rate,
            "profit_factor": profit_factor,
            "total_trades": len(trading_history),
            "avg_holding_period": self._calculate_avg_holding_period(trading_history)
        }
```

这些高级示例展示了 TradingAgents 框架的扩展能力和在复杂金融应用中的使用方法。通过这些示例，您可以构建更加复杂和专业的交易系统。

<!-- docs/examples/basic-examples.md -->

# 基本使用示例

## 概述

本文档提供了 TradingAgents 框架的基本使用示例，帮助您快速上手并了解各种功能的使用方法。

## 示例 1: 基本股票分析

### 最简单的使用方式
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 使用默认配置
ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# 分析苹果公司股票
state, decision = ta.propagate("AAPL", "2024-01-15")

print(f"推荐动作: {decision['action']}")
print(f"置信度: {decision['confidence']:.2f}")
print(f"推理: {decision['reasoning']}")
```

### 输出示例
```
推荐动作: buy
置信度: 0.75
推理: 基于强劲的基本面数据和积极的技术指标，建议买入AAPL股票...
```

## 示例 2: 自定义配置分析

### 配置优化的分析
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

def analyze_with_custom_config(symbol, date):
    """使用自定义配置进行分析"""
    
    # 创建自定义配置
    config = DEFAULT_CONFIG.copy()
    config.update({
        "deep_think_llm": "gpt-4o-mini",      # 使用经济模型
        "quick_think_llm": "gpt-4o-mini",     # 使用经济模型
        "max_debate_rounds": 2,               # 增加辩论轮次
        "max_risk_discuss_rounds": 1,         # 风险讨论轮次
        "online_tools": True,                 # 使用实时数据
    })
    
    # 选择特定的分析师
    selected_analysts = ["market", "fundamentals", "news"]
    
    # 初始化分析器
    ta = TradingAgentsGraph(
        selected_analysts=selected_analysts,
        debug=True,
        config=config
    )
    
    print(f"开始分析 {symbol} ({date})...")
    
    # 执行分析
    state, decision = ta.propagate(symbol, date)
    
    return state, decision

# 使用示例
state, decision = analyze_with_custom_config("TSLA", "2024-01-15")

print("\n=== 分析结果 ===")
print(f"股票: TSLA")
print(f"动作: {decision['action']}")
print(f"数量: {decision.get('quantity', 0)}")
print(f"置信度: {decision['confidence']:.1%}")
print(f"风险评分: {decision['risk_score']:.1%}")
```

## 示例 3: 批量股票分析

### 分析多只股票
```python
import pandas as pd
from datetime import datetime, timedelta

def batch_analysis(symbols, date):
    """批量分析多只股票"""
    
    # 配置
    config = DEFAULT_CONFIG.copy()
    config["max_debate_rounds"] = 1  # 减少辩论轮次以提高速度
    config["online_tools"] = True
    
    ta = TradingAgentsGraph(debug=False, config=config)
    
    results = []
    
    for symbol in symbols:
        try:
            print(f"正在分析 {symbol}...")
            
            # 执行分析
            state, decision = ta.propagate(symbol, date)
            
            # 收集结果
            result = {
                "symbol": symbol,
                "action": decision.get("action", "hold"),
                "confidence": decision.get("confidence", 0.5),
                "risk_score": decision.get("risk_score", 0.5),
                "reasoning": decision.get("reasoning", "")[:100] + "..."  # 截取前100字符
            }
            
            results.append(result)
            print(f"✅ {symbol}: {result['action']} (置信度: {result['confidence']:.1%})")
            
        except Exception as e:
            print(f"❌ {symbol}: 分析失败 - {e}")
            results.append({
                "symbol": symbol,
                "action": "error",
                "confidence": 0.0,
                "risk_score": 1.0,
                "reasoning": f"分析失败: {e}"
            })
    
    return pd.DataFrame(results)

# 使用示例
tech_stocks = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
analysis_date = "2024-01-15"

results_df = batch_analysis(tech_stocks, analysis_date)

print("\n=== 批量分析结果 ===")
print(results_df[["symbol", "action", "confidence", "risk_score"]])

# 筛选买入建议
buy_recommendations = results_df[results_df["action"] == "buy"]
print(f"\n买入建议 ({len(buy_recommendations)} 只):")
for _, row in buy_recommendations.iterrows():
    print(f"  {row['symbol']}: 置信度 {row['confidence']:.1%}")
```

## 示例 4: 不同LLM提供商对比

### 对比不同LLM的分析结果
```python
def compare_llm_providers(symbol, date):
    """对比不同LLM提供商的分析结果"""
    
    providers_config = {
        "OpenAI": {
            "llm_provider": "openai",
            "deep_think_llm": "gpt-4o-mini",
            "quick_think_llm": "gpt-4o-mini",
        },
        "Google": {
            "llm_provider": "google",
            "deep_think_llm": "gemini-pro",
            "quick_think_llm": "gemini-pro",
        },
        # 注意: 需要相应的API密钥
    }
    
    results = {}
    
    for provider_name, provider_config in providers_config.items():
        try:
            print(f"使用 {provider_name} 分析 {symbol}...")
            
            # 创建配置
            config = DEFAULT_CONFIG.copy()
            config.update(provider_config)
            config["max_debate_rounds"] = 1
            
            # 初始化分析器
            ta = TradingAgentsGraph(debug=False, config=config)
            
            # 执行分析
            state, decision = ta.propagate(symbol, date)
            
            results[provider_name] = {
                "action": decision.get("action", "hold"),
                "confidence": decision.get("confidence", 0.5),
                "risk_score": decision.get("risk_score", 0.5),
            }
            
            print(f"✅ {provider_name}: {results[provider_name]['action']}")
            
        except Exception as e:
            print(f"❌ {provider_name}: 失败 - {e}")
            results[provider_name] = {"error": str(e)}
    
    return results

# 使用示例
comparison_results = compare_llm_providers("AAPL", "2024-01-15")

print("\n=== LLM提供商对比结果 ===")
for provider, result in comparison_results.items():
    if "error" not in result:
        print(f"{provider}:")
        print(f"  动作: {result['action']}")
        print(f"  置信度: {result['confidence']:.1%}")
        print(f"  风险评分: {result['risk_score']:.1%}")
    else:
        print(f"{provider}: 错误 - {result['error']}")
```

## 示例 5: 历史回测分析

### 简单的历史回测
```python
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def historical_backtest(symbol, start_date, end_date, interval_days=7):
    """简单的历史回测"""
    
    # 配置
    config = DEFAULT_CONFIG.copy()
    config["max_debate_rounds"] = 1
    config["online_tools"] = True
    
    ta = TradingAgentsGraph(debug=False, config=config)
    
    # 生成日期列表
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    
    results = []
    
    while current_date <= end_date_obj:
        date_str = current_date.strftime("%Y-%m-%d")
        
        try:
            print(f"分析 {symbol} 在 {date_str}...")
            
            # 执行分析
            state, decision = ta.propagate(symbol, date_str)
            
            result = {
                "date": date_str,
                "action": decision.get("action", "hold"),
                "confidence": decision.get("confidence", 0.5),
                "risk_score": decision.get("risk_score", 0.5),
            }
            
            results.append(result)
            print(f"  {result['action']} (置信度: {result['confidence']:.1%})")
            
        except Exception as e:
            print(f"  错误: {e}")
        
        # 移动到下一个日期
        current_date += timedelta(days=interval_days)
    
    return pd.DataFrame(results)

# 使用示例
backtest_results = historical_backtest(
    symbol="AAPL",
    start_date="2024-01-01",
    end_date="2024-01-31",
    interval_days=7
)

print("\n=== 历史回测结果 ===")
print(backtest_results)

# 统计分析
action_counts = backtest_results["action"].value_counts()
print(f"\n动作分布:")
for action, count in action_counts.items():
    print(f"  {action}: {count} 次")

avg_confidence = backtest_results["confidence"].mean()
print(f"\n平均置信度: {avg_confidence:.1%}")
```

## 示例 6: 实时监控

### 实时股票监控
```python
import time
from datetime import datetime

def real_time_monitor(symbols, check_interval=300):
    """实时监控股票"""
    
    config = DEFAULT_CONFIG.copy()
    config["max_debate_rounds"] = 1
    config["online_tools"] = True
    
    ta = TradingAgentsGraph(debug=False, config=config)
    
    print(f"开始监控 {len(symbols)} 只股票...")
    print(f"检查间隔: {check_interval} 秒")
    print("按 Ctrl+C 停止监控\n")
    
    try:
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            print(f"=== {current_time} ===")
            
            for symbol in symbols:
                try:
                    # 执行分析
                    state, decision = ta.propagate(symbol, current_date)
                    
                    action = decision.get("action", "hold")
                    confidence = decision.get("confidence", 0.5)
                    
                    # 输出结果
                    status_emoji = "🟢" if action == "buy" else "🔴" if action == "sell" else "🟡"
                    print(f"{status_emoji} {symbol}: {action.upper()} (置信度: {confidence:.1%})")
                    
                    # 高置信度买入/卖出提醒
                    if confidence > 0.8 and action in ["buy", "sell"]:
                        print(f"  ⚠️  高置信度{action}信号!")
                
                except Exception as e:
                    print(f"❌ {symbol}: 分析失败 - {e}")
            
            print(f"下次检查: {check_interval} 秒后\n")
            time.sleep(check_interval)
    
    except KeyboardInterrupt:
        print("\n监控已停止")

# 使用示例（注释掉以避免长时间运行）
# watch_list = ["AAPL", "GOOGL", "TSLA"]
# real_time_monitor(watch_list, check_interval=300)  # 每5分钟检查一次
```

## 示例 7: 错误处理和重试

### 健壮的分析函数
```python
import time
from typing import Optional, Tuple

def robust_analysis(symbol: str, date: str, max_retries: int = 3) -> Optional[Tuple[dict, dict]]:
    """带错误处理和重试的分析函数"""
    
    config = DEFAULT_CONFIG.copy()
    config["max_debate_rounds"] = 1
    
    for attempt in range(max_retries):
        try:
            print(f"分析 {symbol} (尝试 {attempt + 1}/{max_retries})...")
            
            ta = TradingAgentsGraph(debug=False, config=config)
            state, decision = ta.propagate(symbol, date)
            
            # 验证结果
            if not decision or "action" not in decision:
                raise ValueError("分析结果无效")
            
            print(f"✅ 分析成功: {decision['action']}")
            return state, decision
            
        except Exception as e:
            print(f"❌ 尝试 {attempt + 1} 失败: {e}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print(f"所有尝试都失败了")
                return None

# 使用示例
result = robust_analysis("AAPL", "2024-01-15", max_retries=3)

if result:
    state, decision = result
    print(f"最终结果: {decision['action']}")
else:
    print("分析失败")
```

## 示例 8: 结果保存和加载

### 保存分析结果
```python
import json
import pickle
from datetime import datetime

def save_analysis_result(symbol, date, state, decision, format="json"):
    """保存分析结果"""
    
    # 创建结果目录
    import os
    results_dir = "analysis_results"
    os.makedirs(results_dir, exist_ok=True)
    
    # 生成文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{symbol}_{date}_{timestamp}"
    
    # 准备数据
    result_data = {
        "symbol": symbol,
        "date": date,
        "timestamp": timestamp,
        "decision": decision,
        "state_summary": {
            "analyst_reports": getattr(state, "analyst_reports", {}),
            "research_reports": getattr(state, "research_reports", {}),
            "trader_decision": getattr(state, "trader_decision", {}),
            "risk_assessment": getattr(state, "risk_assessment", {}),
        }
    }
    
    if format == "json":
        filepath = os.path.join(results_dir, f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2, ensure_ascii=False)
    
    elif format == "pickle":
        filepath = os.path.join(results_dir, f"{filename}.pkl")
        with open(filepath, "wb") as f:
            pickle.dump(result_data, f)
    
    print(f"结果已保存到: {filepath}")
    return filepath

# 使用示例
ta = TradingAgentsGraph(debug=False, config=DEFAULT_CONFIG.copy())
state, decision = ta.propagate("AAPL", "2024-01-15")

# 保存结果
save_analysis_result("AAPL", "2024-01-15", state, decision, format="json")
```

这些基本示例展示了 TradingAgents 框架的主要功能和使用模式。您可以根据自己的需求修改和扩展这些示例。


<!-- docs/faq/faq.md -->

# 常见问题解答 (FAQ)

## 概述

本文档收集了用户在使用 TradingAgents 框架时最常遇到的问题和解答，帮助您快速解决常见问题。

## 🚀 安装和配置

### Q1: 安装时出现依赖冲突怎么办？

**A:** 依赖冲突通常是由于不同包的版本要求不兼容导致的。解决方法：

```bash
# 方法1: 使用新的虚拟环境
conda create -n tradingagents-clean python=3.11
conda activate tradingagents-clean
pip install -r requirements.txt

# 方法2: 使用 pip-tools 解决冲突
pip install pip-tools
pip-compile requirements.in
pip-sync requirements.txt

# 方法3: 逐个安装核心依赖
pip install langchain-openai langgraph finnhub-python pandas
```

### Q2: API 密钥设置后仍然报错？

**A:** 检查以下几个方面：

1. **环境变量设置**：
```bash
# 检查环境变量是否正确设置
echo $OPENAI_API_KEY
echo $FINNHUB_API_KEY

# Windows 用户
echo %OPENAI_API_KEY%
echo %FINNHUB_API_KEY%
```

2. **密钥格式验证**：
```python
import os
# OpenAI 密钥应该以 'sk-' 开头
openai_key = os.getenv('OPENAI_API_KEY')
print(f"OpenAI Key: {openai_key[:10]}..." if openai_key else "Not set")

# FinnHub 密钥是字母数字组合
finnhub_key = os.getenv('FINNHUB_API_KEY')
print(f"FinnHub Key: {finnhub_key[:10]}..." if finnhub_key else "Not set")
```

3. **权限检查**：
```python
# 测试 API 连接
import openai
import finnhub

# 测试 OpenAI
try:
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=5
    )
    print("OpenAI API 连接成功")
except Exception as e:
    print(f"OpenAI API 错误: {e}")

# 测试 FinnHub
try:
    finnhub_client = finnhub.Client(api_key=os.getenv('FINNHUB_API_KEY'))
    quote = finnhub_client.quote('AAPL')
    print("FinnHub API 连接成功")
except Exception as e:
    print(f"FinnHub API 错误: {e}")
```

### Q3: 支持哪些 Python 版本？

**A:** TradingAgents 支持 Python 3.10, 3.11, 和 3.12。推荐使用 Python 3.11 以获得最佳性能和兼容性。

```bash
# 检查 Python 版本
python --version

# 如果版本不符合要求，使用 pyenv 安装
pyenv install 3.11.7
pyenv global 3.11.7
```

## 💰 成本和使用

### Q4: 使用 TradingAgents 的成本是多少？

**A:** 成本主要来自 LLM API 调用：

**典型成本估算**（单次分析）：
- **经济模式**：$0.01-0.05（使用 gpt-4o-mini）
- **标准模式**：$0.05-0.15（使用 gpt-4o）
- **高精度模式**：$0.10-0.30（使用 gpt-4o + 多轮辩论）

**成本优化建议**：
```python
# 低成本配置
cost_optimized_config = {
    "deep_think_llm": "gpt-4o-mini",
    "quick_think_llm": "gpt-4o-mini",
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "online_tools": False  # 使用缓存数据
}
```

### Q5: 如何控制 API 调用成本？

**A:** 多种成本控制策略：

1. **设置预算限制**：
```python
class BudgetController:
    def __init__(self, daily_budget=50):
        self.daily_budget = daily_budget
        self.current_usage = 0
    
    def check_budget(self, estimated_cost):
        if self.current_usage + estimated_cost > self.daily_budget:
            raise Exception("Daily budget exceeded")
        return True
```

2. **使用缓存**：
```python
config = {
    "online_tools": False,  # 使用缓存数据
    "cache_duration": 3600  # 1小时缓存
}
```

3. **选择性分析师**：
```python
# 只使用核心分析师
selected_analysts = ["market", "fundamentals"]  # 而不是全部四个
```

## 🔧 技术问题

### Q6: 分析速度太慢怎么办？

**A:** 多种优化方法：

1. **并行处理**：
```python
config = {
    "parallel_analysis": True,
    "max_workers": 4
}
```

2. **使用更快的模型**：
```python
config = {
    "deep_think_llm": "gpt-4o-mini",  # 更快的模型
    "quick_think_llm": "gpt-4o-mini"
}
```

3. **减少辩论轮次**：
```python
config = {
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1
}
```

4. **启用缓存**：
```python
config = {
    "online_tools": True,
    "cache_enabled": True
}
```

### Q7: 内存使用过高怎么解决？

**A:** 内存优化策略：

1. **限制缓存大小**：
```python
config = {
    "memory_cache": {
        "max_size": 500,  # 减少缓存项数量
        "cleanup_threshold": 0.7
    }
}
```

2. **分批处理**：
```python
# 分批分析多只股票
def batch_analysis(symbols, batch_size=5):
    for i in range(0, len(symbols), batch_size):
        batch = symbols[i:i+batch_size]
        # 处理批次
        yield analyze_batch(batch)
```

3. **清理资源**：
```python
import gc

def analyze_with_cleanup(symbol, date):
    try:
        result = ta.propagate(symbol, date)
        return result
    finally:
        gc.collect()  # 强制垃圾回收
```

### Q8: 网络连接不稳定导致分析失败？

**A:** 网络问题解决方案：

1. **重试机制**：
```python
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay * (2 ** attempt))
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=3)
def robust_analysis(symbol, date):
    return ta.propagate(symbol, date)
```

2. **超时设置**：
```python
config = {
    "timeout": 60,  # 60秒超时
    "connect_timeout": 10
}
```

3. **代理设置**：
```python
import os
os.environ['HTTP_PROXY'] = 'http://proxy.company.com:8080'
os.environ['HTTPS_PROXY'] = 'https://proxy.company.com:8080'
```

## 📊 数据和分析

### Q9: 某些股票无法获取数据？

**A:** 数据获取问题排查：

1. **检查股票代码**：
```python
# 确保使用正确的股票代码格式
symbols = {
    "US": "AAPL",           # 美股
    "HK": "0700.HK",        # 港股
    "CN": "000001.SZ"       # A股
}
```

2. **验证数据源**：
```python
def check_data_availability(symbol):
    try:
        # 检查 FinnHub
        finnhub_data = finnhub_client.quote(symbol)
        print(f"FinnHub: {symbol} - OK")
    except:
        print(f"FinnHub: {symbol} - Failed")
    
    try:
        # 检查 Yahoo Finance
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        info = ticker.info
        print(f"Yahoo: {symbol} - OK")
    except:
        print(f"Yahoo: {symbol} - Failed")
```

3. **使用备用数据源**：
```python
config = {
    "data_sources": {
        "primary": "finnhub",
        "fallback": ["yahoo", "alpha_vantage"]
    }
}
```

### Q10: 分析结果不准确或不合理？

**A:** 提高分析准确性的方法：

1. **增加辩论轮次**：
```python
config = {
    "max_debate_rounds": 3,  # 增加辩论轮次
    "max_risk_discuss_rounds": 2
}
```

2. **使用更强的模型**：
```python
config = {
    "deep_think_llm": "gpt-4o",  # 使用更强的模型
    "quick_think_llm": "gpt-4o-mini"
}
```

3. **调整分析师权重**：
```python
config = {
    "analyst_weights": {
        "fundamentals": 0.4,  # 增加基本面权重
        "technical": 0.3,
        "news": 0.2,
        "social": 0.1
    }
}
```

4. **启用更多数据源**：
```python
config = {
    "online_tools": True,
    "data_sources": ["finnhub", "yahoo", "reddit", "google_news"]
}
```

## 🛠️ 开发和扩展

### Q11: 如何创建自定义智能体？

**A:** 创建自定义智能体的步骤：

1. **继承基础类**：
```python
from tradingagents.agents.analysts.base_analyst import BaseAnalyst

class CustomAnalyst(BaseAnalyst):
    def __init__(self, llm, config):
        super().__init__(llm, config)
        self.custom_tools = self._initialize_custom_tools()
    
    def perform_analysis(self, data: Dict) -> Dict:
        # 实现自定义分析逻辑
        return {
            "custom_score": 0.75,
            "custom_insights": ["insight1", "insight2"],
            "recommendation": "buy"
        }
```

2. **注册到框架**：
```python
# 在配置中添加自定义智能体
config = {
    "custom_analysts": {
        "custom": CustomAnalyst
    }
}
```

### Q12: 如何集成新的数据源？

**A:** 集成新数据源的方法：

1. **创建数据提供器**：
```python
class CustomDataProvider:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_data(self, symbol):
        # 实现数据获取逻辑
        return {"custom_metric": 0.85}
```

2. **注册数据源**：
```python
config = {
    "custom_data_sources": {
        "custom_provider": CustomDataProvider
    }
}
```

## 🚨 错误处理

### Q13: 常见错误代码及解决方法

**A:** 主要错误类型和解决方案：

| 错误类型 | 原因 | 解决方法 |
|---------|------|---------|
| `API_KEY_INVALID` | API密钥无效 | 检查密钥格式和权限 |
| `RATE_LIMIT_EXCEEDED` | 超过API限制 | 降低调用频率或升级账户 |
| `NETWORK_TIMEOUT` | 网络超时 | 检查网络连接，增加超时时间 |
| `DATA_NOT_FOUND` | 数据不存在 | 检查股票代码，使用备用数据源 |
| `INSUFFICIENT_MEMORY` | 内存不足 | 减少缓存大小，分批处理 |

### Q14: 如何启用调试模式？

**A:** 调试模式配置：

```python
# 启用详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 启用调试模式
config = {
    "debug": True,
    "log_level": "DEBUG",
    "save_intermediate_results": True
}

# 使用调试配置
ta = TradingAgentsGraph(debug=True, config=config)
```

## 📞 获取帮助

### Q15: 在哪里可以获得更多帮助？

**A:** 多种获取帮助的渠道：

1. **官方文档**: [docs/README.md](../README.md)
2. **GitHub Issues**: [提交问题](https://github.com/TauricResearch/TradingAgents/issues)
3. **Discord 社区**: [加入讨论](https://discord.com/invite/hk9PGKShPK)
4. **邮箱支持**: support@tauric.ai

### Q16: 如何报告 Bug？

**A:** Bug 报告模板：

```markdown
## Bug 描述
简要描述遇到的问题

## 复现步骤
1. 执行的代码
2. 使用的配置
3. 输入的参数

## 预期行为
描述期望的结果

## 实际行为
描述实际发生的情况

## 环境信息
- Python 版本:
- TradingAgents 版本:
- 操作系统:
- 相关依赖版本:

## 错误日志
粘贴完整的错误信息
```

如果您的问题没有在这里找到答案，请通过上述渠道联系我们获取帮助。


<!-- docs/guides/a-share-analysis-guide.md -->

# A股分析使用指南

## 🎯 概述

TradingAgents-CN v0.1.3 新增了完整的A股市场支持，通过集成通达信API，为用户提供实时的A股数据分析能力。

## 🚀 快速开始

### 1. 确保环境配置

```bash
# 激活虚拟环境
.\env\Scripts\Activate.ps1  # Windows
source env/bin/activate     # Linux/macOS

# 确保已安装通达信API支持
pip install pytdx
```

### 2. 启动Web界面

```bash
python -m streamlit run web/app.py
```

### 3. 选择A股市场

在Web界面中：
1. 在"选择市场"下拉框中选择 **"A股"**
2. 在股票代码输入框中输入A股代码
3. 选择分析师和研究深度
4. 点击"开始分析"

## 📊 支持的A股代码格式

### 主要板块代码规则

| 代码前缀 | 市场板块 | 示例代码 | 股票名称 |
|----------|----------|----------|----------|
| **000xxx** | 深圳主板 | 000001 | 平安银行 |
| **002xxx** | 深圳中小板 | 002415 | 海康威视 |
| **003xxx** | 深圳主板 | 003816 | 中国广核 |
| **300xxx** | 创业板 | 300750 | 宁德时代 |
| **600xxx** | 上海主板 | 600519 | 贵州茅台 |
| **601xxx** | 上海主板 | 601318 | 中国平安 |
| **603xxx** | 上海主板 | 603259 | 药明康德 |
| **688xxx** | 科创板 | 688981 | 中芯国际 |

### 热门股票代码示例

#### 🏦 银行股
- `000001` - 平安银行
- `600036` - 招商银行
- `601398` - 工商银行
- `601288` - 农业银行

#### 🍷 白酒股
- `600519` - 贵州茅台
- `000858` - 五粮液
- `000568` - 泸州老窖
- `002304` - 洋河股份

#### 🔋 新能源
- `300750` - 宁德时代
- `002594` - 比亚迪
- `300274` - 阳光电源
- `002460` - 赣锋锂业

#### 💻 科技股
- `000002` - 万科A
- `000651` - 格力电器
- `002415` - 海康威视
- `000725` - 京东方A

## 🔧 数据源说明

### 通达信API优势

| 特性 | 通达信API | Yahoo Finance | 优势说明 |
|------|-----------|---------------|----------|
| **A股覆盖** | ✅ 完整覆盖 | ❌ 不支持 | 独有的A股数据源 |
| **实时性** | ✅ 秒级更新 | ⚠️ 15分钟延迟 | 适合日内交易分析 |
| **中文支持** | ✅ 原生中文 | ❌ 英文为主 | 股票名称、板块中文显示 |
| **成本** | ✅ 完全免费 | ✅ 免费 | 无API调用限制 |
| **配置复杂度** | ✅ 零配置 | ✅ 零配置 | 即装即用 |

### 可用服务器

系统自动使用经过测试的可用服务器：
- 武汉电信主站1 (119.97.185.59:7709)
- 广州双线主站7 (116.205.183.150:7709)
- 广州双线主站6 (116.205.171.132:7709)
- 北京双线主站4 (124.70.75.113:7709)
- 等10个验证可用的服务器

## 📈 分析功能特色

### 1. 实时行情数据

- **当前价格**: 实时股价更新
- **涨跌幅**: 当日涨跌幅度和涨跌金额
- **成交量**: 实时成交量和成交额
- **五档买卖**: 买一到买五、卖一到卖五价格和数量

### 2. 历史数据分析

- **K线数据**: 日线、周线、月线历史数据
- **技术指标**: MA、RSI、MACD、布林带等
- **价格走势**: 历史价格变化趋势分析
- **成交量分析**: 量价关系分析

### 3. A股特色分析

- **涨跌停分析**: 识别涨停、跌停等A股特有现象
- **ST股票识别**: 特别处理股票的风险提示
- **板块轮动**: A股特有的板块轮动规律分析
- **政策影响**: 中国政策对股价的影响分析

## 🕐 交易时间说明

### A股交易时间

- **上午**: 09:30 - 11:30
- **下午**: 13:00 - 15:00
- **休市**: 周末、法定节假日

### 数据获取说明

| 时间段 | 数据类型 | 说明 |
|--------|----------|------|
| **交易时间** | 实时数据 | 秒级更新的实时行情 |
| **非交易时间** | 收盘数据 | 显示最后交易日的收盘价 |
| **周末/节假日** | 历史数据 | 可获取历史K线和技术指标 |

## 🎯 使用示例

### 示例1: 分析贵州茅台

1. 选择市场: **A股**
2. 输入代码: **600519**
3. 选择分析师: **全部分析师**
4. 研究深度: **深度分析**
5. 点击"开始分析"

**预期结果**:
- 实时股价和涨跌幅
- 技术指标分析
- 基本面评估
- 新闻和社交媒体情绪
- 综合投资建议

### 示例2: 分析宁德时代

1. 选择市场: **A股**
2. 输入代码: **300750**
3. 选择分析师: **技术分析师 + 基本面分析师**
4. 研究深度: **标准分析**
5. 点击"开始分析"

**预期结果**:
- 创业板股票特色分析
- 新能源行业趋势
- 技术形态识别
- 估值水平评估

## ⚠️ 注意事项

### 1. 网络要求

- 需要稳定的网络连接访问通达信服务器
- 如果连接失败，系统会自动尝试备用服务器
- 建议在网络环境良好时进行分析

### 2. 数据准确性

- 实时数据来源于通达信免费服务器
- 重要投资决策建议交叉验证多个数据源
- 系统提供的是分析建议，不构成投资建议

### 3. 使用限制

- 通达信API为免费服务，可能存在访问限制
- 建议合理使用，避免频繁请求
- 如遇到连接问题，可稍后重试

## 🔧 故障排除

### 常见问题

#### 1. 连接失败

**问题**: 显示"通达信API连接失败"

**解决方案**:
```bash
# 检查网络连接
ping 119.97.185.59

# 重新测试服务器
python tests/fast_tdx_test.py

# 检查防火墙设置
```

#### 2. 数据获取失败

**问题**: 连接成功但无法获取数据

**解决方案**:
- 确认股票代码格式正确
- 检查是否为交易时间
- 尝试其他股票代码验证

#### 3. 分析速度慢

**问题**: A股分析比美股慢

**解决方案**:
- 选择较少的分析师
- 降低研究深度
- 检查网络连接质量

## 📊 性能优化建议

### 1. 分析师选择

- **快速分析**: 选择1-2个核心分析师
- **全面分析**: 选择所有分析师（耗时较长）
- **专项分析**: 根据需求选择特定分析师

### 2. 研究深度

- **快速**: 2-4分钟，适合日内交易
- **标准**: 5-8分钟，适合短期投资
- **深度**: 10-15分钟，适合长期投资
- **全面**: 15-25分钟，适合重要决策

### 3. 使用技巧

- 在交易时间进行分析获得最新数据
- 批量分析多只股票时适当间隔
- 保存分析结果供后续参考

## 🎉 总结

TradingAgents-CN v0.1.3 的A股支持为中国投资者提供了：

1. **🇨🇳 本土化体验**: 完整的A股数据覆盖
2. **⚡ 实时分析**: 秒级数据更新
3. **💰 零成本**: 免费的数据源
4. **🔧 易用性**: 零配置即用
5. **📊 专业性**: 多维度分析框架

现在您可以像分析美股一样，对A股进行专业的多智能体协作分析！


<!-- docs/guides/config-management-guide.md -->

# 配置管理和成本统计使用指南

## 📋 概述

TradingAgents-CN v0.1.3 新增了完整的配置管理和成本统计系统，让您可以：

- 🔧 **统一管理API密钥和模型配置**
- 💰 **实时跟踪Token使用和成本**
- 📊 **查看详细的使用统计和趋势**
- ⚙️ **自定义系统设置和费率**

## 🚀 快速开始

### 1. 启动Web界面

```bash
# 激活虚拟环境
.\env\Scripts\Activate.ps1  # Windows
source env/bin/activate     # Linux/macOS

# 启动Web应用
python -m streamlit run web/app.py
```

### 2. 访问配置管理

1. 在Web界面左侧选择 **"⚙️ 配置管理"**
2. 选择要管理的功能：
   - **模型配置** - 管理API密钥和模型参数
   - **定价设置** - 设置各供应商的费率
   - **使用统计** - 查看Token使用和成本统计
   - **系统设置** - 配置系统默认参数

## 🤖 模型配置管理

### 支持的模型供应商

| 供应商 | 模型示例 | 货币 | 说明 |
|--------|----------|------|------|
| **阿里百炼** | qwen-turbo, qwen-plus-latest, qwen-max | CNY | 国产模型，推荐使用 |
| **OpenAI** | gpt-3.5-turbo, gpt-4, gpt-4-turbo | USD | 国际领先模型 |
| **Google** | gemini-pro, gemini-pro-vision | USD | Google最新模型 |
| **Anthropic** | claude-3-sonnet, claude-3-opus | USD | 高质量对话模型 |

### 配置步骤

#### **添加新模型**

1. 进入 **"模型配置"** 页面
2. 在 **"添加新模型"** 部分填写：
   - **供应商**: 选择模型提供商
   - **模型名称**: 输入具体模型名（如 qwen-plus-latest）
   - **API密钥**: 输入您的API密钥
   - **最大Token数**: 设置输出限制（1000-32000）
   - **温度参数**: 控制输出随机性（0.0-2.0）
   - **启用模型**: 是否在分析中使用

3. 点击 **"添加模型"** 保存

#### **编辑现有模型**

1. 在模型列表中选择要编辑的模型
2. 修改相应参数
3. 点击 **"保存配置"**

### 模型配置示例

```json
{
  "provider": "dashscope",
  "model_name": "qwen-plus-latest",
  "api_key": "sk-your-api-key-here",
  "max_tokens": 4000,
  "temperature": 0.7,
  "enabled": true
}
```

## 💰 定价设置管理

### 默认费率表

#### **阿里百炼 (CNY/1000 tokens)**
| 模型 | 输入价格 | 输出价格 | 说明 |
|------|----------|----------|------|
| qwen-turbo | ¥0.002 | ¥0.006 | 快速响应 |
| qwen-plus | ¥0.004 | ¥0.012 | 平衡性能 |
| qwen-max | ¥0.020 | ¥0.060 | 最强性能 |

#### **OpenAI (USD/1000 tokens)**
| 模型 | 输入价格 | 输出价格 | 说明 |
|------|----------|----------|------|
| gpt-3.5-turbo | $0.0015 | $0.002 | 经济实用 |
| gpt-4 | $0.03 | $0.06 | 强大性能 |
| gpt-4-turbo | $0.01 | $0.03 | 优化版本 |

#### **Google (USD/1000 tokens)**
| 模型 | 输入价格 | 输出价格 | 说明 |
|------|----------|----------|------|
| gemini-pro | $0.00025 | $0.0005 | 高性价比 |
| gemini-pro-vision | $0.00025 | $0.0005 | 支持图像 |

### 自定义定价

1. 进入 **"定价设置"** 页面
2. 选择要编辑的模型定价
3. 修改：
   - **输入价格**: 每1000个输入token的价格
   - **输出价格**: 每1000个输出token的价格
   - **货币**: CNY/USD/EUR
4. 点击 **"保存定价"**

## 📊 使用统计和成本分析

### 统计数据类型

#### **总体统计**
- **总成本**: 指定时间内的总花费
- **总请求数**: API调用次数
- **输入Token**: 总输入token数量
- **输出Token**: 总输出token数量

#### **按供应商统计**
- **各供应商成本分布**
- **使用频率对比**
- **平均成本分析**

#### **使用趋势**
- **每日成本趋势图**
- **每日请求数趋势**
- **成本变化分析**

### 查看统计

1. 进入 **"使用统计"** 页面
2. 选择统计时间范围：
   - 最近7天
   - 最近30天
   - 最近90天
   - 最近365天
3. 查看详细统计图表和数据

### 成本控制

#### **设置成本警告**
1. 进入 **"系统设置"** 页面
2. 设置 **"成本警告阈值"**
3. 当日成本超过阈值时会收到警告

#### **成本优化建议**
- **选择合适的模型**: 根据需求选择性价比最高的模型
- **控制Token使用**: 合理设置最大Token数
- **监控使用趋势**: 定期查看成本统计

## ⚙️ 系统设置

### 基本设置

| 设置项 | 说明 | 默认值 |
|--------|------|--------|
| **默认供应商** | 新分析时的默认模型供应商 | dashscope |
| **默认模型** | 默认使用的模型名称 | qwen-turbo |
| **启用成本跟踪** | 是否记录Token使用和成本 | 启用 |
| **成本警告阈值** | 日成本超过此值时警告 | ¥100 |
| **首选货币** | 成本显示的首选货币 | CNY |
| **自动保存使用记录** | 是否自动保存使用记录 | 启用 |
| **最大使用记录数** | 保留的最大记录数量 | 10000 |

### 数据管理

#### **导出配置**
- 导出所有配置到JSON文件
- 便于备份和迁移

#### **清空使用记录**
- 清空所有Token使用记录
- 释放存储空间

#### **重置配置**
- 恢复所有配置到默认值
- 谨慎使用此功能

## 🔧 高级功能

### Token使用跟踪

系统会自动跟踪每次分析的Token使用：

```python
# 自动记录的信息
{
    "timestamp": "2025-06-28T10:30:00",
    "provider": "dashscope",
    "model_name": "qwen-plus",
    "input_tokens": 2500,
    "output_tokens": 1200,
    "cost": 0.024,
    "session_id": "analysis_abc123_20250628_1030",
    "analysis_type": "A股_analysis"
}
```

### 成本计算公式

```
总成本 = (输入Token数 / 1000) × 输入单价 + (输出Token数 / 1000) × 输出单价
```

### 会话跟踪

每次分析都会生成唯一的会话ID，用于：
- 跟踪单次分析的完整成本
- 分析不同类型任务的成本差异
- 优化Token使用策略

## 📈 使用场景示例

### 场景1：成本预算管理

**目标**: 控制月度AI使用成本在¥500以内

**操作**:
1. 设置成本警告阈值为¥16.67（500/30天）
2. 选择性价比高的模型（如qwen-turbo）
3. 定期查看使用统计，调整使用频率

### 场景2：多模型对比

**目标**: 比较不同模型的性价比

**操作**:
1. 配置多个模型（qwen-turbo, qwen-plus, gpt-3.5-turbo）
2. 对同一股票进行多次分析
3. 在使用统计中比较成本和效果

### 场景3：团队使用管理

**目标**: 管理团队的AI使用成本

**操作**:
1. 为不同团队成员配置不同的会话ID前缀
2. 通过使用统计分析各成员的使用情况
3. 制定使用规范和预算分配

## ⚠️ 注意事项

### 数据安全
- **API密钥加密存储**: 系统会安全存储您的API密钥
- **本地数据**: 所有配置和使用记录都存储在本地
- **定期备份**: 建议定期导出配置进行备份

### 成本控制
- **实时监控**: 定期查看使用统计
- **合理设置**: 根据需求设置合适的Token限制
- **模型选择**: 选择适合任务的模型，避免过度使用高成本模型

### 故障排除
- **配置丢失**: 使用"重置配置"功能恢复默认设置
- **成本异常**: 检查定价设置是否正确
- **统计错误**: 清空使用记录后重新开始统计

## 🔮 未来功能

### 计划中的功能
- **多货币汇率转换**: 自动转换不同货币的成本
- **成本预测**: 基于历史数据预测未来成本
- **使用报告**: 生成详细的使用报告
- **团队管理**: 支持多用户和权限管理
- **API集成**: 提供配置管理的API接口

---

**通过配置管理系统，您可以更好地控制AI使用成本，优化分析效果！** 💰📊


<!-- docs/localization/chinese-social-media-integration.md -->

# 中国社交媒体平台集成方案

## 🎯 概述

为了更好地服务中国用户，TradingAgents-CN 需要集成中国本土的社交媒体和财经平台，以获取更准确的市场情绪和投资者观点。

## 🌐 平台对应关系

### 国外 vs 国内平台映射

| 国外平台 | 国内对应平台 | 主要功能 | 数据价值 |
|----------|-------------|----------|----------|
| **Reddit** | **微博** | 话题讨论、热点追踪 | 市场情绪、热点事件 |
| **Twitter** | **微博** | 实时动态、新闻传播 | 即时反应、舆论趋势 |
| **Discord** | **微信群/QQ群** | 社区讨论 | 深度交流、专业观点 |
| **Telegram** | **钉钉/企业微信** | 专业交流 | 机构观点、内部消息 |

### 中国特色财经平台

| 平台类型 | 主要平台 | 特色功能 | 数据获取难度 |
|----------|----------|----------|-------------|
| **专业投资社区** | 雪球、东方财富股吧 | 股票讨论、投资策略 | 中等 |
| **综合社交媒体** | 微博、知乎 | 财经大V、专业分析 | 较高 |
| **新闻资讯平台** | 财联社、新浪财经 | 实时快讯、深度报道 | 中等 |
| **短视频平台** | 抖音、快手 | 财经科普、投资教育 | 较高 |
| **专业问答** | 知乎 | 深度分析、专业解答 | 中等 |

## 🔧 技术实现方案

### 阶段一：基础集成 (当前可实现)

#### 1. 微博情绪分析
```python
# 微博API集成示例
class WeiboSentimentAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_stock_sentiment(self, stock_symbol, days=7):
        """获取股票相关微博情绪"""
        # 搜索相关微博
        keywords = [stock_symbol, self.get_company_name(stock_symbol)]
        weibo_posts = self.search_weibo(keywords, days)
        
        # 情绪分析
        sentiment_scores = []
        for post in weibo_posts:
            score = self.analyze_sentiment(post['text'])
            sentiment_scores.append({
                'date': post['date'],
                'sentiment': score,
                'influence': post['repost_count'] + post['comment_count']
            })
        
        return self.aggregate_sentiment(sentiment_scores)
```

#### 2. 雪球数据集成
```python
# 雪球股票讨论分析
class XueqiuAnalyzer:
    def get_stock_discussions(self, stock_code):
        """获取雪球股票讨论"""
        # 雪球股票页面爬取
        discussions = self.crawl_xueqiu_discussions(stock_code)
        
        # 分析投资者观点
        bullish_count = 0
        bearish_count = 0
        
        for discussion in discussions:
            sentiment = self.classify_sentiment(discussion['content'])
            if sentiment > 0.6:
                bullish_count += 1
            elif sentiment < 0.4:
                bearish_count += 1
        
        return {
            'bullish_ratio': bullish_count / len(discussions),
            'bearish_ratio': bearish_count / len(discussions),
            'total_discussions': len(discussions)
        }
```

#### 3. 财经新闻聚合
```python
# 中国财经新闻集成
class ChineseFinanceNews:
    def __init__(self):
        self.sources = [
            'cailianshe',  # 财联社
            'sina_finance',  # 新浪财经
            'eastmoney',   # 东方财富
            'tencent_finance'  # 腾讯财经
        ]
    
    def get_stock_news(self, stock_symbol, days=7):
        """获取股票相关新闻"""
        all_news = []
        
        for source in self.sources:
            news = self.fetch_news_from_source(source, stock_symbol, days)
            all_news.extend(news)
        
        # 去重和排序
        unique_news = self.deduplicate_news(all_news)
        return sorted(unique_news, key=lambda x: x['publish_time'], reverse=True)
```

### 阶段二：深度集成 (需要API支持)

#### 1. 知乎专业分析
- 搜索股票相关的专业回答
- 分析知乎大V的投资观点
- 提取高质量的投资分析内容

#### 2. 抖音/快手财经内容
- 分析财经博主的观点
- 统计投资教育内容的趋势
- 监控散户投资者的情绪变化

#### 3. 微信公众号分析
- 跟踪知名财经公众号
- 分析机构研报和投资建议
- 监控政策解读和市场分析

## 📊 数据源优先级建议

### 高优先级 (立即实现)
1. **财联社API** - 专业财经快讯
2. **新浪财经RSS** - 免费新闻源
3. **东方财富股吧爬虫** - 散户情绪
4. **雪球公开数据** - 投资者讨论

### 中优先级 (中期实现)
1. **微博开放平台** - 需要申请API
2. **知乎爬虫** - 专业分析内容
3. **腾讯财经API** - 综合财经数据

### 低优先级 (长期规划)
1. **抖音/快手** - 技术难度高
2. **微信公众号** - 获取困难
3. **私域社群** - 需要特殊渠道

## 🔧 实现建议

### 当前可行的改进

#### 1. 更新社交媒体分析师提示词
```python
# 修改 social_media_analyst.py
system_message = """
您是一位专业的中国市场社交媒体分析师，负责分析中国投资者在各大平台上对特定股票的讨论和情绪。

主要分析平台包括：
- 微博：财经大V观点、热搜话题、散户情绪
- 雪球：专业投资者讨论、股票评级、投资策略
- 东方财富股吧：散户投资者情绪、讨论热度
- 知乎：深度分析文章、专业问答
- 财经新闻：财联社、新浪财经、东方财富等

请重点关注：
1. 投资者情绪变化趋势
2. 关键意见领袖(KOL)的观点
3. 散户与机构投资者的观点差异
4. 热点事件对股价的潜在影响
5. 政策解读和市场预期

请用中文撰写详细的分析报告。
"""
```

#### 2. 添加中国特色的数据工具
```python
# 新增工具函数
def get_chinese_social_sentiment(stock_symbol):
    """获取中国社交媒体情绪"""
    # 整合多个中国平台的数据
    pass

def get_chinese_finance_news(stock_symbol):
    """获取中国财经新闻"""
    # 聚合中国主要财经媒体
    pass
```

### 配置文件更新

#### 环境变量配置
```bash
# 中国社交媒体平台API密钥
WEIBO_API_KEY=your_weibo_api_key
WEIBO_API_SECRET=your_weibo_api_secret

# 财经数据源
CAILIANSHE_API_KEY=your_cailianshe_key
EASTMONEY_API_KEY=your_eastmoney_key

# 替代Reddit的配置
USE_CHINESE_SOCIAL_MEDIA=true
SOCIAL_MEDIA_PLATFORMS=weibo,xueqiu,eastmoney_guba
```

## 💡 实施建议

### 短期目标 (1-2个月)
1. ✅ 集成财联社新闻API
2. ✅ 开发雪球数据爬虫
3. ✅ 更新社交媒体分析师提示词
4. ✅ 添加中文财经术语库

### 中期目标 (3-6个月)
1. 🔄 申请微博开放平台API
2. 🔄 开发知乎内容分析工具
3. 🔄 建立中国财经KOL数据库
4. 🔄 优化中文情绪分析算法

### 长期目标 (6-12个月)
1. 🎯 建立完整的中国社交媒体监控体系
2. 🎯 开发实时情绪指数
3. 🎯 集成更多中国特色数据源
4. 🎯 建立中国市场专用的分析模型

## 🚨 注意事项

### 法律合规
- 遵守中国网络安全法和数据保护法规
- 尊重各平台的robots.txt和使用条款
- 避免过度爬取，使用合理的请求频率
- 保护用户隐私，不存储个人敏感信息

### 技术挑战
- 反爬虫机制：需要使用代理和请求头轮换
- 数据质量：需要过滤垃圾信息和机器人账号
- 实时性：平衡数据新鲜度和系统性能
- 准确性：中文情绪分析的准确性有待提升

### 成本考虑
- API调用费用：优先使用免费或低成本数据源
- 服务器资源：爬虫和数据处理需要额外计算资源
- 维护成本：需要持续监控和更新数据源

## 🎯 总结

通过集成中国本土的社交媒体和财经平台，TradingAgents-CN 将能够：

1. **提供更准确的市场情绪分析**
2. **更好地理解中国投资者行为**
3. **及时捕捉中国市场的热点事件**
4. **提供更符合中国用户习惯的分析报告**

这将显著提升系统在中国市场的适用性和准确性。


<!-- docs/maintenance/upstream-sync.md -->

# 上游同步策略

## 概述

本文档详细说明如何保持 TradingAgents-CN 与原项目 [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 的同步。

## 🎯 同步目标

### 主要目标
- **保持技术先进性**: 及时获得原项目的新功能和改进
- **修复安全问题**: 快速同步安全补丁和Bug修复
- **维护兼容性**: 确保中文增强功能与原项目兼容
- **减少维护成本**: 避免重复开发已有功能

### 平衡原则
- **核心功能同步**: 同步所有核心功能更新
- **文档保持独立**: 保持我们的中文文档体系
- **增强功能保护**: 保护我们的中文增强功能
- **冲突优雅处理**: 妥善处理合并冲突

## 🔄 同步策略

### 1. 监控策略

#### 自动监控
```bash
# 设置GitHub通知
# 1. 访问 https://github.com/TauricResearch/TradingAgents
# 2. 点击 "Watch" -> "Custom" -> 选择 "Releases" 和 "Issues"
# 3. 启用邮件通知
```

#### 定期检查
- **每周检查**: 检查是否有新的提交和发布
- **每月深度同步**: 进行完整的同步和测试
- **重要更新立即同步**: 安全补丁和重大Bug修复

### 2. 分支策略

```
main (我们的主分支)
├── upstream-sync-YYYYMMDD (同步分支)
├── feature/chinese-enhancement (中文增强功能)
└── hotfix/urgent-fixes (紧急修复)

upstream/main (原项目主分支)
```

#### 分支说明
- **main**: 我们的稳定主分支，包含所有中文增强
- **upstream-sync-YYYYMMDD**: 临时同步分支，用于合并上游更新
- **feature/chinese-enhancement**: 我们的功能增强分支
- **hotfix/urgent-fixes**: 紧急修复分支

### 3. 同步流程

#### 标准同步流程

```bash
# 1. 检查当前状态
git status
git log --oneline -5

# 2. 获取上游更新
git fetch upstream

# 3. 检查新提交
git log --oneline HEAD..upstream/main

# 4. 使用自动化脚本同步
python scripts/sync_upstream.py

# 5. 解决冲突（如果有）
# 手动编辑冲突文件
git add <resolved_files>
git commit

# 6. 测试同步结果
python -m pytest tests/
python examples/basic_example.py

# 7. 推送更新
git push origin main
```

#### 使用自动化脚本

```bash
# 基本同步
python scripts/sync_upstream.py

# 使用rebase策略
python scripts/sync_upstream.py --strategy rebase

# 自动模式（不询问确认）
python scripts/sync_upstream.py --auto
```

## ⚠️ 冲突处理策略

### 常见冲突类型

#### 1. 文档冲突
**原因**: 我们有完整的中文文档，原项目可能更新英文文档

**处理策略**:
```bash
# 保持我们的中文文档，参考原项目更新内容
# 冲突文件: README.md, docs/
# 解决方案: 保留我们的版本，手动同步有价值的内容
```

#### 2. 配置文件冲突
**原因**: 配置文件格式或默认值变更

**处理策略**:
```bash
# 仔细比较差异，合并有价值的配置
git diff HEAD upstream/main -- config/
# 手动合并配置更改
```

#### 3. 代码功能冲突
**原因**: 核心代码逻辑变更

**处理策略**:
```bash
# 优先采用上游版本，然后重新应用我们的增强
# 1. 接受上游版本
git checkout --theirs <conflicted_file>
# 2. 重新应用我们的增强功能
# 3. 测试确保功能正常
```

### 冲突解决优先级

1. **安全修复**: 最高优先级，立即采用上游版本
2. **Bug修复**: 高优先级，通常采用上游版本
3. **新功能**: 中等优先级，评估后决定是否采用
4. **文档更新**: 低优先级，保持我们的中文版本
5. **配置变更**: 低优先级，谨慎合并

## 📋 同步检查清单

### 同步前检查
- [ ] 当前分支是否干净（无未提交更改）
- [ ] 是否有正在进行的功能开发
- [ ] 是否有未解决的Issue需要考虑
- [ ] 备份当前状态（创建标签）

### 同步过程检查
- [ ] 上游更新是否获取成功
- [ ] 新提交是否包含重大变更
- [ ] 是否存在合并冲突
- [ ] 冲突是否正确解决

### 同步后检查
- [ ] 代码是否能正常运行
- [ ] 测试是否全部通过
- [ ] 文档是否需要更新
- [ ] 中文增强功能是否正常
- [ ] 配置文件是否正确

## 🧪 测试策略

### 自动化测试
```bash
# 运行完整测试套件
python -m pytest tests/ -v

# 运行基本功能测试
python examples/basic_example.py

# 运行性能测试
python tests/performance_test.py
```

### 手动测试
```bash
# 测试核心功能
python -c "
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())
state, decision = ta.propagate('AAPL', '2024-01-15')
print(f'Decision: {decision}')
"

# 测试中文文档
# 检查 docs/ 目录下的文档是否正常显示
```

## 📊 同步记录

### 同步日志格式
```json
{
  "sync_time": "2024-01-15T10:30:00Z",
  "upstream_commits": 5,
  "conflicts_resolved": 2,
  "files_changed": ["tradingagents/core.py", "config/default.yaml"],
  "tests_passed": true,
  "notes": "同步了新的风险管理功能"
}
```

### 版本标记策略
```bash
# 同步前创建标签
git tag -a v1.0.0-cn-pre-sync -m "同步前状态"

# 同步后创建标签
git tag -a v1.0.1-cn -m "同步上游更新 v1.2.3"

# 推送标签
git push origin --tags
```

## 🚨 应急处理

### 同步失败回滚
```bash
# 回滚到同步前状态
git reset --hard v1.0.0-cn-pre-sync

# 或者回滚到上一个提交
git reset --hard HEAD~1

# 强制推送（谨慎使用）
git push origin main --force-with-lease
```

### 紧急热修复
```bash
# 创建热修复分支
git checkout -b hotfix/urgent-fix

# 应用修复
# ... 修复代码 ...

# 快速合并
git checkout main
git merge hotfix/urgent-fix
git push origin main

# 删除热修复分支
git branch -d hotfix/urgent-fix
```

## 📅 同步计划

### 定期同步计划
- **每周一**: 检查上游更新，评估同步需求
- **每月第一周**: 进行完整同步和测试
- **重大版本发布后**: 立即评估和同步

### 特殊情况处理
- **安全漏洞**: 24小时内同步
- **重大Bug**: 48小时内同步
- **新功能**: 1周内评估，2周内同步

## 🤝 社区协作

### 与原项目互动
- **Issue报告**: 向原项目报告发现的Bug
- **功能建议**: 提出有价值的功能建议
- **代码贡献**: 将通用改进贡献回原项目

### 维护透明度
- **同步日志**: 公开同步记录和决策过程
- **变更说明**: 详细说明每次同步的内容
- **用户通知**: 及时通知用户重要更新

通过这套完整的同步策略，我们可以确保 TradingAgents-CN 始终保持与原项目的技术同步，同时维护我们独特的中文增强价值。


<!-- docs/overview/installation.md -->

# 详细安装指南

## 概述

本指南提供了 TradingAgents 框架的详细安装说明，包括不同操作系统的安装步骤、依赖管理、环境配置和常见问题解决方案。

## 系统要求

### 硬件要求
- **CPU**: 双核 2.0GHz 或更高 (推荐四核)
- **内存**: 最少 4GB RAM (推荐 8GB 或更高)
- **存储**: 至少 5GB 可用磁盘空间
- **网络**: 稳定的互联网连接 (用于API调用和数据获取)

### 软件要求
- **操作系统**: 
  - Windows 10/11 (64位)
  - macOS 10.15 (Catalina) 或更高版本
  - Linux (Ubuntu 18.04+, CentOS 7+, 或其他主流发行版)
- **Python**: 3.10, 3.11, 或 3.12 (推荐 3.11)
- **Git**: 用于克隆代码仓库

## 安装步骤

### 1. 安装 Python

#### Windows
```powershell
# 方法1: 从官网下载安装包
# 访问 https://www.python.org/downloads/windows/
# 下载 Python 3.11.x 安装包并运行

# 方法2: 使用 Chocolatey
choco install python311

# 方法3: 使用 Microsoft Store
# 在 Microsoft Store 搜索 "Python 3.11" 并安装

# 验证安装
python --version
pip --version
```

#### macOS
```bash
# 方法1: 使用 Homebrew (推荐)
brew install python@3.11

# 方法2: 使用 pyenv
brew install pyenv
pyenv install 3.11.7
pyenv global 3.11.7

# 方法3: 从官网下载
# 访问 https://www.python.org/downloads/macos/

# 验证安装
python3 --version
pip3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# 更新包列表
sudo apt update

# 安装 Python 3.11
sudo apt install python3.11 python3.11-pip python3.11-venv

# 设置默认 Python 版本 (可选)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# 验证安装
python3 --version
pip3 --version
```

#### Linux (CentOS/RHEL)
```bash
# 安装 EPEL 仓库
sudo yum install epel-release

# 安装 Python 3.11
sudo yum install python311 python311-pip

# 或使用 dnf (较新版本)
sudo dnf install python3.11 python3.11-pip

# 验证安装
python3.11 --version
pip3.11 --version
```

### 2. 克隆项目

```bash
# 克隆项目仓库
git clone https://github.com/TauricResearch/TradingAgents.git

# 进入项目目录
cd TradingAgents

# 查看项目结构
ls -la
```

### 3. 创建虚拟环境

#### 使用 venv (推荐)
```bash
# Windows
python -m venv tradingagents
tradingagents\Scripts\activate

# macOS/Linux
python3 -m venv tradingagents
source tradingagents/bin/activate

# 验证虚拟环境
which python  # 应该指向虚拟环境中的 Python
```

#### 使用 conda
```bash
# 创建环境
conda create -n tradingagents python=3.11

# 激活环境
conda activate tradingagents

# 验证环境
conda info --envs
```

#### 使用 pipenv
```bash
# 安装 pipenv
pip install pipenv

# 创建环境并安装依赖
pipenv install

# 激活环境
pipenv shell
```

### 4. 安装依赖

#### 基础安装
```bash
# 升级 pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

# 验证安装
pip list | grep langchain
pip list | grep tradingagents
```

#### 开发环境安装
```bash
# 安装开发依赖 (如果有 requirements-dev.txt)
pip install -r requirements-dev.txt

# 或安装可编辑模式
pip install -e .

# 安装额外的开发工具
pip install pytest black flake8 mypy jupyter
```

#### 可选依赖
```bash
# Redis 支持 (用于高级缓存)
pip install redis

# 数据库支持
pip install sqlalchemy psycopg2-binary

# 可视化支持
pip install matplotlib seaborn plotly

# Jupyter 支持
pip install jupyter ipykernel
python -m ipykernel install --user --name=tradingagents
```

### 5. 配置 API 密钥

#### 获取 API 密钥

**OpenAI API**
1. 访问 [OpenAI Platform](https://platform.openai.com/)
2. 注册账户并登录
3. 导航到 API Keys 页面
4. 创建新的 API 密钥
5. 复制密钥 (注意: 只显示一次)

**FinnHub API**
1. 访问 [FinnHub](https://finnhub.io/)
2. 注册免费账户
3. 在仪表板中找到 API 密钥
4. 复制密钥

**其他可选 API**
- **Anthropic**: [console.anthropic.com](https://console.anthropic.com/)
- **Google AI**: [ai.google.dev](https://ai.google.dev/)

#### 设置环境变量

**Windows (PowerShell)**
```powershell
# 临时设置 (当前会话)
$env:OPENAI_API_KEY="your_openai_api_key"
$env:FINNHUB_API_KEY="your_finnhub_api_key"

# 永久设置 (系统环境变量)
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your_openai_api_key", "User")
[Environment]::SetEnvironmentVariable("FINNHUB_API_KEY", "your_finnhub_api_key", "User")
```

**Windows (Command Prompt)**
```cmd
# 临时设置
set OPENAI_API_KEY=your_openai_api_key
set FINNHUB_API_KEY=your_finnhub_api_key

# 永久设置 (需要重启)
setx OPENAI_API_KEY "your_openai_api_key"
setx FINNHUB_API_KEY "your_finnhub_api_key"
```

**macOS/Linux**
```bash
# 临时设置 (当前会话)
export OPENAI_API_KEY="your_openai_api_key"
export FINNHUB_API_KEY="your_finnhub_api_key"

# 永久设置 (添加到 ~/.bashrc 或 ~/.zshrc)
echo 'export OPENAI_API_KEY="your_openai_api_key"' >> ~/.bashrc
echo 'export FINNHUB_API_KEY="your_finnhub_api_key"' >> ~/.bashrc
source ~/.bashrc
```

#### 使用 .env 文件 (推荐)
```bash
# 创建 .env 文件
cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key
FINNHUB_API_KEY=your_finnhub_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
TRADINGAGENTS_RESULTS_DIR=./results
TRADINGAGENTS_LOG_LEVEL=INFO
EOF

# 安装 python-dotenv (如果未安装)
pip install python-dotenv
```

### 6. 验证安装

#### 基本验证
```bash
# 检查 Python 版本
python --version

# 检查已安装的包
pip list | grep -E "(langchain|tradingagents|openai|finnhub)"

# 检查环境变量
python -c "import os; print('OpenAI:', bool(os.getenv('OPENAI_API_KEY'))); print('FinnHub:', bool(os.getenv('FINNHUB_API_KEY')))"
```

#### 功能验证
```python
# test_installation.py
import sys
import os

def test_installation():
    """测试安装是否成功"""
    
    print("=== TradingAgents 安装验证 ===\n")
    
    # 1. Python 版本检查
    print(f"Python 版本: {sys.version}")
    if sys.version_info < (3, 10):
        print("❌ Python 版本过低，需要 3.10 或更高版本")
        return False
    else:
        print("✅ Python 版本符合要求")
    
    # 2. 依赖包检查
    required_packages = [
        'langchain_openai',
        'langgraph',
        'finnhub',
        'pandas',
        'requests'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} 已安装")
        except ImportError:
            print(f"❌ {package} 未安装")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n缺少依赖包: {missing_packages}")
        return False
    
    # 3. API 密钥检查
    api_keys = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'FINNHUB_API_KEY': os.getenv('FINNHUB_API_KEY')
    }
    
    for key_name, key_value in api_keys.items():
        if key_value:
            print(f"✅ {key_name} 已设置")
        else:
            print(f"❌ {key_name} 未设置")
    
    # 4. TradingAgents 导入测试
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        from tradingagents.default_config import DEFAULT_CONFIG
        print("✅ TradingAgents 核心模块导入成功")
    except ImportError as e:
        print(f"❌ TradingAgents 导入失败: {e}")
        return False
    
    print("\n🎉 安装验证完成!")
    return True

if __name__ == "__main__":
    success = test_installation()
    sys.exit(0 if success else 1)
```

运行验证脚本:
```bash
python test_installation.py
```

## 常见问题解决

### 1. Python 版本问题
```bash
# 问题: python 命令找不到或版本错误
# 解决方案:

# Windows: 使用 py 启动器
py -3.11 --version

# macOS/Linux: 使用具体版本
python3.11 --version

# 创建别名 (Linux/macOS)
alias python=python3.11
```

### 2. 权限问题
```bash
# 问题: pip 安装时权限被拒绝
# 解决方案:

# 使用用户安装
pip install --user -r requirements.txt

# 或使用虚拟环境 (推荐)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 3. 网络连接问题
```bash
# 问题: pip 安装超时或连接失败
# 解决方案:

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 或配置永久镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 4. 依赖冲突问题
```bash
# 问题: 包版本冲突
# 解决方案:

# 清理环境重新安装
pip freeze > installed_packages.txt
pip uninstall -r installed_packages.txt -y
pip install -r requirements.txt

# 或使用新的虚拟环境
deactivate
rm -rf tradingagents  # 删除旧环境
python -m venv tradingagents
source tradingagents/bin/activate
pip install -r requirements.txt
```

### 5. API 密钥问题
```bash
# 问题: API 密钥无效或未设置
# 解决方案:

# 检查密钥格式
echo $OPENAI_API_KEY | wc -c  # 应该是 51 字符 (sk-...)

# 重新设置密钥
unset OPENAI_API_KEY
export OPENAI_API_KEY="your_correct_api_key"

# 测试 API 连接
python -c "
import openai
import os
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
print('API 连接测试成功')
"
```

## 高级安装选项

### 1. Docker 安装
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["python", "-m", "cli.main"]
```

```bash
# 构建镜像
docker build -t tradingagents .

# 运行容器
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -e FINNHUB_API_KEY=$FINNHUB_API_KEY tradingagents
```

### 2. 开发环境设置
```bash
# 安装开发工具
pip install pre-commit black isort flake8 mypy pytest

# 设置 pre-commit hooks
pre-commit install

# 配置 IDE (VS Code)
code --install-extension ms-python.python
code --install-extension ms-python.black-formatter
```

### 3. 性能优化
```bash
# 安装加速库
pip install numpy scipy numba

# GPU 支持 (如果需要)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

## 卸载指南

### 完全卸载
```bash
# 停用虚拟环境
deactivate

# 删除虚拟环境
rm -rf tradingagents  # Linux/macOS
rmdir /s tradingagents  # Windows

# 删除项目文件
cd ..
rm -rf TradingAgents

# 清理环境变量 (可选)
unset OPENAI_API_KEY
unset FINNHUB_API_KEY
```

安装完成后，您可以继续阅读 [快速开始指南](quick-start.md) 来开始使用 TradingAgents。


<!-- docs/overview/project-overview.md -->

# TradingAgents 项目概述

## 项目简介

TradingAgents 是一个基于多智能体大语言模型（LLM）的金融交易框架，由 Tauric Research 开发并开源。本项目为中文增强版（v0.1.4），专为中国用户提供完整的A股支持、国产LLM集成和中文文档体系。

该项目模拟真实世界交易公司的运作模式，通过部署多个专业化的AI智能体来协作评估市场条件并做出交易决策。

## 项目背景

### 研究动机
传统的算法交易系统通常依赖单一的分析模型或策略，难以应对复杂多变的金融市场。而真实的交易公司通常采用团队协作的方式，由不同专业背景的分析师、研究员、交易员和风险管理人员共同参与决策过程。

TradingAgents 项目的核心理念是将这种人类专家团队的协作模式数字化，通过多个专业化的AI智能体来重现这种协作决策过程。

### 技术创新
- **多智能体协作**: 首次将多智能体系统应用于金融交易决策
- **专业化分工**: 每个智能体专注于特定的分析领域
- **结构化辩论**: 通过智能体间的辩论机制提高决策质量
- **动态风险管理**: 实时评估和调整投资风险

## 核心特性

### 1. 多维度市场分析
- **基本面分析**: 深入分析公司财务数据和基本面指标
- **技术分析**: 运用技术指标识别价格趋势和交易信号
- **新闻分析**: 实时监控和分析市场新闻及宏观事件
- **情绪分析**: 分析社交媒体和投资者情绪

### 2. 智能体协作机制
- **并行分析**: 多个分析师同时工作，提高效率
- **结构化辩论**: 看涨和看跌研究员进行观点交锋
- **共识形成**: 通过协商机制达成投资共识
- **风险评估**: 多层次风险管理和控制

### 3. 灵活的架构设计
- **模块化组件**: 易于扩展和定制
- **多LLM支持**: 🇨🇳 阿里百炼、Google AI、OpenAI、Anthropic等
- **统一配置**: 简化的.env配置系统，启用开关完全生效
- **智能降级**: 数据库不可用时自动使用文件缓存

### 4. 丰富的数据集成
- **🇨🇳 A股数据**: 通达信API实时行情和历史数据 ✅
- **美股数据**: FinnHub、Yahoo Finance实时数据 ✅
- **新闻数据**: Google News、财经新闻集成 ✅
- **社交数据**: Reddit情绪分析 ✅
- **数据库支持**: MongoDB + Redis + 智能缓存 ✅

### 5. 现代化Web界面 ✅ **v0.1.2新增**
- **Streamlit界面**: 直观的Web管理平台
- **实时进度**: 分析过程可视化跟踪
- **配置管理**: API密钥和系统配置管理
- **Token统计**: 实时成本追踪和优化建议
- **响应式设计**: 支持桌面和移动端访问

## 应用场景

### 1. 量化投资研究
- 策略开发和回测
- 因子挖掘和验证
- 风险模型构建
- 投资组合优化

### 2. 金融科技应用
- 智能投顾系统
- 风险管理平台
- 市场分析工具
- 交易决策支持

### 3. 学术研究
- 多智能体系统研究
- 金融AI应用研究
- 行为金融学研究
- 市场微观结构研究

### 4. 教育培训
- 金融分析教学
- 交易策略学习
- 风险管理培训
- AI应用示例

## 技术优势

### 1. 先进的AI技术
- **大语言模型**: 利用最新的LLM技术进行金融分析
- **多智能体系统**: 复杂的协作和决策机制
- **自然语言处理**: 高质量的文本分析和理解
- **机器学习**: 持续学习和优化能力

### 2. 专业的金融知识
- **全面的分析框架**: 覆盖基本面、技术面、消息面等多个维度
- **风险管理**: 完善的风险识别、评估和控制机制
- **市场理解**: 深入的金融市场知识和经验
- **实战导向**: 贴近真实交易环境的设计

### 3. 开放的生态系统
- **开源框架**: 完全开源，支持社区贡献
- **标准接口**: 易于集成和扩展
- **丰富文档**: 详细的技术文档和使用指南
- **活跃社区**: 持续的维护和改进

## 性能表现

### 1. 分析准确性
- 多维度分析提高预测准确性
- 智能体协作减少单点偏差
- 结构化辩论提升决策质量

### 2. 系统效率
- 并行处理提高分析速度
- 智能缓存减少重复计算
- 优化的数据流提升性能

### 3. 风险控制
- 多层次风险评估
- 实时风险监控
- 动态风险调整

## 发展路线图

### 短期目标 (3-6个月)
- 完善核心功能
- 优化性能表现
- 扩展数据源支持
- 增强用户体验

### 中期目标 (6-12个月)
- 支持更多资产类别
- 增加高级分析功能
- 开发可视化界面
- 构建插件生态

### 长期目标 (1-2年)
- 实现实盘交易支持
- 开发移动端应用
- 建立商业化模式
- 拓展国际市场

## 社区与生态

### 开源社区
- **GitHub**: 代码托管和协作开发
- **Discord**: 实时交流和技术支持
- **论坛**: 深度讨论和经验分享
- **文档**: 持续更新的技术文档

### 合作伙伴
- **学术机构**: 与高校和研究院所合作
- **金融机构**: 与银行、基金等机构合作
- **技术公司**: 与AI和金融科技公司合作
- **数据提供商**: 与数据供应商建立合作

### 贡献方式
- **代码贡献**: 提交代码改进和新功能
- **文档完善**: 改进文档和教程
- **问题反馈**: 报告bug和提出建议
- **社区建设**: 参与讨论和帮助他人

## 免责声明

TradingAgents 框架仅用于研究和教育目的。交易表现可能因多种因素而异，包括所选择的骨干语言模型、模型温度、交易周期、数据质量和其他非确定性因素。

**本框架不构成财务、投资或交易建议。** 用户在使用本框架进行任何投资决策时，应当谨慎评估风险，并咨询专业的财务顾问。

## 联系我们

- **官方网站**: [https://tauric.ai](https://tauric.ai)
- **GitHub**: [https://github.com/TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- **Discord**: [TradingResearch](https://discord.com/invite/hk9PGKShPK)
- **Twitter**: [@TauricResearch](https://x.com/TauricResearch)
- **邮箱**: contact@tauric.ai

TradingAgents 代表了金融AI技术的前沿探索，我们期待与全球的研究者、开发者和金融专家一起，推动这一领域的发展和创新。


<!-- docs/overview/quick-start.md -->

# 快速开始指南

## 概述

本指南将帮助您快速上手 TradingAgents 框架，从安装到运行第一个交易分析，只需几分钟时间。

## 前置要求

### 系统要求
- **操作系统**: Windows 10+, macOS 10.15+, 或 Linux
- **Python**: 3.10 或更高版本
- **内存**: 至少 4GB RAM (推荐 8GB+)
- **存储**: 至少 2GB 可用空间

### API 密钥
在开始之前，您需要获取以下API密钥：

1. **🇨🇳 阿里百炼 API Key** (推荐)
   - 访问 [阿里云百炼平台](https://dashscope.aliyun.com/)
   - 注册账户并获取API密钥
   - 国产模型，无需科学上网，响应速度快

2. **FinnHub API Key** (必需)
   - 访问 [FinnHub](https://finnhub.io/)
   - 注册免费账户并获取API密钥

3. **Google AI API Key** (推荐)
   - 访问 [Google AI Studio](https://aistudio.google.com/)
   - 获取免费API密钥，支持Gemini模型

4. **其他API密钥** (可选)
   - OpenAI API (需要科学上网)
   - Anthropic API (需要科学上网)

## 快速安装

### 1. 克隆项目
```bash
# 克隆中文增强版
git clone https://github.com/hsliuping/TradingAgents-CN.git
cd TradingAgents-CN
```

### 2. 创建虚拟环境
```bash
# 使用 conda
conda create -n tradingagents python=3.13
conda activate tradingagents

# 或使用 venv
python -m venv tradingagents
source tradingagents/bin/activate  # Linux/macOS
# tradingagents\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

创建 `.env` 文件（推荐方式）：
```bash
# 复制配置模板
cp .env.example .env

# 编辑 .env 文件，配置以下API密钥：

# 🇨🇳 阿里百炼 (推荐)
DASHSCOPE_API_KEY=your_dashscope_api_key_here

# FinnHub (必需)
FINNHUB_API_KEY=your_finnhub_api_key_here

# Google AI (可选)
GOOGLE_API_KEY=your_google_api_key_here

# 数据库配置 (可选，默认禁用)
MONGODB_ENABLED=false
REDIS_ENABLED=false
```

## 第一次运行

### 🌐 使用Web界面 (推荐)

最简单的开始方式是使用Web管理界面：

```bash
# 启动Web界面
streamlit run web/app.py
```

然后在浏览器中访问 `http://localhost:8501`

Web界面提供：
1. 🎛️ 直观的股票分析界面
2. ⚙️ API密钥和配置管理
3. 📊 实时分析进度显示
4. 💰 Token使用统计
5. 🇨🇳 完整的中文界面

### 使用命令行界面 (CLI)

如果您偏好命令行：

```bash
python -m cli.main
```

### 使用 Python API

创建一个简单的Python脚本：

```python
# quick_start.py
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 创建配置
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4o-mini"  # 使用较便宜的模型进行测试
config["quick_think_llm"] = "gpt-4o-mini"
config["max_debate_rounds"] = 1  # 减少辩论轮次以节省成本
config["online_tools"] = True  # 使用在线数据

# 初始化交易智能体图
ta = TradingAgentsGraph(debug=True, config=config)

# 执行分析
print("开始分析 AAPL...")
state, decision = ta.propagate("AAPL", "2024-01-15")

# 输出结果
print("\n=== 分析结果 ===")
print(f"推荐动作: {decision.get('action', 'hold')}")
print(f"置信度: {decision.get('confidence', 0.5):.2f}")
print(f"风险评分: {decision.get('risk_score', 0.5):.2f}")
print(f"推理过程: {decision.get('reasoning', 'N/A')}")
```

运行脚本：
```bash
python quick_start.py
```

## 配置选项

### 基本配置
```python
config = {
    # LLM 设置
    "llm_provider": "openai",           # 或 "anthropic", "google"
    "deep_think_llm": "gpt-4o-mini",    # 深度思考模型
    "quick_think_llm": "gpt-4o-mini",   # 快速思考模型
    
    # 辩论设置
    "max_debate_rounds": 1,             # 辩论轮次 (1-5)
    "max_risk_discuss_rounds": 1,       # 风险讨论轮次
    
    # 数据设置
    "online_tools": True,               # 使用在线数据
}
```

### 智能体选择
```python
# 选择要使用的分析师
selected_analysts = [
    "market",        # 技术分析师
    "fundamentals",  # 基本面分析师
    "news",         # 新闻分析师
    "social"        # 社交媒体分析师
]

ta = TradingAgentsGraph(
    selected_analysts=selected_analysts,
    debug=True,
    config=config
)
```

## 示例分析流程

### 完整的分析示例
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
import json

def analyze_stock(symbol, date):
    """分析指定股票"""
    
    # 配置
    config = DEFAULT_CONFIG.copy()
    config["deep_think_llm"] = "gpt-4o-mini"
    config["quick_think_llm"] = "gpt-4o-mini"
    config["max_debate_rounds"] = 2
    config["online_tools"] = True
    
    # 创建分析器
    ta = TradingAgentsGraph(
        selected_analysts=["market", "fundamentals", "news", "social"],
        debug=True,
        config=config
    )
    
    print(f"正在分析 {symbol} ({date})...")
    
    try:
        # 执行分析
        state, decision = ta.propagate(symbol, date)
        
        # 输出详细结果
        print("\n" + "="*50)
        print(f"股票: {symbol}")
        print(f"日期: {date}")
        print("="*50)
        
        print(f"\n📊 最终决策:")
        print(f"  动作: {decision.get('action', 'hold').upper()}")
        print(f"  数量: {decision.get('quantity', 0)}")
        print(f"  置信度: {decision.get('confidence', 0.5):.1%}")
        print(f"  风险评分: {decision.get('risk_score', 0.5):.1%}")
        
        print(f"\n💭 推理过程:")
        print(f"  {decision.get('reasoning', 'N/A')}")
        
        # 分析师报告摘要
        if hasattr(state, 'analyst_reports'):
            print(f"\n📈 分析师报告摘要:")
            for analyst, report in state.analyst_reports.items():
                score = report.get('overall_score', report.get('score', 0.5))
                print(f"  {analyst}: {score:.1%}")
        
        return decision
        
    except Exception as e:
        print(f"❌ 分析失败: {e}")
        return None

# 运行示例
if __name__ == "__main__":
    # 分析苹果公司股票
    result = analyze_stock("AAPL", "2024-01-15")
    
    if result:
        print("\n✅ 分析完成!")
    else:
        print("\n❌ 分析失败!")
```

## 常见问题解决

### 1. API 密钥错误
```
错误: OpenAI API key not found
解决: 确保正确设置了 OPENAI_API_KEY 环境变量
```

### 2. 网络连接问题
```
错误: Connection timeout
解决: 检查网络连接，或使用代理设置
```

### 3. 内存不足
```
错误: Out of memory
解决: 减少 max_debate_rounds 或使用更小的模型
```

### 4. 数据获取失败
```
错误: Failed to fetch data
解决: 检查 FINNHUB_API_KEY 是否正确，或稍后重试
```

## 成本控制建议

### 1. 使用较小的模型
```python
config["deep_think_llm"] = "gpt-4o-mini"    # 而不是 "gpt-4o"
config["quick_think_llm"] = "gpt-4o-mini"   # 而不是 "gpt-4o"
```

### 2. 减少辩论轮次
```python
config["max_debate_rounds"] = 1              # 而不是 3-5
config["max_risk_discuss_rounds"] = 1        # 而不是 2-3
```

### 3. 选择性使用分析师
```python
# 只使用核心分析师
selected_analysts = ["market", "fundamentals"]  # 而不是全部四个
```

### 4. 使用缓存数据
```python
config["online_tools"] = False  # 使用缓存数据而不是实时数据
```

## 下一步

现在您已经成功运行了第一个分析，可以：

1. **探索更多功能**: 查看 [API参考文档](../api/core-api.md)
2. **自定义配置**: 阅读 [配置指南](../configuration/config-guide.md)
3. **开发自定义智能体**: 参考 [扩展开发指南](../development/extending.md)
4. **查看更多示例**: 浏览 [示例和教程](../examples/basic-examples.md)

## 获取帮助

如果遇到问题，可以：
- 查看 [常见问题](../faq/faq.md)
- 访问 [GitHub Issues](https://github.com/TauricResearch/TradingAgents/issues)
- 加入 [Discord 社区](https://discord.com/invite/hk9PGKShPK)
- 查看 [故障排除指南](../faq/troubleshooting.md)

祝您使用愉快！🚀


<!-- docs/research-depth-guide.md -->

# 研究深度配置指南

## 📊 研究深度级别说明

TradingAgents-CN 提供5个研究深度级别，每个级别在分析质量、耗时和资源消耗方面有不同的平衡。

### 🚀 1级 - 快速分析
**适用场景**: 日常快速决策、市场概览

**配置特点**:
- ⚡ **辩论轮次**: 1轮 (最少)
- 🧠 **模型选择**: qwen-turbo + qwen-plus (最快)
- 💾 **记忆功能**: 禁用 (加速)
- 🌐 **在线工具**: 禁用 (使用缓存数据)
- ⏱️ **预期耗时**: 2-4分钟
- 💰 **成本**: 最低

**优点**:
- 速度最快
- 成本最低
- 适合频繁查询

**缺点**:
- 分析深度有限
- 可能错过细节信息

---

### 📈 2级 - 基础分析
**适用场景**: 常规投资决策、基础研究

**配置特点**:
- ⚡ **辩论轮次**: 1轮
- 🧠 **模型选择**: qwen-plus + qwen-plus (平衡)
- 💾 **记忆功能**: 启用
- 🌐 **在线工具**: 启用 (获取最新数据)
- ⏱️ **预期耗时**: 4-6分钟
- 💰 **成本**: 较低

**优点**:
- 速度较快
- 包含最新数据
- 成本可控

**缺点**:
- 辩论深度有限

---

### 🎯 3级 - 标准分析 (默认推荐)
**适用场景**: 重要投资决策、标准研究流程

**配置特点**:
- ⚡ **辩论轮次**: 1轮 (研究员) + 2轮 (风险评估)
- 🧠 **模型选择**: qwen-plus + qwen-max (质量优先)
- 💾 **记忆功能**: 启用
- 🌐 **在线工具**: 启用
- ⏱️ **预期耗时**: 6-10分钟
- 💰 **成本**: 中等

**优点**:
- 平衡速度和质量
- 风险评估更深入
- 适合大多数场景

**缺点**:
- 耗时适中

---

### 🔬 4级 - 深度分析
**适用场景**: 重大投资决策、详细研究报告

**配置特点**:
- ⚡ **辩论轮次**: 2轮 (研究员) + 2轮 (风险评估)
- 🧠 **模型选择**: qwen-plus + qwen-max (高质量)
- 💾 **记忆功能**: 启用
- 🌐 **在线工具**: 启用
- ⏱️ **预期耗时**: 10-15分钟
- 💰 **成本**: 较高

**优点**:
- 分析深度高
- 多轮辩论确保全面性
- 适合重要决策

**缺点**:
- 耗时较长
- 成本较高

---

### 🏆 5级 - 全面分析
**适用场景**: 最重要的投资决策、完整研究报告

**配置特点**:
- ⚡ **辩论轮次**: 3轮 (研究员) + 3轮 (风险评估)
- 🧠 **模型选择**: qwen-max + qwen-max (最高质量)
- 💾 **记忆功能**: 启用
- 🌐 **在线工具**: 启用
- ⏱️ **预期耗时**: 15-25分钟
- 💰 **成本**: 最高

**优点**:
- 最全面的分析
- 最高质量的推理
- 最可靠的结果

**缺点**:
- 耗时最长
- 成本最高

## 📋 选择建议

### 🎯 根据使用场景选择

| 场景 | 推荐级别 | 理由 |
|------|----------|------|
| 日常市场监控 | 1-2级 | 快速获取市场概况 |
| 常规投资决策 | 2-3级 | 平衡速度和质量 |
| 重要投资决策 | 3-4级 | 确保分析质量 |
| 重大资金投入 | 4-5级 | 最全面的风险评估 |
| 研究报告撰写 | 4-5级 | 需要详细的分析内容 |

### ⏰ 根据时间预算选择

| 可用时间 | 推荐级别 | 预期结果 |
|----------|----------|----------|
| 2-5分钟 | 1-2级 | 快速决策参考 |
| 5-10分钟 | 2-3级 | 标准投资建议 |
| 10-15分钟 | 3-4级 | 深度分析报告 |
| 15分钟以上 | 4-5级 | 最全面的研究 |

### 💰 根据成本考虑选择

| 预算考虑 | 推荐级别 | 成本效益 |
|----------|----------|----------|
| 成本敏感 | 1-2级 | 最经济的选择 |
| 平衡考虑 | 2-3级 | 性价比最高 |
| 质量优先 | 3-4级 | 高质量分析 |
| 不计成本 | 4-5级 | 最佳质量 |

## 🔧 技术细节

### 辩论轮次影响
- **1轮**: 基础观点交换
- **2轮**: 深入讨论和反驳
- **3轮**: 全面辩论和共识

### 模型选择影响
- **qwen-turbo**: 速度最快，适合快速分析
- **qwen-plus**: 平衡速度和质量
- **qwen-max**: 最高质量，适合深度分析

### 记忆功能影响
- **启用**: 从历史决策中学习，提高准确性
- **禁用**: 加快分析速度，降低成本

### 在线工具影响
- **启用**: 获取最新市场数据
- **禁用**: 使用缓存数据，加快速度

## 💡 最佳实践

1. **首次使用**: 建议从3级开始，了解系统能力
2. **日常监控**: 使用1-2级进行快速扫描
3. **重要决策**: 使用3-4级确保质量
4. **关键投资**: 使用4-5级获得最全面分析
5. **成本控制**: 根据投资金额调整分析级别

## 🎯 总结

研究深度级别是控制分析质量、速度和成本的核心参数。选择合适的级别可以：

- ✅ 优化分析时间
- ✅ 控制使用成本  
- ✅ 获得适当的分析深度
- ✅ 满足不同场景需求

建议根据具体的投资场景、时间预算和质量要求来选择最适合的研究深度级别。


<!-- docs/security/api_keys_security.md -->

# API密钥安全指南

## 🚨 重要安全提醒

### ⚠️ 绝对不要做的事情

1. **不要将.env文件提交到Git仓库**
   - .env文件包含敏感的API密钥
   - 一旦提交到公开仓库，密钥可能被恶意使用
   - 即使删除提交，Git历史中仍然存在

2. **不要在代码中硬编码API密钥**
   ```python
   # ❌ 错误做法
   api_key = "sk-1234567890abcdef"
   
   # ✅ 正确做法
   api_key = os.getenv("DASHSCOPE_API_KEY")
   ```

3. **不要在日志中输出完整的API密钥**
   ```python
   # ❌ 错误做法
   print(f"Using API key: {api_key}")
   
   # ✅ 正确做法
   print(f"Using API key: {api_key[:12]}...")
   ```

### ✅ 安全最佳实践

#### 1. 使用环境变量
```bash
# 在.env文件中配置
DASHSCOPE_API_KEY=your_real_api_key_here
FINNHUB_API_KEY=your_real_finnhub_key_here
```

#### 2. 正确的文件权限
```bash
# 设置.env文件只有所有者可读写
chmod 600 .env
```

#### 3. 使用.gitignore
确保.gitignore包含：
```
.env
.env.local
.env.*.local
```

#### 4. 定期轮换API密钥
- 定期更换API密钥
- 如果怀疑密钥泄露，立即更换
- 监控API使用情况，发现异常立即处理

## 🔧 配置步骤

### 1. 复制示例文件
```bash
cp .env.example .env
```

### 2. 编辑.env文件
```bash
# 使用您喜欢的编辑器
notepad .env        # Windows
nano .env           # Linux/Mac
code .env           # VS Code
```

### 3. 填入真实API密钥
```bash
# 阿里百炼API密钥 (推荐)
DASHSCOPE_API_KEY=sk-your-real-dashscope-key

# 金融数据API密钥 (必需)
FINNHUB_API_KEY=your-real-finnhub-key
```

### 4. 验证配置
```bash
python -m cli.main config
```

## 🔍 API密钥获取指南

### 阿里百炼 (推荐)
1. 访问 https://dashscope.aliyun.com/
2. 注册/登录阿里云账号
3. 开通百炼服务
4. 在控制台获取API密钥

### FinnHub (必需)
1. 访问 https://finnhub.io/
2. 注册免费账号
3. 在Dashboard获取API密钥
4. 免费账户每分钟60次请求

### OpenAI (可选)
1. 访问 https://platform.openai.com/
2. 注册账号并充值
3. 在API Keys页面创建密钥

## 🚨 如果API密钥泄露了怎么办？

### 立即行动
1. **立即撤销泄露的API密钥**
   - 登录对应的API提供商控制台
   - 删除或禁用泄露的密钥

2. **生成新的API密钥**
   - 创建新的API密钥
   - 更新.env文件中的配置

3. **检查使用记录**
   - 查看API使用日志
   - 确认是否有异常使用

4. **更新代码配置**
   - 更新本地.env文件
   - 通知团队成员更新配置

### 预防措施
1. **使用Git hooks**
   - 设置pre-commit hooks检查敏感文件
   - 防止意外提交.env文件

2. **定期审计**
   - 定期检查Git历史
   - 确保没有敏感信息泄露

3. **团队培训**
   - 培训团队成员安全意识
   - 建立安全操作规范

## 📋 安全检查清单

- [ ] .env文件已添加到.gitignore
- [ ] 没有在代码中硬编码API密钥
- [ ] .env文件权限设置正确 (600)
- [ ] 定期轮换API密钥
- [ ] 监控API使用情况
- [ ] 团队成员了解安全规范
- [ ] 设置了pre-commit hooks (可选)

## 🔗 相关资源

- [Git安全最佳实践](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)
- [环境变量安全指南](https://12factor.net/config)
- [API密钥管理最佳实践](https://owasp.org/www-project-api-security/)

---

**记住：安全无小事，API密钥保护是每个开发者的责任！** 🔐


<!-- docs/troubleshooting/finnhub-news-data-setup.md -->

# Finnhub新闻数据配置指南

## 问题描述

如果您遇到以下错误信息：

```
[DEBUG] FinnhubNewsTool调用，股票代码: AAPL 
获取新闻数据失败: [Errno 2] No such file or directory: '/Users/yluo/Documents/Code/ScAI/FR1-data\\finnhub_data\\news_data\\AAPL_data_formatted.json'
```

这表明存在以下问题：
1. **路径配置错误**：混合了Unix和Windows路径分隔符
2. **数据文件不存在**：缺少Finnhub新闻数据文件
3. **数据目录配置**：数据目录路径不正确

## 解决方案

### 1. 路径修复（已自动修复）

我们已经修复了 `tradingagents/default_config.py` 中的路径配置：

```python
# 修复前（硬编码Unix路径）
"data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",

# 修复后（跨平台兼容路径）
"data_dir": os.path.join(os.path.expanduser("~"), "Documents", "TradingAgents", "data"),
```

### 2. 数据目录结构

正确的数据目录结构应该是：

```
~/Documents/TradingAgents/data/
├── finnhub_data/
│   ├── news_data/
│   │   ├── AAPL_data_formatted.json
│   │   ├── TSLA_data_formatted.json
│   │   └── ...
│   ├── insider_senti/
│   ├── insider_trans/
│   └── ...
└── other_data/
```

### 3. 获取Finnhub数据

#### 方法一：使用API下载（推荐）

1. **配置Finnhub API密钥**
   ```bash
   # 在.env文件中添加
   FINNHUB_API_KEY=your_finnhub_api_key_here
   ```

2. **运行数据下载脚本**
   ```bash
   # 下载新闻数据
   python scripts/download_finnhub_data.py --data-type news --symbols AAPL,TSLA,MSFT
   
   # 或者下载所有数据
   python scripts/download_finnhub_data.py --all
   ```

#### 方法二：手动创建测试数据

如果您只是想测试功能，可以创建示例数据：

```bash
# 运行测试脚本，会自动创建示例数据
python tests/test_finnhub_news_fix.py
```

### 4. 验证配置

运行以下命令验证配置是否正确：

```bash
# 验证路径修复
python tests/test_finnhub_news_fix.py

# 测试新闻数据获取
python -c "
from tradingagents.dataflows.interface import get_finnhub_news
result = get_finnhub_news('AAPL', '2025-01-02', 7)
print(result[:200])
"
```

## 错误处理改进

我们已经改进了错误处理，现在当数据文件不存在时，会显示详细的错误信息：

```
⚠️ 无法获取AAPL的新闻数据 (2024-12-26 到 2025-01-02)
可能的原因：
1. 数据文件不存在或路径配置错误
2. 指定日期范围内没有新闻数据
3. 需要先下载或更新Finnhub新闻数据
建议：检查数据目录配置或重新获取新闻数据
```

## 配置选项

### 自定义数据目录

如果您想使用自定义数据目录，可以在代码中设置：

```python
from tradingagents.dataflows.config import set_config

# 设置自定义数据目录
config = {
    "data_dir": "C:/your/custom/data/directory"
}
set_config(config)
```

### 环境变量配置

您也可以通过环境变量设置：

```bash
# Windows
set TRADINGAGENTS_DATA_DIR=C:\your\custom\data\directory

# Linux/Mac
export TRADINGAGENTS_DATA_DIR=/your/custom/data/directory
```

## 常见问题

### Q1: 数据目录权限问题

**问题**：无法创建或写入数据目录

**解决方案**：
```bash
# Windows（以管理员身份运行）
mkdir "C:\Users\%USERNAME%\Documents\TradingAgents\data"

# Linux/Mac
mkdir -p ~/Documents/TradingAgents/data
chmod 755 ~/Documents/TradingAgents/data
```

### Q2: Finnhub API配额限制

**问题**：API调用次数超限

**解决方案**：
1. 升级Finnhub API计划
2. 使用缓存减少API调用
3. 限制数据获取频率

### Q3: 数据格式错误

**问题**：JSON文件格式不正确

**解决方案**：
```bash
# 验证JSON格式
python -c "import json; print(json.load(open('path/to/file.json')))"

# 重新下载数据
python scripts/download_finnhub_data.py --force-refresh
```

## 技术细节

### 修复的文件

1. **`tradingagents/default_config.py`**
   - 修复硬编码的Unix路径
   - 使用跨平台兼容的路径构建

2. **`tradingagents/dataflows/finnhub_utils.py`**
   - 添加文件存在性检查
   - 改进错误处理和调试信息
   - 使用UTF-8编码读取文件

3. **`tradingagents/dataflows/interface.py`**
   - 改进get_finnhub_news函数的错误提示
   - 提供详细的故障排除建议

### 路径处理逻辑

```python
# 跨平台路径构建
data_path = os.path.join(
    data_dir, 
    "finnhub_data", 
    "news_data", 
    f"{ticker}_data_formatted.json"
)

# 文件存在性检查
if not os.path.exists(data_path):
    print(f"⚠️ [DEBUG] 数据文件不存在: {data_path}")
    return {}
```

## 联系支持

如果您仍然遇到问题，请：

1. 运行诊断脚本：`python tests/test_finnhub_news_fix.py`
2. 检查日志输出中的详细错误信息
3. 确认Finnhub API密钥配置正确
4. 提供完整的错误堆栈信息

---

**更新日期**：2025-01-02  
**版本**：v1.0  
**适用范围**：TradingAgents-CN v0.1.3+

<!-- docs/troubleshooting/streamlit-file-watcher-fix.md -->

# Streamlit文件监控错误解决方案

## 问题描述

在运行Streamlit Web应用时，可能会遇到以下错误：

```
Exception in thread Thread-9:
Traceback (most recent call last):
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "C:\code\TradingAgentsCN\env\lib\site-packages\watchdog\observers\api.py", line 213, in run
    self.dispatch_events(self.event_queue)
  ...
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'C:\\code\\TradingAgentsCN\\web\\pages\\__pycache__\\config_management.cpython-310.pyc.2375409084592'
```

## 问题原因

这个错误是由Streamlit的文件监控系统（watchdog）引起的：

1. **Python字节码文件生成**：当Python运行时，会在`__pycache__`目录中生成`.pyc`字节码文件
2. **临时文件命名**：Python有时会创建带有随机后缀的临时字节码文件
3. **文件监控冲突**：Streamlit的watchdog监控器会尝试监控这些临时文件
4. **文件删除竞争**：当Python删除或重命名这些临时文件时，watchdog仍在尝试访问它们
5. **FileNotFoundError**：导致文件未找到错误

## 解决方案

### 方案1：Streamlit配置文件（推荐）

我们已经创建了`.streamlit/config.toml`配置文件来解决这个问题：

```toml
[server.fileWatcher]
# 禁用对临时文件和缓存文件的监控
watcherType = "auto"
# 排除__pycache__目录和.pyc文件
excludePatterns = [
    "**/__pycache__/**",
    "**/*.pyc",
    "**/*.pyo",
    "**/*.pyd",
    "**/.git/**",
    "**/node_modules/**",
    "**/.env",
    "**/venv/**",
    "**/env/**"
]
```

### 方案2：清理缓存文件

定期清理Python缓存文件：

```bash
# Windows PowerShell
Get-ChildItem -Path . -Recurse -Name "__pycache__" | Remove-Item -Recurse -Force

# Linux/macOS
find . -type d -name "__pycache__" -exec rm -rf {} +
```

### 方案3：环境变量设置

设置环境变量禁用Python字节码生成：

```bash
# 在.env文件中添加
PYTHONDONTWRITEBYTECODE=1
```

或在启动脚本中：

```python
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
```

## 验证解决方案

1. **重启Streamlit应用**：
   ```bash
   python web/run_web.py
   ```

2. **检查配置生效**：
   - 确认`.streamlit/config.toml`文件存在
   - 观察是否还有文件监控错误

3. **监控日志**：
   - 查看控制台输出
   - 确认没有FileNotFoundError

## 预防措施

1. **保持.gitignore更新**：确保`__pycache__/`和`*.pyc`在.gitignore中
2. **定期清理**：定期清理开发环境中的缓存文件
3. **配置监控**：使用Streamlit配置文件排除不必要的文件监控
4. **环境隔离**：使用虚拟环境避免全局Python环境污染

## 相关文档

- [Streamlit配置文档](https://docs.streamlit.io/library/advanced-features/configuration)
- [Python字节码文件说明](https://docs.python.org/3/tutorial/modules.html#compiled-python-files)
- [Watchdog文件监控库](https://python-watchdog.readthedocs.io/)

## 常见问题

**Q: 为什么会生成这些临时文件？**
A: Python在编译模块时会创建字节码文件以提高加载速度，有时会使用临时文件名避免冲突。

**Q: 这个错误会影响应用功能吗？**
A: 通常不会影响核心功能，但会在控制台产生错误日志，影响开发体验。

**Q: 可以完全禁用文件监控吗？**
A: 不建议，文件监控用于热重载功能。建议使用排除模式而不是完全禁用。

## 更新日志

- **2025-01-03**: 创建解决方案文档
- **2025-01-03**: 添加Streamlit配置文件
- **2025-01-03**: 更新.gitignore规则

<!-- docs/usage/investment_analysis_guide.md -->

# TradingAgents-CN 投资分析使用指南

## 🎯 概述

TradingAgents-CN 是一个基于多智能体大语言模型的投资分析框架，能够为您提供专业的股票分析报告。

## 🚀 快速开始

### 1. 基础配置

确保您已经配置了必要的API密钥：

```bash
# 检查配置状态
python -m cli.main config

# 运行集成测试
python -m cli.main test
```

### 2. 使用方式选择

#### 🌐 Web界面 (推荐新手)
```bash
# 启动Web界面
python -m streamlit run web/app.py
```
然后在浏览器中访问 `http://localhost:8501`

**优点**:
- 直观易用的图形界面
- 实时进度显示
- 详细的配置选项
- 结果可视化展示

**详细使用说明**: 请参考 [Web界面使用指南](web-interface-guide.md)

#### 💻 命令行界面 (适合开发者)
```bash
# 中文优化版本（推荐）
python examples/dashscope/demo_dashscope_chinese.py

# 完整功能版本
python examples/dashscope/demo_dashscope.py

# 简化测试版本
python examples/dashscope/demo_dashscope_simple.py
```

**优点**:
- 快速执行
- 易于自动化
- 适合批量处理

## 📊 分析内容详解

### 技术面分析
- **价格趋势**: 短期、中期、长期趋势判断
- **技术指标**: MA、MACD、RSI、布林带等
- **支撑阻力**: 关键价位和交易区间
- **成交量**: 量价关系分析

### 基本面分析
- **财务状况**: 营收、利润、现金流分析
- **业务结构**: 各业务板块表现
- **市场地位**: 竞争优势和市场份额
- **增长前景**: 未来发展机会

### 市场情绪分析
- **投资者情绪**: 市场参与者态度
- **分析师评级**: 专业机构观点
- **机构持仓**: 大资金动向
- **热点关注**: 市场焦点话题

### 风险评估
- **宏观风险**: 经济环境影响
- **行业风险**: 竞争和周期性风险
- **公司风险**: 特定经营风险
- **监管风险**: 政策变化影响

### 投资建议
- **评级建议**: 买入/持有/卖出
- **目标价位**: 短期和长期目标
- **时间框架**: 投资周期建议
- **风险控制**: 止损和仓位管理

## 🛠️ 自定义分析

### 修改分析参数

您可以通过修改示例程序来自定义分析：

```python
# 在 demo_dashscope_chinese.py 中修改
STOCK_SYMBOL = "TSLA"  # 改为您想分析的股票
ANALYSIS_DATE = "2024-06-26"  # 修改分析日期
```

### 支持的股票代码

- **美股**: AAPL, TSLA, MSFT, GOOGL, AMZN, NVDA 等
- **指数**: SPY, QQQ, DIA 等ETF
- **其他**: 大部分在美国交易所上市的股票

## 🎯 使用技巧

### 1. 选择合适的模型

```python
# 在配置中选择不同的模型
"deep_think_llm": "qwen-max",     # 最高质量，适合深度分析
"quick_think_llm": "qwen-plus",   # 平衡性能，日常使用
# "qwen-turbo" 适合快速查询
```

### 2. 分析不同时间段

```python
# 修改分析日期来分析历史表现
ANALYSIS_DATE = "2024-01-01"  # 年初分析
ANALYSIS_DATE = "2024-06-01"  # 半年度分析
```

### 3. 关注特定方面

您可以在提示词中强调特定分析方向：
- 技术面分析
- 基本面分析
- 风险评估
- 行业比较

## ⚠️ 重要提醒

### 投资风险提示

1. **仅供参考**: 分析结果仅供参考，不构成投资建议
2. **风险自担**: 投资有风险，决策需谨慎
3. **多方验证**: 建议结合其他信息源进行验证
4. **专业咨询**: 重大投资决策建议咨询专业财务顾问

### 数据准确性

1. **实时性**: 数据可能存在延迟，请以实际市场数据为准
2. **完整性**: AI分析可能遗漏某些重要信息
3. **准确性**: 预测和建议存在不确定性

## 🔧 故障排除

### 常见问题

1. **API密钥错误**: 检查.env文件中的密钥配置
2. **网络连接**: 确保网络连接正常
3. **模型响应慢**: 可以尝试使用qwen-turbo模型

### 获取帮助

```bash
# 查看帮助信息
python -m cli.main help

# 查看示例程序
python -m cli.main examples
```

## 📈 高级用法

### 批量分析

您可以修改程序来分析多只股票：

```python
stocks = ["AAPL", "MSFT", "GOOGL", "TSLA"]
for stock in stocks:
    # 运行分析逻辑
    analyze_stock(stock)
```

### 定期分析

设置定时任务来定期生成分析报告：

```bash
# 使用cron或Windows任务计划程序
# 每日运行分析
0 9 * * * python examples/dashscope/demo_dashscope_chinese.py
```

## 🎓 学习资源

### 推荐阅读

1. **技术分析**: 学习技术指标的含义和应用
2. **基本面分析**: 了解财务报表分析方法
3. **风险管理**: 掌握投资风险控制技巧
4. **市场心理**: 理解市场情绪和行为金融学

### 实践建议

1. **模拟交易**: 先用模拟账户练习
2. **小额试验**: 从小额投资开始
3. **持续学习**: 不断提升投资知识和技能
4. **记录总结**: 记录投资决策和结果，总结经验

---

*免责声明: 本工具仅用于教育和研究目的，不构成投资建议。投资有风险，决策需谨慎。*


<!-- docs/usage/web-interface-guide.md -->

# TradingAgents-CN Web界面使用指南 (v0.1.4)

## 🌐 概述

TradingAgents-CN 提供了直观易用的Web界面，让您可以通过浏览器轻松进行股票投资分析。v0.1.4版本新增了配置管理、Token统计等功能，本指南将详细介绍Web界面的各项功能和配置选项。

## ✨ v0.1.4 新增功能

- 🎛️ **配置管理**: API密钥管理、模型选择、系统配置
- 💰 **Token统计**: 实时Token使用统计和成本追踪
- 💾 **缓存管理**: 数据缓存状态监控和管理
- 🇨🇳 **A股支持**: 完整的A股股票分析功能

## 🚀 启动Web界面

### 1. 启动命令
```bash
# 启动Web界面
python -m streamlit run web/app.py

# 或者使用简化命令
streamlit run web/app.py
```

### 2. 访问地址
启动后，在浏览器中访问：`http://localhost:8501`

## 📊 界面功能详解

### 分析配置区域

#### 基本设置
- **股票代码**: 输入要分析的股票代码
  - 🇺🇸 **美股**: AAPL, TSLA, NVDA, MSFT
  - 🇨🇳 **A股**: 000001, 600036, 000002, 600519
- **分析日期**: 选择分析的基准日期
- **研究深度**: 选择分析的详细程度（1-5级）

#### 🎯 研究深度详细说明

研究深度是控制分析质量、速度和成本的核心参数。不同级别的具体配置如下：

##### 🚀 1级 - 快速分析 (2-4分钟)
**适用场景**: 日常快速决策、市场概览

**技术配置**:
- **辩论轮次**: 1轮 (最少)
- **AI模型**: qwen-turbo + qwen-plus (最快)
- **记忆功能**: ❌ 禁用 (加速)
- **在线工具**: ❌ 禁用 (使用缓存数据)

**特点**:
- ✅ 速度最快、成本最低
- ✅ 适合频繁查询
- ❌ 分析深度有限
- ❌ 可能错过细节信息

##### 📈 2级 - 基础分析 (4-6分钟)
**适用场景**: 常规投资决策、基础研究

**技术配置**:
- **辩论轮次**: 1轮
- **AI模型**: qwen-plus + qwen-plus (平衡)
- **记忆功能**: ✅ 启用
- **在线工具**: ✅ 启用 (获取最新数据)

**特点**:
- ✅ 速度较快、包含最新数据
- ✅ 成本可控
- ❌ 辩论深度有限

##### 🎯 3级 - 标准分析 (6-10分钟) **[默认推荐]**
**适用场景**: 重要投资决策、标准研究流程

**技术配置**:
- **辩论轮次**: 1轮 (研究员) + 2轮 (风险评估)
- **AI模型**: qwen-plus + qwen-max (质量优先)
- **记忆功能**: ✅ 启用
- **在线工具**: ✅ 启用

**特点**:
- ✅ 平衡速度和质量
- ✅ 风险评估更深入
- ✅ 适合大多数场景
- ❌ 耗时适中

##### 🔬 4级 - 深度分析 (10-15分钟)
**适用场景**: 重大投资决策、详细研究报告

**技术配置**:
- **辩论轮次**: 2轮 (研究员) + 2轮 (风险评估)
- **AI模型**: qwen-plus + qwen-max (高质量)
- **记忆功能**: ✅ 启用
- **在线工具**: ✅ 启用

**特点**:
- ✅ 分析深度高
- ✅ 多轮辩论确保全面性
- ✅ 适合重要决策
- ❌ 耗时较长、成本较高

##### 🏆 5级 - 全面分析 (15-25分钟)
**适用场景**: 最重要的投资决策、完整研究报告

**技术配置**:
- **辩论轮次**: 3轮 (研究员) + 3轮 (风险评估)
- **AI模型**: qwen-max + qwen-max (最高质量)
- **记忆功能**: ✅ 启用
- **在线工具**: ✅ 启用

**特点**:
- ✅ 最全面的分析
- ✅ 最高质量的推理
- ✅ 最可靠的结果
- ❌ 耗时最长、成本最高

#### 📋 研究深度选择建议

| 使用场景 | 推荐级别 | 预期耗时 | 成本 | 适用情况 |
|----------|----------|----------|------|----------|
| 日常市场监控 | 1-2级 | 2-6分钟 | 低 | 快速获取市场概况 |
| 常规投资决策 | 2-3级 | 4-10分钟 | 中低 | 平衡速度和质量 |
| 重要投资决策 | 3-4级 | 6-15分钟 | 中高 | 确保分析质量 |
| 重大资金投入 | 4-5级 | 10-25分钟 | 高 | 最全面的风险评估 |
| 研究报告撰写 | 4-5级 | 10-25分钟 | 高 | 需要详细的分析内容 |

### 分析师团队选择

#### 可选分析师类型
- **📊 市场技术分析师**: 技术指标、价格趋势分析
- **💰 基本面分析师**: 财务数据、公司基本面分析
- **📰 新闻分析师**: 新闻事件、市场动态分析
- **💭 社交媒体分析师**: 市场情绪、投资者态度分析

#### 分析师组合建议
- **最快组合**: 只选择"市场技术分析师" (最快)
- **平衡组合**: "市场技术" + "基本面分析师" (推荐)
- **全面组合**: 选择所有分析师 (最全面但最慢)

### 高级选项

#### 模型配置
- **LLM提供商**: 选择AI模型提供商 (阿里百炼/Google AI)
- **具体模型**: 选择使用的具体AI模型

#### 分析选项
- **包含情绪分析**: 是否包含市场情绪分析
- **包含风险评估**: 是否包含详细风险评估
- **自定义提示**: 添加特定的分析要求

## 📈 分析结果解读

### 核心决策指标
- **投资建议**: 买入/持有/卖出
- **目标价位**: AI预测的合理价格目标
- **置信度**: 对决策的信心程度 (0-1)
- **风险评分**: 投资风险等级 (0-1)

### 详细分析报告
- **🧠 AI分析推理**: 决策的详细逻辑
- **📊 技术分析**: 技术指标和趋势分析
- **💰 基本面分析**: 财务状况和业务分析
- **📰 新闻影响**: 相关新闻事件分析
- **💭 市场情绪**: 投资者情绪和态度
- **⚖️ 风险评估**: 详细的风险分析

## 💡 使用技巧

### 速度优化
1. **快速查看**: 使用1-2级研究深度 + 最少分析师
2. **平衡分析**: 使用2-3级研究深度 + 核心分析师
3. **深度研究**: 使用4-5级研究深度 + 全部分析师

### 成本控制
1. **日常监控**: 使用快速模式，降低API调用成本
2. **重要决策**: 使用标准模式，确保分析质量
3. **关键投资**: 使用深度模式，获得最可靠结果

### 结果验证
1. **多次分析**: 对重要股票进行多次分析对比
2. **不同深度**: 使用不同研究深度验证一致性
3. **历史回测**: 查看历史分析的准确性

## 🔧 故障排除

### 常见问题
1. **分析时间过长**: 降低研究深度或减少分析师数量
2. **目标价位显示N/A**: 检查AI模型配置和API连接
3. **分析失败**: 检查API密钥配置和网络连接

### 性能优化
1. **使用缓存**: 启用数据缓存功能
2. **选择合适模型**: 根据需求选择速度和质量平衡的模型
3. **合理配置**: 根据使用场景选择合适的研究深度

## 📞 技术支持

如果您在使用过程中遇到问题，请：
1. 查看控制台错误信息
2. 检查API密钥配置
3. 参考FAQ文档
4. 提交Issue到GitHub仓库


