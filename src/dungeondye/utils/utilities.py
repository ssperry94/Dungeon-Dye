from dungeondye.parser import rollparser
from dungeondye.dice import savedroll
from dungeondye.utils import constants

'''
Functions that adjust various settings, or can make changes to global variables
'''
def add_new_roll(roll_info:tuple, roll_name:str) -> bool:
    #turn into a saved roll
    new_roll = savedroll.SavedRoll(roll_info, roll_name)
     #add to list 
    constants.SAVED_ROLLS_LIST.append(new_roll)
    #write out list 
    parser = rollparser.RollParser()
    return parser.upload() 

def search_saved_rolls(name:str) -> savedroll.SavedRoll:
    for roll in constants.SAVED_ROLLS_LIST:
        if roll.roll_name == name:
            return roll