from pydantic import BaseModel
class MarketWatchCreateRequest(BaseModel):
    name: str; region: str; niche: str; keywords: str; sources: str | None = None
class MarketWatchResponse(BaseModel):
    id: int; name: str; region: str; niche: str; keywords: str; sources: str | None; status: str
    class Config: from_attributes = True
class MarketSignalResponse(BaseModel):
    id: int; title: str; region: str | None; niche: str | None; source: str | None; source_url: str | None; signal_type: str | None; description: str | None; opportunity_score: float; ai_comment: str | None
    class Config: from_attributes = True
