from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

def pencere():
    app=QApplication(sys.argv)
    pencere=QWidget()
    form = QFormLayout()

    form.addRow(QLabel("Kullanıcı Adı: "),QLineEdit())
    sifre=QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("Şifre :"),sifre)
    form.addRow(QLabel("Adres :"),QTextEdit())

    h_box=QHBoxLayout()
    r1=QRadioButton("Erkek")
    r2=QRadioButton("Kadın")
    h_box.addWidget(r1)
    h_box.addWidget(r2)

    form.addRow(QLabel("Cinsiyet"),h_box)
    
    h_box2=QHBoxLayout()
    btn1=QPushButton("Gönder")
    btn2=QPushButton("İptal")
    h_box2.addWidget(btn1)
    h_box2.addWidget(btn2)

    form.addRow(h_box2)

    pencere.setLayout(form)
    pencere.setWindowTitle("Olgu Can")
    pencere.show()
    sys.exit(app.exec())

if __name__=="__main__":
    pencere()