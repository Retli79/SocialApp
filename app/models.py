from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

friendship = Table(
    'friendship',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('friend_id', Integer, ForeignKey('users.id'))
)

group_membership = Table(
    'group_membership',
    Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    friends = relationship(
        "User",
        secondary=friendship,
        primaryjoin=id==friendship.c.user_id,
        secondaryjoin=id==friendship.c.friend_id
    )
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="posts")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(Text)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship("User")
    members = relationship(
        "User",
        secondary=group_membership,
        back_populates="groups"
    )

class Advertisement(Base):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
