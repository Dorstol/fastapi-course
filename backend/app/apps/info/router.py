import socket

from fastapi import APIRouter
from .schemas import BackendInfo, DatabaseInfo
from settings import settings

router = APIRouter(
    prefix="/info",
    tags=["info"],
)


@router.get("/backend", response_model=BackendInfo)
async def get_backend_info() -> BackendInfo:
    """Get current backend info"""
    return {"backend": socket.gethostname(), "random_field": "random_value"}


@router.get("/database_url", response_model=DatabaseInfo)
async def get_database_url() -> DatabaseInfo:
    """Get current database url"""
    return {"database": settings.database_async_url}


@router.get("/sentry-debug")
async def trigger_error():
    pass
