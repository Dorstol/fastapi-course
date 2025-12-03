import socket

from fastapi import APIRouter

from settings import settings

router = APIRouter(
    prefix="/info",
    tags=["info"],
)


@router.get("/backend")
async def get_backend_info():
    """Get current backend info"""
    return {"backend": socket.gethostname()}


@router.get("/database_url")
async def get_database_url():
    """Get current database url"""
    return {"database": settings.database_async_url}
