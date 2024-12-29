import json 
from dungeondye.utils import constants

class SavedRoll:
    _dice_num:int = None
    _dice_side:int = None 
    _modifier:int = None 
    _roll_name:str = None 

    def __init__(self, rolls:tuple, roll_name:str):
        self._dice_num = rolls[0]
        self._dice_side = rolls[1]
        self._modifier = rolls[2]
        self._roll_name = roll_name


                                   
    