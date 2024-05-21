from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from app.database import get_db
from ..auth import get_current_active_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)

@router.post("/advertisement", response_model=schemas.Advertisement)
def create_advertisement(ad: schemas.AdvertisementCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create advertisements")
    return crud.create_advertisement(db=db, ad=ad)

@router.get("/advertisements", response_model=List[schemas.Advertisement])
def read_advertisements(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_advertisements(db=db, skip=skip, limit=limit)
