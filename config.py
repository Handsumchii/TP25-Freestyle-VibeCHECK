# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Key (pulled from .env for security)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Default settings
DEFAULT_CITY = "New York"
DEFAULT_UNITS = "metric"  # Use 'imperial' for Fahrenheit

# Theme settings
LIGHT_THEME = {
    "bg": "#f0f8ff",
    "fg": "#222222",
    "button_bg": "#add8e6",
    "entry_bg": "#ffffff",
}

DARK_THEME = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "button_bg": "#444444",
    "entry_bg": "#333333",
}

# Affirmations (rotated daily or randomly)
AFFIRMATIONS = [
    "You got this!",
    "Progress over perfection.",
    "Breathe. Reset. Go again.",
    "Your efforts matter.",
    "Trust the process.",
    "One step at a time.",
    "Stay present, stay grounded.",
    "You've come a long way.",
    "Vibes don't lie. You're doing great.",
    "Your energy is unmatched.",
]

# Mood options for journaling
MOODS = ["😊 Happy", "😐 Okay", "😟 Anxious", "😢 Sad", "😡 Frustrated", "😴 Tired"]

# Path to journal file
JOURNAL_FILE = "weather_journal.json"

