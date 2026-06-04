from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
class OutreachMessage(Base):
    __tablename__ = "outreach_messages"
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False)
    channel = Column(String(50), nullable=False)
    subject = Column(String(500), nullable=True)
    message = Column(Text, nullable=False)
    status = Column(String(120), default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
