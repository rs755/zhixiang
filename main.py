import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import gui
from function import *


guanzhijing, guanzhijing_o = 65, False
guanzonggao, guanzonggao_o = 290, False
dsw = 'sw'
guan_paibu, guan_paibu_o = [6, 4], False
yinshua, yinshua_o = '水墨印', False
neika_geban = 'neika'
dianban_c = 1


class MyWindow(gui.Ui_MainWindow):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.pushButton.clicked.connect(self.calculate)
        self.buttonGroup_d.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_guangaigao.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_dsw.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_guanpaibu.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_yinshua.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_neika_geban.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_dianban.buttonClicked.connect(self.rbclicked)

    def calculate(self):
        global guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c, guanzhijing_o, guanzonggao_o, guan_paibu_o, yinshua_o
        if guanzhijing_o:
            guanzhijing = int(self.lineEdit_d4.text())
        if guanzonggao_o == 'o1':
            guanzonggao = (int(self.lineEdit_guangao.text()) + int(self.lineEdit_gaigao.text()) - 7)
        if guanzonggao_o == 'o2':
            guanzonggao = int(self.lineEdit_guanzonggao.text())
        if guan_paibu_o:
            guan_paibu = [int(self.lineEdit_p5h.text()), int(self.lineEdit_p5s.text())]
        if yinshua_o:
            yinshua = self.lineEdit_y3.text()
        text = calculator(guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c)
        self.plainTextEdit.setPlainText(text)

    def rbclicked(self):
        global guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c, guanzhijing_o, guanzonggao_o, guan_paibu_o, yinshua_o
        if self.buttonGroup_d.checkedButton() == self.radioButton_d1:
            guanzhijing = 65
            guanzhijing_o = False
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d2:
            guanzhijing = 60
            guanzhijing_o = False
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d3:
            guanzhijing = 52
            guanzhijing_o = False
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d4:
            guanzhijing_o = True

        if self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guangaigao:
            guanzonggao_o = 'o1'
        elif self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guanzonggao:
            guanzonggao_o = 'o2'

        if self.buttonGroup_dsw.checkedButton() == self.radioButton_shuangwa:
            dsw = 'sw'
        elif self.buttonGroup_dsw.checkedButton() == self.radioButton_danwa:
            dsw = 'dw'

        if self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p1:
            guan_paibu = [6, 4]
            guan_paibu_o = False
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p2:
            guan_paibu = [4, 3]
            guan_paibu_o = False
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p3:
            guan_paibu = [6, 5]
            guan_paibu_o = False
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p4:
            guan_paibu = [5, 4]
            guan_paibu_o = False
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p5:
            guan_paibu_o = True

        if self.buttonGroup_yinshua.checkedButton() == self.radioButton_y1:
            yinshua = '水墨印'
            yinshua_o = False
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y2:
            yinshua = '彩印'
            yinshua_o = False
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y3:
            yinshua_o = True

        if self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n1:
            neika_geban = 'neika'
        elif self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n2:
            neika_geban = 'geban'
        elif self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n3:
            neika_geban = 'no'

        if self.buttonGroup_dianban.checkedButton() == self.radioButton_n4:
            dianban_c = 1
        elif self.buttonGroup_dianban.checkedButton() == self.radioButton_n5:
            dianban_c = 2
        elif self.buttonGroup_dianban.checkedButton() == self.radioButton_n6:
            dianban_c = 0



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
