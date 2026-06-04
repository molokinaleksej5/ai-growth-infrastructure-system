from pydantic import BaseModel
class CampaignCreateRequest(BaseModel):
    name: str; target_region: str | None = None; target_niche: str | None = None; offer: str; tone: str = "professional"
class SequenceGenerateRequest(BaseModel):
    campaign_id: int; lead_id: int; channel: str = "email"; steps: int = 3
class CampaignResponse(BaseModel):
    id: int; name: str; target_region: str | None; target_niche: str | None; offer: str; tone: str; status: str
    class Config: from_attributes = True
class SequenceResponse(BaseModel):
    id: int; campaign_id: int; lead_id: int; channel: str; step_number: int; subject: str | None; message: str; status: str
    class Config: from_attributes = True
