from pydantic import BaseModel
class LeadCreateRequest(BaseModel):
    query: str
    region: str
    limit_per_source: int = 10
class LeadResponse(BaseModel):
    id: int; title: str; region: str | None; score: float; status: str; source: str | None; source_url: str | None
    class Config: from_attributes = True
