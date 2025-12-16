from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from apps.core.dependencies import get_async_session
from apps.users.crud import user_manager
from apps.users.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/login")
async def user_login(
    data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session),
):
    user = await user_manager.get(field=User.email, field_value=data.username, session=session,)
    if not user:
        raise HTTPException(detail="User not found", status_code=404,)
    return {"data": [data.username, data.password]}
