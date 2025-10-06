from sqlalchemy import Integer,String,Column,Date
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from database import Base

class User(Base):
  __tablename__="user_data"
  user_id=Column(Integer,primary_key=True,index=True)
  name=Column(String)
  dob=Column(Date)
  address=Column(String)
  email=Column(String,unique=True,index=True)
  password=Column(String)
  posts = relationship("Post", back_populates="user") 

class Post(Base):
  __tablename__ = "post"
  pid = Column(Integer, primary_key=True, index=True)
  post = Column(String, nullable=False)
  response = Column(String, nullable=True)
  uid = Column(Integer, ForeignKey("user_data.user_id"))

  user = relationship("User", back_populates="posts")