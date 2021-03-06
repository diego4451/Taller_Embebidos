# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Access.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

def NtoM(num):
    if(num < 0):
        p = "-£"
        num *= -1
    else:
        p = "£"
    M = str(num%1000)
    num //= 1000
    while(num > 0):
        while((len(M)%3) != 0):
            M = "0" + M
        M = str(num%1000) + "," + M
        num //= 1000
    return p + M

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(10, 130, 41, 41))
        self.Button_1.setObjectName("Button_1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 50, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(50, 130, 41, 41))
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(90, 130, 41, 41))
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(10, 170, 41, 41))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(50, 170, 41, 41))
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(90, 170, 41, 41))
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(10, 210, 41, 41))
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(50, 210, 41, 41))
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(90, 210, 41, 41))
        self.Button_9.setObjectName("Button_9")
        self.Backspace = QtWidgets.QPushButton(self.centralwidget)
        self.Backspace.setGeometry(QtCore.QRect(130, 170, 41, 41))
        self.Backspace.setObjectName("Backspace")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(50, 250, 81, 41))
        self.Enter.setObjectName("Enter")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(10, 250, 41, 41))
        self.Button_0.setObjectName("Button_0")
        self.Deposit = QtWidgets.QPushButton(self.centralwidget)
        self.Deposit.setGeometry(QtCore.QRect(130, 250, 81, 41))
        self.Deposit.setObjectName("Deposit")
        self.Withdraw = QtWidgets.QPushButton(self.centralwidget)
        self.Withdraw.setGeometry(QtCore.QRect(130, 210, 81, 41))
        self.Withdraw.setObjectName("Withdraw")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 71, 51))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 10, 141, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 90, 141, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 71, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.balance = 143247
        self.change = 0
        self.string = NtoM(self.balance)
        self.textEdit_2.setPlainText(self.string)
        self.textEdit_3.setPlainText(self.string)
        self.string = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Account Access"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_1.clicked.connect(lambda: self.click(1))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.clicked.connect(lambda: self.click(2))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.clicked.connect(lambda: self.click(3))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.clicked.connect(lambda: self.click(4))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.clicked.connect(lambda: self.click(5))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.clicked.connect(lambda: self.click(6))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.clicked.connect(lambda: self.click(7))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.clicked.connect(lambda: self.click(8))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.clicked.connect(lambda: self.click(9))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.clicked.connect(lambda: self.click(0))
        self.Backspace.setText(_translate("MainWindow", "←"))
        self.Backspace.clicked.connect(self.backspace)
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Enter.clicked.connect(self.enter)
        self.Deposit.setText(_translate("MainWindow", "Deposit"))
        self.Deposit.clicked.connect(self.deposit)
        self.Withdraw.setText(_translate("MainWindow", "Withdraw"))
        self.Withdraw.clicked.connect(self.withdraw)

        self.label.setText(_translate("MainWindow", "Available\n"
" Balance:"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"text-align=right; -qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Change:"))
        self.label_3.setText(_translate("MainWindow", "Remaining\n"
"Balance:"))

    def click(self, x):
        if(self.change < 0):
            x *= -1
        self.change = 10*self.change + x
        self.string = NtoM(self.change)
        self.textEdit.setPlainText(self.string)
        self.textEdit_3.setPlainText(NtoM(self.balance + self.change))

    def backspace(self):
        self.string = self.string[0:-1]
        self.change //= 10
        self.textEdit.setPlainText(self.string)
        self.textEdit_3.setPlainText(NtoM(self.balance + self.change))

    def enter(self):
        self.balance += self.change
        self.textEdit_2.setPlainText(NtoM(self.balance))
        self.textEdit_3.setPlainText("")
        self.string = ""
        self.change = 0
        self.textEdit.setPlainText("£0")

    def deposit(self):
        if(self.change < 0):
            self.string = self.string[1:]
            self.textEdit.setPlainText(self.string)
            self.textEdit_3.setPlainText(NtoM(self.balance + self.change))
            self.change *= -1

    def withdraw(self):
        if(self.change > 0):
            self.string = "-" + self.string
            self.textEdit.setPlainText(self.string)
            self.textEdit_3.setPlainText(NtoM(self.balance + self.change))
            self.change *= -1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
