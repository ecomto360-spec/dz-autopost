from sqlalchemy import Column, Integer, String, Text
from database import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    niche = Column(String, nullable=True)
    target_audience = Column(Text, nullable=True)
    tone = Column(String, nullable=True)
    fb_page_id = Column(String, nullable=True)
    ig_account_id = Column(String, nullable=True)
    linkedin_urn = Column(String, nullable=True)