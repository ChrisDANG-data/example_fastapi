
from enum import IntEnum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime




# def Postbase(BaseModel):

#     id: Optional[int]
#     titre: str
#     content: str
#     is_published: bool = True
#     publishedon: datetime = Field(default_factory =datetime)

# class post(BaseModel):
#     title: str
#     message: str 
#     published: bool=True    
#     id: Optional[int] = None  
#     createdon: datetime = Field(default_factory=datetime.utcnow)

class UserCredential(BaseModel):
    email: EmailStr
    password: str
    
class PostBase(BaseModel):
    title: str
    message: str 
    published: bool=True

  

class UserOut(BaseModel):
    id : int
    email: EmailStr   

    class Config:
        from_attributes = True    

class Post(PostBase):
    owner_id :int
    createdon: datetime
    owner: UserOut    
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    post: Post
    votes: int
    class Config:
        from_attributes = True

class PostCreate(PostBase):
    pass
    class Config:
        from_attributes = True


class Users(BaseModel):
    email : EmailStr
    password : str






class Token(BaseModel):
    access_token:str
    token_type: str

# class TokenData(BaseModel):
#     id: Optional[str]= None


class TokenData(BaseModel):
    id: int | None = None


class VoteOut(BaseModel):
    post_id: int
    user_id: int
    

class VoteDir(IntEnum):
    REMOVE = 0
    ADD = 1
      
class Vote(BaseModel):
    post_id: int
    dir: VoteDir