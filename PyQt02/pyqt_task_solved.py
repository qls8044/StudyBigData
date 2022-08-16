import sys
from time import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI 스레드와 작업스레드 분리
class Worker(QThread):
    # QThread는 화면을 그릴 권한이 없음. 
    # 대신 통신을 통해서 UI Thread가 그림을 그릴 수 있도록 통신 수행
    valChangeSignal = pyqtSignal(int) 
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True # working이라는 클래스 내부변수 만들고 지정하기

    def run(self):
        while self.working:
            for i in range(0,1000000):
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i) # UI Thread가 화면을 그릴 수 있게함
                time.sleep(0.0001) # 1 micro sec 타임 슬립함


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
        # Worker 클래스 생성
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress) # Thtread 에서 받은 시그널은 updateProgress에서 처리

    @pyqtSlot(int)
    def updateProgress(self, val): # val이 Worker Thread에서 전달받은 반복값
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 999999:
            self.worker.working = False

    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0,999999)
        self.worker.start()
        self.worker.working = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()