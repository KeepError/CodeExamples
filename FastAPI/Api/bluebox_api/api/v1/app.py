from fastapi.applications import FastAPI

from .auth.routers import auth_router
from .middlewares import ExceptionsMiddleware
from .user.routers import users_router


def get_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(ExceptionsMiddleware)

    app.include_router(auth_router)
    app.include_router(users_router)

    return app
