from pydantic import BaseModel
class PipelineSummaryResponse(BaseModel):
    total_leads: int; new: int; contacted: int; qualified: int; proposal_prepared: int; proposal_sent: int; won: int; lost: int; high_score_leads: int; average_score: float
class LeadRecommendationResponse(BaseModel):
    lead_id: int; title: str; score: float; status: str; priority: str; next_action: str; reason: str
