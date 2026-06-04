from sqlalchemy.orm import Session
from app.models.company import Company
from app.models.lead import Lead
class DeduplicationService:
    def find_company(self, db: Session, name: str, website: str | None = None):
        if website:
            c=db.query(Company).filter(Company.website==website).first()
            if c: return c
        return db.query(Company).filter(Company.name.ilike(name)).first()
    def lead_exists(self, db: Session, title: str, source_url: str | None = None) -> bool:
        if source_url and db.query(Lead).filter(Lead.source_url==source_url).first(): return True
        return db.query(Lead).filter(Lead.title.ilike(title)).first() is not None
