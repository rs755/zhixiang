import sys
from PyQt5 import QtWidgets
import gui
from function import *


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
        text = calculator(self.guanzhijing, self.guanzonggao, self.dsw, self.guan_paibu, self.yinshua, self.neika_geban, self.dianban_c)
        self.plainTextEdit.setText(text)

    def rbclicked(self):
        if self.buttonGroup_d.checkedButton() == self.radioButton_d1:
            self.guanzhijing = 65
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d2:
            self.guanzhijing = 60
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d3:
            self.guanzhijing = 52
        elif self.buttonGroup_d.checkedButton() == self.radioButton_d4:
            self.guanzhijing = int(self.lineEdit_d4.text())

        if self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guangaigao:
            self.guanzonggao = int(self.lineEdit_guangao.text()) + int(self.lineEdit_gaigao.text())
        elif self.buttonGroup_guangaigao.checkedButton() == self.radioButton_guanzonggao:
            self.guanzonggao = int(self.lineEdit_guanzonggao.text())

        if self.buttonGroup_dsw.checkedButton() == self.radioButton_shuangwa:
            self.dsw = 'sw'
        elif self.buttonGroup_dsw.checkedButton() == self.radioButton_danwa:
            self.dsw = 'dw'

        if self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p1:
            self.guan_paibu = [6, 4]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p2:
            self.guan_paibu = [4, 3]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p3:
            self.guan_paibu = [6, 5]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p4:
            self.guan_paibu = [5, 4]
        elif self.buttonGroup_guanpaibu.checkedButton() == self.radioButton_p5:
            self.guan_paibu = [int(self.lineEdit_p5h.text()), int(self.lineEdit_p5s.text())]

        if self.buttonGroup_yinshua.checkedButton() == self.radioButton_y1:
            self.yinshua = '水墨印'
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y2:
            self.yinshua = '彩印'
        elif self.buttonGroup_yinshua.checkedButton() == self.radioButton_y3:
            self.yinshua = self.lineEdit_y3.text()

        if self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n1:
            self.neika_geban = 'neika'
        elif self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n2:
            self.neika_geban = 'geban'
        elif self.buttonGroup_neika_geban.checkedButton() == self.radioButton_n3:
            self.neika_geban = 'no'

        if self.buttonGroup_dianban.checkedButton() == self.radioButton_n4:
            self.dianban_c = 1
        elif self.buttonGroup_dianban.checkedButton() == self.radioButton_n5:
            self.dianban_c = 2
        elif self.buttonGroup_dianban.checkedButton() == self.radioButton_n6:
            self.dianban_c = 0



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
