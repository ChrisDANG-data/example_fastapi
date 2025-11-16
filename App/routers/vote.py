from fastapi import Depends, Response,HTTPException,status, APIRouter
from .. import schemas
from .. import database,oauth2,models
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/vote",
    tags=["Vote"]

)

@router.post("/",status_code=status.HTTP_201_CREATED) 
def vote(vote:schemas.Vote, db: Session  =Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{vote.post_id} are not founded ")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id , models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == schemas.VoteDir.ADD:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already posted on post id {vote.post_id}")
        new_post = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_post)
        db.commit()
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote is not found")
        vote_query.delete(synchronize_session= False)
        db.commit()
    return {"message":"successfully deleted vote"}
