
class SavedRoll:
    dice_num:int = None
    dice_side:int = None 
    modifier:int = None 
    roll_name:str = None 

    def __init__(self, rolls:tuple, roll_name:str):
        self.dice_num = rolls[0]
        self.dice_side = rolls[1]
        self.modifier = rolls[2]
        self.roll_name = roll_name

    @property
    def get_dice_num(self) -> int:
        return self.dice_num

    @property
    def get_dice_side(self) -> int:
        return self.dice_side                    
    
    @property
    def get_modifier(self) -> int:
        return self.modifier 

    @property
    def get_roll_name(self) -> str:
        return self.roll_name       