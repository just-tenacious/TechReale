# main.py

from fastapi import FastAPI
from routes import admin, user

app = FastAPI()

app.include_router(admin.router)
app.include_router(user.router)
