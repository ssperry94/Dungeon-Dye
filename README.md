
# Dungeon Dye

Dungeon Dye is a feature-rich dice rolling app designed for tabletop RPG players. It allows users to save frequently used rolls and quickly retrieve them for convenience. With an intuitive interface and streamlined roll management, Dungeon Dye enhances your gameplay experience by eliminating repetitive dice inputs.

## License

This software is licensed under GNU General Public License v3, which means:

- You can freely use, modify, and distribute it.
- Any modifications or redistributions must also be open-source under GPL v3. 
- For full details, please view the `LICENSE.MD` file or visit [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.txt)





## Description

Dungeon Dye is a lightweight, fully customizable dice rolling app designed for tabletop RPG players and Game Masters. If you’re tired of repeatedly rolling the same dice combinations, Dungeon Dye lets you create custom rolls and save them for quick access. This dice roller is perfect for the lazy GM or efficient player who wants to focus on the adventure and eliminate some overhead. 

Dungeon Dye is completely open-source and fully modifiable, giving you complete control over how you use it. If you choose to modify and distribute it, please ensure it complies with the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt) license.
## How to Run

You can either clone this repo and build it yourself or download the latest exe file from the releases page. Below are instructions for how to build this project from the source code. 

### Dependencies 
- [Python v3.11](https://www.python.org/downloads/) or later
- [Pyinstaller](https://pyinstaller.org/en/stable/installation.html) (only if building the exe yourself)
- see all other dependencies in `requirements.txt` 

### Running from the Executable 
If you've downloaded the executable, make sure that the package includes a resources directory with an images and jsons subdirectory, and the executable. 

To run, simply double click the executable file. **NOTE** this executable *has no digital signature* so Windows SmartScreen may flag this application. To bypass, simply click More Info -> Run Anyway.  
### How to Build 
To build and run from the command line:

1. clone this repository with `git clone https://github.com/ssperry94/Dungeon-Dye`
2. `cd Dungeon-Dye` 
3. Create a virtual environment (optional but recommended) 
4. run `pip install -r requirements.txt`
5. run `cd src` 
6. run `python -m dungeondye.main` 

To create the executable yourself: 

1. Ensure pyinstaller is install on your machine (see dependencies section)
2. clone this repository with `git clone https://github.com/ssperry94/Dungeon-Dye`
2. `cd Dungeon-Dye` 
3. Create a virtual environment (optional but recommended) 
4. run `pip install -r requirements.txt`
5. run `pyinstaller src/dungeondye/main.py --onefile --noconsole`
6. Copy the resources folder from the src directory to the dist directory using one of the following commands:
- PowerShell: `Copy-Item -Path src/resources -Destination ./dist -Recurse`

- Command Prompt: `robocopy ./src/resources ./dist/resources /e`

- Bash: `cp ./src/resource ./dist -r`

7. `cd ./dist` then double click on the executable
## Tutorial

Once the application is running, using it is fairly straight forward. In the main menu, you should see this screen:

<p><img src='/docs/main_menu.png'></p>

On the left side, there is a Dice Number box, a Dice Side box, and a modifier box. You can either select values straight from the box, or type in any numerical value greater than or equal to zero. Dice number refers to how many dice you wish to roll, and dice side indicates the type of dice being thrown. 

The modifier box adds that number to your final roll. For example, to roll 2d8 + 3, the dice number box should be set to 2, the dice side to 8, and the modifier to 3.  

<p><img src='/docs/2_d_8.png'></p>

To roll, either click the button in the center of the app with the d20 on it, or use the keyboard shortcut CTRL+R. The box underneath the roll button displays the output of the roll. 

To save a roll, simply either click the save button in the bottom center, or press CTRL+S. That will bring up the roll saver screen. 

<p><img src='/docs/save_menu.png'></p> 

All of the dice information will default to what is currently being rolled in the main menu, but you can change these values as needed. Once you are ready to save, make sure to name your roll. Each name must be unique to your roll. If you try and give a roll the same name as another, it will ask if you wish to overwrite this roll. 

To access your saved roll, simply click on the Saved Rolls box - which is where Dungeon Dye will store all of your rolls. Upon selecting the roll, you'll notice that all of the boxes in the main menu will automatically update to the values within that roll. 

To delete any rolls in your list, simply click on the settings button, and the settings menu will appear. 

<p><img src='/docs/settings.png'></p>

As of now, there are only options to either delete specific rolls or clear the entire list. Simply checkmark the rolls you wish to delete and hit the delete button. If you wish to delete all your rolls, you can either select them all or hit the clear button. 

