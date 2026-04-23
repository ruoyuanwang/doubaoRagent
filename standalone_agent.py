#!/usr/bin/env python3
"""
学术报告生成Agent - 完全独立本地版本
不依赖任何Coze内部包，可以在普通Python环境运行
"""
import os
import sys
import json
from typing import Annotated, List, Dict, Any
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 尝试导入LangChain相关包
try:
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI
    from langgraph.graph import MessagesState
    from langgraph.graph.message import add_messages
    from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
    from langchain.tools import tool
    from langgraph.checkpoint.memory import MemorySaver
    LANGCHAIN_AVAILABLE = True
except ImportError as e:
    print(f"警告: 缺少LangChain相关包: {e}")
    print("请运行: uv sync 或 pip install langchain langchain-openai langgraph")
    LANGCHAIN_AVAILABLE = False

# ============================================
# 学术领域定义
# ============================================

ACADEMIC_DOMAINS = {
    "computer_science": "计算机科学",
    "artificial_intelligence": "人工智能",
    "machine_learning": "机器学习",
    "biology": "生物学",
    "physics": "物理学",
    "chemistry": "化学",
    "medicine": "医学",
    "economics": "经济学",
    "mathematics": "数学",
    "environmental_science": "环境科学"
}

# ============================================
# 模拟工具（不依赖Coze SDK）
# ============================================

@tool
def get_available_domains() -> str:
    """获取可用的学术领域列表"""
    return json.dumps(ACADEMIC_DOMAINS, ensure_ascii=False, indent=2)

@tool
def search_academic_data(domain: str, query: str, count: int = 10) -> str:
    """
    模拟搜索学术数据
    
    注意：这是一个模拟工具，不执行真实搜索
    完整版本需要在Coze平台运行
    """
    simulated_data = {
        "domain": domain,
        "query": query,
        "content_data": [
            {
                "title": f"{domain}领域研究综述",
                "content": f"这是关于{query}的研究内容摘要...",
                "url": "https://example.com/paper1",
                "summary": f"{domain}领域最新研究进展"
            }
        ],
        "structured_data": [
            {
                "title": f"{query}相关研究",
                "authors": ["Researcher A", "Researcher B"],
                "keywords": [domain, query, "research"],
                "year": 2024,
                "journal": "Journal of Academic Research",
                "url": "https://example.com/paper1",
                "citations": 10
            }
        ]
    }
    
    print(f"📚 模拟搜索: {domain} - {query}")
    print("   (提示: 完整搜索功能需要在Coze平台运行)")
    
    return json.dumps(simulated_data, ensure_ascii=False, indent=2)

@tool
def generate_article_structure(domain: str, topic: str, content_data: str) -> str:
    """
    模拟生成文章结构
    
    注意：这是一个模拟工具
    """
    structure = {
        "title": f"{topic}研究报告",
        "chapters": [
            {
                "id": 1,
                "title": "引言",
                "description": "介绍研究背景和意义",
                "needs_visualization": False
            },
            {
                "id": 2,
                "title": "文献综述",
                "description": "回顾相关研究",
                "needs_visualization": True,
                "visualization_prompt": "研究发展时间线"
            },
            {
                "id": 3,
                "title": "研究方法",
                "description": "介绍研究方法",
                "needs_visualization": False
            },
            {
                "id": 4,
                "title": "结论",
                "description": "总结研究发现",
                "needs_visualization": False
            }
        ]
    }
    
    print(f"📝 模拟生成文章结构")
    return json.dumps(structure, ensure_ascii=False, indent=2)

@tool
def generate_chapter_content(chapter_title: str, chapter_description: str, content_data: str) -> str:
    """
    模拟生成章节内容
    
    注意：这是一个模拟工具
    """
    content = f"""# {chapter_title}

{chapter_description}

本章将详细讨论相关内容。基于收集到的学术资料，我们可以分析以下几点：

1. 研究背景与现状
2. 主要研究成果
3. 未来发展方向

（注意：完整的内容生成功能需要在Coze平台运行）

---

*本章内容由模拟工具生成，实际使用时会根据真实学术资料生成。*
"""
    
    print(f"✍️  模拟生成章节: {chapter_title}")
    return content

@tool
def generate_final_report(article_structure: str, chapter_contents: str, images: str, references: str) -> str:
    """
    模拟生成最终报告
    
    注意：这是一个模拟工具
    """
    report = f"""# 学术研究报告

## 目录
1. 引言
2. 文献综述
3. 研究方法
4. 结论

## 1. 引言

（章节内容...）

## 参考文献

[1] 模拟参考文献

---

*本报告由模拟工具生成，完整功能需要在Coze平台运行。*
"""
    
    print("📄 模拟生成最终报告")
    return report

@tool
def generate_academic_image(prompt: str, style: str = "professional") -> str:
    """
    模拟生成学术图像
    
    注意：这是一个模拟工具
    """
    print(f"🎨 模拟生成图像: {prompt}")
    print("   (提示: 完整图像生成功能需要在Coze平台运行)")
    
    return json.dumps({
        "success": True,
        "image_url": "https://via.placeholder.com/800x600?text=Academic+Image",
        "prompt": prompt,
        "note": "这是模拟的图像URL"
    }, ensure_ascii=False)

@tool
def generate_references(content_data: str) -> str:
    """
    模拟生成参考文献
    
    注意：这是一个模拟工具
    """
    print("📚 模拟生成参考文献")
    
    return json.dumps({
        "references": [
            {
                "id": 1,
                "authors": "Author, A., & Author, B.",
                "year": "2024",
                "title": "研究论文标题",
                "source": "期刊名称",
                "url": "https://example.com",
                "citation": "Author, A., & Author, B. (2024). 研究论文标题. 期刊名称."
            }
        ]
    }, ensure_ascii=False, indent=2)

# 其他模拟工具
generate_keyword_cloud = generate_academic_image
generate_citation_chart = generate_academic_image
generate_timeline_chart = generate_academic_image
generate_chapter_visualization = generate_academic_image

# ============================================
# Agent构建
# ============================================

def get_platform_config():
    """获取平台配置"""
    platform = os.getenv("PLATFORM", "volcengine").lower()
    
    if platform == "volcengine":
        # 火山引擎豆包API配置
        api_key = os.getenv("VOLCENGINE_API_KEY", "")
        base_url = os.getenv("VOLCENGINE_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
        model = os.getenv("VOLCENGINE_MODEL_ID", "")
        
        if not api_key:
            print("⚠️  警告: VOLCENGINE_API_KEY 未配置")
            print("   请编辑 .env 文件填入你的API密钥")
        
        if not model:
            print("⚠️  警告: VOLCENGINE_MODEL_ID 未配置")
            print("   请编辑 .env 文件填入你的模型ID (ep-xxxxxx)")
        
        return {
            "platform": "volcengine",
            "api_key": api_key,
            "base_url": base_url,
            "model": model
        }
    else:
        # Coze平台配置（备用）
        api_key = os.getenv("COZE_WORKLOAD_IDENTITY_API_KEY", "")
        base_url = os.getenv("COZE_INTEGRATION_MODEL_BASE_URL", "https://api.coze.cn")
        
        return {
            "platform": "coze",
            "api_key": api_key,
            "base_url": base_url,
            "model": "doubao-seed-2-0-pro-260215"
        }

# 默认保留最近 20 轮对话 (40 条消息)
MAX_MESSAGES = 40

def _windowed_messages(old, new):
    """滑动窗口: 只保留最近 MAX_MESSAGES 条消息"""
    return add_messages(old, new)[-MAX_MESSAGES:]

class AgentState(MessagesState):
    messages: Annotated[list[AnyMessage], _windowed_messages]

def build_agent():
    """构建Agent（独立版本）"""
    if not LANGCHAIN_AVAILABLE:
        print("❌ LangChain不可用，无法构建Agent")
        return None
    
    platform_config = get_platform_config()
    
    # 检查API配置
    if not platform_config['api_key']:
        print("⚠️  API密钥未配置，将使用模拟模式")
        print("   要使用真实API，请编辑 .env 文件")
    
    # 工具列表
    tools = [
        get_available_domains,
        search_academic_data,
        generate_article_structure,
        generate_chapter_content,
        generate_final_report,
        generate_academic_image,
        generate_keyword_cloud,
        generate_citation_chart,
        generate_timeline_chart,
        generate_chapter_visualization,
        generate_references
    ]
    
    # 系统提示词
    system_prompt = """你是一位专业的学术报告生成助手，擅长从多个学术领域收集资料、分析数据，并生成高质量的学术报告。

注意：这是本地独立版本，搜索和图像生成等功能使用模拟实现。
完整功能需要在Coze平台运行。

可用的学术领域：
- computer_science (计算机科学)
- artificial_intelligence (人工智能)
- machine_learning (机器学习)
- biology (生物学)
- physics (物理学)
- chemistry (化学)
- medicine (医学)
- economics (经济学)
- mathematics (数学)
- environmental_science (环境科学)
"""
    
    if not platform_config['api_key'] or not platform_config['model']:
        # 没有API配置，返回None（模拟模式）
        print("🔧 运行在模拟模式（无API配置）")
        return None
    
    try:
        # 构建LLM
        llm = ChatOpenAI(
            model=platform_config['model'],
            api_key=platform_config['api_key'],
            base_url=platform_config['base_url'],
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            streaming=True,
            timeout=int(os.getenv("TIMEOUT_SECONDS", "600")),
            default_headers={
                "X-Client-Request-Id": "Coze,Integrations",
            } if platform_config['platform'] == 'volcengine' else {}
        )
        
        print(f"🗻 使用火山引擎豆包API" if platform_config['platform'] == 'volcengine' else f"🔷 使用Coze平台")
        print(f"   模型: {platform_config['model']}")
        
        # 使用MemorySaver作为checkpointer
        checkpointer = MemorySaver()
        
        return create_agent(
            model=llm,
            system_prompt=system_prompt,
            tools=tools,
            checkpointer=checkpointer,
            state_schema=AgentState,
        )
        
    except Exception as e:
        print(f"❌ 构建Agent失败: {e}")
        print("   运行在模拟模式")
        return None

# ============================================
# 简单的模拟对话（当没有API时使用）
# ============================================

def mock_conversation():
    """模拟对话"""
    print("\n" + "="*80)
    print("  🔧 模拟模式 - 无API配置")
    print("="*80)
    print("\n这是一个模拟版本，用于测试基本功能。")
    print("要使用完整功能，请：")
    print("1. 编辑 .env 文件填入你的火山引擎API密钥和模型ID")
    print("2. 或者在Coze平台运行完整版本")
    
    print(f"\n📚 可用的学术领域:")
    for code, name in ACADEMIC_DOMAINS.items():
        print(f"   - {code}: {name}")
    
    print("\n💡 示例对话:")
    print('   "有哪些可用的学术领域？"')
    print('   "请生成一份关于人工智能的报告"')
    
    print("\n" + "="*80)

# ============================================
# 主程序
# ============================================

def main():
    """主程序"""
    print("="*80)
    print("  学术报告生成Agent - 独立本地版本")
    print("="*80)
    
    # 构建Agent
    agent = build_agent()
    
    if agent is None:
        # 模拟模式
        mock_conversation()
        return
    
    # 真实Agent模式
    print("\n✅ Agent构建成功！")
    print("\n开始对话（输入 'quit' 退出）:")
    print("-"*80)
    
    config = {"configurable": {"thread_id": "standalone_test_001"}}
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出', 'q']:
                print("\n再见！")
                break
            
            if not user_input:
                continue
            
            print("\nAgent: ", end="", flush=True)
            
            response = ""
            for event in agent.stream(
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
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
