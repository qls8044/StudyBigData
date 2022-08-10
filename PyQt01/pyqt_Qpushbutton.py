import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400) 
        self.setWindowTitle('Q Push Button!!')
        self.show()

    def addControls(self) -> None:
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(510,350,120,40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()