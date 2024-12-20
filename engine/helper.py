"""
This module provides helper functions for a virtual assistant, including functionalities 
such as greeting the user, fetching the user's schedule, opening social media platforms, 
searching the web, and extracting terms for YouTube searches.
"""

import re
import json
import datetime
import time
import webbrowser
from engine import command


def extract_yt_term(command):
    """
    Extracts the YouTube search term from the command.

    Args:
        command (str): The user's spoken command.

    Returns:
        str: The extracted search term or None if not found.
    """
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None


def load_intents(file_path):
    """
    Loads the intents.json file.

    Args:
        file_path (str): Path to the intents file.

    Returns:
        dict: Parsed JSON content.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        command.speak("The intents file could not be found.")
        return {}
    except json.JSONDecodeError:
        command.speak("The intents file contains invalid JSON.")
        return {}


intents_data = load_intents("engine\\intents.json")


def calculate_day():
    """
    Determines the current day of the week.

    Returns:
        str: The name of the current day.
    """
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return day_dict.get(day, "Unknown")


def hello():
    """
    Greets the user based on the current time of day and mentions the day and time.
    """
    hour = int(datetime.datetime.now().hour)
    current_time = time.strftime("%I:%M:%p")
    day = calculate_day()

    if hour < 12:
        greet = "Good morning"
    elif hour < 17:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    command.speak(f"{greet} Poorna, it's {day} and the time is {current_time}.")


def open_social_media(command):
    """
    Opens a social media platform in the web browser based on the user's command.

    Args:
        command (str): The user's spoken command.
    """
    platforms = {
        "facebook": "https://www.facebook.com/",
        "whatsapp": "https://web.whatsapp.com/",
        "discord": "https://discord.com/",
        "instagram": "https://www.instagram.com/",
    }
    for platform, url in platforms.items():
        if platform in command:
            command.speak(f"Opening {platform.capitalize()}.")
            webbrowser.open(url)
            return
    command.speak("No matching social media platform found.")


def schedule():
    """
    Speaks the user's schedule for the current day of the week.
    """
    day = calculate_day().lower()
    command.speak(" Poorna, today's schedule is:")
    weekly_schedule = {
        "monday": (
            "From 9:00 to 9:50, Algorithms; 10:00-11:50, System Design; "
            "Break from 12:00-2:00; Programming Lab at 2:00."
        ),
        "tuesday": (
            "From 9:00 to 9:50, Web Development; 10:00-10:50, Break; "
            "11:00-12:50, Database Systems; Break 1:00-2:00; Open Source Projects Lab at 2:00."
        ),
        "wednesday": (
            "9:00-10:50, Machine Learning; 11:00-11:50, Operating Systems; "
            "12:00-12:50, Ethics; Break 1:00-2:00; Software Engineering Workshop at 2:00."
        ),
        "thursday": (
            "9:00-10:50, Computer Networks; 11:00-12:50, Cloud Computing; "
            "Break 1:00-2:00; Cybersecurity Lab at 2:00."
        ),
        "friday": (
            "9:00-9:50, Artificial Intelligence; 10:00-10:50, Advanced Programming; "
            "11:00-12:50, UI/UX Design; Break 1:00-2:00; Capstone Project at 2:00."
        ),
        "saturday": (
            "9:00-11:50, Capstone Team Meeting; 12:00-12:50, Innovation Class; "
            "Break 1:00-2:00; Personal Development after 2:00."
        ),
        "sunday": "It's a holiday, but review deadlines and catch up on projects.",
    }
    command.speak(weekly_schedule.get(day, "No schedule available for today."))


def browse_web(query):
    """
    Performs a web search based on the user's query.

    Args:
        query (str): The user's spoken query.
    """
    if "google" in query:
        command.speak("Poorna, what should I search on Google?")
        search_term = command.takecommand()
        if search_term:
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            command.speak("I didn't catch that.")
    else:
        command.speak("No recognized browsing platform mentioned.")
