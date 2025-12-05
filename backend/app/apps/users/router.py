from fastapi import APIRouter, status
from apps.users.schemas import UserCreate, UserCreated

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/create", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserCreated:
    user = UserCreated(id=12, **user.dict())
    return user
