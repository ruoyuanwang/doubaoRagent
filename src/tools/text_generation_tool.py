"""文本生成工具"""
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
def generate_article_structure(domain: str, topic: str, content_data: str) -> str:
    """
    根据学术数据生成文章结构
    
    Args:
        domain: 学术领域
        topic: 主题
        content_data: JSON格式的内容数据
    
    Returns:
        JSON格式的文章结构
    """
    ctx = request_context.get() or new_context(method="generate_article_structure")
    
    client = LLMClient(ctx=ctx)
    
    system_prompt = """你是一位专业的学术报告结构设计师。根据提供的学术领域、主题和参考资料，设计一个完整的学术报告结构。

要求：
1. 生成一个包含3-5个主要章节的报告结构
2. 每个章节应该有明确的标题和内容描述
3. 结构应该逻辑清晰，从引言到结论递进
4. 考虑学术报告的专业性和可读性

输出格式（JSON）：
{
    "title": "报告标题",
    "chapters": [
        {
            "id": 1,
            "title": "章节标题",
            "description": "章节内容描述",
            "needs_visualization": true/false,
            "visualization_prompt": "如果需要可视化，提供图表生成提示词"
        }
    ]
}
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"领域：{domain}\n主题：{topic}\n参考资料：{content_data}")
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
        return json.dumps({"error": f"生成结构失败: {str(e)}"}, ensure_ascii=False)

@tool
def generate_chapter_content(chapter_title: str, chapter_description: str, content_data: str) -> str:
    """
    根据章节要求和参考内容生成章节文本
    
    Args:
        chapter_title: 章节标题
        chapter_description: 章节描述
        content_data: JSON格式的参考内容数据
    
    Returns:
        生成的章节文本内容
    """
    ctx = request_context.get() or new_context(method="generate_chapter_content")
    
    client = LLMClient(ctx=ctx)
    
    system_prompt = """你是一位专业的学术写作助手。根据章节要求和参考资料，生成高质量的学术章节内容。

要求：
1. 内容应该专业、准确、有深度
2. 引用参考资料中的观点和数据
3. 保持逻辑连贯性
4. 字数控制在500-1000字
5. 使用学术化的语言风格
6. 适当分段，提高可读性
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"章节标题：{chapter_title}\n章节要求：{chapter_description}\n参考资料：{content_data}")
    ]
    
    try:
        response = client.invoke(
            messages=messages,
            model="doubao-seed-1-8-251228",
            temperature=0.7
        )
        
        return get_text_content(response.content)
        
    except Exception as e:
        return f"生成章节内容失败: {str(e)}"

@tool
def generate_final_report(article_structure: str, chapter_contents: str, images: str, references: str) -> str:
    """
    综合所有内容生成最终报告
    
    Args:
        article_structure: JSON格式的文章结构
        chapter_contents: JSON格式的各章节内容
        images: JSON格式的图片信息
        references: JSON格式的参考文献
    
    Returns:
        完整的Markdown格式报告
    """
    ctx = request_context.get() or new_context(method="generate_final_report")
    
    client = LLMClient(ctx=ctx)
    
    system_prompt = """你是一位专业的学术报告排版专家。将所有内容整合为一份完整的Markdown格式学术报告。

要求：
1. 使用标准的Markdown格式
2. 正确插入图片（使用![图片描述](图片URL)格式）
3. 在适当位置引用参考文献
4. 保持专业的学术风格
5. 确保结构清晰，层次分明
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"""文章结构：{article_structure}
各章节内容：{chapter_contents}
图片信息：{images}
参考文献：{references}""")
    ]
    
    try:
        response = client.invoke(
            messages=messages,
            model="doubao-seed-1-8-251228",
            temperature=0.7
        )
        
        return get_text_content(response.content)
        
    except Exception as e:
        return f"生成最终报告失败: {str(e)}"
