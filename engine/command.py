"""
This module handles text-to-speech conversion, speech recognition, and processing of voice commands
such as opening applications or playing YouTube videos.

It uses pyttsx3 for speech synthesis, speech_recognition for voice input, and eel for communication
between Python and a web interface.
"""

import pyttsx3
import speech_recognition as sr
import eel
from engine import features
from engine import helper


# Initialize eel
eel.init("www")


def speak(text):
    """
    Converts the given text to speech.

    Args:
        text (str): The text to be spoken.
    """
    text = str(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Set to female voice
    engine.setProperty("rate", 174)  # Set speech speed
    engine.say(text)
    engine.runAndWait()


def takecommand():
    """
    Listens for audio input from the microphone and converts it to text.

    Returns:
        str: The recognized speech in lowercase, or an empty string if recognition fails.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        A=print("Can you please repeat")
        speak(A)
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

    return query.lower()


@eel.expose
def all_commands(message=1):
    """
    Processes user commands received via voice or message.

    Args:
        message (str, optional): User input text. Defaults to 1 for voice input.
    """
    if message == 1:
        query = takecommand()
    else:
        query = message

    try:
        if "open" in query:
            features.open_command(query)
        elif "play" in query and "on youtube" in query:
            features.play_youtube(query)
        elif "hello" in query:
            helper.hello()

        elif "social media" in query:
            helper.open_social_media(query)
        elif "schedule" in query:
            helper.schedule()
        elif "google" in query:
            helper.browse_web(query)

        else:
            features.chatBot(query)
    except Exception as e:
        print(f"An error occurred: {e}")
