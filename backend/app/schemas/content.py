from pydantic import BaseModel
class ContentPlanCreateRequest(BaseModel):
    name: str; target_audience: str; niche: str; region: str | None = None; goals: str | None = None
class ContentGenerateRequest(BaseModel):
    content_plan_id: int; content_type: str = "linkedin_post"; topic: str
class ContentPlanResponse(BaseModel):
    id: int; name: str; target_audience: str; niche: str; region: str | None; goals: str | None; topics: str | None; status: str
    class Config: from_attributes = True
class ContentItemResponse(BaseModel):
    id: int; content_type: str; topic: str; target_audience: str | None; text: str; status: str
    class Config: from_attributes = True
