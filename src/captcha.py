from PIL import Image
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import captcha_processing

class Captcha:
    """验证码类"""

    def get_captcha(self, driver, url):
        """模拟登录获取验证码"""
        directory_name = 'captcha'  # 存放本次获取的二维码的文件夹名
        driver.maximize_window()  # 将浏览器最大化
        driver.get(url)
        # driver.execute_script('document.body.style.zoom="0.8"')  # Windows默认缩放比例125%
        # 截取当前网页并放到文件夹中命名为printscreen，该网页有需要的验证码
        driver.save_screenshot("./" + directory_name + "/printscreen.png")
        wait = WebDriverWait(driver, 10)
        imgElement = wait.until(EC.presence_of_element_located((By.ID, 'validatorCodeOfLogin')))  # 定位验证码
        location = imgElement.location  # 获取验证码x,y轴坐标
        print(location)
        size = imgElement.size  # 获取验证码的长宽
        print(size)
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 需要截取的位置坐标
        i = Image.open("./" + directory_name + "/printscreen.png")  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取需要的区域
        frame4 = frame4.convert('RGB')
        frame4.save("./" + directory_name + "/captcha.png", dpi=(300.0, 300.0))  # 保存截下来的验证码图片


if __name__ == '__main__':
    while 1:
        captcha = Captcha()
        captcha.get_captcha()
        prossingObj = captcha_processing.Captcha_processing()
        if len(prossingObj.img_to_str()) != 0:
            break
        sleep(1)

