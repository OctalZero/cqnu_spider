from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

from controller_login import ControllerLogin
from controller_home import ControllerHome
from controller_webs import ControllerWebs
from controller_teachers import ControllerTeachers
from controller_info import ControllerInfo
from controller_reserve import ControllerReserve
from controller_lobby1 import ControllerLobby1
from controller_lobby2 import ControllerLobby2
from controller_lobby3 import ControllerLobby3

class MainWindow(QWidget):
    """应用主界面类"""

    def __init__(self):
        """初始化应用主界面类"""
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        """初始化ui界面"""
        self.resize(480, 800)
        self.setMinimumSize(QtCore.QSize(480, 800))
        self.setMaximumSize(QtCore.QSize(480, 800))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("cqnu_spider")
        self.setStyleSheet("color: rgb(200, 200, 200);\n"
                                 "background-color: rgb(47, 79, 79);")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 填满整个界面

        # 设置widgetStack,并填入每个界面
        self.stack = QStackedWidget()
        self.loginUi = ControllerLogin()
        self.homeUi = ControllerHome()
        self.websUi = ControllerWebs()
        self.teachersUi = ControllerTeachers()
        self.teacherInfoUi = ControllerInfo()
        self.reserveUi = ControllerReserve()
        self.lobby1Ui = ControllerLobby1()
        self.lobby2Ui = ControllerLobby2()
        self.lobby3Ui = ControllerLobby3()

        self.layout.addWidget(self.stack)
        self.stack.addWidget(self.loginUi)
        self.stack.addWidget(self.homeUi)
        self.stack.addWidget(self.websUi)
        self.stack.addWidget(self.teachersUi)
        self.stack.addWidget(self.teacherInfoUi)
        self.stack.addWidget(self.reserveUi)
        self.stack.addWidget(self.lobby1Ui)
        self.stack.addWidget(self.lobby2Ui)
        self.stack.addWidget(self.lobby3Ui)

        # 连接界面切换的信号和槽
        self.loginUi.signal_ui_choose.connect(self.showWindow)
        self.homeUi.signal_ui_choose.connect(self.showWindow)
        self.websUi.signal_ui_choose.connect(self.showWindow)
        self.teachersUi.signal_ui_choose.connect(self.showWindow)
        self.teacherInfoUi.signal_ui_choose.connect(self.showWindow)
        self.reserveUi.signal_ui_choose.connect(self.showWindow)
        self.lobby1Ui.signal_ui_choose.connect(self.showWindow)
        self.lobby2Ui.signal_ui_choose.connect(self.showWindow)
        self.lobby3Ui.signal_ui_choose.connect(self.showWindow)

        # 连接子界面间的信号与槽
        self.teachersUi.signal_teacher_choose.connect(self.teacherInfoUi.on_teacher)
        self.homeUi.pushButton_use.clicked.connect(self.teacherInfoUi.on_use)
        self.homeUi.pushButton_view.clicked.connect(self.teacherInfoUi.on_view)
        self.homeUi.pushButton_about.clicked.connect(self.teacherInfoUi.on_about)

    def showWindow(self, ui):
        if ui == "login":
            self.stack.setCurrentIndex(0)
        elif ui == "home":
            self.stack.setCurrentIndex(1)
        elif ui == "webs":
            self.stack.setCurrentIndex(2)
        elif ui == "teachers":
            self.stack.setCurrentIndex(3)
        elif ui == "teacherInfo":
            self.stack.setCurrentIndex(4)
        elif ui == "reserve":
            self.stack.setCurrentIndex(5)
        elif ui == "lobby1":
            self.stack.setCurrentIndex(6)
        elif ui == "lobby2":
            self.stack.setCurrentIndex(7)
        elif ui == "lobby3":
            self.stack.setCurrentIndex(8)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
