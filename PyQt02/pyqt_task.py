import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./PyQt02/ttask.ui',self)
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.show()
    
    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn1_clicked) # 시그널 연결

    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0,999999)
        for i in range(0,1000000): # 출력해야할 양이 너무 많아서 응답없음 뜸
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()