from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

login_users = APIRouter()

@login_users.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123":
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)
    else:
        return JSONResponse(status_code=401, content={"message": "Credenciales invalidas, intentelo de nuevo"})
