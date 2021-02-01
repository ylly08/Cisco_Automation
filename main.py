import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic

app = widgets.QApplication(sys.argv)
w = uic.loadUi("hauptfenster.ui")

w.show()
sys.exit(app.exec_())
