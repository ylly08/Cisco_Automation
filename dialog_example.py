import sys
from PyQt4 import uic, QtGui, QtCore

main_dialog = uic.loadUiType("GUI.ui")[0]
TestQDialog = uic.loadUiType("Dialog.ui")[0]

def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass()
    myWindow.show()
    app.exec_()

main_dialog = uic.loadUiType("GUI.ui")[0]

TestQDialog = uic.loadUiType("Dialog.ui")[0]

class QDialogClass(object, TestQDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

class MyWindowClass(QtGui.QMainWindow, main_dialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_close.clicked.connect(self.dialog)

    def dialog(self):
        dialog = Qdialog()
        dialog.ui = QDialogClass()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

if __name__ == "__main__":
    main()