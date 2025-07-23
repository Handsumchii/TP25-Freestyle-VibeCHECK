from .ui import WeatherUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherUI(root)
    root.mainloop()
