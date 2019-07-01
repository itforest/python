#1. 먼저 아나콘다가 설치되어 있지 않다면 아나콘다를 설치합니다.
#2. 아나콘다 콘솔 창에서 python -m pip install --upgrade pip으로 pip을 업그레이드 해줍니다.
#3. pip install pyqt5로 pyqt5를 설치해줍니다.

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.setText('emo')
        btn1.move(20,20)
        btn1.clicked.connect(self.emo_click)

        btn2 = QPushButton('&Button2', self)
        btn2.setCheckable(True)
        btn2.setText('miz')
        btn2.move(20,60)
        btn2.clicked.connect(self.miz_click)

        btn3 = QPushButton('&Button3', self)
        btn3.setCheckable(True)
        btn3.setText('zra')
        btn3.move(20,100)
        btn3.clicked.connect(self.zra_click)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setWindowTitle('MainFrame')
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()

    def emo_click(self):
        self.statusBar().showMessage('emo_click')
        # 나는 여기다가 코딩
    def miz_click(self):
        self.statusBar().showMessage('miz_click')
        # 미짱은 여기다가 코딩
    def zra_click(self):
        self.statusBar().showMessage('zra_click')
        # 찌라는 여기다가 코딩
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())