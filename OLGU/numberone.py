from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from olgusql import addatabase
from olgusql import addatabes2
import sqlite3
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):
        self.cb=QComboBox()
        self.gb=QComboBox()
        self.cb.addItems(addatabase())
        self.gb.addItems(addatabes2())  
        self.chbox=QCheckBox("Kabul Ediyorum")
        self.button=QPushButton("Gönder")

        h_box=QHBoxLayout()
        h_box.addWidget(self.cb)
        h_box.addWidget(self.gb)
        h_box.addWidget(self.chbox)
        h_box.addWidget(self.button)

        self.setLayout(h_box)
        self.setWindowTitle("QComboBox")
        self.show()

    




if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())