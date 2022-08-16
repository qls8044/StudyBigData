import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./PyQt02/navernews.ui',self)
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.show()
    
    def addControls(self) -> None:
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()