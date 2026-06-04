from app.services.ai_gateway import AIGateway
class ProposalAIService:
    def __init__(self): self.ai=AIGateway()
    def estimate_pricing(self, lead, company, pricing_model, currency):
        score=lead.get('score') or 0; text=f"{lead.get('title','')} {lead.get('raw_text','')}".lower()
        if 'enterprise' in text or score>=85: base='15000 - 50000'; support='2000 - 8000 / month'
        elif 'automation' in text or 'crm' in text or 'ai' in text: base='5000 - 20000'; support='1000 - 4000 / month'
        else: base='3000 - 10000'; support='500 - 2000 / month'
        return f"{currency} {base}; support: {currency} {support}; model: {pricing_model}"
    def build_roadmap(self, lead): return "Discovery → Architecture → MVP development → Testing → Launch and scaling"
    def build_roi_analysis(self, lead, pricing): return self.ai.generate(f"Create ROI analysis for lead {lead} and pricing {pricing}","You are a B2B ROI analyst.")
    def generate_proposal(self, lead, company, offer_type, pricing_model, currency):
        pricing=self.estimate_pricing(lead,company,pricing_model,currency); roadmap=self.build_roadmap(lead); roi=self.build_roi_analysis(lead,pricing)
        full=self.ai.generate(f"Create full commercial proposal. Company:{company}. Lead:{lead}. Offer:{offer_type}. Pricing:{pricing}. Roadmap:{roadmap}. ROI:{roi}","You are a senior B2B solution architect.")
        return {"title":f"Commercial Proposal for {company.get('name') or 'Client'}","pricing":pricing,"roadmap":roadmap,"roi_analysis":roi,"full_text":full}
