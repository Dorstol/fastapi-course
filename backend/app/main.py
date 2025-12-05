from app_factory import get_application
from apps.users.router import router as users_router

app = get_application()

app.include_router(users_router)