from fastapi.security import HTTPBearer
from config.jwt_manager import validate_token
from config.mongo_connection import connect_to_mongodb
from fastapi import Request, HTTPException
from models.user import User

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if not auth:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        token_data = validate_token(auth.credentials)
        if not token_data:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        collection = connect_to_mongodb('test', 'users')
        user = None
        if "_id" in token_data:  # Assuming you store user ID in the token
            user = User.objects(id=token_data["_id"]).first()
        elif "email" in token_data:  # Assuming email is unique
            user = User.objects(email=token_data["email"]).first()
        elif "username" in token_data:  # Assuming username is unique
            user = User.objects(username=token_data["username"]).first()
        
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return auth
