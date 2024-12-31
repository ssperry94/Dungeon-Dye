from PyQt5 import QtWidgets, QtGui
from dungeondye.utils import constants, utilities
from dungeondye.gui import valueerror

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

    def setupUi(self, rolls:tuple) -> None:
        self.setObjectName("save_panel")
        self.setWindowTitle("Roll Saver")
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._layout = QtWidgets.QGridLayout(self)
        self._initalize_widgets(rolls)
        self._initalize_buttons()
        

    def show(self) -> None:
        self.exec_()
    
    def _initalize_widgets(self, rolls) -> None:
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
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_side_label.setFont(font)
        self._dice_side_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_side_label.setObjectName("_dice_side_label")
        self._layout.addWidget(self._dice_side_label, 2, 1)

        self._dice_side_combo = QtWidgets.QComboBox()
        self._dice_side_combo.setEditable(True)
        self._dice_side_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_side_combo.setObjectName("_dice_side_combo")
        self._layout.addWidget(self._dice_side_combo, 3, 1)

        self._modifier_label = QtWidgets.QLabel("Modifier")
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._modifier_label.setFont(font)
        self._modifier_label.setStyleSheet("color:\"#FE2B26\"")
        self._modifier_label.setObjectName("_modifier_label")
        self._layout.addWidget(self._modifier_label, 4, 1)

        self._modifiers_combo = QtWidgets.QComboBox()
        self._modifiers_combo.setEditable(True)
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
        
        self._set_combos(rolls)

    def _initalize_buttons(self) -> None:
        self._exit_button = QtWidgets.QPushButton(text = "Exit")
        self._exit_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._exit_button.setObjectName("exit_button")
        self._exit_button.setFixedSize(85, 23)
        self._exit_button.clicked.connect(self.reject)
        self._layout.addWidget(self._exit_button, 8,0)

        self._save_button = QtWidgets.QPushButton(text = "Confirm")
        self._save_button.setStyleSheet("background-color:\"#FE2B26\";color:black;font-family:\"Copperplate Gothic Bold\"")
        self._save_button.setObjectName("save_button")
        self._save_button.setFixedSize(85, 23)
        self._save_button.clicked.connect(self._save)
        self._layout.addWidget(self._save_button, 8, 2)

    def _set_combos(self, rolls:tuple) -> None:
        self._dice_number_combo.addItems(constants.DICE_NUM_LIST)
        self._dice_number_combo.setCurrentText(str(rolls[0]))
        self._dice_side_combo.addItems(constants.DICE_SIDE_LIST)
        self._dice_side_combo.setCurrentText(str(rolls[1]))
        self._modifiers_combo.addItems(constants.MODIFIER_LIST)
        self._modifiers_combo.setCurrentText(str(rolls[2]))

    def _save(self) -> None:
        #get current combo values (including name)
        try:
            rolls = (int(self._dice_number_combo.currentText()), int(self._dice_side_combo.currentText()), int(self._modifiers_combo.currentText()))
            roll_name = self._roll_name_text.text()
            if roll_name == '':
                raise ValueError
            if utilities.add_new_roll(rolls, roll_name) == True:
                success = QtWidgets.QMessageBox()
                success.setIcon(QtWidgets.QMessageBox.Information)
                success.setWindowTitle("Success")
                success.setText("Roll successfully saved!")
                success.exec_()

            else:
                error = valueerror.ErrorBox("Roll Save Fail", "Could not save roll")
                error.show()
            
            self.reject()
        except ValueError:
            val_error = valueerror.ErrorBox("Incomplete Information", "Error! Please ensure that the number of dice and the type of dye is entered correctly.")
            val_error.show()
        #confirm name is correct
        #append to saved roll's list 
        #write that list to json
        