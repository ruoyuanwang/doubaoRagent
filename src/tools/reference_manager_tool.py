"""引用文献管理工具"""
import json
from typing import List, Dict
from langchain.tools import tool
from coze_coding_dev_sdk import LLMClient
from coze_coding_utils.log.write_log import request_context
from coze_coding_utils.runtime_ctx.context import new_context
from langchain_core.messages import SystemMessage, HumanMessage

def get_text_content(content):
    """安全获取文本内容的辅助函数"""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        if content and isinstance(content[0], str):
            return " ".join(content)
        else:
            return " ".join(item.get("text", "") for item in content if isinstance(item, dict) and item.get("type") == "text")
    return str(content)

@tool
def generate_references(content_data: str) -> str:
    """
    根据内容数据生成参考文献列表
    
    Args:
        content_data: JSON格式的内容数据
    
    Returns:
        JSON格式的参考文献列表
    """
    ctx = request_context.get() or new_context(method="generate_references")
    
    client = LLMClient(ctx=ctx)
    
    system_prompt = """你是一位专业的参考文献管理助手。根据提供的学术资料，生成标准格式的参考文献列表。

要求：
1. 使用APA或MLA格式（选择APA格式）
2. 每条参考文献应包含：作者、年份、标题、来源、URL等信息
3. 按字母顺序排列
4. 如果某些信息缺失，使用合理的占位符
5. 生成5-10条参考文献

输出格式（JSON）：
{
    "references": [
        {
            "id": 1,
            "authors": "作者列表",
            "year": "年份",
            "title": "标题",
            "source": "来源",
            "url": "URL",
            "citation": "APA格式引用"
        }
    ]
}
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"参考资料：{content_data}")
    ]
    
    try:
        response = client.invoke(
            messages=messages,
            model="doubao-seed-1-8-251228",
            temperature=0.7
        )
        
        text_content = get_text_content(response.content)
        
        # 尝试提取JSON
        import re
        json_match = re.search(r'\{[\s\S]*\}', text_content)
        if json_match:
            return json_match.group(0)
        return text_content
        
    except Exception as e:
        return json.dumps({
            "error": f"生成参考文献失败: {str(e)}",
            "references": []
        }, ensure_ascii=False)

@tool
def format_citation(reference: str, citation_style: str = "APA") -> str:
    """
    格式化单个引用
    
    Args:
        reference: JSON格式的参考文献信息
        citation_style: 引用格式 (APA, MLA, Chicago等)
    
    Returns:
        格式化后的引用字符串
    """
    ctx = request_context.get() or new_context(method="format_citation")
    
    try:
        ref_data = json.loads(reference)
        
        if citation_style == "APA":
            return f"{ref_data.get('authors', 'Unknown')} ({ref_data.get('year', 'n.d.')}). {ref_data.get('title', 'Untitled')}. {ref_data.get('source', 'Unknown Source')}"
        elif citation_style == "MLA":
            return f"{ref_data.get('authors', 'Unknown')}. \"{ref_data.get('title', 'Untitled')}\". {ref_data.get('source', 'Unknown Source')}, {ref_data.get('year', 'n.d.')}"
        else:
            return f"{ref_data.get('authors', 'Unknown')}. {ref_data.get('title', 'Untitled')}. {ref_data.get('source', 'Unknown Source')}, {ref_data.get('year', 'n.d.')}"
            
    except Exception as e:
        return f"格式化引用失败: {str(e)}"

@tool
def extract_citations_from_text(text: str) -> str:
    """
    从文本中提取需要引用的地方
    
    Args:
        text: 学术文本
    
    Returns:
        JSON格式的引用位置建议
    """
    ctx = request_context.get() or new_context(method="extract_citations_from_text")
    
    client = LLMClient(ctx=ctx)
    
    system_prompt = """你是一位专业的学术编辑。分析提供的学术文本，指出哪些地方需要添加引用标注。

要求：
1. 找出陈述事实、数据或观点的句子
2. 建议在适当位置添加[1][2]等引用标记
3. 提供简短的说明为什么需要引用

输出格式（JSON）：
{
    "citation_suggestions": [
        {
            "text": "需要引用的句子",
            "position": "位置描述",
            "reason": "需要引用的原因"
        }
    ]
}
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"文本：{text}")
    ]
    
    try:
        response = client.invoke(
            messages=messages,
            model="doubao-seed-1-8-251228",
            temperature=0.3
        )
        
        text_content = get_text_content(response.content)
        
        # 尝试提取JSON
        import re
        json_match = re.search(r'\{[\s\S]*\}', text_content)
        if json_match:
            return json_match.group(0)
        return text_content
        
    except Exception as e:
        return json.dumps({
            "error": f"提取引用建议失败: {str(e)}",
            "citation_suggestions": []
        }, ensure_ascii=False)
