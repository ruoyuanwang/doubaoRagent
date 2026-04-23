"""学术报告生成Agent - 支持Coze和火山引擎双平台"""
import os
import json
from typing import Annotated
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from coze_coding_utils.runtime_ctx.context import default_headers
from storage.memory.memory_saver import get_memory_saver

# 导入工具
from tools.academic_crawler_tool import search_academic_data, get_available_domains
from tools.text_generation_tool import (
    generate_article_structure,
    generate_chapter_content,
    generate_final_report
)
from tools.image_generation_tool import (
    generate_academic_image,
    generate_keyword_cloud,
    generate_citation_chart,
    generate_timeline_chart,
    generate_chapter_visualization
)
from tools.reference_manager_tool import generate_references

LLM_CONFIG = "config/agent_llm_config.json"

# 默认保留最近 20 轮对话 (40 条消息)
MAX_MESSAGES = 40

def _windowed_messages(old, new):
    """滑动窗口: 只保留最近 MAX_MESSAGES 条消息"""
    return add_messages(old, new)[-MAX_MESSAGES:] # type: ignore

class AgentState(MessagesState):
    messages: Annotated[list[AnyMessage], _windowed_messages]

def get_platform_config():
    """获取平台配置"""
    platform = os.getenv("PLATFORM", "coze").lower()
    
    if platform == "volcengine":
        # 火山引擎豆包API配置
        api_key = os.getenv("VOLCENGINE_API_KEY", "")
        base_url = os.getenv("VOLCENGINE_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
        model = os.getenv("VOLCENGINE_MODEL_ID", "")
        
        if not api_key or not model:
            raise ValueError(
                "火山引擎配置不完整！请检查 .env 文件中的：\n"
                "  - VOLCENGINE_API_KEY\n"
                "  - VOLCENGINE_MODEL_ID\n"
                "  - VOLCENGINE_BASE_URL (可选)"
            )
        
        return {
            "platform": "volcengine",
            "api_key": api_key,
            "base_url": base_url,
            "model": model
        }
    else:
        # Coze平台配置（默认）
        api_key = os.getenv("COZE_WORKLOAD_IDENTITY_API_KEY", "")
        base_url = os.getenv("COZE_INTEGRATION_MODEL_BASE_URL", "https://api.coze.cn")
        
        return {
            "platform": "coze",
            "api_key": api_key,
            "base_url": base_url
        }

def build_agent(ctx=None):
    workspace_path = os.getenv("COZE_WORKSPACE_PATH", "/workspace/projects")
    config_path = os.path.join(workspace_path, LLM_CONFIG)

    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    # 获取平台配置
    platform_config = get_platform_config()
    
    # 从配置文件读取或从环境变量覆盖
    temperature = float(os.getenv("TEMPERATURE", cfg['config'].get('temperature', 0.7)))
    max_tokens = int(os.getenv("MAX_COMPLETION_TOKENS", cfg['config'].get('max_completion_tokens', 32768)))
    timeout = cfg['config'].get('timeout', 600)
    thinking = cfg['config'].get('thinking', 'disabled')

    # 根据平台选择模型
    if platform_config['platform'] == 'volcengine':
        model = platform_config['model']
        print(f"🗻 使用火山引擎豆包API - 模型: {model}")
    else:
        model = cfg['config'].get("model", "doubao-seed-1-8-251228")
        print(f"🔷 使用Coze平台 - 模型: {model}")

    # 构建LLM配置
    llm_kwargs = {
        "model": model,
        "api_key": platform_config['api_key'],
        "base_url": platform_config['base_url'],
        "temperature": temperature,
        "streaming": True,
        "timeout": timeout,
        "extra_body": {
            "thinking": {
                "type": thinking
            }
        }
    }

    # 火山引擎需要特殊的header
    if platform_config['platform'] == 'volcengine':
        llm_kwargs["default_headers"] = {
            "X-Client-Request-Id": "Coze,Integrations",
        }
    else:
        llm_kwargs["default_headers"] = default_headers(ctx) if ctx else {}

    llm = ChatOpenAI(**llm_kwargs)

    # 工具列表
    tools = [
        search_academic_data,
        get_available_domains,
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

    return create_agent(
        model=llm,
        system_prompt=cfg.get("sp"),
        tools=tools,
        checkpointer=get_memory_saver(),
        state_schema=AgentState,
    )
