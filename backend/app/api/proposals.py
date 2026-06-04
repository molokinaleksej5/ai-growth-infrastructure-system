from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.company import Company
from app.models.lead import Lead
from app.models.proposal import Proposal
from app.schemas.proposal import ProposalGenerateRequest,ProposalResponse
from app.services.proposal_ai import ProposalAIService
router=APIRouter(prefix='/proposals',tags=['Proposal & Sales AI'])
@router.post('/generate',response_model=ProposalResponse)
def generate_proposal(payload:ProposalGenerateRequest,db:Session=Depends(get_db)):
    lead=db.query(Lead).filter(Lead.id==payload.lead_id).first()
    if not lead: raise HTTPException(404,'Lead not found')
    company=db.query(Company).filter(Company.id==lead.company_id).first(); data=ProposalAIService().generate_proposal(lead.__dict__,company.__dict__ if company else {},payload.offer_type,payload.pricing_model,payload.currency)
    p=Proposal(lead_id=lead.id,**data,status='draft'); db.add(p); lead.status='proposal_prepared'; db.commit(); db.refresh(p); return p
@router.get('/',response_model=list[ProposalResponse])
def get_proposals(db:Session=Depends(get_db)): return db.query(Proposal).order_by(Proposal.id.desc()).limit(100).all()
@router.patch('/{proposal_id}/status')
def update_status(proposal_id:int,status:str,db:Session=Depends(get_db)):
    p=db.query(Proposal).filter(Proposal.id==proposal_id).first()
    if not p: return {'error':'Proposal not found'}
    p.status=status; db.commit(); return {'success':True,'proposal_id':p.id,'status':p.status}
