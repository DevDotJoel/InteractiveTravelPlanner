from typing import List
from configs.Enviroment import get_environment_variables
from models.SuggestionModel import SuggestionModel
from models.TravelPreferencesModel import TravelPreferencesModel
import openai
import json
env = get_environment_variables()


client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=env.OPENAI_KEY,
)
example_json = {
    "suggestions": [
        {
            "country": "Country",
            "activities": [
                "Ski",
                "Cycling"
            ],
            "itineraries": [
                "Sailing French Islands of Southern Ocean",
                "Climbing on Southern Ocean Islands Peaks"
            ]

        }
    ]
}
class TravelService:

    def get_travel_suggestions(self, preferences: TravelPreferencesModel) -> List[SuggestionModel]:
        activities_str = ', '.join(
            activity.value for activity in preferences.activities)
        prompt = (
            f"Provide valid JSON output. "
            f"Suggest travel destinations and activities for a {preferences.travel_type.value} vacation "
            f"with activities like {activities_str} and detailed itineraries. "
            f"Provide one column 'country', a column 'activities' representing the activities, and another column 'itineraries' representing the itineraries."
        )
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " +
                    json.dumps(example_json)},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,)
        finish_reason = chat_completion.choices[0].finish_reason
        if (finish_reason == "stop"):
            data = chat_completion.choices[0].message.content

            result = json.loads(data)
            suggestions = [SuggestionModel(**suggestion)
                           for suggestion in result['suggestions']]
            return suggestions
        else:
            print("Error! provide more tokens please")