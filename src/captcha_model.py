from urllib import request
from PIL import Image
import cv2
import os
import time
import random

import captcha_processing

class CaptchaModel:
    """训练验证码模型的类"""

    def get_and_save_captcha(self, n):
        """获取并保存验证码"""
        try:
            url = 'https://csxrz.cqnu.edu.cn/cas/verCode?random=1637483898334'  # 验证码url
            request.urlretrieve(url, './test_model/' + 'verify_' + str(n) + '.tif')
            print('第' + str(n) + '张图片下载成功')
        except Exception:
            print('第' + str(n) + '张图片下载失败')

    def get_proxy(self):
        """使用代理"""
        # - 1、设置代理地址
        proxys = [{'http': '39.137.69.10:8080'},
                  {'http': '111.206.6.101:80'},
                  {'http': '120.210.219.101:8080'},
                  {'http': '111.206.6.101:80'},
                  {'https': '120.237.156.43:8088'}]
        # - 2、创建ProxyHandler
        proxy = random.choice(proxys)
        proxy_handler = request.ProxyHandler(proxy)
        # - 3、创建Opener
        opener = request.build_opener(proxy_handler)
        # - 4、导入Opener
        request.install_opener(opener)

    def captcha_to_file(self, n):
        """存放n-1张验证码到文件夹"""
        for i in range(1, n):
            # get_proxy()
            # time.sleep(random.randint(1, 4))
            self.get_and_save_captcha(i)

    def modle_processing(self):
        """对准备训练的模型进行所有的降噪处理"""
        prossing_obj = captcha_processing.Captcha_processing()
        directory_name = 'verify_pictures'  # 存放二维码的文件夹名
        for filename in os.listdir(r"./" + directory_name):
            img = cv2.imread(directory_name + "/" + filename)

            ret, img2 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)  # 二值化
            img = prossing_obj.operate_img(img2, 2)
            img = prossing_obj.around_white(img)
            img = prossing_obj.noise_unsome_piexl(img)

            crop_size = (500, 200)
            img = cv2.resize(img, crop_size, interpolation=cv2.INTER_CUBIC)
            img = Image.fromarray(img)
            img.save('./' + directory_name + "/" + filename, dpi=(300.0, 300.0))


if __name__ == '__main__':
    model = CaptchaModel()
    model.captcha_to_file(251)
    model.modle_processing()