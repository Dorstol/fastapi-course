from apps.auth.schemas import LoginResponseShema
from apps.auth.password_handler import PasswordHandler

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from settings import settings
from apps.users.crud import user_manager
from apps.users.models import User
from fastapi import HTTPException, status

class AuthHandler:
    def __init__(self):
        self.access_token_lifetime = settings.ACCESS_TOKEN_LIFETIME_MINUTES
        self.refresh_token_lifetime = settings.REFRESH_TOKEN_LIFETIME_MINUTES
        self.secret_key = settings.JWT_SECRET_KEY
        self.algorithm = settings.JWT_ALGORITHM

    async def get_login_token_pairs(
        self,
        session: AsyncSession,
        data: OAuth2PasswordRequestForm,
    ) -> LoginResponseShema:
        user: User | None = await user_manager.get(
            session=session,
            field=User.email,
            field_value=data.username,
        )
        if not user:
            raise HTTPException(
                detail="User not found",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        is_valid_password = await PasswordHandler.verify_password(
            plain_password=data.password,
            hashed_password=user.hashed_password,
        )
        if not is_valid_password:
            raise HTTPException(
                detail="Invalid password",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return LoginResponseSchema(
            access_token="access token",
            refresh_token="refresh token",
            expires_in=self.access_token_lifetime,
        )


auth_handler = AuthHandler()
