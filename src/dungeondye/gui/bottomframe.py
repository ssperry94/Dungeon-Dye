from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonFrame(QtWidgets.QWidget):
    _exit_button:QtWidgets.QPushButton
    _save_button:QtWidgets.QPushButton
    _settings_button:QtWidgets.QPushButton
    _frame_layout:QtWidgets.QHBoxLayout

    def setupUI(self) -> None:
        self.setObjectName("button_panel")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self._frame_layout = QtWidgets.QHBoxLayout(self)
        self._initalize_buttons()

    def _initalize_buttons(self) -> None:
        self._exit_button = QtWidgets.QPushButton(text = "Exit")
        self._exit_button.setStyleSheet("background-color:\"#FE2B26\"")
        self._exit_button.setObjectName("exit_button")
        self._exit_button.setFixedSize(93,28)
        self._frame_layout.addWidget(self._exit_button)

        self._save_button = QtWidgets.QPushButton(text = "Save")
        self._save_button.setStyleSheet("background-color:\"#FE2B26\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(93,28)
        self._frame_layout.addWidget(self._save_button)

        self._settings_button = QtWidgets.QPushButton(text = "Settings")
        self._settings_button.setStyleSheet("background-color:\"#FE2B26\"")
        self._settings_button.setObjectName("settings_button")
        self._settings_button.setFixedSize(93,28)
        self._frame_layout.addWidget(self._settings_button)