from dungeondye.gui import roller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

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
    
    def setupUi(self):
        self.setObjectName("dice_panel")
        self.resize(915, 379)
        self.setStyleSheet("background-color:rgb(35, 40, 48)\n"
"")
        self._dice_number_label = QtWidgets.QLabel(self)
        self._dice_number_label.setGeometry(QtCore.QRect(40, 40, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_number_label.setFont(font)
        self._dice_number_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_number_label.setObjectName("_dice_number_label")
        self._dice_number_combo = QtWidgets.QComboBox(self)
        self._dice_number_combo.setGeometry(QtCore.QRect(40, 70, 131, 22))
        self._dice_number_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_number_combo.setEditable(False)
        self._dice_number_combo.setObjectName("_dice_number_combo")
        self._dice_side_label = QtWidgets.QLabel(self)
        self._dice_side_label.setGeometry(QtCore.QRect(40, 100, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._dice_side_label.setFont(font)
        self._dice_side_label.setStyleSheet("color:\"#FE2B26\"")
        self._dice_side_label.setObjectName("_dice_side_label")
        self._dice_side_combo = QtWidgets.QComboBox(self)
        self._dice_side_combo.setGeometry(QtCore.QRect(40, 130, 131, 22))
        self._dice_side_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._dice_side_combo.setObjectName("_dice_side_combo")
        self._modifier_label = QtWidgets.QLabel(self)
        self._modifier_label.setGeometry(QtCore.QRect(40, 160, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._modifier_label.setFont(font)
        self._modifier_label.setStyleSheet("color:\"#FE2B26\"")
        self._modifier_label.setObjectName("_modifier_label")
        self._modifiers_combo = QtWidgets.QComboBox(self)
        self._modifiers_combo.setGeometry(QtCore.QRect(40, 180, 131, 22))
        self._modifiers_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._modifiers_combo.setObjectName("_modifiers_combo")
        self.roll_button = QtWidgets.QPushButton(self)
        self.roll_button.setGeometry(QtCore.QRect(450, 220, 93, 28))
        self.roll_button.setStyleSheet("background-color:\"#FE2B26\"")
        self.roll_button.setText("")
        self.roll_button.setObjectName("roll_button")
        self._saved_roll_combo = QtWidgets.QComboBox(self)
        self._saved_roll_combo.setGeometry(QtCore.QRect(780, 140, 131, 22))
        self._saved_roll_combo.setStyleSheet("color:\"white\"; background-color:\"#6A0DAD\"; border: 1px solid black ")
        self._saved_roll_combo.setObjectName("_saved_roll_combo")
        self._saved_rolls_label = QtWidgets.QLabel(self)
        self._saved_rolls_label.setGeometry(QtCore.QRect(780, 110, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self._saved_rolls_label.setFont(font)
        self._saved_rolls_label.setStyleSheet("color:\"#FE2B26\"")
        self._saved_rolls_label.setObjectName("_saved_rolls_label")
        self._output_browser = QtWidgets.QTextBrowser(self)
        self._output_browser.setGeometry(QtCore.QRect(300, 260, 381, 131))
        self._output_browser.setStyleSheet("color:\"#6A0DAD\";border:1px solid white;")
        self._output_browser.setObjectName("_output_browser")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("dice_panel", "Form"))
        self._dice_number_label.setText(_translate("dice_panel", "Dice Number"))
        self._dice_side_label.setText(_translate("dice_panel", "Dice Side"))
        self._modifier_label.setText(_translate("dice_panel", "Modifiers "))
        self._saved_rolls_label.setText(_translate("dice_panel", "Saved Rolls"))

