from aqt import mw
from aqt.qt import *
from anki.hooks import addHook
import requests
import time

# SETUP
# Pushover API credentials
USER_KEY = "YOUR-PUSHOVER-USER-KEY"
API_TOKEN = "YOUR-PUSHOVER-API-TOKEN"
# Setup reminder interval (enter interval in minutes, default is 60m)
INTERVAL = 60


def check_due_cards():
    # Get the number of due cards
    due_count = len(mw.col.find_cards('is:due'))
    if due_count:
        send_pushover_notification(due_count)


def send_pushover_notification(due_count):
    # Pushover API endpoint
    url = "https://api.pushover.net/1/messages.json"

    # Prep Notification
    payload = {
        "token": API_TOKEN,
        "user": USER_KEY,
        "message": f"You have {due_count} cards due!",
        "title": "Anki Reminder"
    }

    # Send the request
    response = requests.post(url, data=payload)

    # This is for me to debug stuff
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")


def setup_timer():
    interval_ms = INTERVAL * 60 * 1000  # Convert interval to milliseconds
    mw.progress.timer(interval_ms, check_due_cards, repeat=True)


# Add the setup_timer function to Anki's startup hook
addHook("profileLoaded", setup_timer)
