from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from app.database import get_db
from ..auth import get_current_active_user

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.create_group(db=db, group=group, user_id=current_user.id)

@router.post("/{group_id}/join", response_model=schemas.Group)
def join_group(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.join_group(db=db, user_id=current_user.id, group_id=group_id)

@router.post("/{group_id}/leave", response_model=schemas.Group)
def leave_group(group_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return crud.leave_group(db=db, user_id=current_user.id, group_id=group_id)
