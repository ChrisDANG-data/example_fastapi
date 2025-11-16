from fastapi import Depends, Response,HTTPException,status, APIRouter
from ..database import Session,get_db
from typing import Optional,List
from .. import schemas,models,util
from psycopg2 import IntegrityError
import traceback

router = APIRouter(
    prefix="/users",
    tags = ['users']
)



@router.post("/", status_code=status.HTTP_201_CREATED)
def create_users(user: schemas.Users, db: Session = Depends(get_db)):
    # Hash the password using the updated hash function (with SHA256 + bcrypt)
    hashed_password = util.hash_password(user.password)
    user.password = hashed_password
    
    # Create new user
    new_user = models.User(**user.model_dump())
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"

        )
    # except Exception as e:
    #     db.rollback()
    #     # log full traceback
        
    #     traceback.print_exc()
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail="Internal Server Error"
    #     )

# get specific user 
@router.get("/{id}",response_model=schemas.UserOut)
def getuser(id:int, db : Session =Depends(get_db)):
    # print(db.query(models.User).all())
    
    finduser= db.query(models.User).filter(models.User.id == id).first()
   
    if not finduser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{id} was not found "
            ) 
    return finduser