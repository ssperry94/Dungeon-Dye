from PyQt5.QtWidgets import QMessageBox

class ErrorBox():
    _box:QMessageBox = None
    _window_title:str = None
    _message:str = None 

    def __init__(self, window_title:str, message:str):
        self._box = QMessageBox()
        self._window_title = window_title
        self._message = message
        self._create_box()
    
    def _create_box(self) -> None:
        self._box.setIcon(QMessageBox.Critical)
        self._box.setWindowTitle(self._window_title)
        self._box.setText(self._message)

    def show(self):
        self._box.exec_()
