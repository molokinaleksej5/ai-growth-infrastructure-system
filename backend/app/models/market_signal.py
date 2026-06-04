from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base
class MarketSignal(Base):
    __tablename__ = "market_signals"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    region = Column(String(120), nullable=True)
    niche = Column(String(255), nullable=True)
    source = Column(String(255), nullable=True)
    source_url = Column(String(1000), nullable=True)
    signal_type = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    opportunity_score = Column(Float, default=0)
    ai_comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
