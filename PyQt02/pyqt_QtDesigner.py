import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./PyQt02/basic01.ui',self)
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.show()
    
    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결

    def btn1_clicked(self):
        QMessageBox.information(self,'signal','self.btn1_clicked!') # 첫번째 내용은 창 제목, 두번째 내용은 창 내용. 일반적인 정보 창
        self.label.setText('메시지 : btn1 버튼 클릭!!!!')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()