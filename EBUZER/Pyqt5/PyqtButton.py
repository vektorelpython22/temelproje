import sys
from  PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from  PyQt5.QtGui import QIcon
from  PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Şablon"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        #button 
        button = QPushButton("İlk Düğme",self)
        button.setToolTip("Bu bir örnek düğme")
        button.move(100,70)
        button.clicked.connect(self.on_click)
        

        self.show()


    @pyqtSlot()
    def on_click(self):
        print("PyQt5")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        