import os


class Config:
    USERS_SERVICE_URL = os.getenv("USERS_SERVICE_URL")
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")
