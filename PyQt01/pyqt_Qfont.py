import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: # 생성자는 기본적으로 리턴값이 없음. -> None 리턴할 게 없다
        super().__init__()
        self.initUi()
    
    # 화면 정의를 위해 만든 사용자 함수
    def initUi(self) -> None:
        self.setGeometry(300, 200, 500,500) # 앞에 두개 숫자는 x,y 좌표로 전체 창에서 차지하는 위치(저만큼 공백생김), 뒤에 두개는 창 자체의 넓이랑 높이임
        self.setWindowTitle('QTemplate!!')
        self.text = 'What a wonderful world~!'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 화면을 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('NanumGothic',20))
        paint.drawText(105,100, 'HELL WORLD~')

        paint.setPen(QColor(0,250,10)) # 이 구문으로 what~ 글자 색깔을 바꿈
        paint.setFont(QFont('Impact',10)) # 이 구문은 밑에 구문에 적용됨. what ~ 가 impact 글씨체로 10으로 나오게 함
        paint.drawText(event.rect(), Qt.AlignCenter, self.text) # 얘가 what a wonderful world 띄움(self.text를 불러왔으니까)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()