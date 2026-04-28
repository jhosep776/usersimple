from fastapi import APIRouter
from config.db import conn
from models.user import users
from services import user as service
from schemas.user import UserCreate ,UserUpdate


user = APIRouter()

@user.get("/")
async def get_all_users():
    return service.get_users()

@user.get("/{id}")
async def get_one_user(id:int):
    return service.get_user_by_id(id)

@user.post("/")
async def create_user(user:UserCreate):
    return service.create_user(user)

@user.put("/{id}")
async def update_user(id:int ,user:UserUpdate):
    return service.update_user(id, user)

@user.delete("/{id}")
async def delete_user(id:int):
    return  service.delete_user(id)
