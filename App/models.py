from datetime import datetime
import string
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey, Integer, String,  text, Column
from sqlalchemy.orm import relationship, Mapped

from .database import Base


class Post(Base):
    __tablename__ ="posts"
    id = Column(Integer, primary_key =True , nullable =False)
    title = Column (String,nullable=False)
    message = Column (String, nullable= False )    
    published = Column( Boolean, server_default='True', nullable = False )
    createdon =Column (TIMESTAMP(timezone=True), nullable= False, server_default= text("NOW()"))
    owner_id = Column (Integer, ForeignKey("users.id", ondelete="CASCADE"),  nullable = False)
    owner : Mapped["User"] =relationship("User",back_populates="posts") 
    


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    createdon = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))   
    posts = relationship("Post",back_populates="owner" )

class Vote(Base):
    __tablename__="votes"
    id = Column(Integer, primary_key=True, nullable = False)
    post_id =Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)


class New_User(Base):
    __tablename__ = "new_users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    createdon = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    posts = relationship("Post",back_populates="owner" )
