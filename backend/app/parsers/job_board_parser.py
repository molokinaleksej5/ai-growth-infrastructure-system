from app.parsers.base_parser import BaseParser
class JobBoardParser(BaseParser):
    source_name='job_board_demo'
    def search(self, query: str, region: str, limit: int = 20) -> list[dict]:
        return [{"company_name":"AI Automation Studio","website":"https://example-ai-studio.com","title":f"{query} contractor needed","region":region,"raw_text":f"We are looking for outsourcing contractor for {query}. Region: {region}. Need API, automation and AI integration.","source":self.source_name,"source_url":"https://example.com/project/ai-automation","budget":"$5,000 - $20,000","industry":"Software / Automation"},{"company_name":"ScaleOps Tech","website":"https://example-scaleops.com","title":f"B2B automation partner for {region}","region":region,"raw_text":"Company is expanding and needs a software partner for CRM automation, data pipelines and AI assistants.","source":self.source_name,"source_url":"https://example.com/project/scaleops","budget":"$10,000+","industry":"B2B SaaS"}][:limit]
