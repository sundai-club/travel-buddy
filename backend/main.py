from itinerary_generator import generate_itinerary
from tiktok_generator import generate_tiktok


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
