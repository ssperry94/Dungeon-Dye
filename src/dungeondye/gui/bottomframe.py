from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from dungeondye.gui import diceframe, savedmenu

class ButtonFrame(QtWidgets.QWidget):
    _exit_button:QtWidgets.QPushButton
    _save_button:QtWidgets.QPushButton
    _settings_button:QtWidgets.QPushButton
    _frame_layout:QtWidgets.QHBoxLayout
    _button_height:int = 85
    _button_width:int = 23
    _dice_frame:diceframe.DiceFrame = None #used to get info when saving rolls 

    def setupUI(self, diceframe) -> None:
        self._dice_frame = diceframe
        self.setObjectName("button_panel")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self._frame_layout = QtWidgets.QHBoxLayout(self)
        self._frame_layout.setSpacing(100)
        self._initalize_buttons()

    def _initalize_buttons(self) -> None:
        self._exit_button = QtWidgets.QPushButton(text = "Exit")
        self._exit_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._exit_button.setObjectName("exit_button")
        self._exit_button.setFixedSize(self._button_height, self._button_width)
        self._exit_button.clicked.connect(sys.exit)  #may need own exit function here 
        self._frame_layout.addWidget(self._exit_button)

        self._save_button = QtWidgets.QPushButton(text = "Save")
        self._save_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(self._button_height, self._button_width)
        self._save_button.clicked.connect(self.show_save_menu)
        self._frame_layout.addWidget(self._save_button)

        self._settings_button = QtWidgets.QPushButton(text = "Settings")
        self._settings_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._settings_button.setObjectName("settings_button")
        self._settings_button.setFixedSize(self._button_height, self._button_width)
        self._settings_button.clicked.connect(self.show_settings_menu)
        self._frame_layout.addWidget(self._settings_button)
    
    def show_save_menu(self):
        rolls = self._dice_frame.get_current_combo_values()
        if rolls is not None:
            save_menu = savedmenu.SavedMenu()
            save_menu.setupUi(rolls)
            save_menu.show()

    #placeholder for settings menu
    def show_settings_menu(self):
        settings = QtWidgets.QMessageBox()
        settings.setWindowTitle("Coming soon")
        settings.setIcon(QtWidgets.QMessageBox.Information)
        settings.setText("Settings comming soon!")
        settings.exec_()