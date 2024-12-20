"""
This module contains utility functions for the assistant.

Currently, it includes a function to listen for audio input and convert it to text.
"""

import speech_recognition as sr

def takecommand():
    """Listens for audio input and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Speech was unintelligible.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""
