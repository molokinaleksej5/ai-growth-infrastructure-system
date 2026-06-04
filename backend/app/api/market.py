from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.market_signal import MarketSignal
from app.models.market_watch import MarketWatch
from app.schemas.market import MarketWatchCreateRequest,MarketWatchResponse,MarketSignalResponse
from app.services.market_intelligence import MarketIntelligenceService
router=APIRouter(prefix='/market',tags=['Market Intelligence AI'])
@router.post('/watches',response_model=MarketWatchResponse)
def create_market_watch(payload:MarketWatchCreateRequest,db:Session=Depends(get_db)):
    w=MarketWatch(**payload.model_dump()); db.add(w); db.commit(); db.refresh(w); return w
@router.get('/watches',response_model=list[MarketWatchResponse])
def get_watches(db:Session=Depends(get_db)): return db.query(MarketWatch).order_by(MarketWatch.id.desc()).all()
@router.post('/watches/{watch_id}/run',response_model=list[MarketSignalResponse])
def run_watch(watch_id:int,db:Session=Depends(get_db)): return MarketIntelligenceService().run_watch(db,watch_id)
@router.get('/signals',response_model=list[MarketSignalResponse])
def get_signals(db:Session=Depends(get_db)): return db.query(MarketSignal).order_by(MarketSignal.id.desc()).limit(100).all()
@router.get('/signals/top',response_model=list[MarketSignalResponse])
def get_top(db:Session=Depends(get_db)): return db.query(MarketSignal).filter(MarketSignal.opportunity_score>=70).order_by(MarketSignal.opportunity_score.desc()).limit(50).all()
