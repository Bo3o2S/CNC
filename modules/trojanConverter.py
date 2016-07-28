# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Github\CNC\modules\trojan.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Trojan_Attacker(object):
    def setupUi(self, Trojan_Attacker):
        Trojan_Attacker.setObjectName(_fromUtf8("Trojan_Attacker"))
        Trojan_Attacker.resize(454, 258)
        self.centralwidget = QtGui.QWidget(Trojan_Attacker)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 9, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(315, 39, 111, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 9pt \"ADMUI3Lg\";\n"
"font: 75 9pt \"ADMUI3Lg\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(315, 139, 111, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(145, 9, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(175, 29, 41, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(25, 79, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 100, 251, 101))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        Trojan_Attacker.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Trojan_Attacker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Trojan_Attacker.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Trojan_Attacker)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Trojan_Attacker.setStatusBar(self.statusbar)

        self.retranslateUi(Trojan_Attacker)
        QtCore.QMetaObject.connectSlotsByName(Trojan_Attacker)

    def retranslateUi(self, Trojan_Attacker):
        Trojan_Attacker.setWindowTitle(_translate("Trojan_Attacker", "MainWindow", None))
        self.label.setText(_translate("Trojan_Attacker", "<html><head/><body><p><span style=\" font-weight:600;\">Attack Method</span></p></body></html>", None))
        self.pushButton.setText(_translate("Trojan_Attacker", "Make Trojan", None))
        self.pushButton_2.setText(_translate("Trojan_Attacker", "Execute Trojan", None))
        self.label_2.setText(_translate("Trojan_Attacker", "<html><head/><body><p><span style=\" font-weight:600;\">Target Number</span></p></body></html>", None))
        self.label_3.setText(_translate("Trojan_Attacker", "<html><head/><body><p><span style=\" font-weight:600;\">Attack URL</span></p></body></html>", None))
        self.checkBox.setText(_translate("Trojan_Attacker", "Keylogger", None))
        self.checkBox_2.setText(_translate("Trojan_Attacker", "ScreenShot", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Trojan_Attacker = QtGui.QMainWindow()
    ui = Ui_Trojan_Attacker()
    ui.setupUi(Trojan_Attacker)
    Trojan_Attacker.show()
    sys.exit(app.exec_())

