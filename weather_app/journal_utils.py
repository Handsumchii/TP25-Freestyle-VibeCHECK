import os
import json
from datetime import datetime


JOURNAL_FILE = "journal.txt"

def save_journal_entry(entry):
    with open(JOURNAL_FILE, "a", encoding="utf-8") as file:
        file.write(entry + "\n\n")

def load_journal_entries():
    if not os.path.exists(JOURNAL_FILE):
        return ""
    with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
        return file.read()
