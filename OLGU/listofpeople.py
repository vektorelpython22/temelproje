import sys
from  PyQt5.QtWidgets import QApplication,QMainWindow
from  PyQt5.QtGui import QIcon
from PyQt5 import uic 
from KullaniciKayit import KullaniciKayit

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"UI\Listofpeople.ui")
        self.win.usKayit.triggered.connect(self.clkusKayit)
        self.win.show()

    def clkusKayit(self):
        self.userKayit = KullaniciKayit()
        self.userKayit.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        