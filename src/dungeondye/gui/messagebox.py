from PyQt5.QtWidgets import QMessageBox

#custom message box class that keeps all message types in a consistant format, design, and style 
class MessageBox():
    _box:QMessageBox = None
    _window_title:str = None
    _message:str = None 
    _icon = None 

    def __init__(self, window_title:str, message:str, error:bool = False, warning:bool = False, information:bool = False):
        self._box = QMessageBox()
        self._window_title = window_title
        self._message = message
        self._icon = self._set_icon(error, warning, information)
        self._create_box()
    
    def _set_icon(self, error, warning, information):
        if error is True:
            return QMessageBox.Critical 
        elif warning is True:
            return QMessageBox.Warning 
        elif information is True:
            return QMessageBox.Information
        else:
            raise ValueError
        
    def _create_box(self) -> None:
        self._box.setIcon(self._icon)
        self._box.setWindowTitle(self._window_title)
        self._box.setText(self._message)

    @property
    def get_box(self):
        return self._box
    
    def show(self):
       return self._box.exec_()

class ConfirmationBox(MessageBox):
    def __init__(self, window_title, message, error = False, warning = True, information = False):
        super().__init__(window_title, message, error, warning, information)
    
    #overwrite of _create_box to get standard buttons 
    def _create_box(self):
        super()._create_box()
        self._box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self._box.setDefaultButton(QMessageBox.StandardButton.Yes)
