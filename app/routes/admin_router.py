from fastapi import APIRouter, Form
from app.schemas.admin_schema import Token
from app.controllers.admin_controller import login_user, create_user

router = APIRouter()

@router.post("/login", response_model=Token)
def login(username: str = Form(...), password: str = Form(...)):
    return login_user({"username": username, "password": password})

@router.post("/users")
def register(username: str = Form(...), password: str = Form(...)):
    return create_user({"username": username, "password": password})
