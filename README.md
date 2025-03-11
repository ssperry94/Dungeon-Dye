
# Dungeon Dye

Dungeon Dye is a feature-rich dice rolling app designed for tabletop RPG players. It allows users save frequently used rolls, and quickly retrieve them for convenience. With an intuitive interface and streamlined roll management, Dungeon Dye enhances your gameplay experience by eliminating repetitive dice inputs.


## License

This software is liscensed under GNU General Public License v3, which means:

- You can freely use, modify, and distribute it.
- Any modifications or redistributions must also be open-source under GPL v3. 
- For full details, please view the `LICENSE.MD` file or visit [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.txt)






## Discription

Dungeon Dye is a lightweight, fully customizable dice rolling app designed for tabletop RPG players and Game Masters. If you’re tired of repeatedly rolling the same dice combinations, Dungeon Dye lets you create custom rolls and save them for quick access. This dice roller is perfect for the lazy GM or efficient player who wants to focus on the adventure and elimate some overhead. 

Dungeon Dye is completely open-source and fully modifiable, giving you complete control over how you use it. If you choose to modify and distribute it, please ensure it complies with the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt) license.
## How to Run

You can either clone this repo and build it yourself, or download the latest exe file from the releases page. Below are instructions for how to build this project from the source code. 

### Dependancies 
- [Python v3.11](https://www.python.org/downloads/) or later
- [Pyinstaller](https://pyinstaller.org/en/stable/installation.html) (only if building the exe yourself)
- see all other dependancies in `requirements.txt` 

### How to Build 
To build and run from the command line:

1. clone this repository with `git clone https://github.com/ssperry94/Dungeon-Dye`
2. `cd Dungeon-Dye` 
3. Create a virtual enviorment (optional but recommended) 
4. run `pip install -r requirements.txt`
5. run `cd src` 
6. run `python -m dungeondye.main` 

To create the executable yourself: 

1. Ensure pyinstaller is install on your machine (see dependancies section)
2. clone this repository with `git clone https://github.com/ssperry94/Dungeon-Dye`
2. `cd Dungeon-Dye` 
3. Create a virtual enviorment (optional but recommended) 
4. run `pip install -r requirements.txt`
5. run `pyinstaller src/dungeondye/main.py --onefile --noconsole`
6. Copy the resources folder from the src directory using one of the following commands:
```Powershell`Copy-Item -Path src/resources -Destination ./dist -Recurse````



