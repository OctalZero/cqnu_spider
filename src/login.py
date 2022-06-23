from selenium.webdriver.common.by import By
import os

from captcha import Captcha
from captcha_processing import CaptchaProcessing
from browser import Browser

class Login:
    """"模拟登录操作的类"""

    def __init__(self):
        """"初始化登录"""
        self.browser = Browser()
        self.username = ""
        self.password = ""
        self.authCode = ""
        self.fill_info()

    def fill_info(self):
        """填入用户信息"""
        if os.path.exists('./data/user.txt'):
            with open('./data/user.txt', 'r') as f:
                self.username = f.readline().rstrip()
                self.password = f.readline().rstrip()

    def fill_captcha(self, url):
        """"填入验证码"""
        captcha = Captcha()
        captcha.get_captcha(self.browser.driver, url)
        prossingObj = CaptchaProcessing()
        captchaVal = prossingObj.img_to_str()
        print("cap:"+captchaVal)
        if len(captchaVal) != 0:
            self.authCode = captchaVal
            return True
        else:
            return False


    def login_in(self, browser):
        """"首页登录操作"""
        usernameInput = browser.driver.find_element(By.ID, 'username')
        usernameInput.send_keys(self.username)
        passwordInput = browser.driver.find_element(By.ID, 'password')
        passwordInput.send_keys(self.password)
        print("auth:"+self.authCode)
        authCodeInput = browser.driver.find_element(By.ID, 'authCode')
        authCodeInput.send_keys(self.authCode)
        button = browser.driver.find_element(By.ID, 'J-login-btn')
        browser.driver.execute_script("arguments[0].click();", button)
        # button.send_keys(Keys.ENTER) # 通过回车键进入


