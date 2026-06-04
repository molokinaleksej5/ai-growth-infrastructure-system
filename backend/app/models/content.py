from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
class ContentItem(Base):
    __tablename__ = "content_items"
    id = Column(Integer, primary_key=True, index=True)
    content_type = Column(String(120), nullable=False)
    topic = Column(String(500), nullable=False)
    target_audience = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    status = Column(String(120), default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
