'''
Frame containing the exit and save buttons 
'''
import tkinter as tk

class BottomButtons(tk.Frame):
    #private attributes
    _exit_bttn:tk.Button = None
    _save_bttn:tk.Button = None 
    _settings_btn:tk.Button = None

    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column = 0, row = 10)
        self._create_buttons()

    def _create_buttons(self):
        self._exit_bttn = tk.Button(self, text = "Exit", command = lambda: exit(0))
        self._exit_bttn.grid(column = 0, row = 0, padx = 20)
        
        self._save_bttn = tk.Button(self, text = "Save")
        self._save_bttn.grid(column = 1, row = 0, padx = 150)

        self._settings_btn = tk.Button(self, text = "Settings")
        self._settings_btn.grid(column = 2, row = 0, padx = 100, sticky= "nsew")