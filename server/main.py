from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import uvicorn


from . import models, schemas, crud
from .database import engine, SessionLocal
from .routers import users


app = FastAPI()

app.include_router(users.router_users)

