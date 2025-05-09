from fastapi import APIRouter
from fastapi import Request

from util.get_ip_from_nginx import get_real_ip
from util.logger import log

router = APIRouter(prefix="/open", tags=["image bed"])


@router.get("/")
async def list_items():
    return [{"id": 1, "name": "Foo"}]

@router.get("/oo")
async def read_root(request: Request):
    client_ip = get_real_ip(request)
    log.info(f"invoke /image/open/oo, client_ip:{client_ip}")
    return {"Hello": "World", "client_ip": client_ip}
