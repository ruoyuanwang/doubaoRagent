# 部署和运行指南

## 📋 目录
- [环境要求](#环境要求)
- [GitHub部署步骤](#github部署步骤)
- [本地运行配置](#本地运行配置)
- [API配置说明](#api配置说明)
- [运行命令](#运行命令)
- [故障排除](#故障排除)

---

## 环境要求

### 必需软件
- **Python**: 3.12 或更高版本
- **Git**: 最新版本
- **uv**: 包管理器（用于依赖管理）

### 系统要求
- 操作系统: Linux, macOS, 或 Windows (WSL2推荐)
- 内存: 至少 4GB RAM
- 磁盘空间: 至少 2GB 可用空间

---

## GitHub部署步骤

### 方法一：使用GitHub CLI（推荐）

#### 1. 安装GitHub CLI
```bash
# macOS
brew install gh

# Linux (Ubuntu/Debian)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Windows (使用winget)
winget install GitHub.cli
```

#### 2. 登录GitHub
```bash
gh auth login
```
按照提示完成认证。

#### 3. 创建新仓库并推送
```bash
# 进入项目目录
cd /path/to/academic-report-agent

# 创建新的GitHub仓库
gh repo create academic-report-agent --public --source=. --remote=origin --push
```

### 方法二：手动创建仓库

#### 1. 在GitHub上创建新仓库
1. 访问 https://github.com/new
2. 仓库名称: `academic-report-agent`
3. 选择 Public 或 Private
4. **不要**初始化README、.gitignore或LICENSE
5. 点击 "Create repository"

#### 2. 推送代码到GitHub
```bash
# 进入项目目录
cd /path/to/academic-report-agent

# 添加远程仓库（替换为你的用户名）
git remote add origin https://github.com/YOUR_USERNAME/academic-report-agent.git

# 推送代码
git branch -M main
git push -u origin main
```

### 验证部署
访问你的GitHub仓库页面，确认所有文件都已成功推送。

---

## 本地运行配置

### 1. 克隆项目（如果是新机器）
```bash
git clone https://github.com/YOUR_USERNAME/academic-report-agent.git
cd academic-report-agent
```

### 2. 安装依赖
```bash
# 使用uv安装依赖（推荐）
uv sync

# 或者使用pip（如果没有uv）
pip install -r requirements.txt
```

### 3. 创建环境变量文件
在项目根目录创建 `.env` 文件：
```bash
cp .env.example .env
# 然后编辑 .env 文件，填入你的API配置
```

---

## API配置说明

### 必需的环境变量

在 `.env` 文件中配置以下变量：

```env
# ========== COZE平台配置 ==========
# COZE工作负载身份API密钥（必需）
COZE_WORKLOAD_IDENTITY_API_KEY=your_coze_api_key_here

# COZE集成模型基础URL（通常不需要修改）
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn

# ========== 可选配置 ==========
# 日志级别: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL=INFO

# 超时配置（秒）
TIMEOUT_SECONDS=900
```

### 获取COZE API密钥

1. 访问 [COZE平台](https://www.coze.cn)
2. 登录你的账号
3. 进入API密钥管理页面
4. 创建新的API密钥
5. 复制API密钥并填入 `.env` 文件

### LLM模型配置

模型配置位于 `config/agent_llm_config.json`：

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

#### 可用模型
- `doubao-seed-2-0-pro-260215` - 旗舰级模型
- `doubao-seed-1-8-251228` - 多模态Agent优化模型（推荐）
- `doubao-seed-1-6-251015` - 通用模型
- `deepseek-v3-2-251201` - DeepSeek模型
- `kimi-k2-5-260127` - Kimi模型

#### 参数说明
- `temperature`: 控制输出随机性 (0-2)，越高越随机
- `top_p`: 核采样参数 (0-1)
- `max_completion_tokens`: 最大输出token数
- `timeout`: 请求超时时间（秒）
- `thinking`: 思考模式 ("enabled" 或 "disabled")

---

## 运行命令

### 快速开始（推荐）

```bash
# 一键启动脚本
./start.sh
```

### 单独运行测试

#### 1. 简单功能测试
```bash
python simple_test.py
```

#### 2. 交互式对话模式
```bash
python local_test.py
```

#### 3. 启动HTTP服务
```bash
# 使用内置脚本
bash scripts/http_run.sh -m http -p 5000

# 或者直接使用uvicorn
uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload
```

### 开发模式

```bash
# 启用调试日志
export LOG_LEVEL=DEBUG

# 运行测试
python simple_test.py
```

---

## API使用说明

### HTTP API端点

启动HTTP服务后，可以使用以下端点：

#### 1. 聊天接口
```bash
POST /api/chat
Content-Type: application/json

{
    "message": "请生成一份关于人工智能的学术报告",
    "thread_id": "optional-thread-id"
}
```

#### 2. 流式聊天接口
```bash
POST /api/chat/stream
Content-Type: application/json

{
    "message": "你好",
    "thread_id": "optional-thread-id"
}
```

#### 3. 健康检查
```bash
GET /health
```

### 使用curl测试API

```bash
# 健康检查
curl http://localhost:5000/health

# 发送聊天消息
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "你好，请介绍一下你自己"}'
```

---

## 项目结构说明

```
academic-report-agent/
├── .env                      # 环境变量（不提交到git）
├── .env.example             # 环境变量示例
├── .gitignore               # Git忽略文件
├── pyproject.toml           # 项目配置（uv）
├── requirements.txt         # 依赖列表（pip）
├── README.md                # 项目说明
├── DEPLOYMENT.md            # 本文档
├── LOCAL_RUN.md            # 本地运行指南
├── start.sh                 # 一键启动脚本
├── simple_test.py           # 简单测试脚本
├── local_test.py            # 交互式测试脚本
├── config/
│   └── agent_llm_config.json # LLM配置
├── src/
│   ├── agents/
│   │   └── agent.py         # 主Agent代码
│   ├── tools/
│   │   ├── academic_crawler_tool.py
│   │   ├── text_generation_tool.py
│   │   ├── image_generation_tool.py
│   │   └── reference_manager_tool.py
│   ├── storage/
│   └── main.py              # 主入口
└── scripts/
    ├── local_run.sh
    └── http_run.sh
```

---

## 故障排除

### 问题1: ModuleNotFoundError

**错误信息**:
```
ModuleNotFoundError: No module named 'xxx'
```

**解决方案**:
```bash
# 确保在项目根目录
cd /path/to/academic-report-agent

# 重新安装依赖
uv sync

# 或者使用pip
pip install -r requirements.txt
```

### 问题2: API认证失败

**错误信息**:
```
Authentication failed: Invalid API key
```

**解决方案**:
1. 检查 `.env` 文件中的 `COZE_WORKLOAD_IDENTITY_API_KEY` 是否正确
2. 确认API密钥没有过期
3. 重新生成API密钥并更新

### 问题3: 连接超时

**错误信息**:
```
TimeoutError: Connection timed out
```

**解决方案**:
1. 检查网络连接
2. 检查防火墙设置
3. 增加 `timeout` 配置值
4. 尝试使用代理（如果需要）

### 问题4: 权限错误

**错误信息**:
```
PermissionError: [Errno 13] Permission denied
```

**解决方案**:
```bash
# 给脚本添加执行权限
chmod +x start.sh
chmod +x simple_test.py
chmod +x local_test.py

# 或者使用python直接运行
python start.sh
```

### 问题5: Git推送失败

**错误信息**:
```
fatal: Authentication failed
```

**解决方案**:
1. 确认GitHub账号权限
2. 使用个人访问令牌（PAT）代替密码
3. 或者使用SSH方式：
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/academic-report-agent.git
   ```

---

## 开发工作流

### 1. 创建功能分支
```bash
git checkout -b feature/your-feature-name
```

### 2. 提交更改
```bash
git add .
git commit -m "feat: add your feature description"
```

### 3. 推送到GitHub
```bash
git push origin feature/your-feature-name
```

### 4. 创建Pull Request
在GitHub上创建PR，描述你的更改。

---

## 获取帮助

如果遇到问题：
1. 查看本文档的[故障排除](#故障排除)部分
2. 检查GitHub Issues
3. 提交新的Issue描述你的问题

---

## 更新日志

### v1.0.0
- 初始版本发布
- 支持10个学术领域
- 完整的报告生成流程
- 数据可视化功能
- 参考文献管理

---

**祝你使用愉快！** 🎉
