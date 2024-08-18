from itinerary_generator import generate_itinerary
from tiktok_generator import generate_tiktok
import openai
from openai import OpenAI
import json
from stored_strings import standard_output, itinerary_system_prompt, json_system_prompt
import ast
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if OPENAI_API_KEY is None:
    print("Error: OPENAI_API_KEY is not set.")
else:
    print("API Key retrieved successfully.")

preferences = travel_keywords = [
    "Historical landmarks & museums",
    "City tours & sightseeing",
    "Local cuisine & food tours",
    "Beaches & relaxation",
    "Hiking & nature trails",
    "Botanical gardens & parks",
    "Nightlife & entertainment",
    "Shopping & local markets",
    "Art galleries & exhibitions",
    "Cultural festivals & events",
    "Boat rides & water activities",
    "National parks & natural reserves",
    "Theme parks & attractions",
    "Adventure sports & outdoor activities",
    "Religious & spiritual sites",
    "Cooking classes & culinary experiences",
    "Wine, brewery & beverage tastings",
    "Zoos, aquariums & wildlife",
    "Theater, concerts & live performances"
]

traveling_options = ['Friend', 'Family', 'Couple', 'Solo', 'Group']


def get_itinerary(location, date, traveling_with, preferences, additional_preferences, outsourced = None) -> dict:
    """
    :param location: str
    :param date: list
    :param traveling_with: str
    :param preferences: str
    :param additional_preferences: str
    :return: itinerary: dict
    """
    for _ in range(3):
        json_string = raw_itinerary(location, date, traveling_with, preferences, additional_preferences, outsourced = None)
        try:
            ast.literal_eval(json_string)
            return json.loads(json_string)
        except:
            pass
    return "Failed"

def generate_video(itinerary) -> str:
    """
    Takes in an itinerary dict and generates a video and saves it to a file
    :param itinerary: dict
    :return: filepath: str
    """
    filepath = generate_tiktok(itinerary)
    return filepath

def raw_itinerary(location, date, traveling_with, preferences, additional_preferences, outsourced = None):
  
  itinerary_user_prompt = f"""
  Location: {location}.
  Date: {date}.
  Who I am traveling with: {traveling_with}.
  Preferences on activites: {preferences}.
  Additional preferences: {additional_preferences}.
  Data/recommendations from some prominent webpages: {outsourced}.
  """
  generate_itinerary_client = OpenAI(api_key= OPENAI_API_KEY)
  itinerary_response = generate_itinerary_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": itinerary_system_prompt},
      {"role": "user", "content": itinerary_user_prompt}
    ]
  )
  raw_itinerary = itinerary_response.choices[0].message.content
  return raw_itinerary