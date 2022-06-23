from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from ui_webs import Ui_WebsWindow
from web_window import WebWindow

class ControllerWebs(QWidget, Ui_WebsWindow):
    """网站页面控制类"""
    signal_ui_choose = QtCore.pyqtSignal(str)
    signal_web_choose = QtCore.pyqtSignal(int)

    def __init__(self):
        """初始化网站页面控制类"""
        super(ControllerWebs, self).__init__()
        self.setupUi(self)
        self.webWindow = WebWindow()

        # 连接界面返回信号与槽
        self.pushButton_back.clicked.connect(self.on_back)
        # 连接网页信号与槽
        self.pushButton_web1.clicked.connect(self.on_loadWeb1)
        self.pushButton_web2.clicked.connect(self.on_loadWeb2)
        self.pushButton_web3.clicked.connect(self.on_loadWeb3)
        self.pushButton_web4.clicked.connect(self.on_loadWeb4)
        self.pushButton_web5.clicked.connect(self.on_loadWeb5)


    def on_loadWeb1(self):
        """加载网页1的槽"""
        self.signal_web_choose.connect(self.webWindow.on_changewebIndex)
        self.signal_web_choose.emit(1)

    def on_loadWeb2(self):
        """加载网页2的槽"""
        self.signal_web_choose.connect(self.webWindow.on_changewebIndex)
        self.signal_web_choose.emit(2)

    def on_loadWeb3(self):
        """加载网页3的槽"""
        self.signal_web_choose.connect(self.webWindow.on_changewebIndex)
        self.signal_web_choose.emit(3)

    def on_loadWeb4(self):
        """加载网页4的槽"""
        self.signal_web_choose.connect(self.webWindow.on_changewebIndex)
        self.signal_web_choose.emit(4)

    def on_loadWeb5(self):
        """加载网页5的槽"""
        self.signal_web_choose.connect(self.webWindow.on_changewebIndex)
        self.signal_web_choose.emit(5)
        self.webWindow.show()

    def on_back(self):
        """返回到home界面的槽"""
        self.signal_ui_choose.emit("home")



