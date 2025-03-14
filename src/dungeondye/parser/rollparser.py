import json 
from dungeondye.utils import constants, setup
class RollParser:

    def upload(self) -> bool:
        saved_rolls_dict = self.format_saved_rolls()
        with open(constants.SAVED_ROLLS_PATH, 'w') as outfile:
            json.dump(saved_rolls_dict, outfile)
        if saved_rolls_dict == self.retrieve():
            return True 
        else:
            return False

    def retrieve(self) -> dict:
        roll_dict = {}
        try:
            with open(constants.SAVED_ROLLS_PATH, 'r') as infile:
                try:
                    roll_dict = json.load(infile)
                except ValueError:
                    pass
        except FileNotFoundError as e:
            setup.create_saved_roll_file()
            
        return roll_dict
    
    def format_saved_rolls(self) -> dict:
        roll_dict = {}
        for roll in constants.SAVED_ROLLS_LIST:
            roll_dict.update({roll.roll_name : {constants.DICENUM : roll.dice_num, constants.DICESIDE : roll.dice_side, constants.MODIFIER : roll.modifier}})

        return roll_dict
