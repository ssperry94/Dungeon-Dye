from PyQt5 import QtWidgets
import sys
from dungeondye.gui import diceframe, savedmenu, settingsmenu
from dungeondye.utils import constants

class ButtonFrame(QtWidgets.QWidget):
    _exit_button:QtWidgets.QPushButton
    _save_button:QtWidgets.QPushButton
    _settings_button:QtWidgets.QPushButton
    _frame_layout:QtWidgets.QHBoxLayout
    _dice_frame:diceframe.DiceFrame = None #used to get info when saving rolls 

    def setupUI(self, diceframe) -> None:
        self._dice_frame = diceframe
        self.setObjectName("button_panel")
        self.setStyleSheet(f"background-color:{constants.APP_BACKGROUND_COLOR}\n"
"")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self._frame_layout = QtWidgets.QHBoxLayout(self)
        self._frame_layout.setSpacing(100)
        self._initalize_buttons()

    def _initalize_buttons(self) -> None:
        self._exit_button = QtWidgets.QPushButton(text = "Exit")
        self._exit_button.setStyleSheet(f"background-color:\"{constants.BUTTON_COLOR}\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._exit_button.setObjectName("exit_button")
        self._exit_button.setFixedSize(constants.BUTTON_HEIGHT, constants.BUTTON_WIDTH)
        self._exit_button.clicked.connect(sys.exit)  #may need own exit function here 
        self._frame_layout.addWidget(self._exit_button)

        self._save_button = QtWidgets.QPushButton(text = "Save")
        self._save_button.setStyleSheet(f"background-color:\"{constants.BUTTON_COLOR}\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(constants.BUTTON_HEIGHT, constants.BUTTON_WIDTH)
        self._save_button.clicked.connect(self.show_save_menu)
        self._frame_layout.addWidget(self._save_button)

        self._settings_button = QtWidgets.QPushButton(text = "Settings")
        self._settings_button.setStyleSheet(f"background-color:\"{constants.BUTTON_COLOR}\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._settings_button.setObjectName("settings_button")
        self._settings_button.setFixedSize(constants.BUTTON_HEIGHT, constants.BUTTON_WIDTH)
        self._settings_button.clicked.connect(self.show_settings_menu)
        self._frame_layout.addWidget(self._settings_button)
    
    def show_save_menu(self):
        rolls = self._dice_frame.get_current_combo_values()

        #if error was thrown, set dice number, side, and mod to 0
        if rolls is None:
            rolls = (0,0,0)

        save_menu = savedmenu.SavedMenu()
        save_menu.setupUi(rolls)
        save_menu.show()
        self._dice_frame.update_saved_rolls()

    def show_settings_menu(self):
        settings = settingsmenu.SettingsMenu()
        settings.setupUi(self._dice_frame)
        settings.exec_()