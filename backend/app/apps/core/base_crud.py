from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from apps.core.base import Base


class BaseCRUDManager(ABC):
    model: type[Base] = None


    @abstractmethod
    def __init__(self):
        pass


    async def create_instance(self, *, session: AsyncSession, **kwargs) -> Optional[Base]:
        instance = self.model(**kwargs)
        session.add(instance)

        try:
            await session.commit()
            return instance
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
