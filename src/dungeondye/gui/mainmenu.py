from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

class MainMenu(QtWidgets.QMainWindow):
    #load in .ui file from QtDesigner
    #add all other classes into this container
    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi(r'C:\Users\ssper\OneDrive\Projects\Table-Top-Dice-Roller\src\resources\qt\ui\mainwindow.ui', self)
        self.show()
