from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    full_name = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    linkedin_url = Column(String(1000), nullable=True)
    telegram = Column(String(255), nullable=True)
    whatsapp = Column(String(255), nullable=True)
    is_decision_maker = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
