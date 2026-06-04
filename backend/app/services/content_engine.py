from app.services.ai_gateway import AIGateway
class ContentEngine:
    def __init__(self): self.ai=AIGateway()
    def generate_topics(self, plan:dict, count:int=10)->str:
        return self.ai.generate(f"Create {count} B2B content topics for plan: {plan}","You are a B2B content strategist for AI/software companies.")
    def generate_content(self, content_type:str, topic:str, plan:dict)->str:
        return self.ai.generate(f"Generate {content_type} about {topic}. Plan: {plan}. Expert, practical, B2B focused.","You create high-quality B2B content.")
