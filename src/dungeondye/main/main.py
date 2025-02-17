from PyQt5 import QtWidgets
import sys
from dungeondye.gui import mainmenu

#CURRENTLY: need a way to get default path for saved_rolls_json, then detect if file exits, and if not, create one
def run() -> None:
    DungeonDye = QtWidgets.QApplication(sys.argv)
    main_menu = mainmenu.MainMenu()
    main_window = QtWidgets.QMainWindow()
    main_menu.setupUi(main_window)
    sys.exit(DungeonDye.exec_()) 



if __name__ == "__main__":
    run()

