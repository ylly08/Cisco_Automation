import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic


app = widgets.QApplication(sys.argv)
w = uic.loadUi("mainwindow.ui")
d = uic.loadUi("dialog.ui")

def login():
    d.exec_()

widgets.QPushButton.findChild()


w.show()
sys.exit(app.exec_())