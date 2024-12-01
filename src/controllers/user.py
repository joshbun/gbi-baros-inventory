from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..lib.database.main import get_db
from ..utils.password import hash_password, verify_password
from ..models.user import User
from ..schemas.auth import authenticate
from pydantic import BaseModel

router = APIRouter()

class SignupModel(BaseModel):
    name:str
    email:str
    password:str
    
    class Config:
        orm_mode = True

class LoginModel(BaseModel):
    email:str
    password:str

@router.post("/signup", dependencies=[Depends(authenticate)])
async def signup(data:SignupModel, db:Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = User(name=data.name, email=data.email, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", dependencies=[Depends(authenticate)])
async def login(data:LoginModel, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    return user