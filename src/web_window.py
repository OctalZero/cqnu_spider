from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class WebWindow(QMainWindow):

    def __init__(self):
        """初始化浏览器窗口"""
        super().__init__()
        self.setWindowTitle('Browser')
        self.setWindowIcon(QIcon('Images/Icon.png'))
        self.resize(480, 800)

        self.webIndex = 0  # 控制打开的网页

        # 设置浏览器
        self.browser = WebEngineView()

        user_agent = self.browser.page().profile().httpUserAgent()
        self.browser.page().profile().setHttpUserAgent(user_agent + "Android-APP")  # 设置UA标识为安卓
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)  # 支持视频播放
        self.browser.settings().setAttribute(self.browser.settings().PdfViewerEnabled, True)  # 支持PDF
        self.browser.settings().setAttribute(self.browser.settings().AutoLoadImages, True)  # 支持图片自动加载
        self.browser.settings().setAttribute(self.browser.settings().ShowScrollBars, True)  # 支持滚动滑轮

        self.url = ''
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(self.url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)

        # 添加导航栏
        self.navigation_bar = QToolBar('Navigation')
        self.navigation_bar.setMovable(False)
        self.navigation_bar.setIconSize(QSize(16, 16))
        # 添加导航栏到窗口中
        self.addToolBar(self.navigation_bar)

        # 添加前进、后退、刷新的按钮
        back_button = QAction(QIcon('./Images/back.png'), 'Back', self)
        next_button = QAction(QIcon('./Images/next.png'), 'Forward', self)
        reload_button = QAction(QIcon('./Images/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        reload_button.triggered.connect(self.browser.reload)

        # 将按钮添加到导航栏上
        self.navigation_bar.addAction(back_button)
        self.navigation_bar.addAction(next_button)
        self.navigation_bar.addAction(reload_button)

        # 添加URL地址栏
        self.urlbar = QLineEdit()
        # 让地址栏能响应回车按键信号
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.navigation_bar.addSeparator()
        self.navigation_bar.addWidget(self.urlbar)

        # 让浏览器相应url地址的变化
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        """让地址栏默认加URL头"""
        url = QUrl(self.urlbar.text())
        if url.scheme() == '':
            url.setScheme('http')
        self.browser.setUrl(url)

    def renew_urlbar(self, q):
        """将当前网页的链接更新到地址栏"""
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def on_changewebIndex(self, index):
        """改变网页索引的槽"""
        if index == 1:
            self.webIndex = 1
        elif index == 2:
            self.webIndex = 2
        elif index == 3:
            self.webIndex = 3
        elif index == 4:
            self.webIndex = 4
        elif index == 5:
            self.webIndex = 5

        if self.webIndex == 1:
            self.url = 'https://yz.chsi.com.cn/'
            self.browser.setUrl(QUrl(self.url))
            self.setCentralWidget(self.browser)
            self.show()
        elif self.webIndex == 2:
            self.url = 'http://bbs.kaoyan.com/'
            self.browser.setUrl(QUrl(self.url))
            self.setCentralWidget(self.browser)
            self.show()
        elif self.webIndex == 3:
            self.url = 'http://www.chinakaoyan.com/'
            self.browser.setUrl(QUrl(self.url))
            self.setCentralWidget(self.browser)
            self.show()
        elif self.webIndex == 4:
            self.url = 'https://kaoyan.eol.cn/'
            self.browser.setUrl(QUrl(self.url))
            self.setCentralWidget(self.browser)
            self.show()
        elif self.webIndex == 5:
            self.url = 'https://gfsoso.99lb.net/'
            self.browser.setUrl(QUrl(self.url))
            self.setCentralWidget(self.browser)
            self.show()

class WebEngineView(QWebEngineView):
    """重载creatWindow函数的类，实现二级网页跳转"""

    def createWindow(self, QWebEnginePage_WebWindowType):
        return self

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WebWindow()
    window.show()
    sys.exit(app.exec_())