# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.labelFrame = QFrame(self.mainFrame)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setGeometry(QRect(10, 10, 430, 111))
        self.labelFrame.setStyleSheet(u"QFrame {\n"
"	border: 0.5px solid rgb(210, 207, 212);\n"
"}")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.appLabel = QLabel(self.labelFrame)
        self.appLabel.setObjectName(u"appLabel")
        self.appLabel.setGeometry(QRect(70, 9, 300, 91))
        self.appLabel.setStyleSheet(u"QLabel {\n"
"	border: 0px;\n"
"}")
        self.appLabel.setPixmap(QPixmap(u"baleno.png"))
        self.appLabel.setAlignment(Qt.AlignCenter)
        self.inputFrame = QFrame(self.mainFrame)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setGeometry(QRect(13, 130, 430, 271))
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.inputFilterFrame = QFrame(self.inputFrame)
        self.inputFilterFrame.setObjectName(u"inputFilterFrame")
        self.inputFilterFrame.setGeometry(QRect(10, 10, 234, 40))
        self.inputFilterFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFilterFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.inputFilterFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.urlRadioButton = QRadioButton(self.inputFilterFrame)
        self.urlRadioButton.setObjectName(u"urlRadioButton")
        font = QFont()
        font.setFamily(u".AppleSystemUIFont")
        self.urlRadioButton.setFont(font)
        self.urlRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.urlRadioButton)

        self.fileRadioButton = QRadioButton(self.inputFilterFrame)
        self.fileRadioButton.setObjectName(u"fileRadioButton")

        self.horizontalLayout_2.addWidget(self.fileRadioButton)

        self.urlFrame = QFrame(self.inputFrame)
        self.urlFrame.setObjectName(u"urlFrame")
        self.urlFrame.setGeometry(QRect(10, 60, 411, 71))
        self.urlFrame.setFrameShape(QFrame.StyledPanel)
        self.urlFrame.setFrameShadow(QFrame.Raised)
        self.urlEdit = QLineEdit(self.urlFrame)
        self.urlEdit.setObjectName(u"urlEdit")
        self.urlEdit.setGeometry(QRect(10, 20, 391, 31))
        self.urlEdit.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 7px;\n"
"	border: 0.5px solid rgb(32, 32, 32);\n"
"}")
        self.fileFrame = QFrame(self.inputFrame)
        self.fileFrame.setObjectName(u"fileFrame")
        self.fileFrame.setGeometry(QRect(10, 140, 411, 121))
        self.fileFrame.setFrameShape(QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QFrame.Raised)
        self.fileFrame.setEnabled(False)
        self.fileOpenButton = QPushButton(self.fileFrame)
        self.fileOpenButton.setObjectName(u"fileOpenButton")
        self.fileOpenButton.setGeometry(QRect(140, 70, 113, 32))
        self.fileOpenButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(46, 112, 253);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(32, 32, 32);\n"
"}")
        self.fileLabel = QLabel(self.fileFrame)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setGeometry(QRect(100, 30, 201, 20))
        self.fileLabel.setStyleSheet(u"QLabel {\n"
"	border-bottom: 0.5px solid rgb(24, 24, 24);\n"
"}")
        self.fileLabel.setAlignment(Qt.AlignCenter)
        self.buttonFrame = QFrame(self.mainFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setGeometry(QRect(13, 417, 431, 181))
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.startButton = QPushButton(self.buttonFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(60, 37, 113, 71))
        self.startButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(46, 112, 253);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(32, 32, 32);\n"
"}")
        self.folderOpenButton = QPushButton(self.buttonFrame)
        self.folderOpenButton.setObjectName(u"folderOpenButton")
        self.folderOpenButton.setGeometry(QRect(260, 37, 113, 71))
        self.folderOpenButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(46, 112, 253);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(32, 32, 32);\n"
"}")
        self.progressBar = QProgressBar(self.buttonFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 153, 411, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 7px;\n"
"	color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(17, 81, 255);\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appLabel.setText("")
        self.urlRadioButton.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc77c \ub9c1\ud06c", None))
        self.fileRadioButton.setText(QCoreApplication.translate("MainWindow", u"\ub9c1\ud06c \ud30c\uc77c", None))
        self.urlEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ub9c1\ud06c", None))
        self.fileOpenButton.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5f4\uae30", None))
        self.fileLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#212121;\">\ud30c\uc77c\uba85</span></p></body></html>", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc9d1 \uc2dc\uc791", None))
        self.folderOpenButton.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
    # retranslateUi

