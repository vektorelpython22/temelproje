import sys
from  PyQt5.QtWidgets import QApplication,QWidget
from  PyQt5.QtGui import QIcon
from PyQt5 import uic 


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"IBRAHIM\Pyqt5\UI\arayuz.ui")
        self.win.button.clicked.connect(self.click)
        self.win.show()

    def click(self):
        print("Pyqt5")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        