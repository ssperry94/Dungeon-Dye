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
        self.config(bg = "black", width = 10)
        self.grid(row = 0, column = 1)
        self._create_widgets()

    def _create_widgets(self) -> None:
        self._title_lbl = tk.Label(self, text = "Dungeon Dye", bg = "black", fg = "red", width = 50, font = 25)
        self._title_lbl.pack()

    def _create_buttons(self) -> None: 
        pass 