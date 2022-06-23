from selenium import webdriver
import json

class Browser:
    """浏览器类"""

    def __init__(self):
        """"初始化浏览器"""
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--window-size=1920,1080") # 优化selenium性能
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-software-rasterizer")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--allow-running-insecure-content')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def save_cookies(self, cookieType):
        """存放cookie"""
        cookie = {}
        if cookieType == "reserve":  # 存放预定页面的cookie
            for i in self.driver.get_cookies():
                cookie[i["name"]] = i["value"]
                with open("reserve_cookies.txt", "w") as f:
                    f.write(json.dumps(cookie))
