# 快速参考卡 🚀

## 5分钟快速开始

### 第一步：配置API
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env，填入你的COZE API密钥
# COZE_WORKLOAD_IDENTITY_API_KEY=your_api_key_here
```

### 第二步：安装依赖
```bash
uv sync
```

### 第三步：运行！
```bash
# 选择一个：
./start.sh              # 交互式菜单
python simple_test.py  # 快速测试
python local_test.py   # 对话模式
```

---

## 常用命令速查

### Git操作
```bash
# 查看状态
git status

# 添加所有更改
git add .

# 提交
git commit -m "feat: 描述你的更改"

# 推送到GitHub
git push origin main
```

### 项目操作
```bash
# 安装依赖
uv sync

# 运行测试
python simple_test.py

# 交互式对话
python local_test.py

# 启动服务
bash scripts/http_run.sh -m http -p 5000
```

---

## 支持的学术领域

| 代码 | 名称 |
|-----|------|
| `computer_science` | 计算机科学 |
| `artificial_intelligence` | 人工智能 |
| `machine_learning` | 机器学习 |
| `biology` | 生物学 |
| `physics` | 物理学 |
| `chemistry` | 化学 |
| `medicine` | 医学 |
| `economics` | 经济学 |
| `mathematics` | 数学 |
| `environmental_science` | 环境科学 |

---

## 对话示例

```
你: 你好，请介绍一下你自己

你: 有哪些可用的学术领域？

你: 请生成一份关于人工智能发展趋势的学术报告

你: quit
```

---

## 配置文件位置

- **环境变量**: `.env` (从 `.env.example` 复制)
- **LLM配置**: `config/agent_llm_config.json`
- **主Agent**: `src/agents/agent.py`
- **工具**: `src/tools/`

---

## 文档索引

- 📖 **README.md** - 项目概览
- 🚀 **QUICKSTART.md** - 本文档，快速参考
- 📚 **LOCAL_RUN.md** - 本地运行详细指南
- 🛠️ **DEPLOYMENT.md** - 部署和API配置

---

## 获取帮助

遇到问题？按顺序检查：

1. ✅ Python 3.12+ 已安装？
2. ✅ `uv sync` 已运行？
3. ✅ `.env` 文件已配置API密钥？
4. ✅ 网络连接正常？

查看 **DEPLOYMENT.md** 的故障排除部分获取更多帮助。

---

**保存此文件以备快速参考！** 📝
