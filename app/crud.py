from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, username=user.username, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Group).offset(skip).limit(limit).all()

def create_group(db: Session, group: schemas.GroupCreate, user_id: int):
    db_group = models.Group(**group.dict(), admin_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_ads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Advertisement).offset(skip).limit(limit).all()

def create_ad(db: Session, ad: schemas.AdvertisementCreate):
    db_ad = models.Advertisement(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

# Previous CRUD operations...

def get_friend_requests(db: Session, user_id: int):
    return db.query(models.FriendRequest).filter(models.FriendRequest.to_user_id == user_id).all()

def create_friend_request(db: Session, from_user_id: int, to_user_id: int):
    friend_request = models.FriendRequest(from_user_id=from_user_id, to_user_id=to_user_id)
    db.add(friend_request)
    db.commit()
    db.refresh(friend_request)
    return friend_request

def accept_friend_request(db: Session, request_id: int):
    request = db.query(models.FriendRequest).filter(models.FriendRequest.id == request_id).first()
    if request:
        user1 = db.query(models.User).filter(models.User.id == request.from_user_id).first()
        user2 = db.query(models.User).filter(models.User.id == request.to_user_id).first()
        user1.friends.append(user2)
        user2.friends.append(user1)
        db.delete(request)
        db.commit()
    return request

def deny_friend_request(db: Session, request_id: int):
    request = db.query(models.FriendRequest).filter(models.FriendRequest.id == request_id).first()
    if request:
        db.delete(request)
        db.commit()
    return request

def create_group(db: Session, group: schemas.GroupCreate, user_id: int):
    db_group = models.Group(**group.dict(), admin_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def join_group(db: Session, user_id: int, group_id: int):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    group.members.append(user)
    db.commit()
    return group

def leave_group(db: Session, user_id: int, group_id: int):
    group = db.query(models.Group).filter(models.Group.id == group_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    group.members.remove(user)
    db.commit()
    return group

def get_advertisements(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Advertisement).offset(skip).limit(limit).all()

def create_advertisement(db: Session, ad: schemas.AdvertisementCreate):
    db_ad = models.Advertisement(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad


def get_user_posts(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).offset(skip).limit(limit).all()




