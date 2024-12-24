from PyQt5 import QtCore, QtWidgets, QtGui
from dungeondye.gui import diceframe, bottomframe

class MainMenu(object):
    _title_label:QtWidgets.QLabel
    _pixmap:QtGui.QPixmap
    _layout:QtWidgets.QVBoxLayout 

    def setupUi(self, main_window:QtWidgets.QMainWindow) -> None:
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(500, 600)
        main_window.setAccessibleName("")
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("""background-color:rgb(35, 40, 48)\n""")
        main_window.setIconSize(QtCore.QSize(30, 30))
        main_window.setAnimated(True)
        main_window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self._layout = QtWidgets.QVBoxLayout(self.centralwidget)
        # self._layout.setContentsMargins(0,0,0,0)
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
        main_window.setToolTip(_translate("main_window", "<html><head/><body><p><br/></p></body></html>"))

    def _initalize_widgets(self) -> None:
        #set pixmap
        pixmap = QtGui.QPixmap(r'C:\Users\ssper\OneDrive\Projects\Table-Top-Dice-Roller\src\resources\images\DungeonDyeLogo.png')

        #create title label and add logo
        self._title_label = QtWidgets.QLabel(self.centralwidget)
        self._layout.addWidget(self._title_label, alignment=QtCore.Qt.AlignCenter)
        #self._title_label.setGeometry(QtCore.QRect(390, 30, 331, 221))
        self._title_label.setFixedSize(331,221)
        self._title_label.setPixmap(pixmap)
        self._title_label.setStyleSheet("border: 1px solid black")
        self._title_label.setScaledContents(True)
        #self._title_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self._title_label.setObjectName("title_label")
        
    
    def _initalize_frames(self, main_window:QtWidgets.QMainWindow):
        dice_frame = diceframe.DiceFrame(main_window)
        button_frame = bottomframe.ButtonFrame(main_window)
        dice_frame.setupUi()
        button_frame.setupUI()
        self._layout.addWidget(dice_frame, alignment=QtCore.Qt.AlignCenter)
        self._layout.addWidget(button_frame, alignment=QtCore.Qt.AlignCenter)
