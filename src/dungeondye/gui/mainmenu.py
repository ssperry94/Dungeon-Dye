from PyQt5 import QtCore, QtWidgets

class MainMenu(object):
    def setupUi(self, main_window):
        #main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(1116, 807)
        main_window.setAccessibleName("")
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("""background-color:rgb(35, 40, 48)\n""")
        main_window.setIconSize(QtCore.QSize(30, 30))
        main_window.setAnimated(True)
        main_window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.show()
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Dungeon Dice"))
        main_window.setToolTip(_translate("main_window", "<html><head/><body><p><br/></p></body></html>"))
