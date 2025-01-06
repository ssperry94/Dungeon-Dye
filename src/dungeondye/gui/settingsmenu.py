from PyQt5 import QtCore, QtWidgets
from dungeondye.utils import constants

#all tab widgets defined before SettingMenu 
class _DiceSettings(QtWidgets.QWidget):
    _layout:QtWidgets.QGridLayout = None
    _widget_list:list = [] #contains all buttons and roll names
    _roll_container:QtWidgets.QGroupBox = None #a scrollable box that contains all rolls and check button 
    _clear_button:QtWidgets.QPushButton = None #button that clears all saved rolls 
    _delete_button:QtWidgets.QPushButton = None #button that deletes all selected rolls

    def setupUi(self):
        self.setObjectName("dice_settings")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._layout = QtWidgets.QGridLayout(self)
        self._initalize_roll_container()
        self._initalize_buttons()

    def _populate_roll_container(self, layout:QtWidgets.QVBoxLayout):
        for roll in constants.SAVED_ROLLS_LIST:
            roll_btn = QtWidgets.QCheckBox(roll.roll_name)
            self._widget_list.append(roll_btn)
            layout.addWidget(roll_btn)

    def _initalize_roll_container(self):
        self._roll_container = QtWidgets.QGroupBox()
        roll_layout = QtWidgets.QVBoxLayout(self._roll_container)

        self._populate_roll_container(roll_layout)
        self._layout.addWidget(self._roll_container, 0,1)


    def _initalize_buttons(self):
        self._clear_button = QtWidgets.QPushButton(text = "Clear")
        self._clear_button.setObjectName("clear_button")
        self._clear_button.setFixedSize(85,23)
        self._layout.addWidget(self._clear_button, 1,0)

        self._delete_button = QtWidgets.QPushButton(text = "Delete")
        self._delete_button.setObjectName("delete_button")
        self._delete_button.setFixedSize(85,23)
        self._layout.addWidget(self._delete_button, 1,2)

    
class SettingsMenu(QtWidgets.QDialog):
    _tab_widget:QtWidgets.QTabWidget = None
    _dice_tab:QtWidgets.QWidget = None 
    _layout:QtWidgets.QVBoxLayout = None
    #add more tabs here as needed 
    _close_bttn:QtWidgets.QPushButton = None

    def setupUi(self) -> None:
        self.setObjectName("settings_menu")
        self.setWindowTitle("Settings")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._tab_widget = QtWidgets.QTabWidget()
        self._layout = QtWidgets.QGridLayout(self)
        self._initalize_tabs()
        self._initalize_buttons()
        self._layout.addWidget(self._tab_widget, 0, 0)
        self._layout.addWidget(self._close_bttn, 1,0, alignment=QtCore.Qt.AlignHCenter)

    def show(self) -> None:
        self.exec_()

    def _initalize_tabs(self) -> None:
        self._dice_tab = _DiceSettings()
        self._dice_tab.setupUi()
        self._tab_widget.addTab(self._dice_tab, "Roll Manager")

    def _initalize_buttons(self) -> None:
        self._close_bttn = QtWidgets.QPushButton(text = "Close")
        self._close_bttn.setObjectName("close_button")
        self._close_bttn.setFixedSize(85,23)
        self._close_bttn.clicked.connect(self.reject)
