from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
class OutreachCampaign(Base):
    __tablename__ = "outreach_campaigns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    target_region = Column(String(120), nullable=True)
    target_niche = Column(String(255), nullable=True)
    offer = Column(Text, nullable=False)
    tone = Column(String(120), default="professional")
    status = Column(String(120), default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
