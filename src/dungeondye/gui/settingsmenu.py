from PyQt5 import QtWidgets


class SettingsMenu(QtWidgets.QDialog):
    _tab_widget:QtWidgets.QTabWidget = None
    _dice_tab:QtWidgets.QWidget = None 
    #add more tabs here as needed 

    def setupUi(self) -> None:
        self.setObjectName("settings_menu")
        self.setWindowTitle("Settings")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._tab_widget = QtWidgets.QTabWidget()
        self._initalize_tabs()

    def show(self):
        self.exec_()

    def _initalize_tabs(self):
        pass 