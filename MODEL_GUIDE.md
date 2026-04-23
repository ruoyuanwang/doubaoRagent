# 模型配置指南

## 🤖 当前使用的模型

### 1. 主对话模型
- **当前配置**: `doubao-seed-1-8-251228`
- **用途**: Agent主对话、文本生成、文章结构设计等
- **配置位置**: `config/agent_llm_config.json`

### 2. 图像生成模型
- **当前配置**: `doubao-seedream-5-0-260128`
- **用途**: 生成学术图表、词云、可视化等
- **配置位置**: `src/tools/image_generation_tool.py`

### 3. Embedding模型
- **当前状态**: ❌ 未使用
- **说明**: 本项目暂不涉及embedding模型，所有功能基于文本生成和图像生成完成

---

## 🔄 切换到 Doubao 2.0 Pro

### 步骤1：修改主模型配置

编辑 `config/agent_llm_config.json`：

```json
{
    "config": {
        "model": "doubao-seed-2-0-pro-260215",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_completion_tokens": 32768,
        "timeout": 600,
        "thinking": "disabled"
    },
    "sp": "...",
    "tools": [...]
}
```

### 步骤2：（可选）启用思考模式

Doubao 2.0 Pro支持深度思考模式，可以获得更好的推理效果：

```json
{
    "config": {
        "model": "doubao-seed-2-0-pro-260215",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_completion_tokens": 32768,
        "timeout": 600,
        "thinking": "enabled"  // 改为 "enabled"
    }
}
```

**注意**: 启用思考模式会增加响应时间，但推理质量会更高。

---

## 📋 可用模型列表

### 对话/文本生成模型

| 模型ID | 名称 | 特点 | 推荐场景 |
|--------|------|------|---------|
| `doubao-seed-2-0-pro-260215` | Doubao 2.0 Pro | 旗舰级，复杂推理 | ⭐ 复杂学术报告、深度分析 |
| `doubao-seed-2-0-lite-260215` | Doubao 2.0 Lite | 性能成本均衡 | 日常报告生成 |
| `doubao-seed-2-0-mini-260215` | Doubao 2.0 Mini | 快速响应 | 简单查询、快速测试 |
| `doubao-seed-1-8-251228` | Doubao 1.8 | 多模态优化 | 当前默认 |
| `doubao-seed-1-6-251015` | Doubao 1.6 | 通用模型 | 备用选项 |
| `deepseek-v3-2-251201` | DeepSeek V3.2 | 高级推理 | 复杂逻辑任务 |
| `kimi-k2-5-260127` | Kimi K2.5 | 智能体优化 | Agent场景 |

### 图像生成模型

| 模型ID | 名称 | 特点 |
|--------|------|------|
| `doubao-seedream-5-0-260128` | SeeDream 5.0 | 最新版本，高质量 |
| `doubao-seedream-4-5-251128` | SeeDream 4.5 | 稳定版本 |

---

## 🔧 API配置方法

### 方式一：环境变量文件（推荐）

1. 复制环境变量模板
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入：
```env
# ========== 必需配置 ==========
COZE_WORKLOAD_IDENTITY_API_KEY=your_actual_api_key_here

# ========== 可选配置 ==========
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn
LOG_LEVEL=INFO
TIMEOUT_SECONDS=900
```

### 方式二：获取API密钥

1. 访问 [COZE平台](https://www.coze.cn)
2. 登录你的账号
3. 进入 **API密钥管理** 页面
4. 点击 **创建新的API密钥**
5. 复制生成的API密钥（格式通常是 `sk_xxxxxx`）
6. 填入 `.env` 文件的 `COZE_WORKLOAD_IDENTITY_API_KEY`

### 验证配置

运行测试验证配置是否正确：
```bash
python simple_test.py
```

---

## 🎛️ 模型参数调优

### 主模型参数说明

在 `config/agent_llm_config.json` 中：

```json
{
    "config": {
        "model": "doubao-seed-2-0-pro-260215",
        "temperature": 0.7,           // 创造性 (0-2)
        "top_p": 0.9,                 // 核采样 (0-1)
        "max_completion_tokens": 32768, // 最大输出长度
        "timeout": 600,               // 超时时间(秒)
        "thinking": "disabled"        // 思考模式
    }
}
```

### 参数推荐配置

#### 学术报告场景
```json
{
    "model": "doubao-seed-2-0-pro-260215",
    "temperature": 0.7,        // 平衡创造性和准确性
    "top_p": 0.9,
    "max_completion_tokens": 32768,
    "thinking": "enabled"      // 启用深度思考
}
```

#### 快速测试场景
```json
{
    "model": "doubao-seed-2-0-mini-260215",
    "temperature": 0.7,
    "top_p": 0.9,
    "max_completion_tokens": 8192,
    "thinking": "disabled"
}
```

---

## ❓ FAQ

### Q: Embedding模型在哪里使用？
**A**: 本项目**不使用**embedding模型。所有功能通过以下方式实现：
- ✅ 文本生成模型（对话、写作）
- ✅ 图像生成模型（可视化、图表）
- ✅ Web搜索（数据收集）

### Q: 可以使用其他模型吗？
**A**: 可以！在 `config/agent_llm_config.json` 中修改 `model` 字段即可。

### Q: Doubao 2.0 Pro相比1.8有什么提升？
**A**:
- 更强的复杂推理能力
- 更好的多模态理解
- 更长的上下文支持
- 思考模式支持深度推理

### Q: 如何切换回原来的模型？
**A**: 将 `model` 改回 `doubao-seed-1-8-251228` 即可。

---

## 📝 快速配置步骤（Doubao 2.0 Pro）

```bash
# 1. 进入项目目录
cd /workspace/projects

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，填入 COZE_WORKLOAD_IDENTITY_API_KEY

# 3. 修改模型配置为 Doubao 2.0 Pro
# 编辑 config/agent_llm_config.json，将 model 改为:
# "model": "doubao-seed-2-0-pro-260215"

# 4. 安装依赖
uv sync

# 5. 测试运行
python simple_test.py
```

---

## 🔗 相关文档

- [DEPLOYMENT.md](./DEPLOYMENT.md) - 完整部署指南
- [QUICKSTART.md](./QUICKSTART.md) - 5分钟快速开始
- [PUSH_CHECKLIST.md](./PUSH_CHECKLIST.md) - 推送检查清单
