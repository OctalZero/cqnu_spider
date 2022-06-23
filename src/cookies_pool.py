import json

class CookiesPool:
    """Cookies池"""

    def __init__(self):
        """初始化Cookies池"""
        self.reserveCookies = ""

    def get_cookies(self, cookieType):
        """获得cookie"""
        try:
            if cookieType == "reserve":  # 获得预定页面的cookie
                with open("reserve_cookies.txt", "r") as f:
                    cookies = f.read()

                cookies = str(json.loads(cookies))  # 将json类型的cookie处理为可用的str格式
                cookies = cookies.replace('{', '')
                cookies = cookies.replace('}', '')
                cookies = cookies.replace(',', ';')
                cookies = cookies.replace("'", '')
                cookies = cookies.replace(':', '=')
                self.reserveCookies = cookies.replace(' ', '')
        except:
            print("当前无cookie可用")