import copy
import json
import re
import requests
from datetime import date, timedelta
from time import sleep
from selenium.webdriver.common.by import By
from PyQt5 import QtCore

from login import Login
from cookies_pool import CookiesPool

today = date.today().strftime("%Y-%m-%d")   # 今天日期
tomorrow = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")  # 明天日期
dayAfterTomorrow = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")  # 后天日期
urlDream1 = "http://202.202.209.15:8081/product/show.html?id=141"   # 梦一URL
urlDream2 = "http://202.202.209.15:8081/product/show.html?id=142"   # 梦二URL
urlDream3 = "http://202.202.209.15:8081/product/show.html?id=261"   # 梦三URL
tookUrl = 'http://202.202.209.15:8080/order/tobook.html'  # 预定URL
delOrderUrl = 'http://202.202.209.15:8080/order/delorder.html'  # 取消订单URL
delOrderDetailUrl = 'http://202.202.209.15:8081/order/delorderdetail.html'  # 取消订单详情时间段URL

class Reserve(QtCore.QObject):
    """模拟预定梦厅的类"""
    signal_illegal = QtCore.pyqtSignal()  # 账户信息错误
    signal_legal = QtCore.pyqtSignal()  # 账户信息正确

    def __init__(self):
        """初始化预定"""
        super().__init__()
        self.timer = {  # 每个时间段的座位信息,座位余量和座位ID
            "07:30-09:59": ["0", ""],
            "10:00-11:59": ["0", ""],
            "12:00-13:59": ["0", ""],
            "14:00-15:59": ["0", ""],
            "16:00-17:59": ["0", ""],
            "18:00-19:59": ["0", ""],
            "20:00-23:30": ["0", ""]
        }
        self.day = [copy.deepcopy(self.timer), copy.deepcopy(self.timer), copy.deepcopy(self.timer)]  # 对应天数每个梦厅的信息
        self.info = [copy.deepcopy(self.day), copy.deepcopy(self.day), copy.deepcopy(self.day)]  # 所有信息

        self.todayInfoUrl = 'http://202.202.209.15:8081/product/findtime.html?type=day&s_dates='\
               +today  # 今天座位信息URL
        self.tomorrowInfoUrl = 'http://202.202.209.15:8081/product/findtime.html?type=day&s_dates='\
                  +tomorrow  # 明天座位信息URL
        self.datInfoUrl = 'http://202.202.209.15:8081/product/findtime.html?type=day&s_dates='\
             +dayAfterTomorrow  # 后天座位信息URL

    def get_cookies(self):
        """获取cookies"""
        while 1:  # 直到成功跳转页面
            while 1:  # 直到得到的验证码扫描不为空
                login = Login()
                if login.fill_captcha(tookUrl) == True:
                    break
                else:
                    login.browser.driver.close()

            # 获得登录窗口的URL
            loginUrl = login.browser.driver.current_url
            print("loginUrl:" + loginUrl)
            login.login_in(login.browser)

            # 获得当前窗口的URL
            currentUrl = login.browser.driver.current_url
            currentUrl = re.sub(r';jsessionid.+-n1', '', currentUrl)
            print("currentUrl:" + currentUrl)

            if currentUrl == loginUrl:
                # 验证登录信息是否有误
                msg = login.browser.driver.find_element(By.XPATH, '//*[@id="msg"]').get_attribute('textContent')
                print("返回信息："+msg)
                if msg == "密码错误" or msg == "用户名错误.":
                    self.signal_illegal.emit()
                    break
                else:
                    print("验证码错误")

            if currentUrl != loginUrl:
                # 成功登录,存入cookies
                self.signal_legal.emit()
                login.browser.cookies = login.browser.save_cookies("reserve")
                login.browser.driver.close()
                break
            else:
                login.browser.driver.close()

    def get_seat_info(self, day):
        """
        获取座位信息
        :param day: @str "today"、"tomorrow"、"dayAfterTomorrow"
        :return:
        """
        while 1:
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

            if day == "today":
                response = requests.get(self.todayInfoUrl, headers=headers)
            elif day == "tomorrow":
                response = requests.get(self.tomorrowInfoUrl, headers=headers)
            elif day == "dayAfterTomorrow":
                response = requests.get(self.datInfoUrl, headers=headers)

            try:
                currentUrl = str(re.match(r'http://.+login', response.url).group())
                if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                    self.get_cookies()
                    continue
            except:
                print("cookies可用")

            jsonInfo = json.loads(response.text)
            print(jsonInfo)
            print(response.url)
            print(response.status_code)
            if jsonInfo['object'] != None:
                for i in jsonInfo['object']:
                    if day == "today":
                        dayIndex = 0
                    elif day == "tomorrow":
                        dayIndex = 1
                    elif day == "dayAfterTomorrow":
                        dayIndex = 2

                    if i['REMARK'] == "梦一厅":
                        lobbyIndex = 0
                    elif i['REMARK'] == "梦二厅":
                        lobbyIndex = 1
                    elif i['REMARK'] == "梦三厅":
                        lobbyIndex = 2

                    self.info[dayIndex][lobbyIndex][i['TIME_NO']][0] = i['SURPLUS']  # 存入座位数量
                    self.info[dayIndex][lobbyIndex][i['TIME_NO']][1] = i['ID']  # 存入座位ID

            break

    def show_seat_info(self):
        """显示座位信息"""
        print("今天\n梦一厅："+str(self.info[0][0])+"\n梦二厅："+str(self.info[0][1])+"\n梦三厅："+str(self.info[0][2]))
        print("明天\n梦一厅："+str(self.info[1][0])+"\n梦二厅："+str(self.info[1][1])+"\n梦三厅："+str(self.info[1][2]))
        print("后天\n梦一厅："+str(self.info[2][0])+"\n梦二厅："+str(self.info[2][1])+"\n梦三厅："+str(self.info[2][2]))

                # print(i['REMARK'])
                # print(i['ID'])
                # print(i['TIME_NO'])
                # print(i['SURPLUS'])


    def reserve_session(self, day, lobby, timer):
        """
        选择预定场次
        :param day:  @str "today"、"tomorrow"、"dayAfterTomorrow"
        :param lobby:  @int 梦一:0  梦二:1  梦三:2
        :param timer:  @list[str] 时间段：0->6
        :return:
        """
        while 1:
            cookiesPool = CookiesPool()
            cookiesPool.get_cookies("reserve")
            cookie = cookiesPool.reserveCookies

            seat = {}
            if day == "today":
                stock = self.info[0]
            elif day == "tomorrow":
                stock = self.info[1]
            elif day == "dayAfterTomorrow":
                stock = self.info[2]

            if lobby == 0:
                stock = stock[0]
            elif lobby == 1:
                stock = stock[1]
            elif lobby == 2:
                stock = stock[2]

            if "0" in timer:
                stock0 = stock.get("07:30-09:59")[1]
                seat[str(stock0)] = "1"
            if "1" in timer:
                stock1 = stock.get("10:00-11:59")[1]
                seat[str(stock1)] = "1"
            if "2" in timer:
                stock2 = stock.get("12:00-13:59")[1]
                seat[str(stock2)] = "1"
            if "3" in timer:
                stock3 = stock.get("14:00-15:59")[1]
                seat[str(stock3)] = "1"
            if "4" in timer:
                stock4 = stock.get("16:00-17:59")[1]
                seat[str(stock4)] = "1"
            if "5" in timer:
                stock5 = stock.get("18:00-19:59")[1]
                seat[str(stock5)] = "1"
            if "6" in timer:
                stock6 = stock.get("20:00-23:30")[1]
                seat[str(stock6)] = "1"

            param = {}
            param["stock"] = seat
            param["extend"] = {}

            headers = {
                "content-type": 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': '202.202.209.15:8080',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                              'Chrome/96.0.4664.45 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': cookie
            }
            data = {
                'param': str(param),
                'json': 'true'
            }
            response = requests.post(tookUrl, headers=headers, data=data)
            try:
                currentUrl = str(re.match(r'http://.+login', response.url).group())
                if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                    self.get_cookies()
                    continue
            except:
                print("cookies可用")
            print(response.text)
            print(response.status_code)

            break

    def self_reserve_lobby(self, day, lobby, timer):
        """
        自己预约指定位置
        :param day:  @str "today"、"tomorrow"、"dayAfterTomorrow"
        :param lobby:  @int 梦一:0  梦二:1  梦三:2
        :param timer:  @list 时间段：0->6
        :return:
        """
        self.get_seat_info(day)
        self.reserve_session(day, lobby, timer)

    def check_order(self, orderType, orderPage):
        """
        查看订单
        :param orderType:  @str  "1"->正常订单 "2"->取消订单 "4"->违约订单
        :param orderPage:  @str  显示的页数,每页最多显示8行
        :return:
        """
        orderUrl = 'http://202.202.209.15:8080/yyuser/searchorder.html?page=' + orderPage + '&rows=8&status=' \
                   + orderType + '&iscomment='
        while 1:
            cookiesPool = CookiesPool()
            cookiesPool.get_cookies("reserve")
            cookie = cookiesPool.reserveCookies

            headers = {
                'Host': '202.202.209.15:8080',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                              'Chrome/96.0.4664.45 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': cookie
            }
            response = requests.get(orderUrl, headers=headers)
            try:
                currentUrl = str(re.match(r'http://.+login', response.url).group())
                if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                    self.get_cookies()
                    continue
            except:
                print("cookies可用")
            print(response.text)
            print(response.status_code)

            order = {'id': '', 'lobby': '', 'seat': '', 'date': '', 'timer': ''}
            orderPage = []
            response = requests.get(orderUrl, headers=headers)
            orderInfos = response.json()
            for i in range(len(orderInfos)):
                orderPage.append(copy.deepcopy(order))
            print(orderInfos)
            for i, orderInfo in enumerate(orderInfos):
                orderPage[i]['id'] = orderInfo['orderid']
                orderPage[i]['lobby'] = orderInfo['servicenames']
                orderPage[i]['seat'] = orderInfo['remark']
                orderPage[i]['date'] = orderInfo['stockDate']
                orderPage[i]['timer'] = orderInfo['remark1']
            print(orderPage)
            print(response.status_code)

            break

    def cancel_order(self, id):
        """
        取消整个订单
        :param id:  @str  订单号
        :return: message:  @str 订单取消状态
        """
        while 1:
            cookiesPool = CookiesPool()
            cookiesPool.get_cookies("reserve")
            cookie = cookiesPool.reserveCookies

            headers = {
                'Host': '202.202.209.15:8080',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                              'Chrome/96.0.4664.45 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': cookie
            }
            data = {
                'orderid': id,
                'json': 'true'
            }
            response = requests.post(delOrderUrl, headers=headers, data=data)
            try:
                currentUrl = str(re.match(r'http://.+login', response.url).group())
                if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                    self.get_cookies()
                    continue
            except:
                print("cookies可用")

            print(response.status_code)
            message = response.json()['message']

            return message

    def cancel_seat(self, id, index):
        """
        取消订单中具体某个时间段的订单
        :param id:  @str  订单号
        :param index: @int  取消的时间段位于订单中的索引
        :return: message @str 订单取消状态
        """
        orderViewUrl = 'http://202.202.209.15:8081/order/myorder_view.html?id='+id
        while 1:
            cookiesPool = CookiesPool()
            cookiesPool.get_cookies("reserve")
            cookie = cookiesPool.reserveCookies

            headers = {
                'Host': '202.202.209.15:8080',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                              'Chrome/96.0.4664.45 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': cookie
            }
            response = requests.get(orderViewUrl, headers=headers)
            try:
                currentUrl = str(re.match(r'http://.+login', response.url).group())
                if currentUrl == "http://csxrz.cqnu.edu.cn/cas/login":
                    self.get_cookies()
                    continue
            except:
                print("cookies可用")

            print(response.status_code)
            response = response.text
            timerIds = re.findall("验证码 (\d*)", response)  # 订单里每个时间段的ID
            print(timerIds)
            try:
                timerId = timerIds[index]
                headers = {
                    'Host': '202.202.209.15:8080',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                  'Chrome/96.0.4664.45 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
                    'cookie': cookie
                }
                data = {
                    'id': timerId,
                    'json': 'true'
                }
                response = requests.post(delOrderDetailUrl, headers=headers, data=data)

                print(response.status_code)
                message = response.json()['message']
                print(message)
                return message
            except:
                print("服务器又出问题啦!")
                break

    def advance_reserve(self, lobby):
        """自动提前预约指定梦厅全天位置"""
        self.get_seat_info("dayAfterTomorrow")  # 大概率位置在1-3排,具体依赖于有无其他程序在预约
        timer = ["0", "1", "2", "3", "4", "5", "6"]
        self.reserve_session("dayAfterTomorrow", lobby, timer)
        sleep(30)


if __name__ == '__main__':
    reserve = Reserve()
    # timer = ["0"]
    # reserve.self_reserve_lobby("dayAfterTomorrow", 0, timer)
    reserve.get_seat_info("today")
    reserve.get_seat_info("tomorrow")
    reserve.get_seat_info("dayAfterTomorrow")
    reserve.show_seat_info()
    # reserve.check_order("1", "1")
    # print(reserve.cancel_order('1638086679731935'))
    # reserve.cancel_seat('1638171658865279', 1)
    # reserve.get_cookies()
