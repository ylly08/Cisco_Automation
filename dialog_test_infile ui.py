from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QDialog, QLineEdit
from PyQt5 import uic
from ciscoaxl import axl
import sys

'''
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
'''
#hauptfenster = uic.loadUi("mainwindow.ui")
#testdialog = uic.loadUi("dialog.ui")

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi("mainwindow.ui",self)
        self.button = self.findChild(QPushButton, "login")
        self.button.clicked.connect(self.PressButtonWrite)
        self.show()
    def PressButtonWrite(self):
        dia = Dialog()


class Dialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi("login.ui", self)
        self.button = self.findChild(QPushButton, "test")
        self.button1 = self.findChild(QLineEdit,"cucm_ip")
        ##QLineEdit.setText("abcd")
        #self.button1.setText("Abcd")
        #print(self.button1.text())
        self.button.clicked.connect(self.login)
        self.exec_()
        print(self.button1.text())

    def login(self):
        self.close()
        print('closed')

    ##def ip(self):




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UI()
    w.show()
    app.exec_()




