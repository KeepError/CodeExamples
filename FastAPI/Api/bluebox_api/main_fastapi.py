from fastapi import FastAPI

from api.v1 import app as app_v1

app = FastAPI()

app.mount("/v1", app_v1.get_app())
