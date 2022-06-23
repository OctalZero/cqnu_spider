from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from ui_reserve import Ui_ReserveWindow
from work_thread import CommonReserveThread, ContinueReserveThread

class ControllerReserve(QWidget, Ui_ReserveWindow):
    """梦厅预定控制类"""
    signal_ui_choose = QtCore.pyqtSignal(str)
    signal_lobby_choose = QtCore.pyqtSignal(int)

    def __init__(self):
        """初始化教师控制类"""
        super(ControllerReserve, self).__init__()
        self.setupUi(self)
        self.commonReserveThread = None  # 初始化普通预定线程
        self.continueReserveThread = None  # 初始化普通预定线程

        # 连接界面的信号与槽
        self.pushButton_back.clicked.connect(lambda: self.signal_ui_choose.emit("home"))  # 返回到home界面的槽
        self.pushButton_lobby1.clicked.connect(lambda: self.signal_ui_choose.emit("lobby1"))  # 切换到梦一厅的槽
        self.pushButton_lobby2.clicked.connect(lambda: self.signal_ui_choose.emit("lobby2"))  # 切换到梦二厅的槽
        self.pushButton_lobby3.clicked.connect(lambda: self.signal_ui_choose.emit("lobby3"))  # 切换到梦三厅的槽
        self.pushButton_normal_1.clicked.connect(self.on_normal_reserve1)
        self.pushButton_normal_2.clicked.connect(self.on_normal_reserve2)
        self.pushButton_normal_3.clicked.connect(self.on_normal_reserve3)
        self.pushButton_continu_1.clicked.connect(self.on_continue_reserve1)
        self.pushButton_continu_2.clicked.connect(self.on_continue_reserve2)
        self.pushButton_continu_3.clicked.connect(self.on_continue_reserve3)

    def on_continue_reserve1(self):
        """普通预定梦1的槽"""
        self.continueReserveThread = ContinueReserveThread()
        self.signal_lobby_choose.connect(self.continueReserveThread.on_choose_lobby)
        self.continueReserveThread.signal_is_ready.connect(self.on_start_continue)
        self.signal_lobby_choose.emit(0)

    def on_continue_reserve2(self):
        """普通预定梦2的槽"""
        self.continueReserveThread = ContinueReserveThread()
        self.signal_lobby_choose.connect(self.continueReserveThread.on_choose_lobby)
        self.continueReserveThread.signal_is_ready.connect(self.on_start_continue)
        self.signal_lobby_choose.emit(1)

    def on_continue_reserve3(self):
        """普通预定梦3的槽"""
        self.continueReserveThread = ContinueReserveThread()
        self.signal_lobby_choose.connect(self.continueReserveThread.on_choose_lobby)
        self.continueReserveThread.signal_is_ready.connect(self.on_start_continue)
        self.signal_lobby_choose.emit(2)

    def on_start_continue(self):
        """开始执行线程"""
        print("start")
        self.continueReserveThread.start()
        self.frame_success.setVisible(True)
        self.pushButton_continu_1.setEnabled(False)
        self.pushButton_continu_2.setEnabled(False)
        self.pushButton_continu_3.setEnabled(False)

    def on_normal_reserve1(self):
        """普通预定梦1的槽"""
        self.commonReserveThread = CommonReserveThread()
        self.signal_lobby_choose.connect(self.commonReserveThread.on_choose_lobby)
        self.commonReserveThread.signal_is_ready.connect(self.on_start_normal)
        self.signal_lobby_choose.emit(0)

    def on_normal_reserve2(self):
        """普通预定梦2的槽"""
        self.commonReserveThread = CommonReserveThread()
        self.signal_lobby_choose.connect(self.commonReserveThread.on_choose_lobby)
        self.commonReserveThread.signal_is_ready.connect(self.on_start_normal)
        self.signal_lobby_choose.emit(1)

    def on_normal_reserve3(self):
        """普通预定梦3的槽"""
        self.commonReserveThread = CommonReserveThread()
        self.signal_lobby_choose.connect(self.commonReserveThread.on_choose_lobby)
        self.commonReserveThread.signal_is_ready.connect(self.on_start_normal)
        self.signal_lobby_choose.emit(2)

    def on_start_normal(self):
        """开始执行线程"""
        print("start")
        self.commonReserveThread.start()
        self.frame_success.setVisible(True)
        self.pushButton_normal_1.setEnabled(False)
        self.pushButton_normal_2.setEnabled(False)
        self.pushButton_normal_3.setEnabled(False)


