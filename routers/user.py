from fastapi import APIRouter
from models.user import User
from services.user_service import *
from config.mongo_connection import *
from models.user import *
from schemas.user import User, UserCreate

connection = connect_to_mongodb('test', 'users')
router_users = APIRouter()

@router_users.get('/users', tags=["Users"])
def get_users_function():
    return get_users()

@router_users.get('/user/', tags=["Users"])
def get_user_function(user_username: str):
    return get_user(user_username)

@router_users.post('/user/', tags=["Users"])
def create_user_function(user: UserCreate):
    return create_user(user)

@router_users.put('/user/', tags=["Users"])
def update_user_function(user_username: str, user: UserCreate):
    return update_user(user_username, user)

@router_users.delete('/user/', tags=["Users"])
def delete_user_function(user_username: str):
    return delete_user(user_username)