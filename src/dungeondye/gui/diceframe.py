from PyQt5 import QtCore, QtGui, QtWidgets
from dungeondye.dice import roller, savedroll
from dungeondye.utils import constants, utilities

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
        self.setStyleSheet(f"background-color:{constants.APP_BACKGROUND_COLOR}\n"
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
        self._dice_number_label.setStyleSheet(f"color:\"{constants.LABEL_TEXT_COLOR}\"")
        self._dice_number_label.setObjectName("_dice_number_label")
        self._dice_layout.addWidget(self._dice_number_label, 0, 0)

        self._dice_number_combo = QtWidgets.QComboBox()
        self._dice_number_combo.setEditable(True)
        #self._dice_number_combo.setGeometry(QtCore.QRect(40, 70, 131, 22))
        self._dice_number_combo.setStyleSheet(f"color:\"white\"; background-color:\"{constants.COMBO_COLOR}\"; border: 1px solid black ")
        self._dice_number_combo.setObjectName("_dice_number_combo")
        self._dice_layout.addWidget(self._dice_number_combo, 1, 0)

        self._dice_side_label = QtWidgets.QLabel()
        # self._dice_side_label.setGeometry(QtCore.QRect(40, 100, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_side_label.setFont(font)
        self._dice_side_label.setStyleSheet(f"color:\"{constants.LABEL_TEXT_COLOR}\"")
        self._dice_side_label.setObjectName("_dice_side_label")
        self._dice_layout.addWidget(self._dice_side_label, 2, 0)

        self._dice_side_combo = QtWidgets.QComboBox()
        self._dice_side_combo.setEditable(True)
        # self._dice_side_combo.setGeometry(QtCore.QRect(40, 130, 131, 22))
        self._dice_side_combo.setStyleSheet(f"color:\"white\"; background-color:\"{constants.COMBO_COLOR}\"; border: 1px solid black ")
        self._dice_side_combo.setObjectName("_dice_side_combo")
        self._dice_layout.addWidget(self._dice_side_combo, 3, 0)

        self._modifier_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._modifier_label.setFont(font)
        self._modifier_label.setStyleSheet(f"color:\"{constants.LABEL_TEXT_COLOR}\"")
        self._modifier_label.setObjectName("_modifier_label")
        self._dice_layout.addWidget(self._modifier_label, 4, 0)

        self._modifiers_combo = QtWidgets.QComboBox()
        self._modifiers_combo.setEditable(True)
        self._modifiers_combo.setStyleSheet(f"color:\"white\"; background-color:\"{constants.COMBO_COLOR}\"; border: 1px solid black ")
        self._modifiers_combo.setObjectName("_modifiers_combo")
        self._dice_layout.addWidget(self._modifiers_combo, 5, 0)

        self._saved_rolls_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._saved_rolls_label.setFont(font)
        self._saved_rolls_label.setStyleSheet(f"color:\"{constants.LABEL_TEXT_COLOR}\"")
        self._saved_rolls_label.setObjectName("_saved_rolls_label")
        self._dice_layout.addWidget(self._saved_rolls_label, 2, 2)

        self._saved_roll_combo = QtWidgets.QComboBox()
        self._saved_roll_combo.setEditable(True)
        # self._saved_roll_combo.setGeometry(QtCore.QRect(780, 140, 131, 22))
        self._saved_roll_combo.setStyleSheet(f"color:\"white\"; background-color:\"{constants.COMBO_COLOR}\"; border: 1px solid black ")
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
        self.roll_button.setStyleSheet(f"background-color:\"{constants.BUTTON_COLOR}\"")
        self.roll_button.setObjectName("roll_button")
        self.roll_button.setFixedSize(constants.ROLL_BUTTON_HEIGHT, constants.ROLL_BUTTON_WIDTH)
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
        self._dice_number_combo.addItems(constants.DICE_NUM_LIST)
        self._dice_number_combo.setCurrentIndex(-1)
        self._dice_side_combo.addItems(constants.DICE_SIDE_LIST)
        self._dice_side_combo.setCurrentIndex(-1)
        self._modifiers_combo.addItems(constants.MODIFIER_LIST)
        self.update_saved_rolls()

        self._saved_roll_combo.activated.connect(self._show_saved_roll)

    def update_saved_rolls(self) -> None:
            self._saved_roll_combo.clear()
            self._saved_roll_combo.addItem('')
            for roll in constants.SAVED_ROLLS_LIST:
                self._saved_roll_combo.addItem(roll.roll_name)
                
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
            return None
    
    def _show_saved_roll(self) -> None:
        #get info from whatever current combobox is at
        roll_name = self._saved_roll_combo.currentText()
        if roll_name == '':
            self._dice_number_combo.setCurrentIndex(-1)
            self._dice_side_combo.setCurrentIndex(-1)
            self._modifiers_combo.setCurrentIndex(0)
            return 
        
        saved_roll:savedroll.SavedRoll = utilities.search_saved_rolls(roll_name)

        #if wrong name is entered, ensure that it doesn't get saved to combo box
        if saved_roll is None:
            items = [self._saved_roll_combo.itemText(i) for i in range(self._saved_roll_combo.count())]
            for i, roll in enumerate(items):
                if roll == roll_name:
                    self._saved_roll_combo.removeItem(i)

            return
        
        #set other comboboxes 
        self._dice_number_combo.setCurrentText(str(saved_roll.dice_num))
        self._dice_side_combo.setCurrentText(str(saved_roll.dice_side))
        self._modifiers_combo.setCurrentText(str(saved_roll.modifier))