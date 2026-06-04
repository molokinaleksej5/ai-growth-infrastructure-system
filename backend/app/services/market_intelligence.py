from sqlalchemy.orm import Session
from app.models.market_signal import MarketSignal
from app.models.market_watch import MarketWatch
from app.services.ai_gateway import AIGateway
from app.services.telegram_notify import TelegramNotifyService
class MarketIntelligenceService:
    def __init__(self): self.ai=AIGateway(); self.telegram=TelegramNotifyService()
    def collect_demo_signals(self, watch: MarketWatch):
        return [{"title":f"Growing demand for {watch.niche} in {watch.region}","region":watch.region,"niche":watch.niche,"source":"market_monitor","source_url":"https://example.com/market-signal","signal_type":"demand_growth","description":f"Companies in {watch.region} are increasingly searching for {watch.keywords}."},{"title":f"New outsourcing opportunities: {watch.niche}","region":watch.region,"niche":watch.niche,"source":"contract_monitor","source_url":"https://example.com/contracts","signal_type":"outsourcing_contract","description":f"Companies show contractor search related to {watch.keywords}."}]
    def calculate_signal_score(self, signal):
        score=40; text=f"{signal.get('title','')} {signal.get('description','')}".lower()
        for w in ['outsourcing','contract','ai','automation','software','startup','expansion','contractor','b2b','development']:
            if w in text: score+=6
        return min(score,100)
    def analyze_signal(self, signal):
        return {"opportunity_score":self.calculate_signal_score(signal),"ai_comment":self.ai.generate(f"Analyze market signal: {signal}","You are a market intelligence analyst.")}
    def run_watch(self, db: Session, watch_id:int):
        watch=db.query(MarketWatch).filter(MarketWatch.id==watch_id).first(); created=[]
        if not watch: return []
        for raw in self.collect_demo_signals(watch):
            a=self.analyze_signal(raw); s=MarketSignal(**raw, opportunity_score=a['opportunity_score'], ai_comment=a['ai_comment'])
            db.add(s); db.commit(); db.refresh(s)
            if s.opportunity_score>=70: self.telegram.send_message(f"<b>New Market Signal</b>\n{s.title}\nScore: {s.opportunity_score}")
            created.append(s)
        return created
