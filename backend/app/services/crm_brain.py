from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.lead import Lead
from app.services.ai_gateway import AIGateway
class CRMBrainService:
    def __init__(self): self.ai=AIGateway()
    def get_pipeline_summary(self, db: Session):
        def c(status): return db.query(Lead).filter(Lead.status==status).count()
        avg=db.query(func.avg(Lead.score)).scalar() or 0
        return {"total_leads":db.query(Lead).count(),"new":c('new'),"contacted":c('contacted'),"qualified":c('qualified'),"proposal_prepared":c('proposal_prepared'),"proposal_sent":c('proposal_sent'),"won":c('won'),"lost":c('lost'),"high_score_leads":db.query(Lead).filter(Lead.score>=80).count(),"average_score":round(float(avg),2)}
    def get_priority(self, lead): return 'high' if lead.score>=85 else 'medium' if lead.score>=60 else 'low'
    def get_next_action(self, lead):
        return {'new':'Generate personalized outreach and enrich company data.','contacted':'Prepare follow-up.','qualified':'Generate proposal.','proposal_prepared':'Send proposal.','proposal_sent':'Prepare ROI follow-up.','won':'Handoff to delivery.','lost':'Record reason and keep for future.'}.get(lead.status,'Review lead manually.')
    def get_lead_recommendations(self, db: Session, limit:int=20):
        leads=db.query(Lead).order_by(Lead.score.desc(),Lead.id.desc()).limit(limit).all()
        return [{"lead_id":l.id,"title":l.title,"score":l.score,"status":l.status,"priority":self.get_priority(l),"next_action":self.get_next_action(l),"reason":l.score_reason or 'No reason'} for l in leads]
    def generate_ai_management_report(self, db:Session):
        return self.ai.generate(f"Create management report. Summary:{self.get_pipeline_summary(db)} Recommendations:{self.get_lead_recommendations(db,10)}","You are a CRM analytics and B2B growth advisor.")
