"""学术数据爬取工具"""
import json
from typing import List, Dict, Optional
from langchain.tools import tool
from coze_coding_dev_sdk import SearchClient
from coze_coding_utils.log.write_log import request_context
from coze_coding_utils.runtime_ctx.context import new_context

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

@tool
def search_academic_data(domain: str, query: str, count: int = 10) -> str:
    """
    搜索学术数据，返回精选正文内容和结构化元数据
    
    Args:
        domain: 学术领域 (如: computer_science, artificial_intelligence等)
        query: 搜索关键词
        count: 返回结果数量
    
    Returns:
        JSON格式的搜索结果，包含正文内容和结构化元数据
    """
    ctx = request_context.get() or new_context(method="search_academic_data")
    
    client = SearchClient(ctx=ctx)
    
    # 构建搜索查询
    search_query = f"{ACADEMIC_DOMAINS.get(domain, domain)} {query} academic research"
    
    try:
        # 搜索学术内容
        response = client.web_search(
            query=search_query,
            count=count
        )
        
        # 整理结果
        results = {
            "domain": domain,
            "query": query,
            "content_data": [],  # 正文数据（精选）
            "structured_data": []  # 结构化数据（用于画图）
        }
        
        for idx, item in enumerate(response.web_items):
            # 正文数据（精选少数）
            if idx < 3:
                results["content_data"].append({
                    "title": item.title,
                    "content": item.snippet,
                    "url": item.url,
                    "summary": item.summary if item.summary else item.snippet[:200]
                })
            
            # 结构化数据（全部）
            results["structured_data"].append({
                "title": item.title,
                "authors": extract_authors(item.title),
                "keywords": extract_keywords(item.title + " " + (item.snippet or "")),
                "year": extract_year(item.publish_time),
                "country": "Unknown",  # 需要更复杂的提取逻辑
                "journal": item.site_name,
                "url": item.url,
                "citations": 0,  # 模拟引用数
                "publish_time": item.publish_time
            })
        
        return json.dumps(results, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": f"搜索失败: {str(e)}",
            "domain": domain,
            "query": query
        }, ensure_ascii=False)

def extract_authors(title: str) -> List[str]:
    """从标题中提取作者（简化版）"""
    # 实际应用中需要更复杂的NLP处理
    return ["Unknown Author"]

def extract_keywords(text: str) -> List[str]:
    """提取关键词（简化版）"""
    # 实际应用中可以使用TF-IDF等方法
    words = text.split()
    keywords = [word for word in words if len(word) > 3][:10]
    return keywords[:10] if keywords else ["research", "academic"]

def extract_year(publish_time: Optional[str]) -> int:
    """提取年份"""
    if publish_time:
        # 尝试从时间字符串中提取年份
        import re
        year_match = re.search(r'(\d{4})', publish_time)
        if year_match:
            return int(year_match.group(1))
    return 2024

@tool
def get_available_domains() -> str:
    """获取可用的学术领域列表"""
    return json.dumps(ACADEMIC_DOMAINS, ensure_ascii=False, indent=2)
