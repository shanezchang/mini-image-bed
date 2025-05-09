from typing import Optional
from fastapi import FastAPI, Request, Header


def get_real_ip(request: Request, x_forwarded_for: Optional[str] = Header(None)):
    """综合获取真实IP的优先级逻辑"""
    if x_forwarded_for:
        # 处理多级代理链：X-Forwarded-For: client, proxy1, proxy2
        client_ip = x_forwarded_for.split(",")[0].strip()
    elif request.headers.get("X-Real-IP"):
        client_ip = request.headers["X-Real-IP"]
    else:
        client_ip = request.client.host  # 最后回退

    return client_ip
