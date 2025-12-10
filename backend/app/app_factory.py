from fastapi import FastAPI, Request
from scalar_fastapi import get_scalar_api_reference

from apps.info.router import router as info_router
from settings import settings


def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        root_path="/api",
    )

    if settings.DEBUG:
        app.include_router(info_router)

    @app.get("/scalar", include_in_schema=False)
    async def scalar_html(request: Request):
        return get_scalar_api_reference(
            openapi_url=request.scope.get("root_path", "") + app.openapi_url,
            title=app.title,
        )

    return app
