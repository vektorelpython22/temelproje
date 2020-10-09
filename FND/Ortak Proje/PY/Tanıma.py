import sys
from  PyQt5.QtWidgets import QApplication,QWidget

from PyQt5 import uic 


class App(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"FND\Ortak Proje\UI\YüzTanıma.ui",self)
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        