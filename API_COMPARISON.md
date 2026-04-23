# 🔑 Coze vs 火山引擎 API对比指南

## 🤔 两个不同的平台

**Coze平台**和**火山引擎/方舟**是**两个不同的平台**：

| 特性 | Coze平台 | 火山引擎/方舟 |
|-----|----------|-------------|
| 网址 | coze.cn | ark.cn-beijing.volces.com |
| 定位 | 一站式AI应用开发平台 | 字节跳动云服务平台 |
| API获取 | Coze平台内部 | 火山引擎控制台 |
| 计费 | Coze的计费体系 | 火山引擎的计费体系 |

---

## 🔑 如何获取Coze API Key

### 步骤1：注册/登录Coze平台
1. 访问：https://www.coze.cn
2. 注册/登录你的账号

### 步骤2：获取API Key
1. 登录后，进入 **设置** 或 **API密钥管理** 页面
2. 点击 **创建新的API密钥**
3. 复制生成的API Key（格式通常是 `sk_xxxxxx`）

### 步骤3：在项目中使用
在 `.env` 文件中配置：
```env
PLATFORM=coze
COZE_WORKLOAD_IDENTITY_API_KEY=你的Coze_API_Key
```

---

## 💰 计费标准

### Coze平台计费
- Coze有自己的计费体系
- 具体价格需要查看Coze平台的定价页面
- 通常有免费额度供测试使用

### 火山引擎/方舟计费
- 火山引擎有独立的计费体系
- 具体价格需要查看火山引擎控制台
- 不同模型有不同的价格

### 重要说明
⚠️ **Coze和火山引擎的计费是分开的！**
- 它们是两个独立的平台
- API Key不通用
- 计费标准不同

---

## 🎯 如何选择

### 选择Coze平台
✅ 优点：
- 一站式开发平台
- 集成了搜索、图像生成等工具
- 开箱即用，配置简单

⚠️ 注意：
- 需要使用Coze的API Key
- 按照Coze的计费标准

### 选择火山引擎
✅ 优点：
- 可以使用自己的接入点（ep-xxxxxx）
- 直接调用豆包模型

⚠️ 注意：
- 需要搜索和图像生成的替代方案
- 或在Coze平台使用完整功能

---

## 💡 我的建议

### 方案A：在Coze平台使用（推荐）⭐
1. 获取Coze API Key
2. 在Coze平台导入项目
3. 享受完整功能（真实搜索+真实图像生成）
4. 按照Coze的计费

### 方案B：本地测试LLM对话
1. 使用 `standalone_agent.py`
2. 配置火山引擎API Key
3. 测试LLM对话功能
4. 搜索和图像生成是模拟的

---

## 📝 总结

| 问题 | 答案 |
|-----|------|
| Coze API怎么获得？ | 访问 coze.cn → 登录 → API密钥管理 → 创建新密钥 |
| 计费标准相同吗？ | **不同！** 它们是两个独立平台，计费分开 |
| API Key通用吗？ | **不通用！** Coze和火山引擎是不同的Key |

---

## 🔗 相关文档

- **[COZE_PLATFORM_GUIDE.md](./COZE_PLATFORM_GUIDE.md)** - Coze平台使用指南
- **[PLATFORM_COMPARISON.md](./PLATFORM_COMPARISON.md)** - 平台功能对比
- **[DUAL_PLATFORM_GUIDE.md](./DUAL_PLATFORM_GUIDE.md)** - 双平台配置指南
