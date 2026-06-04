from sqlalchemy.orm import Session
from app.models.company import Company
from app.models.lead import Lead
from app.parsers.normalizer import normalize_lead_item
from app.parsers.job_board_parser import JobBoardParser
from app.parsers.clutch_parser import ClutchParser
from app.parsers.google_places_parser import GooglePlacesParser
from app.parsers.directory_parser import DirectoryParser
from app.services.lead_scoring import LeadScoringService
from app.services.telegram_notify import TelegramNotifyService
from app.services.deduplication import DeduplicationService
class LeadHunterService:
    def __init__(self):
        self.parsers=[JobBoardParser(),ClutchParser(),GooglePlacesParser(),DirectoryParser()]
        self.scoring=LeadScoringService(); self.telegram=TelegramNotifyService(); self.dedup=DeduplicationService()
    def run_search(self, db: Session, query: str, region: str, limit_per_source: int = 20) -> list[Lead]:
        created=[]
        for parser in self.parsers:
            for raw in parser.search(query=query, region=region, limit=limit_per_source):
                item=normalize_lead_item(raw)
                if not item['title'] or self.dedup.lead_exists(db,item['title'],item.get('source_url')): continue
                company=self.dedup.find_company(db,item['company_name'],item.get('website'))
                if not company:
                    company=Company(name=item['company_name'],website=item.get('website'),country=item.get('region'),industry=item.get('industry'),source=item.get('source'),source_url=item.get('source_url'),description=item.get('raw_text'))
                    db.add(company); db.flush()
                lead_data={"title":item.get('title'),"region":item.get('region'),"raw_text":item.get('raw_text'),"budget":item.get('budget'),"industry":item.get('industry'),"source":item.get('source')}
                score,reason=self.scoring.calculate_basic_score(lead_data); summary=self.scoring.generate_ai_summary(lead_data)
                lead=Lead(company_id=company.id,title=item.get('title'),need_type=query,region=item.get('region'),budget=item.get('budget'),raw_text=item.get('raw_text'),ai_summary=summary,score=score,score_reason=reason,source=item.get('source'),source_url=item.get('source_url'))
                db.add(lead); db.commit(); db.refresh(lead); self.telegram.notify_new_lead(lead.title,lead.score,lead.source_url); created.append(lead)
        return created
