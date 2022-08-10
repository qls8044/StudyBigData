import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: # 생성자는 기본적으로 리턴값이 없음. -> None 리턴할 게 없다
        super().__init__()
        self.initUi()
    
    def initUi(self) -> None:
        self.setGeometry(300, 200, 500,200) # 앞에 두개 숫자는 x,y 좌표로 전체 창에서 차지하는 위치(저만큼 공백생김), 뒤에 두개는 창 자체의 넓이랑 높이임
        self.setWindowTitle('QTemplate!!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()