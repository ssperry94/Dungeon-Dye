'''
Frame that contains the title menu, and settings button
Occupies the top half of main menu window 
'''

#imports
import tkinter as tk 

class Title(tk.Frame):
    #private fields
    _main_frame:tk.Frame = None  
    _title_lbl:tk.Label = None
    _settings_btn:tk.Button = None

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg = "black")
        self.grid_rowconfigure(0, weight=1)  # Allow row to expand
        self.grid_columnconfigure(0, weight=1)  # Title label column
        self.grid_columnconfigure(1, weight=0)  # Settings button column
        self.grid(row = 0, column = 0, sticky = "nsew")

        self._create_widgets()
        self._create_buttons()

    def _create_widgets(self) -> None:
        self._title_lbl = tk.Label(self, text = "Dungeon Dye", bg = "black", fg = "red", font = 25, pady = 3)
        self._title_lbl.grid(column = 0, row = 0, sticky = "nsew")

    def _create_buttons(self) -> None: 
        self._settings_btn = tk.Button(self, text = "Settings")
        self._settings_btn.grid(column = 1, row = 0, padx = 15, sticky= "nsew")