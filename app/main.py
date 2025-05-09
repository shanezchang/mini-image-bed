# import os
# import sys
#
# # project base path
# PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# sys.path.append(PROJ_DIR)

from util.logger import log
from core.config import WEB_PORT, WEB_HOST

from typing import Union
from typing import Optional

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Request, Header

app = FastAPI()


def get_real_ip(request: Request, x_forwarded_for: Optional[str] = Header(None)) -> str:
    """综合获取真实IP的优先级逻辑"""
    client_ip = "0.0.0.0"
    try:
        if x_forwarded_for:
            # 处理多级代理链：X-Forwarded-For: client, proxy1, proxy2
            client_ip = x_forwarded_for.split(",")[0].strip()
        elif request.headers.get("X-Real-IP"):
            client_ip = request.headers["X-Real-IP"]
        else:
            client_ip = request.client.host  # 最后回退
    except Exception as e:
        log.warn(f"get_real_ip failed:{e}")

    return client_ip


@app.get("/")
def read_root(request: Request):
    client_ip = get_real_ip(request)
    log.info(f"invoke /, client_ip:{client_ip}")
    return {"Hello": "World", "client_ip": client_ip}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# 定义数据模型，对应JSON中的数据结构
class ScanParam(BaseModel):
    code_src_name: str
    code_branch_name: str


@app.post("/do_code_scan")
def do_code_scan(param: ScanParam):
    log.info(f"invoke /do_code_scan, param:{param}")
    user_dict = param.model_dump()
    log.info(user_dict)
    return {"code": "0", "message": "OK", "data": param}


if __name__ == "__main__":
    uvicorn.run(app, host=WEB_HOST, port=WEB_PORT)
