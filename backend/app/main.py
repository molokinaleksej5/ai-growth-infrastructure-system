from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import *
from app.api import leads, outreach, market, content, proposals, analytics
Base.metadata.create_all(bind=engine)
app=FastAPI(title='AI Growth Infrastructure System',description='AI-first infrastructure for B2B growth automation.',version='1.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(leads.router); app.include_router(outreach.router); app.include_router(market.router); app.include_router(content.router); app.include_router(proposals.router); app.include_router(analytics.router)
@app.get('/')
def root(): return {'status':'running','project':'AI Growth Infrastructure System'}
