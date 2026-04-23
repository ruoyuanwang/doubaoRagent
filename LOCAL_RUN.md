# 学术报告生成Agent - 本地运行指南

## 📋 项目概述

这是一个功能完整的学术报告生成Agent，可以自动完成从资料收集到报告产出的全流程。

## 🚀 快速开始

### 前置要求

- Python 3.12 或更高版本
- uv 包管理器（项目已内置）

### 1. 安装依赖

```bash
# 进入项目目录
cd /workspace/projects

# 安装所有依赖
uv sync
```

### 2. 运行简单测试

```bash
# 运行简单测试，验证基本功能
python simple_test.py
```

### 3. 交互式对话

```bash
# 启动交互式对话模式
python local_test.py
```

## 📝 使用示例

### 交互式对话示例

启动 `local_test.py` 后，你可以尝试以下对话：

```
你: 你好，请介绍一下你自己

你: 有哪些可用的学术领域？

你: 请生成一份关于人工智能发展趋势的学术报告

你: quit
```

### 测试用的学术领域

- `computer_science` - 计算机科学
- `artificial_intelligence` - 人工智能
- `machine_learning` - 机器学习
- `biology` - 生物学
- `physics` - 物理学
- `chemistry` - 化学
- `medicine` - 医学
- `economics` - 经济学
- `mathematics` - 数学
- `environmental_science` - 环境科学

## 🔧 项目结构

```
/workspace/projects/
├── src/
│   ├── agents/
│   │   └── agent.py          # 主Agent代码
│   ├── tools/
│   │   ├── academic_crawler_tool.py    # 学术数据爬取工具
│   │   ├── text_generation_tool.py     # 文本生成工具
│   │   ├── image_generation_tool.py    # 图像生成工具
│   │   └── reference_manager_tool.py   # 引用文献管理工具
│   └── storage/
├── config/
│   └── agent_llm_config.json  # LLM配置文件
├── simple_test.py              # 简单测试脚本
├── local_test.py               # 交互式测试脚本
├── LOCAL_RUN.md               # 本文档
└── pyproject.toml             # 项目配置
```

## 🛠️ 核心功能

### 1. 学术数据爬取
- 支持多领域学术文献搜索
- 自动提取正文内容和结构化元数据
- 智能提取关键词、作者、年份等信息

### 2. 报告生成
- 自动设计文章结构
- 分章节生成专业内容
- 整合所有内容生成完整报告

### 3. 数据可视化
- 关键词云生成
- 引用关系图表
- 时间线图表
- 章节定制可视化

### 4. 参考文献管理
- 自动生成参考文献列表
- 支持APA/MLA格式
- 智能引用位置标注

## 📊 测试脚本说明

### simple_test.py
简单的非流式测试脚本，用于验证基本功能：
- 测试Agent导入和构建
- 测试基本对话功能
- 测试工具调用

### local_test.py
完整的交互式测试脚本：
- 流式输出，实时看到Agent回复
- 支持多轮对话
- 完整的对话记忆功能

## ⚙️ 配置说明

### LLM配置 (config/agent_llm_config.json)

```json
{
    "config": {
        "model": "doubao-seed-1-8-251228",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_completion_tokens": 32768,
        "timeout": 600,
        "thinking": "disabled"
    },
    "sp": "系统提示词...",
    "tools": [工具列表...]
}
```

## 🔍 故障排除

### 问题1: 导入错误
```
ImportError: No module named 'xxx'
```
**解决**: 运行 `uv sync` 安装所有依赖

### 问题2: 权限错误
```
Permission denied: ...
```
**解决**: 确保脚本有执行权限 `chmod +x *.py`

### 问题3: 测试脚本无响应
**解决**: 检查网络连接和API配置

## 💡 进阶使用

### 自定义测试

你可以创建自己的测试脚本：

```python
from agents.agent import build_agent
from langchain_core.messages import HumanMessage
from coze_coding_utils.runtime_ctx.context import new_context

# 构建Agent
ctx = new_context(method="custom_test")
agent = build_agent(ctx)

# 发送消息
config = {"configurable": {"thread_id": "my_test"}}
result = agent.invoke(
    {"messages": [HumanMessage(content="你的消息")]},
    config=config
)

# 打印结果
print(result["messages"][-1].content)
```

## 📞 获取帮助

如果遇到问题，请检查：
1. Python版本是否为3.12+
2. 所有依赖是否已安装 (`uv sync`)
3. 网络连接是否正常
4. 配置文件是否完整

祝你使用愉快！🎉
