'''
File containing all constatns and settings read in from settings.json
Need functionality for settings.json as well
'''

from dungeondye.dice import savedroll
from dungeondye.utils import utilities
#path to the saved rolls json 
SAVED_ROLLS_PATH:str = r'C:\Users\ssper\OneDrive\Projects\Table-Top-Dice-Roller\src\resources\jsons\saved_rolls.json'

#exact spelling of keys of dictionary:
DICENUM = "dicenumber"
DICESIDE = "diceside"
MODIFIER = "modifier"

#list that contains dice numbers 
DICE_NUM_LIST = [str(num) for num in range(1,101)] #number of dye possible
DICE_SIDE_LIST = ['4','6','8','10','12','20','100'] #standard dice sides 
MODIFIER_LIST = [str(num) for num in range(0,101)] #number you can modify

#list of all saved rolls 
SAVED_ROLLS_LIST:savedroll.SavedRoll = utilities.create_saved_rolls_list() 

