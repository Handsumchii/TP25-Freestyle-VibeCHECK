import tkinter as tk
from tkinter import messagebox
from .weather import get_weather_data
from .journal_utils import save_journal_entry, load_journal_entries
from .config import AFFIRMATIONS


class WeatherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VibeCheck: Weather Edition")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.insert(0, "Enter City")
        self.city_entry.pack(pady=10)

        self.weather_display = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
        self.weather_display.pack(pady=10)

        self.search_button = tk.Button(root, text="Get Weather", command=self.fetch_weather)
        self.search_button.pack(pady=5)

        self.mood_label = tk.Label(root, text="How are you feeling?")
        self.mood_label.pack()

        self.mood_var = tk.StringVar(value="😊")
        mood_options = {"😢": 1, "😐": 2, "🙂": 3, "😊": 4, "🤩": 5}
        for emoji in mood_options.keys():
            tk.Radiobutton(root, text=emoji, variable=self.mood_var, value=emoji).pack(anchor="w")

        self.note_label = tk.Label(root, text="Add a note:")
        self.note_label.pack()

        self.note_entry = tk.Text(root, height=4, width=40)
        self.note_entry.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Entry", command=self.save_entry)
        self.save_button.pack(pady=10)

        self.view_button = tk.Button(root, text="View Past Entries", command=self.view_entries)
        self.view_button.pack(pady=5)

    def fetch_weather(self):
        city = self.city_entry.get()
        data = get_weather_data(city)
        if data:
            self.weather_display.config(text=format_weather(data))
        else:
            messagebox.showerror("Error", "Could not fetch weather data.")

    def save_entry(self):
        emoji = self.mood_var.get()
        mood_score = {"😢": 1, "😐": 2, "🙂": 3, "😊": 4, "🤩": 5}[emoji]
        note = self.note_entry.get("1.0", tk.END).strip()
        timestamp = datetime.datetime.now().strftime("%I:%M %p, %B %d")

        entry = f"Mood: {emoji} ({mood_score}) at {timestamp}\nNote: {note}\n"
        save_journal_entry(entry)

        affirmation = random.choice(AFFIRMATIONS)
        messagebox.showinfo("Entry Saved!", f"✅ Saved!\n💬 {affirmation}")
        self.note_entry.delete("1.0", tk.END)

    def view_entries(self):
        entries = load_journal_entries()
        messagebox.showinfo("Journal Entries", entries or "No entries yet.")
