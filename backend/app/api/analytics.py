from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.analytics import PipelineSummaryResponse,LeadRecommendationResponse
from app.services.crm_brain import CRMBrainService
router=APIRouter(prefix='/analytics',tags=['CRM Brain & Analytics'])
@router.get('/summary',response_model=PipelineSummaryResponse)
def summary(db:Session=Depends(get_db)): return CRMBrainService().get_pipeline_summary(db)
@router.get('/recommendations',response_model=list[LeadRecommendationResponse])
def recommendations(db:Session=Depends(get_db)): return CRMBrainService().get_lead_recommendations(db)
@router.get('/management-report')
def report(db:Session=Depends(get_db)): return {'report':CRMBrainService().generate_ai_management_report(db)}
