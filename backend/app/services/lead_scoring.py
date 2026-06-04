from app.services.ai_gateway import AIGateway
class LeadScoringService:
    def __init__(self): self.ai = AIGateway()
    def calculate_basic_score(self, lead_data: dict) -> tuple[float, str]:
        score=0; reasons=[]; region=(lead_data.get('region') or '').lower(); text=(lead_data.get('raw_text') or '').lower(); budget=(lead_data.get('budget') or '').lower()
        target_regions=['usa','united states','australia','europe','germany','france','uae','qatar','south korea','korea']
        if any(r in region for r in target_regions): score+=20; reasons.append('target region')
        keywords=['ai','automation','software','outsourcing','contractor','development','crm','b2b','data','machine learning','backend','api']
        matched=[w for w in keywords if w in text]; score+=min(len(matched)*7,35)
        if matched: reasons.append('matched keywords: '+', '.join(matched))
        if budget: score+=15; reasons.append('budget mentioned')
        if 'urgent' in text or 'asap' in text: score+=10; reasons.append('urgent request')
        if 'startup' in text or 'scale' in text or 'expansion' in text: score+=10; reasons.append('growth signal')
        return min(score,100), '; '.join(reasons)
    def generate_ai_summary(self, lead_data: dict) -> str:
        return self.ai.generate(f"Analyze this B2B lead and summarize it for sales team.\n{lead_data}", "You are a B2B sales intelligence analyst.")
