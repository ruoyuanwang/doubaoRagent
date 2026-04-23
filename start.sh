#!/bin/bash
# 学术报告生成Agent - 快速启动脚本

echo "========================================"
echo "  学术报告生成Agent"
echo "========================================"
echo ""

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# 检查Python版本
echo "[1/3] 检查Python环境..."
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "✗ 未找到Python，请先安装Python 3.12+"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
echo "✓ Python版本: $PYTHON_VERSION"

# 检查uv
echo ""
echo "[2/3] 检查依赖管理..."
if ! command -v uv &> /dev/null; then
    echo "✗ 未找到uv，请先安装uv"
    echo "  安装命令: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi
echo "✓ uv已安装"

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo ""
    echo "虚拟环境不存在，正在创建..."
    uv venv
fi

# 检查依赖
echo ""
echo "[3/3] 检查项目依赖..."
if [ ! -f "uv.lock" ]; then
    echo "正在安装依赖..."
    uv sync
else
    echo "✓ 依赖已安装"
fi

echo ""
echo "========================================"
echo "  启动选项"
echo "========================================"
echo ""
echo "1. 简单测试 - 验证基本功能"
echo "2. 交互式对话 - 与Agent聊天"
echo "3. 查看使用说明"
echo "4. 退出"
echo ""
read -p "请选择 (1-4): " choice

case $choice in
    1)
        echo ""
        echo "启动简单测试..."
        $PYTHON_CMD simple_test.py
        ;;
    2)
        echo ""
        echo "启动交互式对话..."
        echo "(输入 'quit' 退出)"
        echo ""
        $PYTHON_CMD local_test.py
        ;;
    3)
        echo ""
        if command -v cat &> /dev/null; then
            cat LOCAL_RUN.md
        else
            echo "请查看 LOCAL_RUN.md 文件"
        fi
        ;;
    4)
        echo "再见！"
        exit 0
        ;;
    *)
        echo "无效选择"
        exit 1
        ;;
esac
