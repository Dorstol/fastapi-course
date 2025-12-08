from sqlalchemy.ext.asyncio import AsyncSession
from apps.core.base_crud import BaseCRUDManager
from .schemas import UserCreate
from .models import User
from apps.auth.password_handler import PasswordHandler


class UserCRUDManager(BaseCRUDManager):
    def __init__(self):
        self.model = User

    async def create_user(
        self,
        new_user: UserCreate,
        session: AsyncSession,
    ) -> User:
        hasshed_password = await PasswordHandler.get_password_hash(new_user.password)
        user = await self.create_instance(
            session=session,
            name=new_user.name,
            email=new_user.email,
            hashed_password=hasshed_password,
        )
        return user

user_manager = UserCRUDManager()
