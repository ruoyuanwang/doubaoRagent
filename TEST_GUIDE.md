# 🔐 安全配置与测试指南

## ⚠️ 重要安全提醒

**永远不要**在以下地方分享你的API密钥：
- ❌ 公开的聊天对话框
- ❌ GitHub Issues
- ❌ 代码提交（确保.env在.gitignore中）
- ❌ 任何公开场所

**应该**：
- ✅ 只在本地 `.env` 文件中配置
- ✅ 确保 `.env` 在 `.gitignore` 中
- ✅ 如果要分享项目，分享 `.env.example` 而不是 `.env`

---

## 🔧 步骤1：配置你的API信息

### 1.1 创建 .env 文件

在项目根目录下，复制环境变量模板：

```bash
cd /workspace/projects
cp .env.example .env
```

### 1.2 编辑 .env 文件

使用你喜欢的编辑器打开 `.env`，填入你的信息：

```env
# ========== COZE平台配置（必需）==========

# 你的Doubao API密钥
COZE_WORKLOAD_IDENTITY_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# COZE API接入点（如果有自定义接入点）
# 注意：通常不需要修改，保持默认即可
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn

# ========== 可选配置 ==========
LOG_LEVEL=INFO
TIMEOUT_SECONDS=900
```

### 1.3 验证 .gitignore

确保 `.env` 不会被提交到git：

```bash
cat .gitignore
```

应该看到：
```
.env
.venv/
__pycache__/
*.pyc
```

---

## 🧪 步骤2：运行测试

### 测试1：简单功能测试（推荐先试这个）

```bash
cd /workspace/projects
python simple_test.py
```

这个测试会：
1. ✅ 检查模块导入
2. ✅ 初始化Agent
3. ✅ 测试简单对话（自我介绍）
4. ✅ 测试获取领域列表

### 测试2：交互式对话测试

```bash
cd /workspace/projects
python local_test.py
```

然后可以输入：
```
你: 你好，请介绍一下你自己

你: 有哪些可用的学术领域？

你: quit
```

### 测试3：一键启动菜单

```bash
cd /workspace/projects
./start.sh
```

然后选择菜单选项：
- `1` - 简单测试
- `2` - 交互式对话
- `3` - 查看使用说明

---

## 🔍 测试检查清单

运行测试时，检查以下内容：

- [ ] 能正常导入所有模块（无ImportError）
- [ ] 能正常初始化Agent
- [ ] API密钥配置正确（无认证错误）
- [ ] 能正常调用LLM
- [ ] 能正常使用工具
- [ ] 响应时间合理（不超时）
- [ ] 输出质量符合预期

---

## 🐛 常见问题排查

### 问题1: Authentication failed / Invalid API key

**错误信息**:
```
Authentication failed: Invalid API key
```

**解决方案**:
1. 检查 `.env` 文件中的 `COZE_WORKLOAD_IDENTITY_API_KEY` 是否正确
2. 确认API密钥没有多余的空格
3. 确认API密钥没有过期
4. 尝试重新生成API密钥

### 问题2: ModuleNotFoundError

**错误信息**:
```
ModuleNotFoundError: No module named 'xxx'
```

**解决方案**:
```bash
# 确保在项目根目录
cd /workspace/projects

# 重新安装依赖
uv sync
```

### 问题3: Connection timeout / TimeoutError

**错误信息**:
```
TimeoutError: Connection timed out
```

**解决方案**:
1. 检查网络连接
2. 检查防火墙设置
3. 尝试增加超时时间（在 `.env` 中设置 `TIMEOUT_SECONDS=1800`）
4. 如果在中国，可能需要配置代理

### 问题4: FileNotFoundError: .env

**错误信息**:
```
FileNotFoundError: [Errno 2] No such file or directory: '.env'
```

**解决方案**:
```bash
cd /workspace/projects
cp .env.example .env
# 然后编辑 .env 填入你的API密钥
```

---

## 📊 测试成功后的输出示例

### 简单测试成功输出
```
============================================================
  学术报告生成Agent - 简单测试
============================================================

[1/4] 正在导入Agent模块...
✓ Agent模块导入成功

[2/4] 正在初始化上下文...
✓ 上下文初始化成功

[3/4] 正在构建Agent...
✓ Agent构建成功

[4/4] 正在测试简单查询...
============================================================
  测试1: Agent自我介绍
============================================================

Agent回复:
------------------------------------------------------------
你好！我是专业的学术报告生成助手...
------------------------------------------------------------

============================================================
  测试2: 获取可用学术领域
============================================================

Agent回复:
------------------------------------------------------------
以下是目前支持的学术领域列表：
| 领域代码               | 中文名称       |
|------------------------|----------------|
| computer_science       | 计算机科学     |
...
------------------------------------------------------------

============================================================
  测试完成！
============================================================

✓ 所有基本功能测试通过！
```

---

## 🎯 完整测试流程建议

### 第一阶段：基础测试
```bash
# 1. 配置API
cp .env.example .env
# 编辑 .env

# 2. 安装依赖
uv sync

# 3. 运行简单测试
python simple_test.py
```

### 第二阶段：功能测试
```bash
# 1. 交互式对话
python local_test.py

# 2. 尝试生成简单报告
# 输入: "请生成一份关于人工智能的简短报告"
```

### 第三阶段：完整测试（可选）
```bash
# 如果有HTTP服务需求
bash scripts/http_run.sh -m http -p 5000

# 测试API端点
curl http://localhost:5000/health
```

---

## 🔐 安全最佳实践

### 1. .env 文件权限
```bash
# 设置为只有你能读取
chmod 600 .env
```

### 2. 轮换API密钥
- 定期更换API密钥
- 如果怀疑泄漏，立即更换
- 使用最小权限原则

### 3. 监控使用情况
- 定期检查API调用次数
- 关注异常使用模式
- 设置使用告警（如果支持）

---

## ❓ 需要帮助？

如果遇到问题：
1. 查看本文档的"常见问题排查"部分
2. 检查日志输出
3. 确认网络连接
4. 验证API密钥有效性

---

**配置好API密钥后，按照上述步骤测试运行吧！** 🚀
