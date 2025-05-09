from typing import Generic, TypeVar, Optional, Dict, Any, List
from pydantic import BaseModel, Field
from fastapi import status


class BaseResponse(BaseModel):
    code: int = Field(default=status.HTTP_200_OK, description="状态码")
    message: str = Field(default="success", description="提示信息")
    data: object = Field(default=None, description="返回数据")

# 使用 BaseResponse 的一个示例

