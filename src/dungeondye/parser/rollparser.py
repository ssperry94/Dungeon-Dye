import json 
from dungeondye.utils import constants
from dungeondye.dice import savedroll
class RollParser:

    def upload(self):
        saved_rolls_dict = self.format_saved_rolls()
        with open(constants.SAVED_ROLLS_PATH, 'w') as outfile:
            json.dump(saved_rolls_dict, outfile)

    def format_saved_rolls(self) -> dict:
        roll_dict = {}
        for roll in constants.SAVED_ROLLS_LIST:
            roll_dict.update({roll.roll_name : {constants.DICENUM : roll.dice_num, constants.DICESIDE : roll.dice_side, constants.MODIFIER : roll.modifier}})

        return roll_dict

if __name__ == '__main__':
    parser = RollParser()
    parser.upload()