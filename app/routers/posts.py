from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from app.database import get_db
from ..auth import get_current_active_user

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.get_posts(db=db, skip=skip, limit=limit)

@router.get("/user/{user_id}", response_model=List[schemas.Post])
def read_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

@router.get("/friends", response_model=List[schemas.Post])
def read_friends_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    friends_posts = []
    for friend in current_user.friends:
        friend_posts = crud.get_user_posts(db=db, user_id=friend.id, skip=skip, limit=limit)
        friends_posts.extend(friend_posts)
    return friends_posts
