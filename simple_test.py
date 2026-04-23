#!/usr/bin/env python3
"""
学术报告生成Agent - 简单测试脚本
使用方法：python simple_test.py
"""
import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'src'))

# 首先尝试加载环境变量
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# 优先使用本地兼容层
try:
    from local_compat import new_context
except ImportError:
    # 如果本地兼容层不存在，尝试Coze内部工具
    try:
        from coze_coding_utils.runtime_ctx.context import new_context
    except ImportError:
        # 如果都没有，创建简单的替代
        def new_context(method: str = "local", **kwargs):
            class SimpleContext:
                def __init__(self, method):
                    self.method = method
            return SimpleContext(method)

from langchain_core.messages import HumanMessage

def print_separator(title=""):
    """打印分隔线"""
    print("\n" + "="*60)
    if title:
        print(f"  {title}")
        print("="*60)

def test_simple():
    """简单测试"""
    print_separator("学术报告生成Agent - 简单测试")
    
    try:
        # 导入Agent
        print("\n[1/4] 正在导入Agent模块...")
        from agents.agent import build_agent
        print("✓ Agent模块导入成功")
        
        # 创建上下文
        print("\n[2/4] 正在初始化上下文...")
        ctx = new_context(method="simple_test")
        print("✓ 上下文初始化成功")
        
        # 构建Agent
        print("\n[3/4] 正在构建Agent...")
        agent = build_agent(ctx)
        print("✓ Agent构建成功")
        
        # 测试简单查询
        print("\n[4/4] 正在测试简单查询...")
        config = {"configurable": {"thread_id": "simple_test_001"}}
        
        # 第一个测试：介绍自己
        print_separator("测试1: Agent自我介绍")
        result = agent.invoke(
            {"messages": [HumanMessage(content="请简单介绍一下你自己，你可以做什么？")]},
            config=config
        )
        
        if "messages" in result:
            last_msg = result["messages"][-1]
            if hasattr(last_msg, 'content'):
                print("\nAgent回复:")
                print("-" * 60)
                content = last_msg.content
                if isinstance(content, str):
                    print(content[:500] + "..." if len(content) > 500 else content)
                else:
                    print(str(content)[:500] + "...")
                print("-" * 60)
        
        # 第二个测试：获取领域列表
        print_separator("测试2: 获取可用学术领域")
        result2 = agent.invoke(
            {"messages": [HumanMessage(content="有哪些可用的学术领域？")]},
            config=config
        )
        
        if "messages" in result2:
            last_msg = result2["messages"][-1]
            if hasattr(last_msg, 'content'):
                print("\nAgent回复:")
                print("-" * 60)
                content = last_msg.content
                if isinstance(content, str):
                    print(content)
                else:
                    print(str(content))
                print("-" * 60)
        
        print_separator("测试完成！")
        print("\n✓ 所有基本功能测试通过！")
        print("\n接下来你可以:")
        print("  1. 运行 'python local_test.py' 进行交互式对话")
        print("  2. 直接使用Agent生成完整的学术报告")
        
        return True
        
    except ImportError as e:
        print(f"\n✗ 导入错误: {e}")
        print("\n请运行以下命令安装依赖:")
        print("  uv sync")
        return False
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_simple()
    sys.exit(0 if success else 1)
