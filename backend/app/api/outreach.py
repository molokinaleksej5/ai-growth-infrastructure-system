from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.company import Company
from app.models.lead import Lead
from app.models.outreach_campaign import OutreachCampaign
from app.models.outreach_sequence import OutreachSequence
from app.schemas.outreach import CampaignCreateRequest,CampaignResponse,SequenceGenerateRequest,SequenceResponse
from app.services.outreach_ai import OutreachAIService
router=APIRouter(prefix='/outreach',tags=['Outreach AI'])
@router.post('/campaigns',response_model=CampaignResponse)
def create_campaign(payload:CampaignCreateRequest,db:Session=Depends(get_db)):
    c=OutreachCampaign(**payload.model_dump()); db.add(c); db.commit(); db.refresh(c); return c
@router.get('/campaigns',response_model=list[CampaignResponse])
def get_campaigns(db:Session=Depends(get_db)): return db.query(OutreachCampaign).order_by(OutreachCampaign.id.desc()).all()
@router.post('/sequence/generate',response_model=list[SequenceResponse])
def generate_sequence(payload:SequenceGenerateRequest,db:Session=Depends(get_db)):
    campaign=db.query(OutreachCampaign).filter(OutreachCampaign.id==payload.campaign_id).first(); lead=db.query(Lead).filter(Lead.id==payload.lead_id).first()
    if not campaign or not lead: return []
    company=db.query(Company).filter(Company.id==lead.company_id).first(); service=OutreachAIService()
    seq=service.generate_sequence(lead=lead.__dict__, company=company.__dict__ if company else {}, campaign=campaign.__dict__, channel=payload.channel, steps=payload.steps)
    out=[]
    for item in seq:
        row=OutreachSequence(campaign_id=campaign.id,lead_id=lead.id,channel=item['channel'],step_number=item['step_number'],subject=item['subject'],message=item['message'],status='draft')
        db.add(row); db.commit(); db.refresh(row); out.append(row)
    return out
@router.get('/sequences',response_model=list[SequenceResponse])
def get_sequences(db:Session=Depends(get_db)): return db.query(OutreachSequence).order_by(OutreachSequence.id.desc()).limit(100).all()
