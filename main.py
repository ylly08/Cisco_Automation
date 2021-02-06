from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QDialog, QLineEdit, QMenuBar, QComboBox, QProgressBar, QAction
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from ciscoaxl import axl
import sys


'''
cucm = cucm
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
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi("mainwindow.ui",self)
        self.login = self.findChild(QPushButton, "login")
        self.login.clicked.connect(self._login)
        self.exit_in_menu = self.findChild(QAction, "action_exit")
        self.exit_in_menu.triggered.connect(self._exit)
        self.exit = self.findChild(QPushButton, "exit")
        self.exit.clicked.connect(self._exit)
        #self.menuBar

    def _login(self):
        dia = Dialog()

    def _exit(self):
        self.close()


class Dialog(QDialog,QTimer):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi("login.ui", self)
        self.connectbtn = self.findChild(QPushButton, "connect")
        self.cancelbtn = self.findChild(QPushButton, "quit")
        self.ip_addr = self.findChild(QLineEdit,"cucm_ip")
        self.user_name = self.findChild(QLineEdit,"username")
        self.password = self.findChild(QLineEdit,"pwd")
        self.CucmVersion = self.findChild(QComboBox, "cucm_version")
        self.connectbtn.clicked.connect(self.connect_cucm)
        self.cancelbtn.clicked.connect(self._cancel)
        #self.ip_addr.setText("IP Adresse")
        self.load = self.findChild(QProgressBar,"load")
        self.exec_()

    def connect_cucm(self, cucm):
        cucm = self.ip_addr.text()
        username = self.user_name.text()
        password = self.password.text()
        version = self.CucmVersion.currentText()
        timer = QTimer(self)
        timer.timeout.connect(self.loadTimer)
        timer.start(20)
        print(version)
        print (cucm)
        print(username)
        print(password)
        #self.close()

    def loadTimer(self):
        self.load.setValue(self.load.value() + 2)

    def _cancel(self):
        self.close()

    ##def ip(self):


#instanz = Dialog()
#instanz.connect_cucm()
#print (instanz.version)
#u = Dialog()
#print (u)

def main():
    app = QApplication(sys.argv)
    w = UI()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()




