from PyQt5 import QtWidgets
import sys
from dungeondye.gui import mainmenu

def run() -> None:
    DungeonDye = QtWidgets.QApplication(sys.argv)
    main_menu = mainmenu.MainMenu()
    main_window = QtWidgets.QMainWindow()
    main_menu.setupUi(main_window)
    sys.exit(DungeonDye.exec_()) 



if __name__ == "__main__":
    run()

