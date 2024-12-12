from PyQt5 import QtWidgets
import sys
from dungeondye.gui import mainmenu

if __name__ == "__main__":
    DungeonDye = QtWidgets.QApplication(sys.argv)
    main_menu = mainmenu.MainMenu()
    DungeonDye.exec_()
    #DungeonDye.mainloop()
