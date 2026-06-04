from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    title = Column(String(500), nullable=False, index=True)
    need_type = Column(String(255), nullable=True)
    region = Column(String(120), nullable=True)
    budget = Column(String(120), nullable=True)
    raw_text = Column(Text, nullable=True)
    ai_summary = Column(Text, nullable=True)
    score = Column(Float, default=0)
    score_reason = Column(Text, nullable=True)
    status = Column(String(120), default="new", index=True)
    source = Column(String(255), nullable=True)
    source_url = Column(String(1000), nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
