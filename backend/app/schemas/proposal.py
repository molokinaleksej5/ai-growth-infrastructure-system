from pydantic import BaseModel
class ProposalGenerateRequest(BaseModel):
    lead_id: int; offer_type: str = "AI automation / custom software"; pricing_model: str = "fixed + monthly support"; currency: str = "USD"
class ProposalResponse(BaseModel):
    id: int; lead_id: int; title: str; pricing: str | None; roadmap: str | None; roi_analysis: str | None; full_text: str; status: str
    class Config: from_attributes = True
