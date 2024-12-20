"""
This module contains the implementation for Jarvis Assistant's features including:
- Hotword detection ("blueberry")
- Command execution (open apps, search YouTube)
- Play startup sound
- Handle errors in a more specific way
"""

import os
import struct
import time
import sqlite3
import webbrowser
from playsound import playsound
import pywhatkit as kit
import pyaudio
import pyautogui as autogui
import eel
import pvporcupine
from hugchat import hugchat
from engine.config import ASSISTANT_NAME
from engine.command import speak
from engine.helper import extract_yt_term


# Database connection
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()


@eel.expose
def play_startup_sound():
    """
    Plays a sound file when the application starts.
    Replace the sound file path with the appropriate file.
    """
    sound_file = (
        "www/assets/audio/start_sound.mp3"  # Use '/' for cross-platform compatibility
    )
    if os.path.exists(sound_file):
        playsound(sound_file)
    else:
        speak("Startup sound file not found.")


def open_command(query):
    """
    Opens an application or file based on the query.

    Args:
        query (str): The command to execute.
    """
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()

    app_name = query.strip()
    if app_name:
        try:
            # Check if the app exists in the sys_command table
            cursor.execute(
                "SELECT path FROM sys_command WHERE name IN (?)", (app_name,)
            )
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            else:
                # Check if the app exists in the web_command table
                cursor.execute(
                    "SELECT url FROM web_command WHERE name IN (?)", (app_name,)
                )
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    # Attempt to open the command directly at the system level
                    speak("Opening " + query)
                    try:
                        os.system("start " + query)
                    except OSError as os_error:
                        speak(f"System command error: {str(os_error)}")
        except sqlite3.OperationalError as op_error:
            speak(f"Database operation error: {str(op_error)}")
        except sqlite3.DatabaseError as db_error:
            speak(f"Database error: {str(db_error)}")
        except FileNotFoundError as file_error:
            speak(f"File not found: {str(file_error)}")
        except OSError as os_error:  # Handles OS-level issues
            speak(f"Operating system error: {str(os_error)}")
        except ValueError as val_error:  # Catches invalid data errors
            speak(f"Value error: {str(val_error)}")


def play_youtube(query):
    """
    Plays the requested video on YouTube.

    Args:
        query (str): The command containing the video search term.
    """
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Could not extract a YouTube search term.")


def hotword():
    """Listens for the 'blueberry' hotword and triggers actions when detected."""
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Pre-trained keyword 'blueberry' from the available list
        porcupine = pvporcupine.create(keywords=["blueberry"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        # Loop for streaming and listening for the keyword
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # Processing the keyword from the microphone input
            keyword_index = porcupine.process(keyword)

            # Checking if the keyword 'blueberry' is detected
            if keyword_index >= 0:
                print("Hotword 'blueberry' detected")

                # Simulating pressing Win + J
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except OSError as e:
        print(f"OSError occurred: {e}")
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    except KeyboardInterrupt as e:
        print(f"Operation interrupted: {e}")
    except Exception as e:  # Catching unexpected exceptions last
        print(f"An unexpected error occurred: {e}")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


if __name__ == "__main__":
    hotword()


# chat bot
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
