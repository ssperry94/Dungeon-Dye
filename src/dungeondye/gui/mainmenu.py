from PyQt5 import QtCore, QtWidgets, QtGui
from dungeondye.gui import diceframe, bottomframe
from dungeondye.utils import constants

class MainMenu(object):
    _title_label:QtWidgets.QLabel
    _pixmap:QtGui.QPixmap
    _layout:QtWidgets.QVBoxLayout 
    _roll_shortcut:QtWidgets.QShortcut
    _save_shortcut:QtWidgets.QShortcut

    def setupUi(self, main_window:QtWidgets.QMainWindow) -> None:
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(500, 600)
        main_window.setAccessibleName("")
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet(f"""background-color:{constants.APP_BACKGROUND_COLOR}\n""")
        main_window.setIconSize(QtCore.QSize(30, 30))
        main_window.setAnimated(True)
        main_window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self._layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self._initalize_widgets()
        self._initalize_frames(main_window)
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.show()

    def retranslateUi(self, main_window:QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Dungeon Dice"))

    def _initalize_widgets(self) -> None:
        #set pixmap
        pixmap = QtGui.QPixmap(constants.DUNGEON_LOGO)

        #create title label and add logo
        self._title_label = QtWidgets.QLabel(self.centralwidget)
        self._layout.addWidget(self._title_label, alignment=QtCore.Qt.AlignCenter)
        self._title_label.setFixedSize(331,221)
        self._title_label.setPixmap(pixmap)
        self._title_label.setStyleSheet("border: 1px solid black")
        self._title_label.setScaledContents(True)
        self._title_label.setObjectName("title_label")
        
    
    def _initalize_frames(self, main_window:QtWidgets.QMainWindow):
        dice_frame = diceframe.DiceFrame(main_window)
        button_frame = bottomframe.ButtonFrame(main_window)
        dice_frame.setupUi()
        button_frame.setupUI(dice_frame)
        self._initalize_shortcut(main_window, dice_frame, button_frame)
        self._layout.addWidget(dice_frame, alignment=QtCore.Qt.AlignCenter)
        self._layout.addWidget(button_frame, alignment=QtCore.Qt.AlignCenter)

    def _initalize_shortcut(self, main_window:QtWidgets.QMainWindow, dice_frame:diceframe.DiceFrame, bottom_frame:bottomframe.ButtonFrame):
        self._roll_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), main_window)
        self._roll_shortcut.activated.connect(dice_frame.roll)

        self._save_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), main_window)
        self._save_shortcut.activated.connect(bottom_frame.show_save_menu)