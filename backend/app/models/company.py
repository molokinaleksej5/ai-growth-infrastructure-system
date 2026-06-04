from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    website = Column(String(500), nullable=True, index=True)
    country = Column(String(120), nullable=True)
    city = Column(String(120), nullable=True)
    industry = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    source = Column(String(255), nullable=True)
    source_url = Column(String(1000), nullable=True)
    company_size = Column(String(120), nullable=True)
    technologies = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
