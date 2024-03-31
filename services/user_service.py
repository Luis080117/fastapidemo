from models.user import User
from schemas.user import UserCreate

def create_user(user: UserCreate):
    user = User(username=user.username, email=user.email, password=user.password, is_active=user.is_active)
    user.save()
    return {"message": "User created successfully"}

def get_users():
    users = User.objects()
    serialized_users = [{"_id": str(user.id), "username": user.username, "email": user.email, "is_active": user.is_active} for user in users]
    return {"users": serialized_users}

def get_user(user_username: str) -> dict:
    user = User.objects(username=user_username)
    serialized_user = [{"_id": str(user.id), "username": user.username, "email": user.email, "is_active": user.is_active} for user in user]
    return {"user": serialized_user}

def delete_user(user_username: str):
    user = User.objects(username=user_username)
    if user:
        user.delete()
        return {"message": "User deleted successfully"}
    else:
        return {"error": "User not found"}

def update_user(user_username: str, new_user: UserCreate):
    existing_user = User.objects(username=user_username).first()
    if not existing_user:
        return "No user found"
    existing_user.username = new_user.username
    existing_user.email = new_user.email
    existing_user.password = new_user.password
    existing_user.is_active = new_user.is_active
    existing_user.save()
    return {"message": "User updated successfully"}
