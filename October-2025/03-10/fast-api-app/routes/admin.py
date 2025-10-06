from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User , Post
from schemas import UserCreate, UserUpdate, UserOut , AdminPostQueryOut , AdminPostResponse
from email_config import send_password_email, generate_random_password
import logging
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_model=list[UserOut])
def read_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/users/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserOut)
async def create_user(
    user_data: UserCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    password = generate_random_password()

    user = User(**user_data.dict(), password=password)
    db.add(user)
    db.commit()
    db.refresh(user)

    try:
        background_tasks.add_task(send_password_email, user.email, password)
    except Exception as e:
        logging.error(f"Failed to send password email: {e}")

    return user

@router.put("/users/{id}", response_model=UserOut)
def update_user(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": f"User with ID {id} deleted"}

@router.get("/queries", response_model=List[AdminPostQueryOut])
def get_all_user_queries(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@router.get("/queries/{user_id}", response_model=List[AdminPostQueryOut])
def get_queries_by_user(user_id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.uid == user_id).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No queries found for this user")
    return posts

from schemas import AdminPostResponse

@router.put("/queries/{post_id}/respond")
def respond_to_query(
    post_id: int,
    response_data: AdminPostResponse,
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.pid == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.response = response_data.response
    db.commit()
    db.refresh(post)

    return {
        "post_id": post.pid,
        "response": post.response
    }
