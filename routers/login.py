from fastapi import APIRouter, Response
from models.user import User
from services.login_service import user_login  # Assuming user_login is imported correctly
from config.mongo_connection import connect_to_mongodb
from schemas.user import User, UserCreate
from fastapi import Header

connection = connect_to_mongodb('test', 'users')
router_login = APIRouter()

@router_login.post('/login', tags=["Login"])
def login(username: str = Header(None, description="User's username"),
          password: str = Header(None, description="User's password"),
          email: str = Header(None, description="User's email"),
          response: Response = None):
    return user_login(username, password, email, response)
