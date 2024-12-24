from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonFrame(QtWidgets.QWidget):
    _exit_button:QtWidgets.QPushButton
    _save_button:QtWidgets.QPushButton
    _settings_button:QtWidgets.QPushButton
    _frame_layout:QtWidgets.QHBoxLayout
    _button_height:int = 85
    _button_width:int = 23


    def setupUI(self) -> None:
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
        self._frame_layout.addWidget(self._exit_button)

        self._save_button = QtWidgets.QPushButton(text = "Save")
        self._save_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(self._button_height, self._button_width)
        self._frame_layout.addWidget(self._save_button)

        self._settings_button = QtWidgets.QPushButton(text = "Settings")
        self._settings_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._settings_button.setObjectName("settings_button")
        self._settings_button.setFixedSize(self._button_height, self._button_width)
        self._frame_layout.addWidget(self._settings_button)