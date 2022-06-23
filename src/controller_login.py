from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os

from ui_login import Ui_LoginWindow
from work_thread import LoginThread, CheckCookiesThread

class ControllerLogin(QWidget, Ui_LoginWindow):
    """登录控制类"""

    signal_ui_choose = QtCore.pyqtSignal(str)

    def __init__(self):
        """初始化登录控制类"""
        super(ControllerLogin, self).__init__()
        self.setupUi(self)
        self.info = []  # 账号信息
        self.cookiesState = ""  # cookies状态
        self.loginThread = None  # 初始化登录线程
        self.checkCookiesThread = None  # 初始化检测cookies线程

        """自动填入记住的密码"""
        if os.path.exists('./data/user_save.txt'):
            with open('./data/user_save.txt', 'r') as f:
                self.lineEdit_user.setText(f.readline().rstrip())
                self.lineEdit_password.setText(f.readline().rstrip())

        """连接界面触发的信号与槽"""
        self.pushButton_login.clicked.connect(self.on_check_info)

    def on_check_info(self):
        """检测用户信息的槽"""
        if not self.lineEdit_user.text():
            self.frame_error.show()
        elif not self.lineEdit_password.text():
            self.frame_error.show()
        elif len(self.lineEdit_user.text()) != 13:
            self.frame_error.show()
        else:
            self.check_exist()

    def check_exist(self):
        """检测是否有可用cookies存在"""
        if os.path.exists('./data/user_save.txt'):
            with open('./data/user_save.txt', 'r') as f:
                saveUser = f.readline().rstrip()
                savePassword = f.readline().rstrip()
        else:
            self.no_cookie()

        if self.lineEdit_user.text() == saveUser and self.lineEdit_password.text() == savePassword:
            # 当前账户为之前保存账户
            self.checkCookiesThread = CheckCookiesThread()
            # 连接主进程和子进程间信号与槽
            self.checkCookiesThread.signal_cookies_useful.connect(self.on_cookies_state)
            self.checkCookiesThread.signal_cookies_unuseful.connect(self.on_cookies_state)

            self.checkCookiesThread.start()
        else:
            self.no_cookie()

    def on_cookies_state(self, state):
        """接收cookies状态的槽"""
        self.cookiesState = state
        if self.cookiesState == "useful":
            self.signal_ui_choose.emit("home")
        elif self.cookiesState == "unuseful":
            self.no_cookie()
        else:
            self.no_cookie()

    def no_cookie(self):
        """当前无可用cookies,获取新cookies"""
        # 将信息存入文件
        print("no_cookie")
        with open('./data/user.txt', 'w') as f:
            f.write(self.lineEdit_user.text() + '\n')
            f.write(self.lineEdit_password.text())

        self.pushButton_login.setEnabled(False)
        self.checkBox_save_user.setEnabled(False)
        self.info.append(self.lineEdit_user.text())
        self.info.append(self.lineEdit_password.text())
        print(self.info[0])
        print(self.info[1])
        self.loginThread = LoginThread()
        # 连接主进程和子进程间信号与槽
        self.loginThread.signal_illegal.connect(self.on_show_error)
        self.loginThread.signal_button_enable.connect(self.on_button_enable)
        self.loginThread.signal_legal.connect(self.on_success_login)

        self.loginThread.start()
        print("start")

    def on_success_login(self):
        """成功登录的槽"""
        self.signal_ui_choose.emit("home")
        if self.checkBox_save_user.isChecked():
            with open('./data/user_save.txt', 'w') as f:
                f.write(self.lineEdit_user.text()+'\n')
                f.write(self.lineEdit_password.text())


    def on_show_error(self):
        """界面显示错误的槽"""
        self.frame_error.show()

    def on_button_enable(self):
        """按钮可用的槽"""
        self.pushButton_login.setEnabled(True)
        self.checkBox_save_user.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ControllerLogin()
    ui.show()
    sys.exit(app.exec_())




