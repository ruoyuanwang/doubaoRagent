# 💻 本地环境设置指南

## 📍 正确的本地路径

**之前的错误**：我给了你 `/workspace/projects`，这是我的开发环境路径，不是你的本地路径！

**正确做法**：使用你自己克隆仓库的位置。

---

## 🚀 正确的本地设置步骤

### 第一步：克隆你的GitHub仓库

在你想要存放项目的地方打开终端，运行：

```bash
# 进入你想存放项目的目录（例如 Documents, Projects 等）
cd ~/Documents
# 或者
cd ~/Projects

# 克隆你的仓库
git clone https://github.com/ruoyuanwang/doubaoRagent.git

# 进入项目目录
cd doubaoRagent
```

---

### 第二步：确认你在正确的目录

```bash
# 查看当前目录
pwd

# 查看目录内容
ls -la
```

你应该看到这些文件：
```
README.md
ARCHITECTURE.md
PROMPT_GUIDE.md
TEST_GUIDE.md
config/
src/
pyproject.toml
requirements.txt
...
```

---

### 第三步：配置API密钥

```bash
# 在项目根目录下（就是你现在所在的 doubaoRagent 目录）

# 1. 复制环境变量模板
cp .env.example .env

# 2. 用你喜欢的编辑器打开 .env 文件
# macOS: open .env
# Windows: notepad .env
# Linux: nano .env 或 vim .env

# 3. 在 .env 文件中填入：
COZE_WORKLOAD_IDENTITY_API_KEY=你的API密钥
COZE_INTEGRATION_MODEL_BASE_URL=你的接入点（如果不是默认的话）
```

---

### 第四步：安装依赖

```bash
# 确保在 doubaoRagent 目录下

# 使用uv安装依赖（推荐）
uv sync

# 或者使用pip（如果没有uv）
pip install -r requirements.txt
```

---

### 第五步：运行测试！

```bash
# 方式1：简单测试（推荐先试这个）
python simple_test.py

# 方式2：交互式对话
python local_test.py

# 方式3：一键启动菜单（如果是Linux/macOS）
chmod +x start.sh
./start.sh
```

---

## 🔍 快速验证路径的方法

### 检查你是否在正确的目录

```bash
# 检查是否有这些关键文件
ls -la README.md pyproject.toml src/agents/agent.py

# 如果都能看到，说明位置正确！
```

### 如果找不到文件

```bash
# 1. 确认你克隆了仓库
ls -la

# 2. 如果没有 doubaoRagent 目录，重新克隆
git clone https://github.com/ruoyuanwang/doubaoRagent.git
cd doubaoRagent

# 3. 再次检查
ls -la
```

---

## 💡 不同操作系统的路径示例

### macOS
```bash
# 用户主目录下的 Projects 文件夹
cd ~/Projects/doubaoRagent

# 或者 Documents 文件夹
cd ~/Documents/doubaoRagent

# 或者桌面
cd ~/Desktop/doubaoRagent
```

### Windows
```cmd
# 用户主目录下的 Projects 文件夹
cd %USERPROFILE%\Projects\doubaoRagent

# 或者 Documents
cd %USERPROFILE%\Documents\doubaoRagent

# 或者桌面
cd %USERPROFILE%\Desktop\doubaoRagent
```

### Linux
```bash
# 用户主目录下的 Projects 文件夹
cd ~/Projects/doubaoRagent

# 或者 Documents
cd ~/Documents/doubaoRagent
```

---

## 📋 完整命令序列（复制粘贴用）

### 如果你还没有克隆仓库

```bash
# 1. 进入你想存放项目的目录
cd ~/Documents

# 2. 克隆仓库
git clone https://github.com/ruoyuanwang/doubaoRagent.git

# 3. 进入项目目录
cd doubaoRagent

# 4. 配置API
cp .env.example .env
# （现在用编辑器打开 .env 填入你的API密钥）

# 5. 安装依赖
uv sync

# 6. 运行测试
python simple_test.py
```

### 如果你已经克隆了仓库

```bash
# 1. 进入项目目录（用你实际存放的路径）
cd ~/你的路径/doubaoRagent

# 2. 确认位置正确
ls -la

# 3. 配置API（如果还没配置）
cp .env.example .env
# 编辑 .env

# 4. 安装依赖
uv sync

# 5. 运行测试
python simple_test.py
```

---

## ❓ 常见问题

### Q: 我不知道我把仓库克隆到哪了

**A**: 搜索一下：
```bash
# macOS/Linux
find ~ -name "doubaoRagent" -type d 2>/dev/null

# Windows
dir /s /b "%USERPROFILE%\doubaoRagent"
```

### Q: 提示 "command not found: uv"

**A**: 安装uv或使用pip：
```bash
# 安装uv（推荐）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或者直接用pip
pip install -r requirements.txt
```

### Q: 提示 "No such file or directory"

**A**: 确认你在正确的目录：
```bash
pwd
ls -la
# 如果看不到项目文件，说明路径不对
```

---

## 🎯 记住这一点

**不要再用** `/workspace/projects`！

**要用** 你本地克隆仓库的实际路径，例如：
- `~/Documents/doubaoRagent`
- `~/Projects/doubaoRagent`
- 或者你存放的其他位置

---

**按照这个指南操作，应该就没问题了！** 🚀
