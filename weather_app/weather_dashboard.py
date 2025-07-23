import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .weather import get_weather_data
from .journal_utils import load_journal_entries

def format_weather(data):
    name = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["description"].capitalize()
    return f"📍 {name}\n🌡 Temp: {temp}°C (Feels like: {feels_like}°C)\n☁️ Condition: {weather}"
