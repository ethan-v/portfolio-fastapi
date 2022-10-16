from fastapi import FastAPI
from starlette.middleware import Middleware
from pyfolio.services.image_service import ImageService


def exclude_middleware(app: FastAPI, target: str) -> FastAPI:
    new_middlewares: list[Middleware] = []
    for middleware in app.user_middleware:
        if not middleware.cls.__name__ == target:
            new_middlewares.append(middleware)
    app.user_middleware = new_middlewares
    app.middleware_stack = app.build_middleware_stack()
    return app


def objectKeyExist(key, dict_json):
    if key in dict_json:
        return True
    return False


def clean_uploaded_image(real_file_path: str):
    ImageService().clean_resize_images(real_file_path)