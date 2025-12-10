from fastapi import APIRouter, status, Depends
from apps.users.schemas import UserCreate, UserCreated
from sqlalchemy.ext.asyncio import AsyncSession
from apps.core.dependencies import get_async_session
from apps.users.crud import user_manager

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/create", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: UserCreate, session: AsyncSession = Depends(get_async_session)
) -> UserCreated:
    created_user = await user_manager.create_user(new_user=new_user, session=session)
    return created_user
