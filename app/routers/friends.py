from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from app.database import get_db
from ..auth import get_current_active_user

router = APIRouter(
    prefix="/friends",
    tags=["friends"],
    responses={404: {"description": "Not found"}},
)

@router.post("/request", response_model=schemas.FriendRequest)
def send_friend_request(to_user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.id == to_user_id:
        raise HTTPException(status_code=400, detail="Cannot send friend request to yourself")
    return crud.create_friend_request(db=db, from_user_id=current_user.id, to_user_id=to_user_id)

@router.get("/requests", response_model=List[schemas.FriendRequest])
def get_friend_requests(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.get_friend_requests(db=db, user_id=current_user.id)

@router.post("/accept", response_model=schemas.FriendRequest)
def accept_friend_request(request_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    request = crud.accept_friend_request(db=db, request_id=request_id)
    if request.to_user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Cannot accept this friend request")
    return request

@router.post("/deny", response_model=schemas.FriendRequest)
def deny_friend_request(request_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    request = crud.deny_friend_request(db=db, request_id=request_id)
    if request.to_user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Cannot deny this friend request")
    return request
