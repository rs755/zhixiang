# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 264, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_d1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_d1.setFont(font)
        self.radioButton_d1.setChecked(True)
        self.radioButton_d1.setObjectName("radioButton_d1")
        self.buttonGroup_d = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_d.setObjectName("buttonGroup_d")
        self.buttonGroup_d.addButton(self.radioButton_d1)
        self.horizontalLayout_5.addWidget(self.radioButton_d1)
        self.radioButton_d2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_d2.setFont(font)
        self.radioButton_d2.setObjectName("radioButton_d2")
        self.buttonGroup_d.addButton(self.radioButton_d2)
        self.horizontalLayout_5.addWidget(self.radioButton_d2)
        self.radioButton_d3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_d3.setFont(font)
        self.radioButton_d3.setObjectName("radioButton_d3")
        self.buttonGroup_d.addButton(self.radioButton_d3)
        self.horizontalLayout_5.addWidget(self.radioButton_d3)
        self.radioButton_d4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_d4.setText("")
        self.radioButton_d4.setObjectName("radioButton_d4")
        self.buttonGroup_d.addButton(self.radioButton_d4)
        self.horizontalLayout_5.addWidget(self.radioButton_d4)
        self.lineEdit_d4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_d4.setFont(font)
        self.lineEdit_d4.setText("")
        self.lineEdit_d4.setFrame(True)
        self.lineEdit_d4.setObjectName("lineEdit_d4")
        self.horizontalLayout_5.addWidget(self.lineEdit_d4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_guangaigao = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_guangaigao.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_guangaigao.setFont(font)
        self.radioButton_guangaigao.setText("")
        self.radioButton_guangaigao.setChecked(True)
        self.radioButton_guangaigao.setObjectName("radioButton_guangaigao")
        self.buttonGroup_guangaigao = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_guangaigao.setObjectName("buttonGroup_guangaigao")
        self.buttonGroup_guangaigao.addButton(self.radioButton_guangaigao)
        self.horizontalLayout_6.addWidget(self.radioButton_guangaigao)
        self.lineEdit_guangao = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_guangao.setFont(font)
        self.lineEdit_guangao.setStatusTip("")
        self.lineEdit_guangao.setWhatsThis("")
        self.lineEdit_guangao.setText("")
        self.lineEdit_guangao.setFrame(True)
        self.lineEdit_guangao.setObjectName("lineEdit_guangao")
        self.horizontalLayout_6.addWidget(self.lineEdit_guangao)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_gaigao = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_gaigao.setFont(font)
        self.lineEdit_gaigao.setText("")
        self.lineEdit_gaigao.setObjectName("lineEdit_gaigao")
        self.horizontalLayout_6.addWidget(self.lineEdit_gaigao)
        self.radioButton_guanzonggao = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_guanzonggao.setText("")
        self.radioButton_guanzonggao.setChecked(False)
        self.radioButton_guanzonggao.setObjectName("radioButton_guanzonggao")
        self.buttonGroup_guangaigao.addButton(self.radioButton_guanzonggao)
        self.horizontalLayout_6.addWidget(self.radioButton_guanzonggao)
        self.lineEdit_guanzonggao = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_guanzonggao.setFont(font)
        self.lineEdit_guanzonggao.setText("")
        self.lineEdit_guanzonggao.setObjectName("lineEdit_guanzonggao")
        self.horizontalLayout_6.addWidget(self.lineEdit_guanzonggao)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_shuangwa = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_shuangwa.setFont(font)
        self.radioButton_shuangwa.setChecked(True)
        self.radioButton_shuangwa.setObjectName("radioButton_shuangwa")
        self.buttonGroup_dsw = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_dsw.setObjectName("buttonGroup_dsw")
        self.buttonGroup_dsw.addButton(self.radioButton_shuangwa)
        self.horizontalLayout.addWidget(self.radioButton_shuangwa)
        self.radioButton_danwa = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_danwa.setFont(font)
        self.radioButton_danwa.setObjectName("radioButton_danwa")
        self.buttonGroup_dsw.addButton(self.radioButton_danwa)
        self.horizontalLayout.addWidget(self.radioButton_danwa)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_p1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_p1.setFont(font)
        self.radioButton_p1.setChecked(True)
        self.radioButton_p1.setObjectName("radioButton_p1")
        self.buttonGroup_guanpaibu = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_guanpaibu.setObjectName("buttonGroup_guanpaibu")
        self.buttonGroup_guanpaibu.addButton(self.radioButton_p1)
        self.horizontalLayout_2.addWidget(self.radioButton_p1)
        self.radioButton_p2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_p2.setFont(font)
        self.radioButton_p2.setObjectName("radioButton_p2")
        self.buttonGroup_guanpaibu.addButton(self.radioButton_p2)
        self.horizontalLayout_2.addWidget(self.radioButton_p2)
        self.radioButton_p3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_p3.setFont(font)
        self.radioButton_p3.setObjectName("radioButton_p3")
        self.buttonGroup_guanpaibu.addButton(self.radioButton_p3)
        self.horizontalLayout_2.addWidget(self.radioButton_p3)
        self.radioButton_p4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.radioButton_p4.setFont(font)
        self.radioButton_p4.setObjectName("radioButton_p4")
        self.buttonGroup_guanpaibu.addButton(self.radioButton_p4)
        self.horizontalLayout_2.addWidget(self.radioButton_p4)
        self.radioButton_p5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_p5.setText("")
        self.radioButton_p5.setObjectName("radioButton_p5")
        self.buttonGroup_guanpaibu.addButton(self.radioButton_p5)
        self.horizontalLayout_2.addWidget(self.radioButton_p5)
        self.lineEdit_p5h = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_p5h.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_p5h.setFont(font)
        self.lineEdit_p5h.setText("")
        self.lineEdit_p5h.setFrame(True)
        self.lineEdit_p5h.setObjectName("lineEdit_p5h")
        self.horizontalLayout_2.addWidget(self.lineEdit_p5h)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_p5s = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_p5s.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_p5s.setFont(font)
        self.lineEdit_p5s.setObjectName("lineEdit_p5s")
        self.horizontalLayout_2.addWidget(self.lineEdit_p5s)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_y1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_y1.setFont(font)
        self.radioButton_y1.setChecked(True)
        self.radioButton_y1.setObjectName("radioButton_y1")
        self.buttonGroup_yinshua = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_yinshua.setObjectName("buttonGroup_yinshua")
        self.buttonGroup_yinshua.addButton(self.radioButton_y1)
        self.horizontalLayout_7.addWidget(self.radioButton_y1)
        self.radioButton_y2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_y2.setFont(font)
        self.radioButton_y2.setObjectName("radioButton_y2")
        self.buttonGroup_yinshua.addButton(self.radioButton_y2)
        self.horizontalLayout_7.addWidget(self.radioButton_y2)
        self.radioButton_y3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_y3.setFont(font)
        self.radioButton_y3.setText("")
        self.radioButton_y3.setObjectName("radioButton_y3")
        self.buttonGroup_yinshua.addButton(self.radioButton_y3)
        self.horizontalLayout_7.addWidget(self.radioButton_y3)
        self.lineEdit_y3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_y3.setFont(font)
        self.lineEdit_y3.setText("")
        self.lineEdit_y3.setFrame(True)
        self.lineEdit_y3.setObjectName("lineEdit_y3")
        self.horizontalLayout_7.addWidget(self.lineEdit_y3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_n1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n1.setFont(font)
        self.radioButton_n1.setChecked(True)
        self.radioButton_n1.setObjectName("radioButton_n1")
        self.buttonGroup_neika_geban = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_neika_geban.setObjectName("buttonGroup_neika_geban")
        self.buttonGroup_neika_geban.addButton(self.radioButton_n1)
        self.horizontalLayout_3.addWidget(self.radioButton_n1)
        self.radioButton_n2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n2.setFont(font)
        self.radioButton_n2.setObjectName("radioButton_n2")
        self.buttonGroup_neika_geban.addButton(self.radioButton_n2)
        self.horizontalLayout_3.addWidget(self.radioButton_n2)
        self.radioButton_n3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n3.setFont(font)
        self.radioButton_n3.setObjectName("radioButton_n3")
        self.buttonGroup_neika_geban.addButton(self.radioButton_n3)
        self.horizontalLayout_3.addWidget(self.radioButton_n3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_n4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n4.setFont(font)
        self.radioButton_n4.setChecked(True)
        self.radioButton_n4.setObjectName("radioButton_n4")
        self.buttonGroup_dianban = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_dianban.setObjectName("buttonGroup_dianban")
        self.buttonGroup_dianban.addButton(self.radioButton_n4)
        self.horizontalLayout_4.addWidget(self.radioButton_n4)
        self.radioButton_n5 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n5.setFont(font)
        self.radioButton_n5.setObjectName("radioButton_n5")
        self.buttonGroup_dianban.addButton(self.radioButton_n5)
        self.horizontalLayout_4.addWidget(self.radioButton_n5)
        self.radioButton_n6 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_n6.setFont(font)
        self.radioButton_n6.setObjectName("radioButton_n6")
        self.buttonGroup_dianban.addButton(self.radioButton_n6)
        self.horizontalLayout_4.addWidget(self.radioButton_n6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "纸箱规格计算 v2.0"))
        self.radioButton_d1.setText(_translate("MainWindow", "Ø65"))
        self.radioButton_d2.setText(_translate("MainWindow", "Ø60"))
        self.radioButton_d3.setText(_translate("MainWindow", "Ø52"))
        self.radioButton_guangaigao.setToolTip(_translate("MainWindow", "罐盖高"))
        self.lineEdit_guangao.setToolTip(_translate("MainWindow", "罐高"))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.lineEdit_gaigao.setToolTip(_translate("MainWindow", "盖高"))
        self.lineEdit_guanzonggao.setToolTip(_translate("MainWindow", "总高"))
        self.radioButton_shuangwa.setText(_translate("MainWindow", "双瓦"))
        self.radioButton_danwa.setText(_translate("MainWindow", "单瓦"))
        self.radioButton_p1.setText(_translate("MainWindow", "24"))
        self.radioButton_p2.setText(_translate("MainWindow", "12"))
        self.radioButton_p3.setText(_translate("MainWindow", "30"))
        self.radioButton_p4.setText(_translate("MainWindow", "20"))
        self.label.setText(_translate("MainWindow", "x"))
        self.radioButton_y1.setText(_translate("MainWindow", "水墨印"))
        self.radioButton_y2.setText(_translate("MainWindow", "彩印"))
        self.radioButton_n1.setText(_translate("MainWindow", "内卡"))
        self.radioButton_n2.setText(_translate("MainWindow", "隔板"))
        self.radioButton_n3.setText(_translate("MainWindow", "无"))
        self.radioButton_n4.setText(_translate("MainWindow", "下垫板"))
        self.radioButton_n5.setText(_translate("MainWindow", "上下垫板"))
        self.radioButton_n6.setText(_translate("MainWindow", "无"))
        self.pushButton.setText(_translate("MainWindow", "计算"))

