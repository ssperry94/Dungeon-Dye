from PyQt5 import QtWidgets
import sys
from dungeondye.gui import mainmenu

if __name__ == "__main__":
    DungeonDye = QtWidgets.QApplication(sys.argv)
    main_menu = mainmenu.MainMenu()
    main_window = QtWidgets.QMainWindow()
    main_menu.setupUi(main_window)
    DungeonDye.exec_()
    #DungeonDye.mainloop()
