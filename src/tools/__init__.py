"""工具模块"""
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

__all__ = [
    "search_academic_data",
    "get_available_domains",
    "generate_article_structure",
    "generate_chapter_content",
    "generate_final_report",
    "generate_academic_image",
    "generate_keyword_cloud",
    "generate_citation_chart",
    "generate_timeline_chart",
    "generate_chapter_visualization",
    "generate_references"
]
