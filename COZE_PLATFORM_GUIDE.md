# 🚀 Coze平台使用指南

## ✨ 重要说明

**这个项目本来就是为Coze平台设计的！**

本地独立版本只是额外添加的。你不需要回退代码，直接在Coze平台使用即可！

---

## 🎯 如何在Coze平台使用

### 第一步：访问Coze平台

1. 打开浏览器，访问：https://www.coze.cn
2. 登录你的账号

### 第二步：创建/导入项目

#### 选项A：从GitHub导入（推荐）
1. 在Coze平台创建新项目
2. 选择从GitHub导入
3. 输入你的仓库地址：`https://github.com/ruoyuanwang/doubaoRagent`
4. 等待导入完成

#### 选项B：手动上传文件
1. 在Coze平台创建新项目
2. 逐个上传以下核心文件：
   - `src/agents/agent.py`
   - `src/tools/` 下的所有工具文件
   - `config/agent_llm_config.json`
   - `src/storage/memory/memory_saver.py`

### 第三步：配置环境变量

在Coze平台的环境变量配置中：

```env
# 选择平台
PLATFORM=coze  # 或者 volcengine（如果你想用火山引擎）

# Coze平台配置
COZE_WORKLOAD_IDENTITY_API_KEY=你的Coze API密钥

# 或者火山引擎配置
VOLCENGINE_API_KEY=你的火山引擎API密钥
VOLCENGINE_MODEL_ID=ep-your-model-id
```

### 第四步：运行！

在Coze平台的开发环境中：

1. 运行简单测试：
```bash
python simple_test.py
```

2. 或运行交互式测试：
```bash
python local_test.py
```

3. 或启动Web服务：
```bash
bash scripts/http_run.sh -m http -p 5000
```

---

## 📁 Coze平台需要的核心文件

### 必需文件
```
src/
├── agents/
│   └── agent.py              # ⭐ 主Agent代码
├── tools/
│   ├── __init__.py
│   ├── academic_crawler_tool.py    # 搜索工具
│   ├── text_generation_tool.py     # 文本生成
│   ├── image_generation_tool.py    # 图像生成
│   └── reference_manager_tool.py   # 参考文献
├── storage/
│   └── memory/
│       └── memory_saver.py          # 记忆保存
└── main.py                  # Web服务入口

config/
└── agent_llm_config.json    # ⭐ LLM配置

pyproject.toml                # 依赖配置
```

### 可选文件（本地测试用）
```
simple_test.py          # 本地测试用
local_test.py           # 本地测试用
standalone_agent.py     # 本地独立版本（Coze平台不需要）
src/local_compat.py     # 本地兼容层（Coze平台不需要）
```

---

## 🎯 推荐在Coze平台使用的原因

### 1. 完整功能
- ✅ 真实学术搜索（SearchClient）
- ✅ 真实图像生成（ImageGenerationClient）
- ✅ 完整的工具链
- ✅ coze_coding_dev_sdk 可用

### 2. 开箱即用
- ✅ 所有依赖已预装
- ✅ 无需配置本地环境
- ✅ 直接运行即可

---

## 🔄 关于本地版本

本地版本是额外添加的，用于：
- 测试基础LLM对话
- 离线测试基本功能
- 理解代码结构

**但真实的搜索和图像生成功能，必须在Coze平台使用！**

---

## 📝 总结

### Coze平台（推荐用于完整功能）
- 所有代码本来就是为Coze设计的
- 直接导入项目即可
- 真实搜索 + 真实图像生成

### 本地独立版本（用于测试）
- `standalone_agent.py`
- 只能测试LLM对话
- 搜索和图像生成是模拟的

---

## 💡 现在就开始

1. 访问 https://www.coze.cn
2. 导入你的GitHub项目
3. 配置环境变量
4. 运行，享受完整功能！

---

**你不需要回退代码！直接在Coze平台使用即可！** 🚀
