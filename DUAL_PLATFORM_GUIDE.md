# 🔄 双平台配置使用指南

## ✨ 新功能：支持 Coze 和火山引擎双平台！

现在你可以选择使用：
- **Coze平台**（原配置）
- **火山引擎豆包API**（你的配置）

通过 `.env` 文件中的 `PLATFORM` 变量切换。

---

## 📋 快速开始

### 步骤1：复制环境变量模板

```bash
cd ~/Documents/doubaoRagent  # 或你的项目路径
cp .env.example .env
```

### 步骤2：编辑 `.env` 文件

选择你想用的平台，配置对应的API密钥。

---

## 🗻 选项A：使用火山引擎豆包API

### 配置 `.env` 文件

```env
# ========== 平台选择 ==========
PLATFORM=volcengine  # 改为 volcengine

# ========== 火山引擎豆包API配置 ==========
# 你的火山引擎API密钥
VOLCENGINE_API_KEY=000d90d3-8e36-4480-a...  # 填入你的完整API Key

# 火山引擎API基础URL（通常不需要修改）
VOLCENGINE_BASE_URL=https://ark.cn-beijing.volces.com/api/v3

# 你的模型ID（ep-xxxxxx格式）
VOLCENGINE_MODEL_ID=ep-your-model-id-here  # 填入你的模型ID

# ========== 通用配置 ==========
LOG_LEVEL=INFO
TEMPERATURE=0.7
MAX_COMPLETION_TOKENS=32768
```

### 火山引擎配置说明

#### 1. VOLCENGINE_API_KEY
- 格式：`000d90d3-8e36-4480-a...`
- 从火山引擎方舟平台获取
- 必填！

#### 2. VOLCENGINE_BASE_URL
- 默认：`https://ark.cn-beijing.volces.com/api/v3`
- 如果你的接入点在其他区域，修改此地址
- 可选（通常用默认即可）

#### 3. VOLCENGINE_MODEL_ID
- 格式：`ep-20240601xxxxxx`
- 必填！填入你的接入点ID

---

## 🔷 选项B：使用Coze平台

### 配置 `.env` 文件

```env
# ========== 平台选择 ==========
PLATFORM=coze  # 保持 coze（默认）

# ========== Coze平台配置 ==========
COZE_WORKLOAD_IDENTITY_API_KEY=your_coze_api_key_here
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn

# ========== 通用配置 ==========
LOG_LEVEL=INFO
TEMPERATURE=0.7
MAX_COMPLETION_TOKENS=32768
```

---

## 🧪 测试配置

### 配置好 `.env` 后，运行测试：

```bash
cd ~/Documents/doubaoRagent  # 你的项目路径

# 安装依赖（如果还没安装）
uv sync

# 运行简单测试
python simple_test.py
```

### 你应该看到：

如果配置的是**火山引擎**：
```
🗻 使用火山引擎豆包API - 模型: ep-your-model-id
```

如果配置的是**Coze**：
```
🔷 使用Coze平台 - 模型: doubao-seed-2-0-pro-260215
```

---

## 🔄 切换平台

### 从火山引擎切换到Coze：
```env
PLATFORM=coze
```

### 从Coze切换到火山引擎：
```env
PLATFORM=volcengine
```

**注意**：每次切换平台后，确保对应的API密钥已配置！

---

## 📝 环境变量完整说明

### 平台选择
| 变量 | 说明 | 可选值 |
|-----|------|--------|
| `PLATFORM` | 选择平台 | `coze` 或 `volcengine` |

### Coze平台配置
| 变量 | 说明 | 必填？ |
|-----|------|--------|
| `COZE_WORKLOAD_IDENTITY_API_KEY` | Coze API密钥 | PLATFORM=coze时必填 |
| `COZE_INTEGRATION_MODEL_BASE_URL` | Coze API地址 | 可选，默认 `https://api.coze.cn` |

### 火山引擎配置
| 变量 | 说明 | 必填？ |
|-----|------|--------|
| `VOLCENGINE_API_KEY` | 火山引擎API密钥 | PLATFORM=volcengine时必填 |
| `VOLCENGINE_BASE_URL` | 火山引擎API地址 | 可选，默认 `https://ark.cn-beijing.volces.com/api/v3` |
| `VOLCENGINE_MODEL_ID` | 模型ID（ep-xxxxxx） | PLATFORM=volcengine时必填 |

### 通用配置
| 变量 | 说明 | 默认值 |
|-----|------|--------|
| `LOG_LEVEL` | 日志级别 | `INFO` |
| `TEMPERATURE` | 温度参数 | `0.7` |
| `MAX_COMPLETION_TOKENS` | 最大输出token数 | `32768` |

---

## ⚠️ 常见问题

### Q: 提示"火山引擎配置不完整"

**A**: 检查 `.env` 文件：
```env
PLATFORM=volcengine
VOLCENGINE_API_KEY=你的完整API Key
VOLCENGINE_MODEL_ID=ep-your-model-id
```

### Q: 提示认证失败

**A**: 确认：
1. API Key是否正确
2. API Key是否有效、未过期
3. 平台选择是否正确（PLATFORM变量）

### Q: 两个平台可以同时用吗？

**A**: 每次只能用一个平台，但可以通过修改 `PLATFORM` 变量随时切换。

### Q: 模型配置在哪里改？

**A**:
- Coze平台: `config/agent_llm_config.json` 中的 `model` 字段
- 火山引擎: `.env` 文件中的 `VOLCENGINE_MODEL_ID`

---

## 🎯 下一步

1. **配置 `.env`** - 选择平台，填入API密钥
2. **运行测试** - `python simple_test.py`
3. **开始使用** - `python local_test.py`

---

**祝你使用愉快！** 🚀
