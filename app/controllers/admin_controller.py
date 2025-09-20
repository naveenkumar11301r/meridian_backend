# admin_controller.py

from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import timedelta
from app.database import db
from app.admin import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def login_user(user: dict):
    db_user = db.admin.find_one({"username": user["username"]})  # changed users → admin
    if not db_user or not pwd_context.verify(user["password"], db_user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"sub": db_user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

def create_user(user: dict):
    if db.admin.find_one({"username": user["username"]}):  # changed users → admin
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    hashed_password = pwd_context.hash(user["password"])
    db_user = {"username": user["username"], "hashed_password": hashed_password}
    db.admin.insert_one(db_user)  # changed users → admin
    return {"username": user["username"]}

