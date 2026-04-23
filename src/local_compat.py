"""本地兼容层 - 替代Coze内部工具包，使代码可以在本地独立运行"""
from typing import Optional, Dict, Any
from contextvars import ContextVar

# 模拟 request_context
_request_context: ContextVar[Optional[Dict[str, Any]]] = ContextVar(
    "request_context",
    default=None
)

class RequestContext:
    """模拟的请求上下文"""
    def __init__(self, method: str = "local", **kwargs):
        self.method = method
        self.kwargs = kwargs
        self.data = kwargs
    
    def get(self):
        """获取当前上下文"""
        return self

def new_context(method: str = "local", **kwargs) -> RequestContext:
    """
    模拟 coze_coding_utils.runtime_ctx.context.new_context
    
    创建一个新的请求上下文对象，用于本地运行
    
    Args:
        method: 方法名
        **kwargs: 其他参数
    
    Returns:
        RequestContext对象
    """
    ctx = RequestContext(method=method, **kwargs)
    _request_context.set(ctx)
    return ctx

def request_context() -> RequestContext:
    """
    模拟 coze_coding_utils.log.write_log.request_context
    
    获取当前请求上下文
    
    Returns:
        RequestContext对象
    """
    ctx = _request_context.get()
    if ctx is None:
        ctx = RequestContext(method="default")
        _request_context.set(ctx)
    return ctx

def default_headers(ctx: Optional[Any] = None) -> Dict[str, str]:
    """
    模拟 coze_coding_utils.runtime_ctx.context.default_headers
    
    返回默认的HTTP headers
    
    Args:
        ctx: 上下文对象（可选）
    
    Returns:
        headers字典
    """
    headers = {
        "User-Agent": "Academic-Report-Agent/1.0",
        "Accept": "application/json",
    }
    
    # 火山引擎需要的特殊header
    if ctx and hasattr(ctx, 'method') and ctx.method:
        headers["X-Client-Request-Id"] = "Coze,Integrations"
    
    return headers

# 兼容性导出
__all__ = [
    "new_context",
    "request_context",
    "default_headers",
    "RequestContext",
]
