import sys
from  PyQt5.QtWidgets import QApplication,QWidget
from  PyQt5.QtGui import QIcon
from PyQt5 import uic 


class KullaniciKayit(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"IBRAHIM\Pyqt5\UI\KullaniciKayit.ui",self)
        self.initUI()

    def initUI(self):
        self.btIptal.clicked.connect(self.click)
        self.btKaydet.clicked.connect(self.kayit)
    def click(self):
        self.close()
    
    def kayit(self):
        self.txtsoyadi.setText(self.txtadi.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = KullaniciKayit()
    ex.show()
    sys.exit(app.exec_())
        