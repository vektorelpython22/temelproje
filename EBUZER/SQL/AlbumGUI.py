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
        self.cmbArtist.currentIndexChanged.connect(self.degisti)
        self.Artistliste = []
        self.listeGetir()
        self.show()


    def click(self):
        if len(self.txtArtist.text()) > 0:
            liste = ["'"+self.txtTitle.text()+"'",self.txtArtist.text()]
            elcevap =  QMessageBox.question(self,"Soru","Emin misin?",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if elcevap == QMessageBox.Yes:
                if self.db.albumEkle(liste):
                    QMessageBox.information(self,"Bilgi","Bilgileriniz Kaydedilmiştir.",QMessageBox.Ok)
                else:
                    QMessageBox.warning(self,"Hata","Kaydedemedik",QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"Uyarı","Kaydedemedik",QMessageBox.Ok)
    def listeGetir(self):
        self.Artistliste = self.db.artistGetir()
        for indis,isim in self.Artistliste:
            self.cmbArtist.addItem(isim)
        

    def degisti(self):
        for indis,isim in self.Artistliste:
            if self.cmbArtist.currentText() == isim:
                self.txtArtist.setText(str(indis))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        