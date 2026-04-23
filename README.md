# 学术报告生成Agent 📚

一个功能完整的智能学术报告生成系统，可以自动完成从资料收集到报告产出的全流程。

## ✨ 核心功能

- 🔍 **智能学术数据爬取** - 支持10个学术领域的文献搜索
- 📝 **自动报告生成** - 智能设计结构并分章节撰写
- 📊 **数据可视化** - 关键词云、引用关系图、时间线等
- 📋 **参考文献管理** - 自动生成符合学术规范的参考文献
- 💬 **交互式对话** - 支持多轮对话，保持上下文记忆

## 🚀 快速开始

### 方法一：一键启动（推荐）

```bash
cd /workspace/projects
./start.sh
```

### 方法二：直接运行

```bash
cd /workspace/projects

# 1. 安装依赖
uv sync

# 2. 运行简单测试
python simple_test.py

# 3. 或者启动交互式对话
python local_test.py
```

## 📖 文档索引

| 文档 | 说明 |
|-----|------|
| [README.md](./README.md) | 项目概览（本文档） |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 🏗️ **项目架构详解（必读！）** |
| [MODEL_GUIDE.md](./MODEL_GUIDE.md) | 🤖 模型配置和API设置指南 |
| [QUICKSTART.md](./QUICKSTART.md) | ⚡ 5分钟快速参考卡 |
| [LOCAL_RUN.md](./LOCAL_RUN.md) | 📚 详细的本地运行指南 |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | 🛠️ 部署和API配置说明 |
| [GITHUB_GUIDE.md](./GITHUB_GUIDE.md) | 📤 GitHub上传详细指南 |

## ⚡ 5分钟快速开始

### 1️⃣ 配置API
```bash
cp .env.example .env
# 编辑 .env，填入你的COZE API密钥
```

### 2️⃣ 安装依赖
```bash
uv sync
```

### 3️⃣ 运行！
```bash
python simple_test.py  # 快速测试
# 或
python local_test.py   # 交互式对话
```

更多详细信息请查看 [QUICKSTART.md](./QUICKSTART.md)。

## 🎯 支持的学术领域

| 领域代码 | 中文名称 |
|---------|---------|
| computer_science | 计算机科学 |
| artificial_intelligence | 人工智能 |
| machine_learning | 机器学习 |
| biology | 生物学 |
| physics | 物理学 |
| chemistry | 化学 |
| medicine | 医学 |
| economics | 经济学 |
| mathematics | 数学 |
| environmental_science | 环境科学 |

## 💡 使用示例

### 交互式对话

启动后，你可以这样使用：

```
你: 请生成一份关于人工智能发展趋势的学术报告

你: 帮我研究机器学习在医疗领域的应用

你: quit
```

## 📁 项目结构

```
/workspace/projects/
├── src/
│   ├── agents/
│   │   └── agent.py              # 主Agent代码
│   ├── tools/
│   │   ├── academic_crawler_tool.py    # 数据爬取工具
│   │   ├── text_generation_tool.py     # 文本生成工具
│   │   ├── image_generation_tool.py    # 图像生成工具
│   │   └── reference_manager_tool.py   # 参考文献工具
│   └── storage/
├── config/
│   └── agent_llm_config.json    # LLM配置
├── simple_test.py                # 简单测试脚本
├── local_test.py                 # 交互式测试脚本
├── start.sh                      # 一键启动脚本
├── LOCAL_RUN.md                  # 详细使用文档
└── pyproject.toml                # 项目配置
```

## 🛠️ 技术栈

- **LangChain 1.0** - Agent框架
- **LangGraph 1.0** - 工作流编排
- **doubao-seed-1-8** - 大语言模型
- **FastAPI** - Web服务
- **uv** - 包管理器

## 📝 开发说明

### 系统要求

- Python 3.12+
- 支持的操作系统：Linux、macOS、Windows

### 环境配置

项目使用 uv 进行依赖管理，所有依赖已在 `pyproject.toml` 中声明。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目仅供学习和研究使用。

---

**祝使用愉快！** 🎉

如有问题，请查看 [LOCAL_RUN.md](./LOCAL_RUN.md) 获取详细帮助。
