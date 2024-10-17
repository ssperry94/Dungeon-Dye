'''
Main source .py file for Dice Roller
Must run this file. 
'''


from tkinter import Label, Button, Tk
from tkinter.ttk import Combobox
import roller


class MainMenu(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("300x240")
        self.title("Dice Roller")

        num_lbl = Label(self, text = "Dice Number", bg = "white", fg = "green")
        num_lbl.pack()

        numlist = [num for num in range(1,101)]
        num_combo = Combobox(self)
        num_combo['values'] = numlist
        num_combo.pack()

        side_lbl = Label(self, text = "Dice Side", bg = "white", fg = "green")
        side_lbl.pack()

        side_combo = Combobox(self)
        side_combo['values'] = (4,6,8,10,12,20,100)
        side_combo.pack()

        mod_list = [num for num in range(0,101)]
        modifierlbl = Label(self, text = "Modifier number",bg = "white", fg = "green")
        modifierlbl.pack()

        modifier_combo = Combobox(self)
        modifier_combo['values'] = mod_list
        modifier_combo.current(0)
        modifier_combo.pack()

        #button that rolls the dice
        roll_btn = Button(self, text = "Roll", command = lambda: self._roll_dice(outcome_lbl, num_combo, side_combo, modifier_combo))
        roll_btn.pack() 

        outcome_lbl = Label(self,bg = "white", fg = "green")
        outcome_lbl.pack()

    #wrapper function that instantiates a Dice object and modifies the outcome label with the final roll
    def _roll_dice(self, outcome:Label, dice_number:Combobox, dice_sides:Combobox, modifier_box:Combobox) -> None:
        dye = roller.Dice()
        dye.rolldice(outcome, dice_number, dice_sides, modifier_box)

#main
if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()

