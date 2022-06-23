from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from ui_lobby1 import Ui_LobbyWindow1
from reserve import Reserve

class ControllerLobby1(QWidget, Ui_LobbyWindow1):
    """梦一厅控制类"""
    signal_ui_choose = QtCore.pyqtSignal(str)

    def __init__(self):
        """初始化教师控制类"""
        super(ControllerLobby1, self).__init__()
        self.setupUi(self)
        self.reserve = Reserve()  # 实例化reserve类
        self.date = ""  # 记录预计日期

        # 默认获取今天座位
        self.on_today_seat()
        # 连接界面返回信号与槽
        self.pushButton_back.clicked.connect(lambda: self.signal_ui_choose.emit("reserve"))
        self.pushButton_today.clicked.connect(self.on_today_seat)
        self.pushButton_tomorrow.clicked.connect(self.on_tommorow_seat)
        self.pushButton_dayAfterTomorrow.clicked.connect(self.on_dat_seat)
        self.pushButton.clicked.connect(self.on_order)

    def on_order(self):
        """提交订单的槽"""
        timer = []
        if self.checkBox_timer1.isChecked() == True:
            timer.append("0")
        if self.checkBox_timer2.isChecked() == True:
            timer.append("1")
        if self.checkBox_timer3.isChecked() == True:
            timer.append("2")
        if self.checkBox_timer4.isChecked() == True:
            timer.append("3")
        if self.checkBox_timer5.isChecked() == True:
            timer.append("4")
        if self.checkBox_timer6.isChecked() == True:
            timer.append("5")
        if self.checkBox_timer7.isChecked() == True:
            timer.append("6")

        self.reserve.self_reserve_lobby(self.date, 0, timer)
        self.frame_success.setVisible(True)

    def on_today_seat(self):
        """获取今天座位信息并显示给界面的槽"""
        self.pushButton_today.setStyleSheet("background-color: rgb(0,143,150);")  # 按钮一直亮
        self.pushButton_tomorrow.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.pushButton_dayAfterTomorrow.setStyleSheet("background-color: rgba(0,0,0,0);")

        self.reserve.get_seat_info("today")
        self.reserve.get_seat_info("tomorrow")
        self.reserve.get_seat_info("dayAfterTomorrow")
        self.label2_timer1.setText("剩余："+str(self.reserve.info[0][0]["07:30-09:59"][0]))
        self.label2_timer2.setText("剩余："+str(self.reserve.info[0][0]["10:00-11:59"][0]))
        self.label2_timer3.setText("剩余："+str(self.reserve.info[0][0]["12:00-13:59"][0]))
        self.label2_timer4.setText("剩余："+str(self.reserve.info[0][0]["14:00-15:59"][0]))
        self.label2_timer5.setText("剩余："+str(self.reserve.info[0][0]["16:00-17:59"][0]))
        self.label2_timer6.setText("剩余："+str(self.reserve.info[0][0]["18:00-19:59"][0]))
        self.label2_timer7.setText("剩余："+str(self.reserve.info[0][0]["20:00-23:30"][0]))
        self.date = "today"


    def on_tommorow_seat(self):
        """获取明天座位信息并显示给界面的槽"""
        self.pushButton_tomorrow.setStyleSheet("background-color: rgb(0,143,150);")  # 按钮一直亮
        self.pushButton_today.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.pushButton_dayAfterTomorrow.setStyleSheet("background-color: rgba(0,0,0,0);")

        self.reserve.get_seat_info("today")
        self.reserve.get_seat_info("tomorrow")
        self.reserve.get_seat_info("dayAfterTomorrow")
        self.label2_timer1.setText("剩余："+str(self.reserve.info[1][0]["07:30-09:59"][0]))
        self.label2_timer2.setText("剩余："+str(self.reserve.info[1][0]["10:00-11:59"][0]))
        self.label2_timer3.setText("剩余："+str(self.reserve.info[1][0]["12:00-13:59"][0]))
        self.label2_timer4.setText("剩余："+str(self.reserve.info[1][0]["14:00-15:59"][0]))
        self.label2_timer5.setText("剩余："+str(self.reserve.info[1][0]["16:00-17:59"][0]))
        self.label2_timer6.setText("剩余："+str(self.reserve.info[1][0]["18:00-19:59"][0]))
        self.label2_timer7.setText("剩余："+str(self.reserve.info[1][0]["20:00-23:30"][0]))
        self.date = "tomorrow"

    def on_dat_seat(self):
        """获取后天座位信息并显示给界面的槽"""
        self.pushButton_dayAfterTomorrow.setStyleSheet("background-color: rgb(0,143,150);")  # 按钮一直亮
        self.pushButton_tomorrow.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.pushButton_today.setStyleSheet("background-color: rgba(0,0,0,0);")

        self.reserve.get_seat_info("today")
        self.reserve.get_seat_info("tomorrow")
        self.reserve.get_seat_info("dayAfterTomorrow")
        self.label2_timer1.setText("剩余："+str(self.reserve.info[2][0]["07:30-09:59"][0]))
        self.label2_timer2.setText("剩余："+str(self.reserve.info[2][0]["10:00-11:59"][0]))
        self.label2_timer3.setText("剩余："+str(self.reserve.info[2][0]["12:00-13:59"][0]))
        self.label2_timer4.setText("剩余："+str(self.reserve.info[2][0]["14:00-15:59"][0]))
        self.label2_timer5.setText("剩余："+str(self.reserve.info[2][0]["16:00-17:59"][0]))
        self.label2_timer6.setText("剩余："+str(self.reserve.info[2][0]["18:00-19:59"][0]))
        self.label2_timer7.setText("剩余："+str(self.reserve.info[2][0]["20:00-23:30"][0]))
        self.date = "dayAfterTomorrow"

