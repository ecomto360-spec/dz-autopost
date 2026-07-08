from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    generated_text = Column(Text, nullable=True)
    generated_image_url = Column(String, nullable=True)
    status = Column(String, default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PostTarget(Base):
    __tablename__ = "post_targets"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    network = Column(String)
    status = Column(String, default="pending")
    error_message = Column(Text, nullable=True)
    job_id = Column(String, nullable=True)