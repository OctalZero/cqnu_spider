from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from ui_home import Ui_HomeWindow

class ControllerHome(QWidget, Ui_HomeWindow):
    """主页控制类"""
    signal_ui_choose = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ControllerHome, self).__init__()
        self.setupUi(self)

        # 连接界面跳转信号与槽
        self.pushButton_web.clicked.connect(self.on_change_webs)
        self.pushButton_teacher.clicked.connect(self.on_change_teachers)
        self.pushButton_reserve.clicked.connect(self.on_change_reserve)

    def on_change_webs(self):
        """跳转到考研网站界面"""
        self.signal_ui_choose.emit("webs")

    def on_change_teachers(self):
        """跳转到选择教师界面"""
        self.signal_ui_choose.emit("teachers")

    def on_change_reserve(self):
        """跳转到梦厅预定界面"""
        self.signal_ui_choose.emit("reserve")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ControllerHome()
    ui.show()
    sys.exit(app.exec_())