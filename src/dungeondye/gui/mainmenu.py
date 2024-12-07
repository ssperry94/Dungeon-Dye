from tkinter import Label, Button, Tk, Frame
from tkinter.ttk import Combobox
from . import roller, titleframe


class MainMenu(Tk):
    #private attributes
    _main_frame:Frame = None
    _title:titleframe.Title = None
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
 

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("520x340")
        self.title("Dungeon Dice")

        self._main_frame = Frame(self)
        self._main_frame.grid(row = 0, column = 1)

        self._create_widgets()
        self._create_buttons()

    #wrapper function that instantiates a Dice object and modifies the outcome label with the final roll
    def _roll_dice(self) -> None:
        dye = roller.Dice()
        dye.rolldice(self._outcome_lbl, self._num_combo, self._side_combo, self._modifier_combo)

    #function that instantiates all widgets, except for buttons 
    def _create_widgets(self) -> None:

        self._title = titleframe.Title(self._main_frame)
        #label for dice number combo box
        self._num_lbl = Label(self, text = "Dice Number", bg = "white", fg = "green")
        self._num_lbl.grid(row = 1, column = 0)

        #numlist - range for dice number combolist
        #combo box that simulates how many dice to roll
        numlist: list[int] = [num for num in range(1,101)]
        self._num_combo = Combobox(self)
        self._num_combo['values'] = numlist
        self._num_combo.grid(row = 2, column = 0)

        #label that goes above the combo box for dice side 
        self._side_lbl = Label(self, text = "Dice Side", bg = "white", fg = "green")
        self._side_lbl.grid(row = 3, column = 0)

        #combo box to select the dice side 
        self._side_combo = Combobox(self)
        self._side_combo['values'] = (4,6,8,10,12,20,100)
        self._side_combo.grid(row = 4, column = 0)

        #label above modifer combo box
        #mod_list holds all options for adding some modifier 
        mod_list: list[int] = [num for num in range(0,101)]
        self._modifier_lbl = Label(self, text = "Modifier number",bg = "white", fg = "green")
        self._modifier_lbl.grid(row = 5, column = 0)

        #adds a modifer to the roll
        self._modifier_combo = Combobox(self)
        self._modifier_combo['values'] = mod_list
        self._modifier_combo.current(0)
        self._modifier_combo.grid(row = 6, column = 0)

        #displays the outcome of the roll
        self._outcome_lbl = Label(self,bg = "white", fg = "green")
        self._outcome_lbl.grid(row = 8, column = 2)

    #function that instantiates buttons only
    def _create_buttons(self) -> None:
        #button that rolls the dice
        self._roll_btn = Button(self, text = "Roll", command = lambda: self._roll_dice())
        self._roll_btn.grid(row = 7, column = 2)


