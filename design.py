# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 900)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, -10, 821, 651))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(11, 21, 107, 42))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(11, 69, 281, 411))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(430, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.browse = QtGui.QPushButton(self.frame)
        self.browse.setGeometry(QtCore.QRect(440, 160, 111, 41))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(310, 70, 361, 61))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(300, 240, 241, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(300, 290, 381, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(340, 320, 221, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(340, 340, 351, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(340, 360, 341, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(340, 380, 271, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(340, 400, 271, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(340, 420, 211, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 440, 341, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(340, 460, 331, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 520, 121, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(210, 520, 431, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.close = QtGui.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(538, 550, 151, 27))
        self.close.setObjectName(_fromUtf8("close"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuContact_Us = QtGui.QMenu(self.menubar)
        self.menuContact_Us.setObjectName(_fromUtf8("menuContact_Us"))
        self.menuContact_Us_2 = QtGui.QMenu(self.menubar)
        self.menuContact_Us_2.setObjectName(_fromUtf8("menuContact_Us_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionMin = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMin.setIcon(icon)
        self.actionMin.setObjectName(_fromUtf8("actionMin"))
        self.actionHttps_gitter_im_Automatic_leaf_infection_identification_Lobby = QtGui.QAction(MainWindow)
        self.actionHttps_gitter_im_Automatic_leaf_infection_identification_Lobby.setObjectName(_fromUtf8("actionHttps_gitter_im_Automatic_leaf_infection_identification_Lobby"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuContact_Us.addAction(self.actionHelp)
        self.menuContact_Us.addSeparator()
        self.menuContact_Us_2.addAction(self.actionHttps_gitter_im_Automatic_leaf_infection_identification_Lobby)
        self.menubar.addAction(self.menuContact_Us.menuAction())
        self.menubar.addAction(self.menuContact_Us_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">ABOUT</span></p></body></html>", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
, None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Interact</span></p></body></html>", None))
        self.browse.setText(_translate("MainWindow", "Browse", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic L\'; font-style:italic; color:#aa00ff;\">Input an image of leaf through the browse field to know the characteristics of leaf</span></p></body></html>", None))
        
        self.close.setText(_translate("MainWindow", "Close Application", None))
        # self.menuContact_Us.setTitle(_translate("MainWindow", "Menu", None))
        # self.menuContact_Us_2.setTitle(_translate("MainWindow", "Contact Us", None))
        self.actionMin.setText(_translate("MainWindow", "min", None))
        # self.actionHttps_gitter_im_Automatic_leaf_infection_identification_Lobby.setText(_translate("MainWindow", "https://gitter.im/Automatic-leaf-infection-identification/Lobby", None))
        # self.actionHelp.setText(_translate("MainWindow", "Help", None))

