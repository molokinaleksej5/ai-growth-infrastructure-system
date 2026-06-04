from app.config import settings
try:
    from openai import OpenAI
except Exception:
    OpenAI = None
class AIGateway:
    def __init__(self):
        self.default_provider = settings.default_ai_provider
        self.openai_client = OpenAI(api_key=settings.openai_api_key) if OpenAI and settings.openai_api_key and settings.openai_api_key != "your_openai_key" else None
    def generate(self, prompt: str, system: str = "You are a helpful B2B AI assistant.") -> str:
        if self.openai_client:
            try:
                response = self.openai_client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":system},{"role":"user","content":prompt}], temperature=0.4)
                return response.choices[0].message.content or ""
            except Exception as e:
                return f"AI generation failed: {e}"
        return self._mock_response(prompt)
    def _mock_response(self, prompt: str) -> str:
        return "AI mock response. Configure OPENAI_API_KEY to enable real generation.\n\n" + prompt[:900]
