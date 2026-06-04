from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
class Proposal(Base):
    __tablename__ = "proposals"
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False)
    title = Column(String(500), nullable=False)
    pricing = Column(String(255), nullable=True)
    roadmap = Column(Text, nullable=True)
    roi_analysis = Column(Text, nullable=True)
    full_text = Column(Text, nullable=False)
    status = Column(String(120), default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
