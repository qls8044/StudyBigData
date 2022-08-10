# 가장 심플한 PyQt 실행방범

from PyQt5 import QtWidgets as qw

def run():
    app = qw.QApplication([]) # 애플리케이션 생성
    wnd = qw.QMainWindow() # 윈도우 창을 띄움
    label = qw.QLabel('Hello Qt!') # 윈도우에 띄울 글자 씀
    wnd.setCentralWidget(label) # 내가 만든 라벨을 정 중앙에 띄우겠다
    wnd.show() # 윈도우를 보여줘
    app.exec_() # 윈도우가 속한 애플리케이션을 실행

if __name__ == '__main__':
    run()