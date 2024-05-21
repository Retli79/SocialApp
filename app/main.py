from fastapi import FastAPI

from . import auth
from .database import engine
from .models import Base
from .routers import users, posts, groups, friends, admin

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(groups.router)
app.include_router(friends.router)
app.include_router(admin.router)
