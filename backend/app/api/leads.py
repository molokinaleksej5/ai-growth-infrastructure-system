from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadCreateRequest, LeadResponse
from app.services.lead_hunter import LeadHunterService
router=APIRouter(prefix='/leads',tags=['Lead Hunter AI'])
@router.get('/',response_model=list[LeadResponse])
def get_leads(db:Session=Depends(get_db)): return db.query(Lead).order_by(Lead.id.desc()).limit(100).all()
@router.post('/hunt',response_model=list[LeadResponse])
def hunt_leads(payload:LeadCreateRequest,db:Session=Depends(get_db)): return LeadHunterService().run_search(db,payload.query,payload.region,payload.limit_per_source)
@router.patch('/{lead_id}/status')
def update_lead_status(lead_id:int,status:str,db:Session=Depends(get_db)):
    lead=db.query(Lead).filter(Lead.id==lead_id).first()
    if not lead: return {'error':'Lead not found'}
    lead.status=status; db.commit(); return {'success':True,'lead_id':lead.id,'status':lead.status}
