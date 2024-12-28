from PyQt5 import QtCore, QtGui, QtWidgets
from dungeondye.dice import roller
from dungeondye.gui import valueerror

class DiceFrame(QtWidgets.QWidget):
    _dice_number_label:QtWidgets.QLabel = None 
    _dice_number_combo:QtWidgets.QComboBox = None 
    _dice_side_label:QtWidgets.QLabel = None 
    _dice_side_combo:QtWidgets.QComboBox = None 
    _modifier_label:QtWidgets.QLabel = None
    _modifiers_combo:QtWidgets.QComboBox = None 
    _saved_rolls_label:QtWidgets.QLabel = None 
    _saved_rolls_combo:QtWidgets.QComboBox = None 
    roll_button:QtWidgets.QPushButton = None 
    _output_browser:QtWidgets.QTextBrowser = None 
    _dice_layout:QtWidgets.QGridLayout = None
    
    def setupUi(self) -> None:
        self.setObjectName("dice_panel")
        #self.resize(915, 379)
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self._dice_layout = QtWidgets.QGridLayout(self)
        self._initalize_widgets()
        self._initalize_buttons()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _initalize_widgets(self) -> None:
        self._dice_number_label = QtWidgets.QLabel()
        # self._dice_number_label.setGeometry(QtCore.QRect(40, 40, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_number_label.setFont(font)
        self._dice_number_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_number_label.setObjectName("_dice_number_label")
        self._dice_layout.addWidget(self._dice_number_label, 0, 0)

        self._dice_number_combo = QtWidgets.QComboBox()
        self._dice_number_combo.setEditable(True)
        #self._dice_number_combo.setGeometry(QtCore.QRect(40, 70, 131, 22))
        self._dice_number_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_number_combo.setObjectName("_dice_number_combo")
        self._dice_layout.addWidget(self._dice_number_combo, 1, 0)

        self._dice_side_label = QtWidgets.QLabel()
        # self._dice_side_label.setGeometry(QtCore.QRect(40, 100, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_side_label.setFont(font)
        self._dice_side_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_side_label.setObjectName("_dice_side_label")
        self._dice_layout.addWidget(self._dice_side_label, 2, 0)

        self._dice_side_combo = QtWidgets.QComboBox()
        self._dice_side_combo.setEditable(True)
        # self._dice_side_combo.setGeometry(QtCore.QRect(40, 130, 131, 22))
        self._dice_side_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_side_combo.setObjectName("_dice_side_combo")
        self._dice_layout.addWidget(self._dice_side_combo, 3, 0)

        self._modifier_label = QtWidgets.QLabel()
        # self._modifier_label.setGeometry(QtCore.QRect(40, 160, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._modifier_label.setFont(font)
        self._modifier_label.setStyleSheet("color:\"#FE2B26\"")
        self._modifier_label.setObjectName("_modifier_label")
        self._dice_layout.addWidget(self._modifier_label, 4, 0)

        self._modifiers_combo = QtWidgets.QComboBox()
        self._modifiers_combo.setEditable(True)
        # self._modifiers_combo.setGeometry(QtCore.QRect(40, 180, 131, 22))
        self._modifiers_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._modifiers_combo.setObjectName("_modifiers_combo")
        self._dice_layout.addWidget(self._modifiers_combo, 5, 0)

        self._saved_rolls_label = QtWidgets.QLabel()
        # self._saved_rolls_label.setGeometry(QtCore.QRect(780, 110, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._saved_rolls_label.setFont(font)
        self._saved_rolls_label.setStyleSheet("color:\"#FE2B26\"")
        self._saved_rolls_label.setObjectName("_saved_rolls_label")
        self._dice_layout.addWidget(self._saved_rolls_label, 2, 2)

        self._saved_roll_combo = QtWidgets.QComboBox()
        self._saved_roll_combo.setEditable(True)
        # self._saved_roll_combo.setGeometry(QtCore.QRect(780, 140, 131, 22))
        self._saved_roll_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._saved_roll_combo.setObjectName("_saved_roll_combo")
        self._dice_layout.addWidget(self._saved_roll_combo, 3, 2)

        self._populate_combos()

        self._output_browser = QtWidgets.QTextBrowser()
        # self._output_browser.setGeometry(QtCore.QRect(300, 260, 381, 75))
        self._output_browser.setStyleSheet("color:white;border:1px solid black;font-family:\"Copperplate Gothic Bold\"")
        self._output_browser.setObjectName("_output_browser")
        self._dice_layout.addWidget(self._output_browser, 7,0,1,3)

    def _initalize_buttons(self) -> None:
        icon = QtGui.QIcon(r'C:\Users\ssper\OneDrive\Projects\Table-Top-Dice-Roller\src\resources\images\roll_button_image.png')

        self.roll_button = QtWidgets.QPushButton()
        # self.roll_button.setGeometry(QtCore.QRect(450, 220, 93, 28))
        self.roll_button.setStyleSheet("background-color:\"#FE2B26\"")
        #self.roll_button.setText("")
        self.roll_button.setObjectName("roll_button")
        self.roll_button.setFixedSize(100,45)
        self.roll_button.setIcon(icon)
        self.roll_button.setIconSize(QtCore.QSize(45,45))
        self._dice_layout.addWidget(self.roll_button, 6,1)
        self.roll_button.clicked.connect(self.roll)
    
    def retranslateUi(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dice_panel", "Form"))
        self._dice_number_label.setText(_translate("dice_panel", "Dice Number"))
        self._dice_side_label.setText(_translate("dice_panel", "Dice Side"))
        self._modifier_label.setText(_translate("dice_panel", "Modifiers "))
        self._saved_rolls_label.setText(_translate("dice_panel", "Saved Rolls"))

    def _populate_combos(self) -> None:
        dice_num_list = [str(num) for num in range(1,101)] #number of dye possible
        dice_side_list = ['4','6','8','10','12','20','100'] #standard dice sides 
        modifiers_list = [str(num) for num in range(0,101)] #number you can modify

        self._dice_number_combo.addItems(dice_num_list)
        self._dice_number_combo.setCurrentIndex(-1)
        self._dice_side_combo.addItems(dice_side_list)
        self._dice_side_combo.setCurrentIndex(-1)
        self._modifiers_combo.addItems(modifiers_list)

    def roll(self) -> None:
        dice = roller.Dice()
        dice.rolldice(self._output_browser, self._dice_number_combo, self._dice_side_combo, self._modifiers_combo)

    #currently:create value_error message box as its own class 
    #get this into bottom frame
    def get_current_combo_values(self) -> tuple:
        try:
            combo_values = (int(self._dice_number_combo.currentText()), int(self._dice_side_combo.currentText()), int(self._modifiers_combo.currentText()))
            return combo_values
        except ValueError:
            #throw value error window
            val_error = valueerror.ErrorBox("Incomplete Information", "Error! Please ensure that the number of dice and the type of dye is entered correctly.")
            val_error.show()