import random 
from tkinter import messagebox
from tkinter import Label
from tkinter.ttk import Combobox
class Dice: 
    def __init__(self) -> None:
        pass 

    def rolldice(self, lbl:Label, num:Combobox, sides:Combobox, modifier:Combobox) -> None:
        try:
            num = int(num.get())
            sides = int(sides.get())
            modifier = int(modifier.get())
            list = []
            for roll in range(1, num + 1):
                roll = random.randint(1, sides)
                list.append(roll)
            lbl.config(text = f"Roll: {sum(list[0:]) + modifier}")
        except ValueError:
            messagebox.showerror("Error!", "Ensure that a value has been selected for the number and side box.")
