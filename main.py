import sys
from PyQt5 import QtWidgets
import gui
from function import *


guanzhijing = 65
guanzonggao = 290
dsw = 'sw'
guan_paibu = [6, 4]
yinshua = '水墨印'
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
        text = calculator(guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c)
        self.plainTextEdit.setText(text)

    def rbclicked(self):
        global guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c
        if self.buttonGroup_d.checkedButton() == self.radioButton_d1:
            guanzhijing = 65
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d2:
            guanzhijing = 60
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d3:
            guanzhijing = 52
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d4:
            guanzhijing = int(self.lineEdit_d4.text())

        if self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guangaigao:
            guanzonggao = int(self.lineEdit_guangao.text()) + int(self.lineEdit_gaigao.text())
        elif self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guanzonggao:
            guanzonggao = int(self.lineEdit_guanzonggao.text())

        if self.buttonGroup_dsw.checkedButton() == self.radioButton_shuangwa:
            dsw = 'sw'
        elif self.buttonGroup_dsw.checkedButton() == self.radioButton_danwa:
            dsw = 'dw'

        if self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p1:
            guan_paibu = [6, 4]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p2:
            guan_paibu = [4, 3]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p3:
            guan_paibu = [6, 5]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p4:
            guan_paibu = [5, 4]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p5:
            guan_paibu = [int(self.lineEdit_p5h.text()), int(self.lineEdit_p5s.text())]

        if self.buttonGroup_yinshua.checkedButton() == self.radioButton_y1:
            yinshua = '水墨印'
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y2:
            yinshua = '彩印'
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y3:
            yinshua = self.lineEdit_y3.text()

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
