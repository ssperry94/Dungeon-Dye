from PyQt5 import QtCore, QtWidgets
from dungeondye.utils import constants, utilities
from dungeondye.gui import messagebox, diceframe

#all tab widgets defined before SettingMenu 
class _DiceSettings(QtWidgets.QWidget):
    _dice_frame:diceframe.DiceFrame = None
    _layout:QtWidgets.QGridLayout = None
    _widget_list:list = [] #contains all buttons and roll names
    _roll_container:QtWidgets.QGroupBox = None #a scrollable box that contains all rolls and check button 
    _clear_button:QtWidgets.QPushButton = None #button that clears all saved rolls 
    _delete_button:QtWidgets.QPushButton = None #button that deletes all selected rolls

    def setupUi(self, dice_frame:diceframe.DiceFrame):
        self.setObjectName("dice_settings")
        self.setStyleSheet(f"background-color:{constants.APP_BACKGROUND_COLOR}\n"
"")
        self._layout = QtWidgets.QGridLayout(self)
        self._dice_frame = dice_frame
        self._initalize_roll_container()
        self._initalize_buttons()

    def _populate_roll_container(self, layout:QtWidgets.QVBoxLayout):
        if self._widget_list is not None:
            self._widget_list.clear()

        for roll in constants.SAVED_ROLLS_LIST:
            roll_btn = QtWidgets.QCheckBox(roll.roll_name)
            self._widget_list.append(roll_btn)
            layout.addWidget(roll_btn)

    def _initalize_roll_container(self):
        self._roll_container = QtWidgets.QGroupBox()
        roll_layout = QtWidgets.QVBoxLayout(self._roll_container)

        self._populate_roll_container(roll_layout)
        self._layout.addWidget(self._roll_container, 0,1)


    def _initalize_buttons(self):
        self._clear_button = QtWidgets.QPushButton(text = "Clear")
        self._clear_button.setObjectName("clear_button")
        self._clear_button.setFixedSize(85,23)
        self._clear_button.clicked.connect(self.clear_rolls)
        self._layout.addWidget(self._clear_button, 1,0)

        self._delete_button = QtWidgets.QPushButton(text = "Delete")
        self._delete_button.setObjectName("delete_button")
        self._delete_button.setFixedSize(85,23)
        self._delete_button.clicked.connect(self.delete_rolls) #change to a method that brings a confirmation screen
        self._layout.addWidget(self._delete_button, 1,2)

    def clear_rolls(self):
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setWindowTitle("Confirm Deletion")
        confirm.setText("WARNING! This action will permanently delete all saved rolls. Are you sure you wish to proceed?")
        confirm.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        confirm.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirm.exec_()
        self._confirm_clear_rolls(result)
    
    def _confirm_clear_rolls(self, result): #get confirmation and attempt to delete all rolls
        if result == QtWidgets.QMessageBox.Yes:
            if utilities.clear_saved_rolls() == True:
                self._initalize_roll_container() #reset saved rolls in settings menu 
                self._dice_frame.update_saved_rolls() #update dice frame
                success = messagebox.MessageBox("Success", "All saved rolls deleted.", information = True)
                success.show()
            else:
                fail = messagebox.MessageBox("Error", "Error encountered, saved rolls could not be deleted.", error = True)
                fail.show()
        else:
            message = messagebox.MessageBox("No Rolls Deleted", "No rolls were deleted.", information = True)
            message.show()

    def delete_rolls(self):
        deleted_rolls = [roll.text() for roll in self._widget_list if roll.isChecked()]
        deleted_rolls_output = "\n".join(deleted_rolls)
        confirm = QtWidgets.QMessageBox()
        confirm.setIcon(QtWidgets.QMessageBox.Warning)
        confirm.setWindowTitle("Confirm Deletion")
        confirm.setText(f"WARNING! This action will delete the following rolls:\n{deleted_rolls_output}\nAre you sure you wish to proceed?")
        confirm.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        confirm.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirm.exec_()
        self._confirm_delete_rolls(deleted_rolls, result)

    def _confirm_delete_rolls(self, deleted_rolls:list, result) -> bool:
        if result == QtWidgets.QMessageBox.Yes:
            for roll in deleted_rolls:
                roll_index = utilities.find_roll_index(roll)
                if roll_index >= 0:
                    if utilities.remove_roll(roll_index) == False:
                        return False
                else:
                    return False 
            self._initalize_roll_container() #reset saved rolls in settings menu 
            self._dice_frame.update_saved_rolls() #update dice frame
            return True    
        else:
            message = messagebox.MessageBox("No Rolls Deleted", "No rolls were deleted.", information = True)
            message.show()



class SettingsMenu(QtWidgets.QDialog):
    _dice_frame:diceframe.DiceFrame = None 
    _tab_widget:QtWidgets.QTabWidget = None
    _dice_tab:QtWidgets.QWidget = None 
    _layout:QtWidgets.QVBoxLayout = None
    #add more tabs here as needed 
    _close_bttn:QtWidgets.QPushButton = None

    def setupUi(self, dice_frame:diceframe.DiceFrame) -> None:
        self.setObjectName("settings_menu")
        self.setWindowTitle("Settings")
        self.setStyleSheet(f"background-color:{constants.APP_BACKGROUND_COLOR}\n"
"")
        self._tab_widget = QtWidgets.QTabWidget()
        self._layout = QtWidgets.QGridLayout(self)
        self._dice_frame = dice_frame
        self._initalize_tabs(dice_frame)
        self._initalize_buttons()
        self._layout.addWidget(self._tab_widget, 0, 0)
        self._layout.addWidget(self._close_bttn, 1,0, alignment=QtCore.Qt.AlignHCenter)

    # def show(self) -> None:        
    #     self.exec_()

    def _initalize_tabs(self, dice_frame) -> None:
        self._dice_tab = _DiceSettings()
        self._dice_tab.setupUi(dice_frame)
        self._tab_widget.addTab(self._dice_tab, "Roll Manager")

    def _initalize_buttons(self) -> None:
        self._close_bttn = QtWidgets.QPushButton(text = "Close")
        self._close_bttn.setObjectName("close_button")
        self._close_bttn.setFixedSize(85,23)
        self._close_bttn.clicked.connect(self.reject)

    #overwrite of close event to ensure dice settings is properly cleaned up 
    def closeEvent(self, a0):
        self._dice_tab = None
        self._dice_frame = None 
        self.deleteLater()
        super().closeEvent(a0)