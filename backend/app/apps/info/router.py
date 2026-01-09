import socket

from fastapi import APIRouter
from .schemas import BackendInfo, DatabaseInfo
from settings import settings

from apps.services.betterstack_service import betterstack_logger

router = APIRouter(
    prefix="/info",
    tags=["Info"],
)


@router.get("/backend", response_model=BackendInfo)
async def get_backend_info() -> BackendInfo:
    """Get current backend info"""

    betterstack_logger.info(
        "User logged in",
        extra={
            "user_id": 123,
            "debug_info": {"function": "get_backend_info", "status": "OK"},
        }
    )

    betterstack_logger.error(
        "User logged in",
        extra={
            "user_id": 321,
            "debug_info": {"function": "get_backend_info", "status": "ERROR"},
        }
    )

    
    return {"backend": socket.gethostname()}


@router.get("/database_url", response_model=DatabaseInfo)
async def get_database_url() -> DatabaseInfo:
    """Get current database url"""
    return {"database": settings.database_async_url}


@router.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0  # noqa
