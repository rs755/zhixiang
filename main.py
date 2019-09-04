import sys
from PyQt5 import QtWidgets
import gui
from function import *


class MyWindow(gui.Ui_MainWindow):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.pushButton.clicked.connect(self.calculate)
        self.buttonGroup.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_2.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_3.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_4.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_5.buttonClicked.connect(self.rbclicked)
        self.buttonGroup_6.buttonClicked.connect(self.rbclicked)

    def calculate(self):
        global guangao, gaigao
        guangao = int(self.lineEdit_4.text())
        gaigao = int(self.lineEdit_5.text())
        text = calculator(dsw, guanzhijing, guangao, gaigao, guan_heng_c, guan_shu_c, neika_heng_c, neika_shu_c, geban_c, dianban_c, yinshua)
        self.textBrowser.setText(text)

    def rbclicked(self):
        global guanzhijing, dsw, guan_heng_c, guan_shu_c, neika_heng_c, neika_shu_c, geban_c, dianban_c, yinshua
        if self.buttonGroup.checkedButton() == self.radioButton_12:
            guanzhijing = 65
        elif self.buttonGroup.checkedButton() == self.radioButton_13:
            guanzhijing = 60
        elif self.buttonGroup.checkedButton() == self.radioButton_15:
            guanzhijing = 52
        else:
            guanzhijing = int(self.lineEdit_3.text())

        if self.buttonGroup_2.checkedButton() == self.radioButton:
            dsw = 'sw'
        else:
            dsw = 'dw'

        if self.buttonGroup_3.checkedButton() == self.radioButton_3:
            guan_heng_c, guan_shu_c = 6, 4
        elif self.buttonGroup_3.checkedButton() == self.radioButton_4:
            guan_heng_c, guan_shu_c = 4, 3
        else:
            guan_heng_c, guan_shu_c = int(self.lineEdit.text()), int(self.lineEdit_2.text())

        if self.buttonGroup_4.checkedButton() == self.radioButton_6:
            neika_heng_c, neika_shu_c = guan_heng_c-1, guan_shu_c-1
            geban_c = 0
        elif self.buttonGroup_4.checkedButton() == self.radioButton_7:
            geban_c = guan_shu_c-1
            neika_heng_c, neika_shu_c = 0, 0
        else:
            neika_heng_c, neika_shu_c, geban_c = 0, 0, 0

        if self.buttonGroup_5.checkedButton() == self.radioButton_9:
            dianban_c = 1
        elif self.buttonGroup_5.checkedButton() == self.radioButton_10:
            dianban_c = 2
        else:
            dianban_c = 0

        if self.buttonGroup_6.checkedButton() == self.radioButton_16:
            yinshua = '水墨印'
            dsw += 's'
        elif self.buttonGroup_6.checkedButton() == self.radioButton_17:
            yinshua = '彩印'
            dsw += 'c'
        else:
            yinshua = self.lineEdit_6.text()
            dsw = 'o'


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
