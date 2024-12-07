from tkinter import Label, Button, Tk
from tkinter.ttk import Combobox
from . import roller 


class MainMenu(Tk):
    #private attributes
    _title_lbl:Label = None 
    _num_lbl:Label = None
    _num_combo:Combobox = None
    _side_lbl:Label = None
    _side_combo:Combobox = None
    _modifier_lbl:Label = None
    _modifier_combo:Combobox = None
    _outcome_lbl:Label = None
    _saved_rolls_lbl:Label = None
    _saved_rolls_combo:Combobox = None 
    _roll_btn:Button = None 
    _save_btn:Button = None 
    _settings_btn:Button = None 

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("300x240")
        self.title("Dice Roller")

        self._create_widgets()
        self._create_buttons()

    #wrapper function that instantiates a Dice object and modifies the outcome label with the final roll
    def _roll_dice(self, outcome:Label, dice_number:Combobox, dice_sides:Combobox, modifier_box:Combobox) -> None:
        dye = roller.Dice()
        dye.rolldice(outcome, dice_number, dice_sides, modifier_box)

    #function that instantiates all widgets, except for buttons 
    def _create_widgets(self) -> None:
        #label for dice number combo box
        self._num_lbl = Label(self, text = "Dice Number", bg = "white", fg = "green")
        self._num_lbl.pack()

        #numlist - range for dice number combolist
        #combo box that simulates how many dice to roll
        numlist: list[int] = [num for num in range(1,101)]
        self._num_combo = Combobox(self)
        self._num_combo['values'] = numlist
        self._num_combo.pack()

        #label that goes above the combo box for dice side 
        self._side_lbl = Label(self, text = "Dice Side", bg = "white", fg = "green")
        self._side_lbl.pack()

        #combo box to select the dice side 
        self._side_combo = Combobox(self)
        self._side_combo['values'] = (4,6,8,10,12,20,100)
        self._side_combo.pack()

        #label above modifer combo box
        #mod_list holds all options for adding some modifier 
        mod_list: list[int] = [num for num in range(0,101)]
        self._modifier_lbl = Label(self, text = "Modifier number",bg = "white", fg = "green")
        self._modifier_lbl.pack()

        #adds a modifer to the roll
        self._modifier_combo = Combobox(self)
        self._modifier_combo['values'] = mod_list
        self._modifier_combo.current(0)
        self._modifier_combo.pack()

        #displays the outcome of the roll
        self._outcome_lbl = Label(self,bg = "white", fg = "green")
        self._outcome_lbl.pack()

    #function that instantiates buttons only
    def _create_buttons(self) -> None:
        #button that rolls the dice
        self._roll_btn = Button(self, text = "Roll", command = lambda: self._roll_dice(self._outcome_lbl, self._num_combo, self._side_combo, self._modifier_combo))
        self._roll_btn.pack()


