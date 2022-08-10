import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: # 생성자는 기본적으로 리턴값이 없음. -> None 리턴할 게 없다
        super().__init__()
        self.initUi()
    
    # 화면 정의를 위해 만든 사용자 함수
    def initUi(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 500,500) 
        self.setWindowTitle('Qlabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./PyQt01/image/lion.png')) # 창 제목에 아이콘 이미지 넣기
        label1 = QLabel('Label1', self)
        label2 = QLabel('Label2', self)
        label1.setStyleSheet(
            'border-width: 3px;'
            'border-style: solid;' # 스타일은 실선
            'border-color: blue;' # 색깔은 파란색
            'image: url(./PyQt01/image/image1.png)'
        )
        label2.setStyleSheet(
            'border-width: 3px;'
            'border-style: dot-dot-dash;' 
            'border-color: red;' 
            'image: url(./PyQt01/image/image2.png)'
        )
        
        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()