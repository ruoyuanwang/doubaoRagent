#!/usr/bin/env python3
"""
学术报告生成Agent - 本地测试脚本
使用方法：python local_test.py
"""
import asyncio
import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'src'))

from coze_coding_utils.runtime_ctx.context import new_context
from langchain_core.messages import HumanMessage

def print_separator(title=""):
    """打印分隔线"""
    print("\n" + "="*80)
    if title:
        print(f"  {title}")
        print("="*80)

async def test_agent():
    """测试Agent的基本功能"""
    print_separator("学术报告生成Agent - 本地测试")
    
    try:
        # 导入Agent
        from agents.agent import build_agent
        
        print("✓ Agent模块导入成功")
        
        # 创建上下文
        ctx = new_context(method="local_test")
        
        # 构建Agent
        agent = build_agent(ctx)
        print("✓ Agent构建成功")
        
        # 简单对话测试
        print_separator("开始对话测试")
        print("\n你可以直接和Agent对话，输入 'quit' 退出\n")
        
        config = {"configurable": {"thread_id": "local_test_001"}}
        
        while True:
            try:
                user_input = input("\n你: ").strip()
                
                if user_input.lower() in ['quit', 'exit', '退出', 'q']:
                    print("\n再见！")
                    break
                
                if not user_input:
                    continue
                
                print("\nAgent: ", end="", flush=True)
                
                # 流式输出
                response = ""
                async for event in agent.astream(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=config
                ):
                    for key, value in event.items():
                        if key == "agent" and "messages" in value:
                            msg = value["messages"][-1]
                            if hasattr(msg, 'content') and msg.content:
                                content = msg.content
                                if isinstance(content, str):
                                    print(content, end="", flush=True)
                                    response += content
                                elif isinstance(content, list):
                                    for item in content:
                                        if isinstance(item, str):
                                            print(item, end="", flush=True)
                                            response += item
                                        elif isinstance(item, dict) and item.get("type") == "text":
                                            text = item.get("text", "")
                                            print(text, end="", flush=True)
                                            response += text
                
                print()
                
            except KeyboardInterrupt:
                print("\n\n检测到中断，再见！")
                break
            except Exception as e:
                print(f"\n错误: {e}")
                import traceback
                traceback.print_exc()
        
    except ImportError as e:
        print(f"✗ 导入错误: {e}")
        print("\n请确保已安装所有依赖:")
        print("  uv sync")
        return False
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def show_quick_start():
    """显示快速开始指南"""
    print_separator("快速开始指南")
    print("""
1. 安装依赖（如果还没安装）:
   uv sync

2. 运行测试脚本:
   python local_test.py

3. 尝试这些对话示例:
   - "你好，请介绍一下你自己"
   - "有哪些可用的学术领域？"
   - "请生成一份关于人工智能的学术报告"

4. 退出: 输入 'quit' 或按 Ctrl+C
""")

if __name__ == "__main__":
    show_quick_start()
    
    try:
        success = asyncio.run(test_agent())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n再见！")
        sys.exit(0)
