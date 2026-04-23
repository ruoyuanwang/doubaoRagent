# 🏠 独立本地版本使用指南

## ⚠️ 重要说明

原代码依赖Coze平台的内部工具包，在本地无法直接运行。

我为你创建了**两个解决方案**：

---

## 🎯 方案A：使用独立本地版本（推荐先试这个）⭐

### 特点
- ✅ **完全不依赖Coze内部包**
- ✅ 可以在任何Python环境运行
- ✅ 支持火山引擎豆包API
- ⚠️ 搜索和图像生成使用模拟实现

### 快速开始

```bash
# 1. 进入项目目录
cd D:\project\doubaoRagent\doubaoRagent

# 2. 配置环境变量
cp .env.example .env

# 3. 编辑 .env，填入火山引擎配置
PLATFORM=volcengine
VOLCENGINE_API_KEY=000d90d3-8e36-4480-a...
VOLCENGINE_MODEL_ID=ep-your-model-id-here

# 4. 安装依赖
uv sync
# 或
pip install -r requirements.txt

# 5. 运行独立版本！
python standalone_agent.py
```

### 独立版本文件
- **[standalone_agent.py](./standalone_agent.py)** - 完全独立的Agent（不依赖Coze包）

---

## 🌐 方案B：在Coze平台运行（完整功能）

### 特点
- ✅ 所有功能完整工作
- ✅ 真实搜索和图像生成
- ⚠️ 需要在Coze平台环境

### 如何使用
1. 访问Coze平台
2. 导入或复制代码
3. 在Coze开发环境中运行

---

## 🔧 方案A详细步骤

### 步骤1：准备环境

确保你有：
- Python 3.12+
- uv 或 pip
- 火山引擎API密钥和模型ID

### 步骤2：配置 `.env` 文件

```env
# ========== 平台选择 ==========
PLATFORM=volcengine

# ========== 火山引擎豆包API配置 ==========
VOLCENGINE_API_KEY=000d90d3-8e36-4480-a...  # 填入你的完整API Key
VOLCENGINE_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
VOLCENGINE_MODEL_ID=ep-your-model-id-here  # 填入你的模型ID
```

### 步骤3：安装依赖

```bash
# 使用uv（推荐）
uv sync

# 或使用pip
pip install langchain langchain-openai langgraph python-dotenv
```

### 步骤4：运行！

```bash
python standalone_agent.py
```

---

## 📝 两种版本对比

| 功能 | 独立本地版本 | Coze平台版本 |
|-----|-------------|-------------|
| 基础对话 | ✅ | ✅ |
| 火山引擎API | ✅ | ✅ |
| 学术搜索 | ⚠️ 模拟 | ✅ 真实 |
| 图像生成 | ⚠️ 模拟 | ✅ 真实 |
| 依赖Coze包 | ❌ 不依赖 | ✅ 需要 |
| 本地运行 | ✅ | ⚠️ 需要环境 |

---

## 🎯 推荐使用流程

### 第一阶段：测试独立版本
1. 配置 `.env` 填入火山引擎API
2. 运行 `python standalone_agent.py`
3. 测试基础对话功能

### 第二阶段：使用完整版本
1. 在Coze平台导入代码
2. 享受完整的搜索和图像生成功能

---

## ❓ 常见问题

### Q: 提示 `ModuleNotFoundError: No module named 'coze_coding_utils'`

**A**: 使用独立版本！
```bash
python standalone_agent.py
```

### Q: 独立版本的搜索是模拟的？

**A**: 是的。要真实搜索，需要在Coze平台运行。

### Q: 两个版本可以切换吗？

**A**: 可以！
- 本地测试用 `standalone_agent.py`
- 完整功能用Coze平台版本

---

## 📚 相关文档

- **[standalone_agent.py](./standalone_agent.py)** - 独立版本代码
- **[DUAL_PLATFORM_GUIDE.md](./DUAL_PLATFORM_GUIDE.md)** - 双平台配置
- **[VOLCENGINE_SETUP.md](./VOLCENGINE_SETUP.md)** - 火山引擎设置

---

**先试试独立版本：`python standalone_agent.py`** 🚀
