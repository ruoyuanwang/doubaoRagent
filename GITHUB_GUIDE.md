# GitHub上传指南

## 📋 前置检查

✅ **本地git仓库已就绪**
- 所有文件已提交
- 当前在main分支

## 🚀 方法一：使用GitHub CLI（最简单）

### 1. 安装GitHub CLI

#### macOS
```bash
brew install gh
```

#### Linux (Ubuntu/Debian)
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

#### Windows
```powershell
winget install GitHub.cli
```

### 2. 登录GitHub
```bash
gh auth login
```

按照提示：
- 选择 `GitHub.com`
- 选择 `HTTPS` 或 `SSH`
- 选择 `Login with a web browser` 或 `Paste an authentication token`

### 3. 创建仓库并推送（一键完成！）
```bash
cd /workspace/projects
gh repo create academic-report-agent --public --source=. --remote=origin --push
```

就这么简单！🎉

---

## 🔧 方法二：手动创建仓库

### 第一步：在GitHub上创建新仓库

1. 访问: https://github.com/new
2. 填写信息：
   - **Repository name**: `academic-report-agent`
   - **Description**: 智能学术报告生成Agent - 自动完成从资料收集到报告产出的全流程
   - **Public/Private**: 根据需要选择
   - **不要勾选** "Add a README file"
   - **不要勾选** "Add .gitignore"
   - **不要勾选** "Choose a license"
3. 点击 **Create repository**

### 第二步：推送代码

复制GitHub页面上显示的命令，或使用以下命令：

```bash
cd /workspace/projects

# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/academic-report-agent.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 如果使用SSH（推荐）

```bash
# 添加SSH远程仓库
git remote add origin git@github.com:YOUR_USERNAME/academic-report-agent.git

# 推送
git branch -M main
git push -u origin main
```

---

## 🔑 解决认证问题

### 问题：密码认证失败

**解决方案：使用个人访问令牌（PAT）**

1. 访问: https://github.com/settings/tokens
2. 点击 **Generate new token** -> **Generate new token (classic)**
3. 设置：
   - **Note**: `Academic Report Agent`
   - **Expiration**: 根据需要选择
   - **Scopes**: 勾选 `repo`（完整仓库访问权限）
4. 点击 **Generate token**
5. **复制保存**这个token（只显示一次！）

推送时：
```bash
# 用户名使用你的GitHub用户名
# 密码使用刚才生成的PAT
git push -u origin main
```

### 问题：SSH权限被拒绝

**解决方案：设置SSH密钥**

```bash
# 检查是否已有SSH密钥
ls -la ~/.ssh

# 如果没有，生成新密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 启动ssh-agent
eval "$(ssh-agent -s)"

# 添加密钥
ssh-add ~/.ssh/id_ed25519

# 复制公钥
cat ~/.ssh/id_ed25519.pub
```

然后：
1. 访问: https://github.com/settings/keys
2. 点击 **New SSH key**
3. 粘贴公钥内容
4. 保存

---

## ✅ 验证上传成功

### 1. 检查GitHub仓库
访问: https://github.com/YOUR_USERNAME/academic-report-agent

你应该看到：
- ✅ 所有项目文件
- ✅ 提交历史
- ✅ README.md 显示正确

### 2. 测试克隆（在另一台机器上）
```bash
# 克隆你的新仓库
git clone https://github.com/YOUR_USERNAME/academic-report-agent.git
cd academic-report-agent

# 测试运行
cp .env.example .env
# 编辑 .env 填入API密钥
uv sync
python simple_test.py
```

---

## 📝 后续更新代码

### 推送新更改
```bash
# 查看更改
git status

# 添加更改
git add .

# 提交
git commit -m "描述你的更改"

# 推送
git push
```

### 拉取最新更改
```bash
git pull origin main
```

---

## 🎯 推荐的仓库设置

### 1. 添加描述和Topics
在GitHub仓库页面：
- 点击右侧齿轮图标 ⚙️
- Description: `智能学术报告生成Agent - 自动完成从资料收集到报告产出的全流程`
- Website: 可以留空
- Topics: `ai`, `agent`, `academic`, `research`, `llm`, `langchain`

### 2. 添加社交预览
- 仓库设置 -> General -> Social preview
- 可以上传项目logo或截图

### 3. 启用Wiki（可选）
- Settings -> Features -> 勾选 Wikis

---

## 🆘 常见问题

### Q: 推送时提示"remote: Repository not found"
A: 检查：
1. 仓库名称是否正确
2. 用户名是否正确
3. 是否有访问权限

### Q: 提示"fatal: remote origin already exists"
A: 修改现有远程仓库：
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/academic-report-agent.git
```

### Q: 如何改为Private仓库？
A: 在GitHub上：
1. Settings -> General -> Danger Zone
2. 点击 "Change repository visibility"
3. 选择 "Make private"

---

## 📚 更多资源

- [GitHub官方文档](https://docs.github.com)
- [Git入门教程](https://git-scm.com/doc)
- [GitHub CLI文档](https://cli.github.com/manual/)

---

**上传成功后，别忘了分享你的仓库链接！** 🎉
