from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QDialog

from PyQt5 import uic
from ciscoaxl import axl
import sys


cucm = '25.1.1.133'
username = 'ciscoaxl'
password = 'ciscoaxl'
version = '12.5'
ucm = axl(
    username=username,
    password=password,
    cucm=cucm,
    cucm_version=version
)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.PressButtonWrite)
        self.show()

    def PressButtonWrite(self):
          uic.loadUi("dialog.ui",self)





app = QApplication(sys.argv)
w = UI()
app.exec_()
