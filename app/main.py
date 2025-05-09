import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from api.image import router as image_router
from core.config import WEB_PORT, WEB_HOST
from util.logger import log

app = FastAPI()
app.include_router(image_router)


# 定义数据模型，对应JSON中的数据结构
class ScanParam(BaseModel):
    code_src_name: str
    code_branch_name: str


@app.post("/do_code_scan")
async def do_code_scan(param: ScanParam):
    log.info(f"invoke /do_code_scan, param:{param}")
    user_dict = param.model_dump()
    log.info(user_dict)
    return {"code": "0", "message": "OK", "data": param}


if __name__ == "__main__":
    uvicorn.run(app, host=WEB_HOST, port=WEB_PORT)
