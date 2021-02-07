from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QDialog, QLineEdit, QMenuBar, QComboBox, QProgressBar, QAction
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from time import *
from ciscoaxl import axl
import sys


'''
cucm = '10.10.10.10'
username = 'ciscoaxl'
password = 'ciscoaxl'
version = '12.5'
'''
ucm = axl(
    username=username,
    password=password,
    cucm=cucm,
    cucm_version=version
)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("mainwindow.ui",self)
        self.login.clicked.connect(self._login)
        self.menu_exit.triggered.connect(self._exit)
        self.exit.clicked.connect(self._exit)

    def _login(self):
        Login = Dialog()

    def _exit(self):
        self.close()


class Dialog(QDialog,QTimer):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        loadUi("login.ui", self)
        self.ip_addr = self.findChild(QLineEdit,"ip_line")
        self.user_name = self.findChild(QLineEdit,"user_line")
        self.password = self.findChild(QLineEdit,"pwd_line")
        self.cucm_version = self.findChild(QComboBox, "version_b")
        self.connect_b.clicked.connect(self._checkstatus)
        self.cancel_b.clicked.connect(self._cancel)
        self.ip_addr.setText("IP Adresse")
        self.load = self.findChild(QProgressBar,"load")
        self.exec_()

    def _checkstatus(self):
        if self.ip_addr.text() == "" or self.user_name.text() == "" or self.password.text() == "" \
                or self.cucm_version.currentText() == "":
            print("Es fehlt etwas")
            self.ip_addr.setFocus()
        else:
            self._connect()

    def _connect(self):
        cucm = self.ip_addr.text()
        username = self.user_name.text()
        password = self.password.text()
        cucm_version = self.cucm_version.currentText()
        timer = QTimer(self)
        timer.timeout.connect(self._loadTimer)
        timer.start(10)
        #TODO: If / else und Modul aufrufen mit AXL.
        #ucm =
        #ucm = axl('username=username,password=password,cucm=cucm,cucm_version=version')
        print(cucm_version)
        print (cucm)
        print(username)
        print(password)
        #self.close()

    def _loadTimer(self):
        self.load.setValue(self.load.value() + 2)

    def _cancel(self):
        self.close()



def main():
  app = QApplication(sys.argv)
  w = UI()
  w.show()
  app.exec_()

if __name__ == '__main__':
    main()
