import tkinter as tk 
from tkinter import ttk
from . import roller

class DiceFrame(tk.Frame):
        _num_lbl:tk.Label = None
        _num_combo:ttk.Combobox = None
        _side_lbl:tk.Label = None
        _side_combo:ttk.Combobox = None
        _modifier_lbl:tk.Label = None
        _modifier_combo:ttk.Combobox = None
        _outcome_lbl:tk.Label = None
        _saved_rolls_lbl:tk.Label = None
        _saved_rolls_combo:ttk.Combobox = None 
        _roll_btn:tk.Button = None 

        def __init__(self, parent):
                super().__init__(parent)
                self.grid(column = 0, row = 1, sticky="nsew", padx = 20, pady = 20)
                self._create_widgets()
                self._create_buttons()

            #wrapper function that instantiates a Dice object and modifies the outcome label with the final roll
        def _roll_dice(self) -> None:
                dye = roller.Dice()
                dye.rolldice(self._outcome_lbl, self._num_combo, self._side_combo, self._modifier_combo)

        def _create_widgets(self):
                self._num_lbl = tk.Label(self, text = "Dice Number", bg = "white", fg = "green")
                self._num_lbl.grid(row = 1, column = 0)

                #numlist - range for dice number combolist
                #combo box that simulates how many dice to roll
                numlist: list[int] = [num for num in range(1,101)]
                self._num_combo = ttk.Combobox(self)
                self._num_combo['values'] = numlist
                self._num_combo.grid(row = 2, column = 0)

                #tk.Label that goes above the combo box for dice side 
                self._side_lbl = tk.Label(self, text = "Dice Side", bg = "white", fg = "green")
                self._side_lbl.grid(row = 3, column = 0)

                #combo box to select the dice side 
                self._side_combo = ttk.Combobox(self)
                self._side_combo['values'] = (4,6,8,10,12,20,100)
                self._side_combo.grid(row = 4, column = 0)

                #tk.Label above modifer combo box
                #mod_list holds all options for adding some modifier 
                mod_list: list[int] = [num for num in range(0,101)]
                self._modifier_lbl = tk.Label(self, text = "Modifier number",bg = "white", fg = "green")
                self._modifier_lbl.grid(row = 5, column = 0)

                #adds a modifer to the roll
                self._modifier_combo = ttk.Combobox(self)
                self._modifier_combo['values'] = mod_list
                self._modifier_combo.current(0)
                self._modifier_combo.grid(row = 6, column = 0)

                #displays the outcome of the roll
                self._outcome_lbl = tk.Label(self,bg = "white", fg = "green")
                self._outcome_lbl.grid(row = 8, column = 1)

                self._saved_rolls_lbl = tk.Label(self, text = "My Dice", bg = "white", fg = "green")
                self._saved_rolls_lbl.grid(row = 4, column = 2)

                self._saved_rolls_combo = ttk.Combobox(self)
                #add combox list here
                self._saved_rolls_combo.grid(row = 5, column = 2)

        def _create_buttons(self) -> None:
                #button that rolls the dice
                self._roll_btn = tk.Button(self, text = "Roll", command = lambda: self._roll_dice())
                self._roll_btn.grid(row = 7, column = 1, padx = 50, pady = 15)