"""
This script runs the Jarvis Assistant with multiprocessing for:
- Hotword detection (Blueberry)
- Blueberry Assistant main functionality
"""

import multiprocessing
from main import start  # Top-level import
from engine.features import hotword  # Top-level import


def start_blueberry():
    """
    Starts the Blueberry Assistant process.
    """
    print("Process 1 is running.")
    start()


def listen_hotword():
    """
    Starts the hotword detection process.
    """
    print("Process 2 is running.")
    hotword()


if __name__ == "__main__":
    # Create and start processes
    p1 = multiprocessing.Process(target=start_blueberry)
    p2 = multiprocessing.Process(target=listen_hotword)
    p1.start()
    p2.start()

    # Wait for process 1 to finish
    p1.join()

    # Stop process 2 if it's still running
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")
