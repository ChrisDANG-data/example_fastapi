from fastapi import Depends, Response,HTTPException,status, APIRouter
from ..database import Session, get_db
from typing import Optional,List
from .. import schemas,models,oauth2
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)



my_posts=[{"title":"my first post","message":"my first post message","is_published":"True", "id":1},{"title":"my seconde post","message":"my second post message","is_published":"False","id":2}]




@router.get("/",response_model=List[schemas.PostOut])
def test_alchemy(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
                 limit : int =10, stepoff : int =2 , search: Optional[str]="" ):

    #posts = db.query(models.Post).filter(models.Post.title.ilike(f"%{search.strip()}%")).limit(limit).offset(stepoff).all()
    results = db.query(models.Post,func.count(models.Vote.post_id).label("posts")).join(models.Vote,models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(
    models.Post.title.ilike(f"%{search.strip()}%")).limit(limit).offset(stepoff).all()
    output = [{"post": post, "votes": votes} for post, votes in results]
    #print(posts)
    #print(results)
    return output

@router.post("/createposts" , status_code = status.HTTP_201_CREATED,response_model=schemas.Post)
def createclasspost( post: schemas.PostCreate, db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):  
    
    new_post = models.Post(owner_id =current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post




def find_id(id):
    for p in my_posts:
        if p["id"]==id:
            return p
        
def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i

@router.get("/{id}",response_model=schemas.PostOut)
def get_post_by_id(id: int, db : Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    #postget = db.query(models.Post).filter(models.Post.id == id).first()
    postget =db.query(models.Post,func.count(models.Vote.post_id).label("posts")).join(models.Vote,models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not postget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Post with id {id} was not found"
        )
    post, votes = postget
    return {"post": post, "votes": votes}    
    #return  postget




@router.delete("/del/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} is not in the list")
    print(post.id)
    print(current_user.id)
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= " Not authrized for this request")
    db.delete(post)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def update_title(id:int, updatedpost: schemas.PostCreate, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id==id)
    
    post = post_query.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} is not in the list")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= " Not authrized for this request")
    
    post_query.update( updatedpost.model_dump(),synchronize_session=False)

    db.commit() 
    # db.refresh(post_query)   
  
    return post_query.first()





#@app.get("/")
#def root():
    #return {"message": "Hello learn api with youtube!!!!!"}


# @app.get("/posts")
# def sendpost():
#     cursor.execute('''select * from posts''')
#     post = cursor.fetchall()
#     return {"message": post}


#@app.post("/createmyposts")


#def createapost( myfirstpost: dict= Body(...)):
    #print(myfirstpost)
    #return {"message": f" title: {myfirstpost['title']}  post : {myfirstpost['message']}"}



    



#def createclasspost(newepost:post):
    #post_dict = newepost.model_dump()    
    #post_dict['id'] = randrange(0,1000)
    #my_posts = my_posts.append (post_dict)   
    
    #return(post_dict)  #**post.model_dump() title = post.title, message = post.message, published = post.published


 # cursor.execute(''' insert into posts (title, message) Values (%s,%s) returning * ''',(newepost.title,newepost.message))
    # post = cursor.fetchone()
    # conn.commit()


    # post = find_id(id)
    # cursor.execute('''SELECT * FROM posts WHERE id = %s ''', (str(id),))
    # post = cursor.fetchone()
            

# @app.get("/posts/{id}")
# def getpostbyid(id:int):
#     #post = find_id(id)
#     cursor.execute('''select * from posts where id = %s returning * ''', (str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"{str(id)} was not found")
#     return {"message": f"find {post}"}

    # index = find_index(id)
    # cursor.execute('''delete from posts where id= %s returning * ''', (str(id),))
    # deleted_post =cursor.fetchone()
    # conn.commit()
    # my_posts.pop(deleted_post)

