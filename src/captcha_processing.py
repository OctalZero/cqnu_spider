import cv2
from PIL import Image
import tesserocr
import matplotlib.pyplot as plt

class CaptchaProcessing:
    """处理验证码的类"""

    def calculate_noise_count(self, img_obj, w, h):
        """计算邻域非白色的个数"""
        count = 0
        width, height, s = img_obj.shape
        for _w_ in [w - 1, w, w + 1]:
            for _h_ in [h - 1, h, h + 1]:
                if _w_  > width - 1:
                    continue
                if _h_ > height - 1:
                    continue
                if _w_ == w and _h_ == h:
                    continue
                if (img_obj[_w_, _h_, 0] < 233) or (img_obj[_w_, _h_, 1] < 233) or (img_obj[_w_, _h_, 2] < 233):
                    count += 1
        return count

    def operate_img(self, img, k):
        """k邻域降噪"""
        w, h, s = img.shape
        # 从高度开始遍历
        for _w in range(w):
            # 遍历宽度
            for _h in range(h):
                if _h != 0 and _w != 0 and _w < w-1 and _h < h-1:
                    if self.calculate_noise_count(img, _w, _h) < k:
                        img.itemset((_w, _h, 0), 255)
                        img.itemset((_w, _h, 1), 255)
                        img.itemset((_w, _h, 2), 255)

        return img

    def around_white(self, img):
        """图像四周置白色"""
        w, h, s = img.shape
        for _w in range(w):
            for _h in range(h):
                if (_w <= 1) or (_h <= 1) or (_w >= w-1) or (_h >= h-1):
                    img.itemset((_w, _h, 0), 255)
                    img.itemset((_w, _h, 1), 255)
                    img.itemset((_w, _h, 2), 255)
        return img

    def noise_unsome_piexl(self, img):
        """邻域非同色降噪，查找像素点上下左右相邻点的颜色，如果是非白色的非像素点颜色，则填充为白色"""
        # print(img.shape)
        w, h, s = img.shape
        for _w in range(w):
            for _h in range(h):
                if _h != 0 and _w != 0 and _w < w - 1 and _h < h - 1:   # 剔除顶点、底点
                    center_color = img[_w, _h] # 当前坐标颜色
                    # print(center_color)
                    top_color = img[_w, _h + 1]
                    bottom_color = img[_w, _h - 1]
                    left_color = img[_w - 1, _h]
                    right_color = img[_w + 1, _h]
                    cnt = 0
                    if all(top_color == center_color):
                        cnt += 1
                    if all(bottom_color == center_color):
                        cnt += 1
                    if all(left_color == center_color):
                        cnt += 1
                    if all(right_color == center_color):
                        cnt += 1
                    if cnt < 1:
                        img.itemset((_w, _h, 0), 255)
                        img.itemset((_w, _h, 1), 255)
                        img.itemset((_w, _h, 2), 255)
        return img

    def img_processing(self):
        """对本次获取的二维码进行所有的降噪处理,并返回处理后的二维码"""
        directory_name = 'captcha'  # 存放本次获取的二维码的文件夹名

        img = cv2.imread('./' + directory_name + "/captcha.png")
        ret, img2 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)  # 二值化

        # 显示图片对比
        # plt.subplot(121), plt.imshow(img)  # 原始图片
        # plt.subplot(122), plt.imshow(img2)  # 降噪图片
        # plt.show()

        img = self.operate_img(img2, 2)
        img = self.around_white(img)
        img = self.noise_unsome_piexl(img)
        crop_size = (750, 300)  # 增大图片的尺寸，否则无法识别
        img = cv2.resize(img, crop_size, interpolation=cv2.INTER_CUBIC)
        img = Image.fromarray(img)
        img.save('./' + directory_name + "/captcha.png", dpi=(300.0, 300.0))

    def img_to_str(self):
        """将验证码转换为string并返回"""
        directory_name = 'captcha'  # 存放本次获取的二维码的文件夹名

        self.img_processing()
        # 设置teseract路径
        # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open('./' + directory_name + "/captcha.png")
        captchaTxt = tesserocr.image_to_text(img, lang="eng")  # 图片转文字
        result = ''.join(filter(str.isalnum, captchaTxt))    # 只保留字母和数字

        result4 = result[0:4]  # 只获取前4个字符
        print(result4)  # 打印识别的验证码

        return result4


