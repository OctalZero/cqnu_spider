import requests
from lxml import etree

class TeacherSpider:
    """爬取并处理教师信息的类"""

    def __init__(self):
        """初始化教师爬取类"""
        self.teachersName = []
        self.teachersUrl = []

    def get_all_teacher(self):
        """获取所有教师及相关信息页面的url"""
        url = "https://jxxy.cqnu.edu.cn/xygk/szdw.htm"  # 包含所有教师的页面
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/96.0.4664.45 Safari/537.36',
        }

        response = requests.get(url, headers=headers)
        info = response.content.decode('utf-8')
        print(response.status_code)
        html = etree.HTML(info)
        self.teachersName = html.xpath('//a[@class="c134500"]//@title')  # 从首页获取所有教师的名字
        self.teachersUrl = html.xpath('//a[@class="c134500"]//@href')  # 从首页获取每个教师对应的信息网址

        for i, teacherUrl in enumerate(self.teachersUrl):
            self.teachersUrl[i] = teacherUrl[2:]

        for i, teacherName in enumerate(self.teachersName):
            with open('./data/'+teacherName+'.txt', 'w') as f:
                f.write(self.teachersUrl[i])

    def get_teacher_info(self):
        """获取并存入每个教师的个人信息"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/96.0.4664.45 Safari/537.36',
        }
        for i, teacherUrl in enumerate(self.teachersUrl):
            url = "https://jxxy.cqnu.edu.cn/"+teacherUrl
            print(url)
            response = requests.get(url, headers=headers)
            info = response.content.decode('utf-8')
            html = etree.HTML(info)
            teacherInfo = html.xpath('//*[@id="vsb_content"]/p//text()')  # 从个人详情页爬取个人信息
            teacherInfo = [str(i) for i in teacherInfo]
            teacherInfo =''.join(teacherInfo)
            print(teacherInfo)
            with open('./data/' + self.teachersName[i] + '.txt', 'w', encoding='utf-8') as f:  # 要指定'utf-8'编码格式
                f.write(teacherInfo)
        print("信息存入完毕!")

if __name__ == "__main__":
    """测试获取教师信息"""
    teacher = TeacherSpider()
    teacher.get_all_teacher()
    teacher.get_teacher_info()
