# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reserve.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReserveWindow(object):
    def setupUi(self, ReserveWindow):
        ReserveWindow.setObjectName("ReserveWindow")
        ReserveWindow.resize(480, 800)
        ReserveWindow.setMinimumSize(QtCore.QSize(480, 800))
        ReserveWindow.setMaximumSize(QtCore.QSize(480, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReserveWindow.setWindowIcon(icon)
        ReserveWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(47, 79, 79);")
        self.frame_top = QtWidgets.QFrame(ReserveWindow)
        self.frame_top.setGeometry(QtCore.QRect(0, 0, 480, 50))
        self.frame_top.setStyleSheet("background: rgb(205, 104, 57)")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_back.setGeometry(QtCore.QRect(430, 0, 50, 50))
        self.pushButton_back.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_back.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    background: url(:/ui_back/Images/ui_back.png)\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.pushButton_back.setText("")
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_reserve = QtWidgets.QLabel(self.frame_top)
        self.label_reserve.setGeometry(QtCore.QRect(180, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华光综艺_CNKI")
        font.setPointSize(16)
        self.label_reserve.setFont(font)
        self.label_reserve.setObjectName("label_reserve")
        self.frame_success = QtWidgets.QFrame(self.frame_top)
        self.frame_success.setGeometry(QtCore.QRect(10, 10, 450, 30))
        self.frame_success.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_success.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 5px;")
        self.frame_success.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_success.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_success.setObjectName("frame_success")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_success)
        self.horizontalLayout_4.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_success = QtWidgets.QLabel(self.frame_success)
        font = QtGui.QFont()
        font.setFamily("华光综艺_CNKI")
        font.setPointSize(10)
        self.label_success.setFont(font)
        self.label_success.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_success.setAlignment(QtCore.Qt.AlignCenter)
        self.label_success.setObjectName("label_success")
        self.horizontalLayout_4.addWidget(self.label_success)
        self.pushButton_close_2 = QtWidgets.QPushButton(self.frame_success)
        self.pushButton_close_2.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close_2.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;    \n"
"    background-image: url(:/Close/Images/close.png);\n"
"    background-position: center;    \n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);    \n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.pushButton_close_2.setText("")
        self.pushButton_close_2.setObjectName("pushButton_close_2")
        self.horizontalLayout_4.addWidget(self.pushButton_close_2)
        self.frame_manual = QtWidgets.QFrame(ReserveWindow)
        self.frame_manual.setGeometry(QtCore.QRect(0, 50, 480, 30))
        self.frame_manual.setMinimumSize(QtCore.QSize(480, 30))
        self.frame_manual.setMaximumSize(QtCore.QSize(480, 30))
        self.frame_manual.setStyleSheet("background:rgb(51,51,51);")
        self.frame_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_manual.setObjectName("frame_manual")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_manual)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_manual = QtWidgets.QLabel(self.frame_manual)
        font = QtGui.QFont()
        font.setFamily("华光粗黑_CNKI")
        font.setPointSize(12)
        self.label_manual.setFont(font)
        self.label_manual.setObjectName("label_manual")
        self.horizontalLayout_20.addWidget(self.label_manual)
        self.frame_auto = QtWidgets.QFrame(ReserveWindow)
        self.frame_auto.setGeometry(QtCore.QRect(0, 370, 480, 30))
        self.frame_auto.setMinimumSize(QtCore.QSize(480, 30))
        self.frame_auto.setMaximumSize(QtCore.QSize(480, 30))
        self.frame_auto.setStyleSheet("background:rgb(51,51,51);")
        self.frame_auto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_auto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_auto.setObjectName("frame_auto")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_auto)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_auto = QtWidgets.QLabel(self.frame_auto)
        font = QtGui.QFont()
        font.setFamily("华光粗黑_CNKI")
        font.setPointSize(12)
        self.label_auto.setFont(font)
        self.label_auto.setObjectName("label_auto")
        self.horizontalLayout_21.addWidget(self.label_auto)
        self.frame_order = QtWidgets.QFrame(ReserveWindow)
        self.frame_order.setGeometry(QtCore.QRect(0, 590, 480, 30))
        self.frame_order.setMinimumSize(QtCore.QSize(480, 30))
        self.frame_order.setMaximumSize(QtCore.QSize(480, 30))
        self.frame_order.setStyleSheet("background:rgb(51,51,51);")
        self.frame_order.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_order.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_order.setObjectName("frame_order")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_order)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_order = QtWidgets.QLabel(self.frame_order)
        font = QtGui.QFont()
        font.setFamily("华光粗黑_CNKI")
        font.setPointSize(12)
        self.label_order.setFont(font)
        self.label_order.setObjectName("label_order")
        self.horizontalLayout_22.addWidget(self.label_order)
        self.frame_manual_content = QtWidgets.QFrame(ReserveWindow)
        self.frame_manual_content.setGeometry(QtCore.QRect(0, 80, 480, 290))
        self.frame_manual_content.setMinimumSize(QtCore.QSize(480, 290))
        self.frame_manual_content.setMaximumSize(QtCore.QSize(480, 290))
        self.frame_manual_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_manual_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_manual_content.setObjectName("frame_manual_content")
        self.layoutWidget = QtWidgets.QWidget(self.frame_manual_content)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 302, 258))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_lobby3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_lobby3.setMinimumSize(QtCore.QSize(300, 70))
        self.pushButton_lobby3.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(26)
        self.pushButton_lobby3.setFont(font)
        self.pushButton_lobby3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 30px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_lobby3.setObjectName("pushButton_lobby3")
        self.gridLayout.addWidget(self.pushButton_lobby3, 2, 0, 1, 1)
        self.pushButton_lobby1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_lobby1.setMinimumSize(QtCore.QSize(300, 70))
        self.pushButton_lobby1.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(26)
        self.pushButton_lobby1.setFont(font)
        self.pushButton_lobby1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 30px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_lobby1.setObjectName("pushButton_lobby1")
        self.gridLayout.addWidget(self.pushButton_lobby1, 0, 0, 1, 1)
        self.pushButton_lobby2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_lobby2.setMinimumSize(QtCore.QSize(300, 70))
        self.pushButton_lobby2.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(26)
        self.pushButton_lobby2.setFont(font)
        self.pushButton_lobby2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 30px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_lobby2.setObjectName("pushButton_lobby2")
        self.gridLayout.addWidget(self.pushButton_lobby2, 1, 0, 1, 1)
        self.frame_auto_content = QtWidgets.QFrame(ReserveWindow)
        self.frame_auto_content.setGeometry(QtCore.QRect(0, 400, 480, 190))
        self.frame_auto_content.setMinimumSize(QtCore.QSize(480, 190))
        self.frame_auto_content.setMaximumSize(QtCore.QSize(480, 190))
        self.frame_auto_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_auto_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_auto_content.setObjectName("frame_auto_content")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_auto_content)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 461, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("华光粗黑_CNKI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_normal_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_normal_1.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_normal_1.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_normal_1.setFont(font)
        self.pushButton_normal_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_normal_1.setObjectName("pushButton_normal_1")
        self.horizontalLayout.addWidget(self.pushButton_normal_1)
        self.pushButton_normal_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_normal_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_normal_2.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_normal_2.setFont(font)
        self.pushButton_normal_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_normal_2.setObjectName("pushButton_normal_2")
        self.horizontalLayout.addWidget(self.pushButton_normal_2)
        self.pushButton_normal_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_normal_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_normal_3.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_normal_3.setFont(font)
        self.pushButton_normal_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_normal_3.setObjectName("pushButton_normal_3")
        self.horizontalLayout.addWidget(self.pushButton_normal_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("华光粗黑_CNKI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_continu_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_continu_1.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_continu_1.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_continu_1.setFont(font)
        self.pushButton_continu_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_continu_1.setObjectName("pushButton_continu_1")
        self.horizontalLayout_2.addWidget(self.pushButton_continu_1)
        self.pushButton_continu_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_continu_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_continu_2.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_continu_2.setFont(font)
        self.pushButton_continu_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_continu_2.setObjectName("pushButton_continu_2")
        self.horizontalLayout_2.addWidget(self.pushButton_continu_2)
        self.pushButton_continu_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_continu_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_continu_3.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(11)
        self.pushButton_continu_3.setFont(font)
        self.pushButton_continu_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_continu_3.setObjectName("pushButton_continu_3")
        self.horizontalLayout_2.addWidget(self.pushButton_continu_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame_order_content = QtWidgets.QFrame(ReserveWindow)
        self.frame_order_content.setGeometry(QtCore.QRect(0, 620, 480, 180))
        self.frame_order_content.setMinimumSize(QtCore.QSize(480, 180))
        self.frame_order_content.setMaximumSize(QtCore.QSize(480, 180))
        self.frame_order_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_order_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_order_content.setObjectName("frame_order_content")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_order_content)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 10, 311, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_normal = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_normal.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_normal.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(18)
        self.pushButton_normal.setFont(font)
        self.pushButton_normal.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_normal.setObjectName("pushButton_normal")
        self.gridLayout_3.addWidget(self.pushButton_normal, 0, 0, 1, 1)
        self.pushButton_break = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_break.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_break.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(18)
        self.pushButton_break.setFont(font)
        self.pushButton_break.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_break.setObjectName("pushButton_break")
        self.gridLayout_3.addWidget(self.pushButton_break, 0, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(18)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 104, 137);\n"
"    border-radius: 20px;\n"
"    border: 10px solid rgb(205, 16, 118);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 10px solid rgb(255, 255, 0);\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_3.addWidget(self.pushButton_cancel, 1, 0, 1, 1)

        """自定义操作"""
        self.frame_success.setVisible(False)
        self.pushButton_close_2.clicked.connect(lambda: self.frame_success.hide())  # 点X取消成功提示

        self.retranslateUi(ReserveWindow)
        QtCore.QMetaObject.connectSlotsByName(ReserveWindow)

    def retranslateUi(self, ReserveWindow):
        _translate = QtCore.QCoreApplication.translate
        ReserveWindow.setWindowTitle(_translate("ReserveWindow", "cqnu_spider"))
        self.label_reserve.setText(_translate("ReserveWindow", "梦厅预约"))
        self.label_success.setText(_translate("ReserveWindow", "       预定成功！！！"))
        self.label_manual.setText(_translate("ReserveWindow", "    自主预定："))
        self.label_auto.setText(_translate("ReserveWindow", "    自动预定（三天后）："))
        self.label_order.setText(_translate("ReserveWindow", "    我的订单："))
        self.pushButton_lobby3.setText(_translate("ReserveWindow", "梦三厅"))
        self.pushButton_lobby1.setText(_translate("ReserveWindow", "梦一厅"))
        self.pushButton_lobby2.setText(_translate("ReserveWindow", "梦二厅"))
        self.label.setText(_translate("ReserveWindow", "普通预定："))
        self.pushButton_normal_1.setText(_translate("ReserveWindow", "梦一厅"))
        self.pushButton_normal_2.setText(_translate("ReserveWindow", "梦二厅"))
        self.pushButton_normal_3.setText(_translate("ReserveWindow", "梦三厅"))
        self.label_2.setText(_translate("ReserveWindow", "连坐预定："))
        self.pushButton_continu_1.setText(_translate("ReserveWindow", "梦一厅"))
        self.pushButton_continu_2.setText(_translate("ReserveWindow", "梦二厅"))
        self.pushButton_continu_3.setText(_translate("ReserveWindow", "梦三厅"))
        self.pushButton_normal.setText(_translate("ReserveWindow", "正常订单"))
        self.pushButton_break.setText(_translate("ReserveWindow", "违约订单"))
        self.pushButton_cancel.setText(_translate("ReserveWindow", "取消订单"))
import ui_rc