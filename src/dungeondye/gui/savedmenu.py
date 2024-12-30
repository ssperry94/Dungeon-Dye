from PyQt5 import QtWidgets, QtGui
from dungeondye.gui import diceframe

class SavedMenu(QtWidgets.QDialog):
    _dice_side_label:QtWidgets.QLabel = None
    _dice_number_label:QtWidgets.QLabel = None
    _modifier_label:QtWidgets.QLabel = None 
    _roll_name_label:QtWidgets.QLabel = None 

    _dice_number_combo:QtWidgets.QComboBox = None 
    _dice_side_combo:QtWidgets.QComboBox = None 
    _modifier_combo:QtWidgets.QComboBox = None 

    _roll_name_text:QtWidgets.QLineEdit = None 

    _exit_bttn:QtWidgets.QPushButton = None 
    _save_bttn:QtWidgets.QPushButton = None

    _layout:QtWidgets.QGridLayout = None  

    def setupUi(self) -> None:
        self.setObjectName("save_panel")
        self.setWindowTitle("Roll Saver")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._layout = QtWidgets.QGridLayout(self)
        self._initalize_widgets()
        self._initalize_buttons()
        

    def show(self) -> None:
        self.exec_()
    
    def _initalize_widgets(self) -> None:
        self._dice_number_label = QtWidgets.QLabel(text = "Dice Number")
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_number_label.setFont(font)
        self._dice_number_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_number_label.setObjectName("_dice_number_label")
        self._layout.addWidget(self._dice_number_label, 0, 1)

        self._dice_number_combo = QtWidgets.QComboBox()
        self._dice_number_combo.setEditable(True)
        self._dice_number_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_number_combo.setObjectName("_dice_number_combo")
        self._layout.addWidget(self._dice_number_combo, 1, 1)

        self._dice_side_label = QtWidgets.QLabel("Dice Side")
        # self._dice_side_label.setGeometry(QtCore.QRect(40, 100, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_side_label.setFont(font)
        self._dice_side_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_side_label.setObjectName("_dice_side_label")
        self._layout.addWidget(self._dice_side_label, 2, 1)

        self._dice_side_combo = QtWidgets.QComboBox()
        self._dice_side_combo.setEditable(True)
        # self._dice_side_combo.setGeometry(QtCore.QRect(40, 130, 131, 22))
        self._dice_side_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_side_combo.setObjectName("_dice_side_combo")
        self._layout.addWidget(self._dice_side_combo, 3, 1)

        self._modifier_label = QtWidgets.QLabel("Modifier")
        # self._modifier_label.setGeometry(QtCore.QRect(40, 160, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._modifier_label.setFont(font)
        self._modifier_label.setStyleSheet("color:\"#FE2B26\"")
        self._modifier_label.setObjectName("_modifier_label")
        self._layout.addWidget(self._modifier_label, 4, 1)

        self._modifiers_combo = QtWidgets.QComboBox()
        self._modifiers_combo.setEditable(True)
        # self._modifiers_combo.setGeometry(QtCore.QRect(40, 180, 131, 22))
        self._modifiers_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._modifiers_combo.setObjectName("_modifiers_combo")
        self._layout.addWidget(self._modifiers_combo, 5, 1)

        self._roll_name_label = QtWidgets.QLabel(text = "Name")
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._roll_name_label.setFont(font)
        self._roll_name_label.setStyleSheet("color:\"#FE2B26\"")
        self._roll_name_label.setObjectName("_roll_name_label")
        self._layout.addWidget(self._roll_name_label, 6, 1)

        self._roll_name_text = QtWidgets.QLineEdit()
        self._roll_name_text.setStyleSheet("border: 1px solid white; background-color:purple; color:white; font-family:\"Cascadia Code\"")
        self._roll_name_text.setObjectName("_roll_name_text")
        self._layout.addWidget(self._roll_name_text, 7, 1)
        

    def _initalize_buttons(self) -> None:
        self._exit_button = QtWidgets.QPushButton(text = "Exit")
        self._exit_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._exit_button.setObjectName("exit_button")
        self._exit_button.setFixedSize(85, 23)
        # self._exit_button.clicked.connect(sys.exit)  #may need own exit function here 
        self._layout.addWidget(self._exit_button, 8,0)

        self._save_button = QtWidgets.QPushButton(text = "Save")
        self._save_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(85, 23)
        # self._save_button.clicked.connect(self.show_save_menu)
        self._layout.addWidget(self._save_button, 8, 2)