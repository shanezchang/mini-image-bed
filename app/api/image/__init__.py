from fastapi import APIRouter
from . import open

router = APIRouter(prefix="/image")
router.include_router(open.router)
