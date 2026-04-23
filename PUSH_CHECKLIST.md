# ✅ GitHub推送检查清单

## 推送前检查

- [x] 所有代码已提交
- [x] .gitignore配置正确
- [x] 敏感信息（API密钥）不在git中
- [x] .env.example已创建
- [x] 所有文档已完成
- [x] 测试通过

## 推送步骤（选择一种）

### 选项A：使用GitHub CLI（推荐）⭐

```bash
# 1. 安装GitHub CLI（如果还没安装）
# macOS: brew install gh
# Linux: 见GITHUB_GUIDE.md
# Windows: winget install GitHub.cli

# 2. 登录
gh auth login

# 3. 一键创建仓库并推送
gh repo create academic-report-agent --public --source=. --remote=origin --push
```

### 选项B：手动创建

```bash
# 1. 在GitHub上创建新仓库
# 访问: https://github.com/new
# 仓库名: academic-report-agent
# 不要初始化README、.gitignore、LICENSE

# 2. 添加远程仓库（替换YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/academic-report-agent.git

# 3. 推送
git branch -M main
git push -u origin main
```

## 推送后验证

- [ ] 访问 https://github.com/YOUR_USERNAME/academic-report-agent
- [ ] 确认所有文件都已上传
- [ ] 确认README显示正确
- [ ] 测试克隆仓库到新目录

## 运行说明

### 1. 克隆项目
```bash
git clone https://github.com/YOUR_USERNAME/academic-report-agent.git
cd academic-report-agent
```

### 2. 配置环境
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的配置：
# COZE_WORKLOAD_IDENTITY_API_KEY=your_api_key_here
```

### 3. 安装依赖
```bash
# 使用uv（推荐）
uv sync

# 或者使用pip
pip install -r requirements.txt
```

### 4. 运行
```bash
# 选择一个：
./start.sh              # 交互式菜单
python simple_test.py  # 快速测试
python local_test.py   # 对话模式
```

## API配置说明

### 必填配置

在 `.env` 文件中配置：

```env
# COZE API密钥（必需）
COZE_WORKLOAD_IDENTITY_API_KEY=your_coze_api_key_here

# COZE API基础URL（通常不需要修改）
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.cn
```

### 获取COZE API密钥

1. 访问 https://www.coze.cn
2. 登录账号
3. 进入API密钥管理页面
4. 创建新的API密钥
5. 复制并填入 `.env` 文件

### LLM模型配置

编辑 `config/agent_llm_config.json` 可以修改：

- `model`: 模型ID（默认: doubao-seed-1-8-251228）
- `temperature`: 温度参数（0-2）
- `max_completion_tokens`: 最大输出token数

可用模型：
- `doubao-seed-2-0-pro-260215` - 旗舰模型
- `doubao-seed-1-8-251228` - 多模态优化（推荐）
- `doubao-seed-1-6-251015` - 通用模型
- `deepseek-v3-2-251201` - DeepSeek模型
- `kimi-k2-5-260127` - Kimi模型

## 常用命令

### Git命令
```bash
git status                    # 查看状态
git add .                     # 添加所有更改
git commit -m "message"       # 提交
git push                      # 推送
git pull                      # 拉取
```

### 项目命令
```bash
uv sync                      # 安装依赖
python simple_test.py         # 简单测试
python local_test.py          # 交互式对话
./start.sh                    # 启动菜单
```

## 文档索引

- 📖 **README.md** - 项目概览
- ⚡ **QUICKSTART.md** - 5分钟快速参考
- 📚 **LOCAL_RUN.md** - 本地运行详细指南
- 🛠️ **DEPLOYMENT.md** - 部署和API配置
- 📤 **GITHUB_GUIDE.md** - GitHub上传指南
- ✅ **PUSH_CHECKLIST.md** - 本文档

## 需要帮助？

查看相关文档或提交GitHub Issue！

---

**准备好后，选择一种方式推送到GitHub吧！** 🚀
