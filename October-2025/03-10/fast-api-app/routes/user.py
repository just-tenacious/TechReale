from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Post
from schemas import UserOut, TokenResponse, PasswordChangeRequest,PostCreate,PostOut
from auth import create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/user", tags=["User"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/profile/{id}", response_model=UserOut)
def get_profile(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/login", response_model=TokenResponse)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username, User.password == form_data.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Credentials")
    token = create_access_token({"sub": str(user.user_id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/change-password")
def change_password(
    password_data: PasswordChangeRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    current_user = db.merge(current_user)
    if current_user.password != password_data.old_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Old password is incorrect")
    current_user.password = password_data.new_password
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    return {"msg": "Password updated successfully"}

@router.post('/post', response_model=PostOut)
def post_query(
    post_data: PostCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post = Post(post=post_data.post, uid=current_user.user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
