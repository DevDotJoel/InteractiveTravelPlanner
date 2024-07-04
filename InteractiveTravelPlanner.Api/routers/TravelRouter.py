from typing import List
from models.SuggestionModel import SuggestionModel
from models.TravelPreferencesModel import TravelPreferencesModel
from services.TravelService import TravelService
from fastapi import APIRouter, Depends, status
TravelRouterRouter = APIRouter(
    prefix="/api/travel", tags=["travel"]
)


@TravelRouterRouter.post(
    "/",
    name="travel:suggestions",
    response_model=List[SuggestionModel]
)
def create_suggestion(
        travelPreferences: TravelPreferencesModel,
        travelService: TravelService = Depends(),
) -> List[SuggestionModel]:
    return travelService.get_travel_suggestions(preferences=travelPreferences)