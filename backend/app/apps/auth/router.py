from apps.auth.auth_handler import auth_handler
from apps.auth.schemas import LoginResponseShema
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
) -> LoginResponseShema:
    login_response: LoginResponseShema = await auth_handler.get_login_token_pairs(
        session=session,
        data=data,
    )
    return login_response
