

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, models, schemas, util,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login",response_model=schemas.Token)
def login(user_login: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):
  
    user = db.query(models.User).filter(models.User.email == user_login.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not util.verify_password(user_login.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    token = oauth2.create_access_token(data = {"user_id":user.id})
    # return {"acess token":"example"}

    return {"access_token": token, "token_type": "bearer"}  
    

# @router.post("/userslog")
# def create_user(user: schemas.UserCredential, db: Session = Depends(database.get_db)):
#     print(type(user.password))  # should be <class 'str'>



