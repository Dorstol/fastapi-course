from fastapi import APIRouter, status, Depends
from apps.users.schemas import UserCreate, UserCreated
from sqlalchemy.ext.asyncio import AsyncSession
from apps.core.dependencies import get_async_session
from apps.users.crud import user_manager
from apps.auth.dependencies import get_current_user
from apps.users.models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/user-info")
async def user_info(user: User = Depends(get_current_user)) -> UserCreated:
    return UserCreated.from_orm(user)
