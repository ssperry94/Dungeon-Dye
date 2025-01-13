from dungeondye.parser import rollparser
from dungeondye.dice import savedroll
from dungeondye.utils import constants

'''
Functions that adjust various settings, or can make changes to global variables
'''
def search_saved_rolls(name:str) -> savedroll.SavedRoll:
    for roll in constants.SAVED_ROLLS_LIST:
        if roll.roll_name == name:
            return roll
    return None

def add_new_roll(roll_info:tuple, roll_name:str) -> bool:
    #turn into a saved roll
    new_roll = savedroll.SavedRoll(roll_info, roll_name)
     #add to list 
    constants.SAVED_ROLLS_LIST.append(new_roll)
    #write out list 
    parser = rollparser.RollParser()
    return parser.upload() 

def create_saved_rolls_list() -> list:
    saved_roll_list:list = []
    parser = rollparser.RollParser()
    roll_info:dict = parser.retrieve()

    for key, value in roll_info.items():
        roll_name = key
        roll_tuple = (value.get(constants.DICENUM), value.get(constants.DICESIDE), value.get(constants.MODIFIER))
        saved_roll = savedroll.SavedRoll(roll_tuple, roll_name)
        saved_roll_list.append(saved_roll)

    return saved_roll_list

def clear_saved_rolls() -> bool:
    constants.SAVED_ROLLS_LIST.clear()
    parser = rollparser.RollParser()
    return parser.upload()

def find_roll_index(name:str) -> int:
    for index, roll in enumerate(constants.SAVED_ROLLS_LIST):
        if roll.roll_name == name:
            return index 
    
    return -1 #roll couldn't be found

def remove_roll(index:int) -> bool:
    try:
        constants.SAVED_ROLLS_LIST.pop(index)
        parser = rollparser.RollParser()
        return parser.upload()
    except IndexError:
        return False