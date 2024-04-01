from models.user import User
from config.jwt_manager import create_token
from fastapi import Response
from datetime import datetime, timedelta

def user_login(username: str, password: str, email: str, response: Response):
  user = None
  if username and email is None:
    user = User.objects(username=username, password=password).first()
  elif email and username is None:
    user = User.objects(email=email, password=password).first()

  if user:
    # User data for response (without password)
    user_data = {
        "_id": str(user.id),
        "username": user.username,
        "email": user.email,
        "is_active": user.is_active,
        "exp": int((datetime.now() + timedelta(minutes=30)).timestamp())
    }

    # Create JWT token with expiration
    token = create_token(user_data)

    response.status_code = 200
    response.headers["Authorization"] = f"Bearer {token}"
    return {"message": "Login successful"}
  else:
    response.status_code = 404
    return {"error": "User not found"}

