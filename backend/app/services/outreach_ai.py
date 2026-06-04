from app.services.ai_gateway import AIGateway
class OutreachAIService:
    def __init__(self): self.ai=AIGateway()
    def generate_sequence(self, lead:dict, company:dict, campaign:dict, channel:str='email', steps:int=3)->list[dict]:
        prompt=f"Create a personalized B2B outreach sequence. Channel:{channel}. Steps:{steps}. Company:{company}. Lead:{lead}. Campaign:{campaign}. Use STEP N SUBJECT and STEP N MESSAGE format."
        text=self.ai.generate(prompt,"You are a senior B2B sales development strategist.")
        return self._parse_sequence(text,channel,steps)
    def _parse_sequence(self,text,channel,steps):
        result=[]
        for step in range(1,steps+1):
            subject=f"Outreach step {step}" if channel=='email' else None
            message=text if step==1 else f"Follow-up step {step}: {text[:1200]}"
            result.append({"step_number":step,"channel":channel,"subject":subject,"message":message})
        return result
