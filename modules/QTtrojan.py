import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

form_class = uic.loadUiType("trojan.ui")[0]
print form_class

class TrojanWindow(QMainWindow, form_class):
    def __init__(self):
        super(QMainWindow,self).__init__()
        super(form_class, self).__init__()
        self.setupUi(self)
        self.connect(self.MakeTrojan_Button, SIGNAL("clicked()"), self.MakeTrojan_Clicked)
        self.connect(self.ExecuteTrojan_Button, SIGNAL("clicked()"), self.ExecuteTrojan_Clicked)
        self.clicked = 2
        self.nonclicked = 0

    def MakeTrojan_Clicked(self):
        Keylogger_Check = self.Keylogger_CheckBox.checkState()
        ScreenShot_Check = self.ScreenShot_CheckBox.checkState()
        TargetNum_Button = self.TargetNum_Button.toPlainText()
        if Keylogger_Check is self.clicked:
            MakeConfig(keylogger)
        if ScreenShot_Check is self.nonclicked:
            MakeConfig(ScreenShot)
        self.MakeRandomDirectory(TargetNum_Button)


    def ExecuteTrojan_Clicked(self):
        print 1
    def MakeRandomDirectory(self):

if __name__ == "__main__":
    trojan = QApplication(sys.argv)
    trojanWindow = TrojanWindow()
    trojanWindow.show()
    trojan.exec_()
