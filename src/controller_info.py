from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os

from ui_teacher_info import Ui_TeacherInfoWindow

class ControllerInfo(QWidget, Ui_TeacherInfoWindow):
    """教师信息控制类"""
    signal_ui_choose = QtCore.pyqtSignal(str)

    def __init__(self):
        """初始化登录控制类"""
        super(ControllerInfo, self).__init__()
        self.setupUi(self)
        self.backState = ""
        # 连接界面返回信号与槽
        self.pushButton_back.clicked.connect(self.on_back)

    def on_back(self):
        """返回到teachers界面的槽"""
        self.signal_ui_choose.emit(self.backState)

    def load_info(self, name):
        """
        加载教师信息
        :param name: @str 教师姓名
        :return:
        """
        if os.path.exists('./data/'+ name +'.txt'):
            with open('./data/'+ name +'.txt', 'r', encoding="utf-8") as f:
                msg = f.read()
                self.textEdit_info.setPlainText(msg)

    def on_teacher(self, name):
        """选择教师的名字的槽"""
        self.load_info(name)
        self.signal_ui_choose.emit("teacherInfo")
        self.label_site.setText("教师简介")
        self.backState = "teachers"

    def on_use(self):
        """显示功能介绍的槽"""
        self.load_info("use")
        self.signal_ui_choose.emit("teacherInfo")
        self.label_site.setText("功能介绍")
        self.backState = "home"

    def on_view(self):
        """显示梦厅规则的槽"""
        self.load_info("view")
        self.signal_ui_choose.emit("teacherInfo")
        self.label_site.setText("梦厅规则")
        self.backState = "home"

    def on_about(self):
        """显示关于软件的槽"""
        self.load_info("about")
        self.signal_ui_choose.emit("teacherInfo")
        self.label_site.setText("关于软件")
        self.backState = "home"

