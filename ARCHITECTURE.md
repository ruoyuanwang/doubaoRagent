# 项目架构详解

## 📁 完整目录结构

```
academic-report-agent/
├── 📄 根目录文件
│   ├── README.md              # 项目概览 + 文档索引
│   ├── ARCHITECTURE.md        # 本文档，架构详解
│   ├── MODEL_GUIDE.md         # 模型配置指南
│   ├── DEPLOYMENT.md          # 部署指南
│   ├── GITHUB_GUIDE.md        # GitHub上传指南
│   ├── LOCAL_RUN.md           # 本地运行指南
│   ├── QUICKSTART.md          # 快速参考卡
│   ├── PUSH_CHECKLIST.md      # 推送检查清单
│   │
│   ├── .env.example           # 环境变量模板
│   ├── .gitignore             # Git忽略配置
│   ├── pyproject.toml         # 项目配置（uv）
│   ├── requirements.txt       # 依赖列表（pip）
│   │
│   ├── start.sh               # 一键启动脚本
│   ├── simple_test.py         # 简单测试脚本
│   ├── local_test.py          # 交互式测试脚本
│   │
│   └── uv.lock                # 依赖锁定文件
│
├── 📁 config/                  # 配置目录
│   └── agent_llm_config.json  # LLM配置（模型、提示词、工具）
│
├── 📁 src/                     # 源代码目录
│   ├── __init__.py
│   │
│   ├── 📁 agents/              # Agent代码
│   │   ├── __init__.py
│   │   └── agent.py           # ⭐ 主Agent代码（核心）
│   │
│   ├── 📁 tools/               # 工具定义
│   │   ├── __init__.py        # 工具导出
│   │   ├── academic_crawler_tool.py    # 学术数据爬取
│   │   ├── text_generation_tool.py     # 文本生成
│   │   ├── image_generation_tool.py    # 图像生成
│   │   └── reference_manager_tool.py   # 参考文献管理
│   │
│   ├── 📁 storage/             # 存储层
│   │   ├── __init__.py
│   │   ├── 📁 memory/
│   │   │   ├── __init__.py
│   │   │   └── memory_saver.py     # 对话记忆保存
│   │   ├── 📁 database/
│   │   │   ├── __init__.py
│   │   │   ├── db.py
│   │   │   └── 📁 shared/
│   │   │       ├── __init__.py
│   │   │       └── model.py
│   │   └── 📁 s3/
│   │       ├── __init__.py
│   │       └── s3_storage.py
│   │
│   ├── 📁 utils/               # 工具函数
│   │   ├── __init__.py
│   │   └── 📁 file/
│   │       ├── __init__.py
│   │       └── file.py
│   │
│   ├── 📁 graphs/              # 图工作流（备用）
│   │   ├── __init__.py
│   │   └── 📁 nodes/
│   │       └── __init__.py
│   │
│   └── main.py                # ⭐ 主入口文件（Web服务）
│
├── 📁 scripts/                 # 脚本目录
│   ├── load_env.py
│   ├── load_env.sh
│   ├── local_run.sh
│   ├── http_run.sh
│   ├── setup.sh
│   └── pack.sh
│
├── 📁 assets/                  # 资源目录
│
└── 📁 .venv/                   # 虚拟环境（不提交Git）
```

---

## 🔄 系统工作流程（Workflow）

### 整体架构图

```
用户输入
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│                   src/main.py                           │
│              (Web服务入口 / 本地测试入口)              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              src/agents/agent.py                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  build_agent() - 构建Agent实例                   │  │
│  │  1. 读取 config/agent_llm_config.json            │  │
│  │  2. 初始化 LLM (ChatOpenAI)                       │  │
│  │  3. 注册所有 Tools                                │  │
│  │  4. 设置 Memory Checkpointer                       │  │
│  │  5. 返回 create_agent() 结果                       │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
    ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  LLM    │ │  Tools  │ │ Memory  │
    │ (模型)  │ │ (工具)  │ │ (记忆)  │
    └────┬────┘ └────┬────┘ └────┬────┘
         │             │             │
         └─────────────┼─────────────┘
                       │
                       ▼
         ┌─────────────────────────┐
         │   LangGraph Agent Loop  │
         │  (思考 → 工具调用 → 响应)│
         └────────────┬────────────┘
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
    ┌─────────┐              ┌─────────┐
    │  调用   │              │  生成   │
    │  Tools  │              │  响应   │
    └────┬────┘              └────┬────┘
         │                         │
         ▼                         ▼
    ┌─────────────────────────────────────┐
    │     src/tools/ 下的各工具            │
    │  (见下方工具详解)                    │
    └─────────────────────────────────────┘
```

---

## 📦 核心模块详解

### 1️⃣ 主Agent模块 (`src/agents/agent.py`)

#### 核心功能
```python
def build_agent(ctx=None):
    """
    构建完整的Agent实例
    """
    # 步骤1: 读取配置
    cfg = json.load(config/agent_llm_config.json)
    
    # 步骤2: 初始化LLM
    llm = ChatOpenAI(
        model=cfg['config']['model'],  # doubao-seed-2-0-pro-260215
        api_key=os.getenv("COZE_WORKLOAD_IDENTITY_API_KEY"),
        temperature=0.7,
        ...
    )
    
    # 步骤3: 注册所有工具
    tools = [
        search_academic_data,        # 数据爬取
        get_available_domains,       # 领域列表
        generate_article_structure,  # 文章结构
        generate_chapter_content,    # 章节内容
        generate_final_report,       # 最终报告
        generate_academic_image,     # 图像生成
        generate_keyword_cloud,      # 词云
        generate_citation_chart,     # 引用图
        generate_timeline_chart,     # 时间线
        generate_chapter_visualization, # 章节可视化
        generate_references          # 参考文献
    ]
    
    # 步骤4: 创建Agent
    return create_agent(
        model=llm,
        system_prompt=cfg['sp'],     # 系统提示词
        tools=tools,
        checkpointer=get_memory_saver(),  # 对话记忆
        state_schema=AgentState      # 状态定义
    )
```

#### Agent状态管理
```python
class AgentState(MessagesState):
    # 滑动窗口：只保留最近40条消息（20轮对话）
    messages: Annotated[list[AnyMessage], _windowed_messages]

def _windowed_messages(old, new):
    """自动裁剪消息历史，防止上下文过长"""
    return add_messages(old, new)[-MAX_MESSAGES:]  # MAX_MESSAGES=40
```

---

### 2️⃣ 工具模块详解 (`src/tools/`)

#### 工具架构图
```
src/tools/
│
├── __init__.py  # 工具导出入口
│
├── academic_crawler_tool.py
│   ├── @tool search_academic_data()
│   │   └── 功能：搜索学术文献，返回正文+结构化数据
│   │
│   └── @tool get_available_domains()
│       └── 功能：返回10个学术领域列表
│
├── text_generation_tool.py
│   ├── @tool generate_article_structure()
│   │   └── 功能：设计文章章节结构
│   │
│   ├── @tool generate_chapter_content()
│   │   └── 功能：生成单个章节的文本
│   │
│   └── @tool generate_final_report()
│       └── 功能：整合所有内容生成完整报告
│
├── image_generation_tool.py
│   ├── @tool generate_academic_image()
│   │   └── 功能：通用学术图像生成
│   │
│   ├── @tool generate_keyword_cloud()
│   │   └── 功能：关键词云
│   │
│   ├── @tool generate_citation_chart()
│   │   └── 功能：引用关系图
│   │
│   ├── @tool generate_timeline_chart()
│   │   └── 功能：时间线图表
│   │
│   └── @tool generate_chapter_visualization()
│       └── 功能：章节定制可视化
│
└── reference_manager_tool.py
    ├── @tool generate_references()
    │   └── 功能：生成参考文献列表
    │
    ├── @tool format_citation()
    │   └── 功能：格式化单个引用
    │
    └── @tool extract_citations_from_text()
        └── 功能：从文本中提取引用位置
```

#### 工具1: 学术数据爬取 (`academic_crawler_tool.py`)

**数据流**：
```
用户输入 (domain, query)
    │
    ▼
search_academic_data(domain, query)
    │
    ├─→ 使用 SearchClient 搜索Web
    │      └─→ coze_coding_dev_sdk.SearchClient
    │
    ├─→ 整理两种数据：
    │   ├─→ content_data[]     (精选正文，前3条)
    │   │   └─ {title, content, url, summary}
    │   │
    │   └─→ structured_data[]  (结构化元数据，全部)
    │       └─ {title, authors, keywords, year, journal, ...}
    │
    └─→ 返回 JSON 字符串
```

**关键函数**：
- `extract_authors()` - 提取作者
- `extract_keywords()` - 提取关键词
- `extract_year()` - 提取年份

---

#### 工具2: 文本生成 (`text_generation_tool.py`)

**三级文本生成流程**：
```
第1步：生成文章结构
    generate_article_structure(domain, topic, content_data)
    │
    └─→ LLM生成 → 返回JSON
         {
           "title": "报告标题",
           "chapters": [
             {"id": 1, "title": "...", "description": "...", ...}
           ]
         }

第2步：生成各章节内容
    generate_chapter_content(chapter_title, chapter_description, content_data)
    │
    └─→ LLM生成 → 返回 500-1000字 学术文本

第3步：整合最终报告
    generate_final_report(article_structure, chapter_contents, images, references)
    │
    └─→ LLM整合 → 返回完整 Markdown 报告
```

---

#### 工具3: 图像生成 (`image_generation_tool.py`)

**图像生成流程**：
```
结构化数据 / 章节内容
    │
    ▼
图像生成工具
    │
    ├─→ 关键词云
    │   generate_keyword_cloud(structured_data)
    │   └─→ 提取所有关键词 → AI生成词云图像
    │
    ├─→ 引用关系图
    │   generate_citation_chart(structured_data)
    │   └─→ AI生成学术引用网络可视化
    │
    ├─→ 时间线图表
    │   generate_timeline_chart(structured_data)
    │   └─→ AI生成研究发展时间线
    │
    └─→ 章节可视化
        generate_chapter_visualization(chapter_title, content, prompt)
        └─→ AI生成章节专属可视化
```

**底层调用**：
```python
ImageGenerationClient.generate(
    prompt="专业的学术图表...",
    model="doubao-seedream-5-0-260128",
    size="2K"
)
```

---

#### 工具4: 参考文献管理 (`reference_manager_tool.py`)

**参考文献流程**：
```
content_data (搜索结果)
    │
    ▼
generate_references(content_data)
    │
    ├─→ LLM分析搜索结果
    ├─→ 生成APA格式引用
    └─→ 返回 JSON 参考文献列表
         {
           "references": [
             {
               "id": 1,
               "authors": "...",
               "year": "...",
               "title": "...",
               "source": "...",
               "url": "...",
               "citation": "APA格式完整引用"
             }
           ]
         }
```

---

### 3️⃣ 配置文件 (`config/agent_llm_config.json`)

```json
{
    "config": {
        // 模型配置
        "model": "doubao-seed-2-0-pro-260215",
        "temperature": 0.7,           // 创造性 0-2
        "top_p": 0.9,                 // 核采样 0-1
        "max_completion_tokens": 32768, // 最大输出
        "timeout": 600,               // 超时(秒)
        "thinking": "disabled"        // 思考模式
    },
    
    "sp": "系统提示词...",           // Agent的身份和任务
    
    "tools": [                       // 可用工具列表
        "search_academic_data",
        "get_available_domains",
        ...
    ]
}
```

---

### 4️⃣ 存储层 (`src/storage/`)

#### Memory模块 (`src/storage/memory/memory_saver.py`)
```python
def get_memory_saver():
    """
    获取对话记忆保存器
    - 自动降级：PostgreSQL → MemorySaver
    - 支持跨轮次对话记忆
    """
    try:
        # 尝试使用PostgreSQL持久化
        return AsyncPostgresSaver.from_conn_string(...)
    except:
        # 降级到内存存储
        return MemorySaver()
```

---

### 5️⃣ 主入口 (`src/main.py`)

#### Web服务架构
```python
FastAPI应用
    │
    ├─→ /health           (健康检查)
    │
    ├─→ /api/chat         (非流式聊天)
    │   └─→ GraphService.run()
    │
    └─→ /api/chat/stream  (流式聊天，SSE)
        └─→ GraphService.stream_sse()


GraphService类
    │
    ├─→ _get_graph()
    │   └─→ 调用 agents.agent.build_agent()
    │
    ├─→ run()              (同步执行)
    │
    └─→ stream_sse()       (流式SSE输出)
```

---

## 🔄 完整学术报告生成流程

### 步骤详解

```
用户："请生成一份关于人工智能发展趋势的学术报告"
    │
    │
    ▼
【步骤1】理解用户意图
    ├─ Agent分析请求
    ├─ 调用 get_available_domains()
    └─ 确定领域：artificial_intelligence
    │
    ▼
【步骤2】收集学术数据
    ├─ 调用 search_academic_data(
    │       domain="artificial_intelligence",
    │       query="发展趋势"
    │   )
    ├─ 获取两种数据：
    │   ├─ content_data (3篇精选正文)
    │   └─ structured_data (10篇元数据)
    └─ 返回JSON数据
    │
    ▼
【步骤3】设计文章结构
    ├─ 调用 generate_article_structure(
    │       domain="artificial_intelligence",
    │       topic="发展趋势",
    │       content_data=...
    │   )
    └─ LLM生成结构：
       {
         "title": "人工智能发展趋势研究报告",
         "chapters": [
           {"id": 1, "title": "引言", "description": "..."},
           {"id": 2, "title": "技术发展历程", "description": "..."},
           {"id": 3, "title": "当前研究热点", "description": "..."},
           {"id": 4, "title": "未来趋势展望", "description": "..."},
           {"id": 5, "title": "结论", "description": "..."}
         ]
       }
    │
    ▼
【步骤4】生成各章节内容
    ├─ 对每个章节调用 generate_chapter_content()
    ├─ chapter 1: "引言" → 生成500-1000字
    ├─ chapter 2: "技术发展历程" → 生成...
    ├─ ...
    └─ 收集所有章节内容
    │
    ▼
【步骤5】生成可视化图表
    ├─ 调用 generate_keyword_cloud(structured_data)
    │   └─→ 生成AI趋势关键词云
    │
    ├─ 调用 generate_timeline_chart(structured_data)
    │   └─→ 生成AI发展时间线
    │
    ├─ 调用 generate_citation_chart(structured_data)
    │   └─→ 生成引用关系图
    │
    └─ (可选) 为特定章节生成定制可视化
       generate_chapter_visualization(chapter_title, ...)
    │
    ▼
【步骤6】生成参考文献
    ├─ 调用 generate_references(content_data)
    └─ LLM生成APA格式参考文献列表
    │
    ▼
【步骤7】整合最终报告
    ├─ 调用 generate_final_report(
    │       article_structure,
    │       chapter_contents,
    │       images,
    │       references
    │   )
    ├─ LLM整合所有内容
    └─ 返回完整 Markdown 报告
    │
    ▼
【最终输出】
    # 人工智能发展趋势研究报告

    ## 目录
    1. 引言
    2. 技术发展历程
    3. 当前研究热点
    4. 未来趋势展望
    5. 结论

    ## 1. 引言
    ... (500字) ...

    ![关键词云](https://image-url)

    ## 2. 技术发展历程
    ... (800字) ...

    ![时间线](https://image-url)

    ...

    ## 参考文献
    [1] Author, A. (2024). Title...
    [2] ...
```

---

## 📝 每个文件的作用

### 根目录文件

| 文件 | 作用 | 是否必需 |
|-----|------|---------|
| `README.md` | 项目概览、快速开始、文档索引 | ✅ 是 |
| `ARCHITECTURE.md` | 本文档，架构详解 | ✅ 是 |
| `MODEL_GUIDE.md` | 模型配置和API设置指南 | ✅ 是 |
| `DEPLOYMENT.md` | 部署和环境配置 | ✅ 是 |
| `GITHUB_GUIDE.md` | GitHub上传步骤 | ✅ 是 |
| `LOCAL_RUN.md` | 本地运行详细指南 | ✅ 是 |
| `QUICKSTART.md` | 5分钟快速参考卡 | ✅ 是 |
| `PUSH_CHECKLIST.md` | 推送前检查清单 | ✅ 是 |
| `.env.example` | 环境变量模板 | ✅ 是 |
| `.gitignore` | Git忽略配置 | ✅ 是 |
| `pyproject.toml` | uv项目配置 | ✅ 是 |
| `requirements.txt` | pip依赖列表 | ✅ 是 |
| `start.sh` | 一键启动脚本 | ✅ 是 |
| `simple_test.py` | 简单功能测试 | ✅ 是 |
| `local_test.py` | 交互式对话测试 | ✅ 是 |

### src/ 目录

| 文件/目录 | 作用 | 是否必需 |
|----------|------|---------|
| `src/main.py` | Web服务主入口 | ✅ 是 |
| `src/agents/agent.py` | ⭐ 主Agent核心代码 | ✅ 是 |
| `src/tools/__init__.py` | 工具导出 | ✅ 是 |
| `src/tools/academic_crawler_tool.py` | 学术数据爬取工具 | ✅ 是 |
| `src/tools/text_generation_tool.py` | 文本生成工具 | ✅ 是 |
| `src/tools/image_generation_tool.py` | 图像生成工具 | ✅ 是 |
| `src/tools/reference_manager_tool.py` | 参考文献管理 | ✅ 是 |
| `src/storage/memory/memory_saver.py` | 对话记忆 | ✅ 是 |
| `config/agent_llm_config.json` | LLM配置 | ✅ 是 |

---

## 🎯 技术栈总结

| 层次 | 技术 | 说明 |
|-----|------|------|
| **Agent框架** | LangChain 1.0 | Agent构建 |
| **工作流** | LangGraph 1.0 | 状态管理和工作流 |
| **LLM** | Doubao 2.0 Pro | 对话/文本生成 |
| **图像生成** | SeeDream 5.0 | 学术可视化 |
| **Web搜索** | COZE Search | 学术数据收集 |
| **Web服务** | FastAPI | HTTP API |
| **包管理** | uv | 依赖管理 |
| **记忆** | MemorySaver / PG | 对话记忆 |

---

**保存本文档以备参考！** 📚
