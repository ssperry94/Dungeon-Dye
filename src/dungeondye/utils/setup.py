import os 
import json
from dungeondye.utils import constants

'''Functions to assist in startup'''
def setup() -> None:
    if detect_saved_rolls() is False:
        raise FileNotFoundError
    
def detect_saved_rolls() -> bool:
    return os.path.exists(constants.SAVED_ROLLS_PATH)

def get_saved_roll_path() -> str:
    pass 

def create_saved_roll_file() -> bool:
    #write default rolls into User/AppData/Local/DungeonDye 
    with open(constants.SAVED_ROLLS_PATH, "w") as outfile:
        json.dump({}, outfile)
        return True 
    return False

#creates DungeonDye app data directory 
def create_local_data_dir() -> bool:
    pass 