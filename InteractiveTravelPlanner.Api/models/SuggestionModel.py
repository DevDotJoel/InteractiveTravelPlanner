from pydantic import BaseModel
from typing import List
class SuggestionModel(BaseModel):
    country: str
    activities: List[str]
    itineraries: List[str]
