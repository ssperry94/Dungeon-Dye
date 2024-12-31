import json 
from dungeondye.utils import constants

class RollParser:

    def upload(self):
        with(constants.SAVED_ROLLS_PATH, 'w') as outfile:
            saved_rolls_dict = self.format_saved_rolls()
            json.dump(saved_rolls_dict, outfile)