import sys
from  PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from  PyQt5.QtGui import QIcon
from PyQt5 import uic 
from AlbumDB import AlbumDB

class App(QWidget):
    def __init__(self):
        super().__init__()   
        self.db = AlbumDB()
        uic.loadUi(r"IBRAHIM\SQL\arayuz.ui",self)
        self.btKayit.clicked.connect(self.click)
        self.show()


    def click(self):
        liste = ["'"+self.txtTitle.text()+"'",self.txtArtist.text()]
        if self.db.albumEkle(liste):
            QMessageBox.information(self,"Bilgi","Bilgileriniz Kaydedilmiştir.",QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"Hata","Kaydedemedik",QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        