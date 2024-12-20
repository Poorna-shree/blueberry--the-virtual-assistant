"""
main.py

This script initializes the web interface for the virtual assistant and starts the application.
"""

import os
import eel
from engine.features import play_startup_sound
from engine.command import takecommand

def start():
    """
    Initializes and starts the virtual assistant application.

    - Sets up the Eel web interface with the `www` directory.
    - Plays a startup sound to indicate initialization.
    - Listens for user commands.
    - Launches the application in a web browser using Microsoft Edge.

    Note:
    - Ensure that the `msedge.exe` command is available on the system.
    - The web application runs on `http://localhost:8000`.
    """
    # Initialize the Eel web app
    eel.init('www')

    # Play the startup sound
    play_startup_sound()

    # Start listening for user commands
    takecommand()
    # Launch the application
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
