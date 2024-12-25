import random 
from PyQt5.QtWidgets import QTextBrowser, QComboBox

class Dice: 
    def __init__(self) -> None:
        pass 

    def rolldice(self, output:QTextBrowser, num:QComboBox, sides:QComboBox, modifier:QComboBox) -> None:
        try:
            actual_num = int(num.currentText())
            actual_sides = int(sides.currentText())
            actual_modifier = int(modifier.currentText())
            list = []
            for roll in range(1, actual_num + 1):
                roll = random.randint(1, actual_sides)
                list.append(roll)
            final_roll = sum(list[0:])
            #print(f"Total roll: {final_roll}\nModifier: {actual_modifier}\nTotal: {final_roll + actual_modifier}")
            output.setText(f"Rolling {actual_num}d{actual_sides}\nTotal Roll: {final_roll}\nModifier: {actual_modifier}\nFinal Roll: {final_roll + actual_modifier}\n\n")
        except ValueError:
           print("ValueError Thrown")
