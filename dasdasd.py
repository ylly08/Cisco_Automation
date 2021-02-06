from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from ciscoaxl import axl
import sys


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setWindowModality(QtCore.Qt.NonModal)
        mainwindow.setEnabled(True)
        mainwindow.resize(786, 366)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainwindow.sizePolicy().hasHeightForWidth())
        mainwindow.setSizePolicy(sizePolicy)
        mainwindow.setMouseTracking(False)
        mainwindow.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"alternate-background-color: rgb(255, 255, 0);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        mainwindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushbutton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_connect.setEnabled(True)
        self.pushbutton_connect.setGeometry(QtCore.QRect(200, 70, 161, 21))
        self.pushbutton_connect.setStyleSheet("color: rgb(248, 248, 248);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushbutton_connect.setDefault(False)
        self.pushbutton_connect.setObjectName("pushbutton_connect")
        self.cucm_connect = QtWidgets.QLineEdit(self.centralwidget)
        self.cucm_connect.setGeometry(QtCore.QRect(10, 70, 191, 21))
        self.cucm_connect.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cucm_connect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cucm_connect.setObjectName("cucm_connect")
        self.labelhostname = QtWidgets.QLabel(self.centralwidget)
        self.labelhostname.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.labelhostname.setObjectName("labelhostname")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.progressBar.setProperty("value", 11)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        mainwindow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(mainwindow)
        self.action_exit.setObjectName("action_exit")
        self.action_datei = QtWidgets.QAction(mainwindow)
        self.action_datei.setCheckable(False)
        self.action_datei.setChecked(False)
        self.action_datei.setEnabled(True)
        self.action_datei.setObjectName("action_datei")
        self.action_help = QtWidgets.QAction(mainwindow)
        self.action_help.setObjectName("action_help")
        self.menuHelp.addAction(self.action_help)
        self.menuDatei.addAction(self.action_datei)
        self.menuDatei.addAction(self.action_exit)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainwindow)
        self.pushbutton_connect.clicked.connect(mainwindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Automation Tool for CUCM by NTT"))
        mainwindow.setToolTip(_translate("mainwindow", "<html><head/><body><p>Automation Tool by NTT</p></body></html>"))
        self.pushbutton_connect.setToolTip(_translate("mainwindow", "<html><head/><body><p>Connect!</p></body></html>"))
        self.pushbutton_connect.setText(_translate("mainwindow", "Connect to CUCM"))
        self.cucm_connect.setToolTip(_translate("mainwindow", "<html><head/><body><p>IP or Hostname</p></body></html>"))
        self.labelhostname.setText(_translate("mainwindow", "Hostname / IP"))
        self.pushButton.setText(_translate("mainwindow", "PushButton"))
        self.menuHelp.setTitle(_translate("mainwindow", "Help"))
        self.menuDatei.setTitle(_translate("mainwindow", "Datei"))
        self.action_exit.setText(_translate("mainwindow", "Exit"))
        self.action_datei.setText(_translate("mainwindow", "Open File"))
        self.action_help.setText(_translate("mainwindow", "About"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UI()
    w.show()
    app.exec_()
