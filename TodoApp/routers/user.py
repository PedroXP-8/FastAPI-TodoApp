from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import Annotated
from ..models import Users
from starlette import status
from pydantic import BaseModel, Field
from ..database import  SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/user',
    tags=['user']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class PasswrodRequest(BaseModel):
    old_password: str
    new_password: str = Field(min_length=3)

class PhoneNumberRequest(BaseModel):
    password:str
    new_phone_number: str = Field(min_length=11)

@router.get("/user", status_code=status.HTTP_200_OK)
async def read_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail=('Authentication failed'))
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    return user_model

@router.put('/update_user_password', status_code=status.HTTP_204_NO_CONTENT)
async def update_password(user: user_dependency, db: db_dependency, password_request: PasswrodRequest):
    if user is None:
        raise HTTPException(status_code=401, detail=('Authentication failed'))
    
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(password_request.old_password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail=('Error on password change'))
    user_model.hashed_password = bcrypt_context.hash(password_request.new_password)
    db.add(user_model)
    db.commit()
    

@router.put('/update_user_phone_number', status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(user: user_dependency, db: db_dependency, phone_number_request: PhoneNumberRequest):
    if user is None:
        raise HTTPException(status_code=401, detail=('Authentication failed'))
    
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(phone_number_request.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail=('Error on password'))
    user_model.phone_number = phone_number_request.new_phone_number
    db.add(user_model)
    db.commit()