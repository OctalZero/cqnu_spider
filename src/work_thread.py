from PyQt5 import QtCore
import requests
import re
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

from reserve import Reserve
from cookies_pool import CookiesPool


class LoginThread(QtCore.QThread):
    """完成登录操作的线程"""
    signal_illegal = QtCore.pyqtSignal()
    signal_legal = QtCore.pyqtSignal()
    signal_button_enable = QtCore.pyqtSignal()

    def __init__(self):
        """初始化线程"""
        super(LoginThread, self).__init__()

    def __del__(self):
        """回收线程"""
        self.wait()

    def on_illegal(self):
        """账号非法法的槽"""
        self.signal_illegal.emit()
        self.signal_button_enable.emit()

    def on_legal(self):
        """账号合法的槽"""
        self.signal_legal.emit()

    def run(self):
        """重载run,放入线程工作逻辑"""
        reserve = Reserve()
        reserve.signal_illegal.connect(self.on_illegal)
        reserve.signal_legal.connect(self.on_legal)
        reserve.get_cookies()

class CheckCookiesThread(QtCore.QThread):
    """检测Cookies是否有效的线程"""
    signal_cookies_useful = QtCore.pyqtSignal(str)
    signal_cookies_unuseful = QtCore.pyqtSignal(str)

    def __init__(self):
        """初始化线程"""
        super(CheckCookiesThread, self).__init__()

    def __del__(self):
        """回收线程"""
        self.wait()

    def run(self):
        """重载run,放入线程工作逻辑"""
        cookiesPool = CookiesPool()
        cookiesPool.get_cookies("reserve")
        cookie = cookiesPool.reserveCookies
        print(cookie)

        headers = {
            'Host': '202.202.209.15:8081',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/96.0.4664.45 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'cookie': cookie
        }

        url = "http://202.202.209.15:8081/product/show.html?id=141"
        response = requests.get(url, headers=headers)
        try:
            currentUrl = str(re.match(r'http://.+login', response.url).group())
            if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                self.signal_cookies_useful.emit("unuseful")
                print("test unuseful")
            else:
                self.signal_cookies_useful.emit("useful")
                print("test useful")
        except:
            self.signal_cookies_useful.emit("useful")
            print("test useful")
        print("checkCookiesThread over")

class CommonReserveThread(QtCore.QThread):
    """普通预定的线程"""
    signal_is_ready = QtCore.pyqtSignal()

    def __init__(self):
        """初始化线程"""
        super(CommonReserveThread, self).__init__()
        self.lobby = 0

    def __del__(self):
        """回收线程"""
        self.wait()

    def on_choose_lobby(self, lobby):
        """选择梦厅的槽"""
        self.lobby = lobby
        self.signal_is_ready.emit()
        print("choose lobby")
        print(self.lobby)

    def job(self):
        """预定单个座位"""
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        reserve = Reserve()
        reserve.advance_reserve(self.lobby)

    def run(self):
        """重载run,放入线程工作逻辑"""
        print("CommonReserveThread begin")
        scheduler = BlockingScheduler()
        scheduler.add_job(self.job, 'cron', hour='00', minute='12', second='30')  # 设置预定座位的时间
        scheduler.start()
        print("CommonReserveThread over")

class ContinueReserveThread(QtCore.QThread):
    """连坐预定的线程"""
    signal_is_ready = QtCore.pyqtSignal()

    def __init__(self):
        """初始化线程"""
        super(ContinueReserveThread, self).__init__()
        self.lobby = 0

    def __del__(self):
        """回收线程"""
        self.wait()

    def on_choose_lobby(self, lobby):
        """选择梦厅的槽"""
        self.lobby = lobby
        self.signal_is_ready.emit()
        print("choose lobby")
        print(self.lobby)

    def job(self):
        """预定连续座位"""
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        reserve = Reserve()
        for i in range(2):  # 连续预定两个座位
            reserve.advance_reserve(self.lobby)

    def run(self):
        """重载run,放入线程工作逻辑"""
        print("ContinueReserveThread begin")
        scheduler = BlockingScheduler()
        scheduler.add_job(self.job, 'cron', hour='00', minute='10', second='30')  # 设置预定座位的时间
        scheduler.start()
        print("ContinueReserveThread over")