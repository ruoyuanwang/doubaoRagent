"""图像生成工具，包括图表、词云等可视化功能"""
import json
from typing import List, Dict
from langchain.tools import tool
from coze_coding_dev_sdk import ImageGenerationClient
from coze_coding_utils.log.write_log import request_context
from coze_coding_utils.runtime_ctx.context import new_context

@tool
def generate_academic_image(prompt: str, style: str = "professional") -> str:
    """
    使用AI生成学术相关图像
    
    Args:
        prompt: 图像描述提示词
        style: 图像风格 (professional, scientific, minimalist等)
    
    Returns:
        JSON格式的图像URL信息
    """
    ctx = request_context.get() or new_context(method="generate_academic_image")
    
    client = ImageGenerationClient(ctx=ctx)
    
    # 构建完整提示词
    full_prompt = f"Academic {style} style: {prompt}. Professional scientific visualization, white background, high quality, clear labels."
    
    try:
        response = client.generate(
            prompt=full_prompt,
            size="2K"
        )
        
        if response.success:
            return json.dumps({
                "success": True,
                "image_url": response.image_urls[0],
                "prompt": prompt
            }, ensure_ascii=False)
        else:
            return json.dumps({
                "success": False,
                "error": response.error_messages
            }, ensure_ascii=False)
            
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"图像生成失败: {str(e)}"
        }, ensure_ascii=False)

@tool
def generate_keyword_cloud(structured_data: str) -> str:
    """
    从结构化数据生成关键词云
    
    Args:
        structured_data: JSON格式的结构化数据
    
    Returns:
        JSON格式的词云信息
    """
    ctx = request_context.get() or new_context(method="generate_keyword_cloud")
    
    try:
        data = json.loads(structured_data)
        
        # 收集所有关键词
        all_keywords = []
        for item in data.get("structured_data", []):
            keywords = item.get("keywords", [])
            all_keywords.extend(keywords)
        
        if not all_keywords:
            all_keywords = ["research", "academic", "study", "analysis", "data"]
        
        # 使用AI生成词云风格的图像
        keyword_text = ", ".join(all_keywords[:50])
        prompt = f"A professional academic word cloud visualization with keywords: {keyword_text}. Scientific style, blue color scheme, clean design."
        
        return generate_academic_image(prompt, style="scientific")
        
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"生成词云失败: {str(e)}"
        }, ensure_ascii=False)

@tool
def generate_citation_chart(structured_data: str) -> str:
    """
    生成引用关系图表
    
    Args:
        structured_data: JSON格式的结构化数据
    
    Returns:
        JSON格式的图表信息
    """
    ctx = request_context.get() or new_context(method="generate_citation_chart")
    
    try:
        data = json.loads(structured_data)
        
        prompt = """A professional academic citation network visualization showing relationships between research papers. 
        Scientific diagram style, nodes representing papers with titles, edges showing citation relationships. 
        Blue and white color scheme, professional academic design."""
        
        return generate_academic_image(prompt, style="scientific")
        
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"生成引用图表失败: {str(e)}"
        }, ensure_ascii=False)

@tool
def generate_timeline_chart(structured_data: str) -> str:
    """
    生成时间线图表
    
    Args:
        structured_data: JSON格式的结构化数据
    
    Returns:
        JSON格式的图表信息
    """
    ctx = request_context.get() or new_context(method="generate_timeline_chart")
    
    try:
        prompt = """A professional academic timeline visualization showing research development over years. 
        Scientific style, chronological order, key milestones marked, clear labels, blue color scheme."""
        
        return generate_academic_image(prompt, style="professional")
        
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"生成时间线图表失败: {str(e)}"
        }, ensure_ascii=False)

@tool
def generate_chapter_visualization(chapter_title: str, chapter_content: str, visualization_prompt: str) -> str:
    """
    为特定章节生成可视化图像
    
    Args:
        chapter_title: 章节标题
        chapter_content: 章节内容
        visualization_prompt: 可视化提示词
    
    Returns:
        JSON格式的图像信息
    """
    ctx = request_context.get() or new_context(method="generate_chapter_visualization")
    
    try:
        full_prompt = f"""Academic visualization for chapter: {chapter_title}. 
        {visualization_prompt}
        Based on content: {chapter_content[:200]}...
        Professional scientific style, white background, high quality."""
        
        return generate_academic_image(full_prompt, style="professional")
        
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"生成章节可视化失败: {str(e)}"
        }, ensure_ascii=False)
