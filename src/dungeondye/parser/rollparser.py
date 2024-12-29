import json 
from dungeondye.utils import constants

class RollParser:

    def retrive(self) -> dict:
        with open(constants.SAVED_ROLLS_PATH, "r") as roll_file:
            rolls = json.load(roll_file)
            return rolls
        
    def upload(self, rolls:tuple) -> bool:
        #read in whats on saved rolls as a dictionary 
        #add a new entry 
        #write it out 
        with open(constants.SAVED_ROLLS_PATH, "w"):
            pass 

    def _format_data(self, rolls:tuple) -> dict:
        dict = {"dicenumber" : rolls[0],
                "diceside" : rolls[1],
                "modifier" : rolls[2]
                }
        
        return dict