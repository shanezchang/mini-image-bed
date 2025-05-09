from fastapi import status

from app.core.constant import ERROR_MSG
from app.model.response import BaseResponse


class Rsp(object):
    def __init__(self):
        pass

    @staticmethod
    def success(data: object = None) -> dict[str, object]:
        r = BaseResponse(data=data)
        return r.model_dump()

    @staticmethod
    def fail(code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, message: str = ERROR_MSG, data: object = None) -> dict[
        str, object]:
        r = BaseResponse(code=code, message=message, data=data)
        return r.model_dump()


rsp = Rsp()
