from typing import List
from enum import Enum

from pydantic import BaseModel
class TravelType(Enum):
    BEACH = 'beach'
    MOUNTAIN = 'mountain'
    CITY = 'city'


class ActivityType(Enum):
    ADVENTURE = 'adventure'
    RELAXATION = 'relaxation'
    CULTURAL = 'cultural'


class TravelPreferencesModel(BaseModel):
    travel_type: TravelType
    activities: List[ActivityType]
