from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.content import ContentItem
from app.models.content_plan import ContentPlan
from app.schemas.content import ContentPlanCreateRequest,ContentGenerateRequest,ContentPlanResponse,ContentItemResponse
from app.services.content_engine import ContentEngine
router=APIRouter(prefix='/content',tags=['Content AI Engine'])
@router.post('/plans',response_model=ContentPlanResponse)
def create_plan(payload:ContentPlanCreateRequest,db:Session=Depends(get_db)):
    topics=ContentEngine().generate_topics(payload.model_dump(),10); p=ContentPlan(**payload.model_dump(),topics=topics)
    db.add(p); db.commit(); db.refresh(p); return p
@router.get('/plans',response_model=list[ContentPlanResponse])
def get_plans(db:Session=Depends(get_db)): return db.query(ContentPlan).order_by(ContentPlan.id.desc()).all()
@router.post('/generate',response_model=ContentItemResponse)
def generate_content(payload:ContentGenerateRequest,db:Session=Depends(get_db)):
    p=db.query(ContentPlan).filter(ContentPlan.id==payload.content_plan_id).first()
    if not p: raise HTTPException(404,'Content plan not found')
    text=ContentEngine().generate_content(payload.content_type,payload.topic,p.__dict__); item=ContentItem(content_type=payload.content_type,topic=payload.topic,target_audience=p.target_audience,text=text,status='draft')
    db.add(item); db.commit(); db.refresh(item); return item
@router.get('/items',response_model=list[ContentItemResponse])
def get_items(db:Session=Depends(get_db)): return db.query(ContentItem).order_by(ContentItem.id.desc()).limit(100).all()
