from itinerary_generator import generate_itinerary
from tiktok_generator import generate_tiktok

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


def get_itinerary(location, date, traveling_with, preferences, additional_preferences) -> dict:
    """
    :param location: str
    :param date: list
    :param traveling_with: str
    :param preferences: str
    :param additional_preferences: str
    :return: itinerary: dict
    """
    itinerary = generate_itinerary(location, date, traveling_with, preferences, additional_preferences)
    return itinerary


def generate_video(itinerary) -> str:
    """
    Takes in an itinerary dict and generates a video and saves it to a file
    :param itinerary: dict
    :return: filepath: str
    """
    filepath = generate_tiktok(itinerary)
    return filepath
