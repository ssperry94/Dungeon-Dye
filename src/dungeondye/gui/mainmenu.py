import tkinter as tk
from tkinter.ttk import Combobox
from . import titleframe, diceframe, bottomframe


class MainMenu(tk.Tk):
    #private attributes
    _main_frame:tk.Frame = None
    _title:titleframe.Title = None
    _dice_setup:diceframe.DiceFrame = None
    _saved_rolls_lbl:tk.Label = None
    _saved_rolls_combo:Combobox = None 
    _roll_btn:tk.Button = None 
 

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("520x340")
        self.title("Dungeon Dice")

        self._main_frame = tk.Frame(self)
        self._main_frame.grid_rowconfigure(0, weight=1)  # Title frame row
        self._main_frame.grid_columnconfigure(0, weight=1) 
        self._main_frame.grid(row = 0,column = 0,stick="nsew")



        self._create_frames()

    #function that instantiates all frames
    def _create_frames(self) -> None:
        self._title = titleframe.Title(self._main_frame)
        self._dice_setup = diceframe.DiceFrame(self._main_frame)
        




