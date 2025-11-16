from jose import JWSError,jwt
from datetime import datetime,timedelta, timezone
from fastapi import FastAPI, status,HTTPException, Depends

from .database import Session,get_db

from . import schemas,models
from .config import settings

from fastapi.security import OAuth2PasswordBearer
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET_KEY
#Algorith
#Expriation time

SECRET_KEY =settings.fastapi_secretkey
# """"09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7""""
ALGORITHM = settings.fastapi_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.fastapi_expire_time

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWSError:
        raise credentials_exception
    return token_data
    
def get_current_user(token: str = Depends(oauth_scheme), db: Session =Depends(get_db)):
        
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credential"
                                         ,headers={"WWW-Authenticate":"Bearer"})
    token_data =verify_access_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    return user






