# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'polarix_gui2GizZZS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(694, 808)
        MainWindow.setMaximumSize(QSize(10000000, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(138, 226, 52, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(195, 248, 192, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush3 = QBrush(QColor(207, 231, 250, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        brush4 = QBrush(QColor(145, 145, 145, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush5 = QBrush(QColor(209, 247, 226, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.centralwidget.setPalette(palette1)
        self.timeandenergycollib = QTabWidget(self.centralwidget)
        self.timeandenergycollib.setObjectName(u"timeandenergycollib")
        self.timeandenergycollib.setGeometry(QRect(-10, 0, 701, 761))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        self.timeandenergycollib.setPalette(palette2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 570, 291, 141))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(110, 30, 113, 25))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 67, 17))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(110, 60, 113, 25))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 60, 81, 17))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 100, 201, 25))
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 561, 301))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 350, 301, 151))
        self.phas_min3 = QLineEdit(self.groupBox_3)
        self.phas_min3.setObjectName(u"phas_min3")
        self.phas_min3.setGeometry(QRect(30, 60, 41, 22))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 60, 31, 16))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 60, 41, 20))
        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(260, 60, 41, 22))
        self.time_colli = QPushButton(self.groupBox_3)
        self.time_colli.setObjectName(u"time_colli")
        self.time_colli.setGeometry(QRect(30, 100, 221, 21))
        font = QFont()
        font.setFamily(u"UnBatang")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.time_colli.setFont(font)
        self.time_colli.setStyleSheet(u"font: italic 11pt \"Ubuntu Mono\";\n"
"font: 75 italic 11pt \"UnBatang\";")
        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(160, 60, 60, 22))
        self.spinBox.setMinimum(-180)
        self.spinBox.setMaximum(180)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(86, 60, 71, 20))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(350, 350, 311, 161))
        palette3 = QPalette()
        brush6 = QBrush(QColor(130, 201, 252, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        self.groupBox_2.setPalette(palette3)
        self.groupBox_2.setAutoFillBackground(False)
        self.Energy_colli = QPushButton(self.groupBox_2)
        self.Energy_colli.setObjectName(u"Energy_colli")
        self.Energy_colli.setGeometry(QRect(60, 100, 201, 21))
        self.Energy_colli.setFont(font)
        self.Energy_colli.setAutoFillBackground(False)
        self.Energy_colli.setStyleSheet(u"font: italic 11pt \"Ubuntu Mono\";\n"
"font: 75 italic 11pt \"UnBatang\";")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(190, 110, 71, 16))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 21, 17))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 60, 41, 25))
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 60, 41, 25))
        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(160, 60, 60, 22))
        self.spinBox_2.setMinimum(-180)
        self.spinBox_2.setMaximum(180)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 60, 38, 17))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 60, 91, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        self.single_measur = QPushButton(self.tab)
        self.single_measur.setObjectName(u"single_measur")
        self.single_measur.setGeometry(QRect(190, 530, 281, 31))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 654, 241, 31))
        self.timeandenergycollib.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 80, 220, 40))
        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 150, 220, 40))
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(60, 230, 220, 40))
        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(320, 310, 220, 40))
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(320, 370, 220, 40))
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(320, 434, 220, 40))
        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(510, 110, 113, 25))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(406, 110, 71, 31))
        self.timeandenergycollib.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 694, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.timeandenergycollib.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"pulse duration measeremtn", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1st phase", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2nd phase", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"temporla measrement", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"time collibration", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.time_colli.setText(QCoreApplication.translate("MainWindow", u"do time collibration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TDS phase", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"energy collibration ", None))
        self.Energy_colli.setText(QCoreApplication.translate("MainWindow", u"measurement by Bending ", None))
        self.label_14.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"down", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Magnet current", None))
        self.single_measur.setText(QCoreApplication.translate("MainWindow", u"Do single measurment ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"online measurement", None))
        self.timeandenergycollib.setTabText(self.timeandenergycollib.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Time and Energy collibration", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"take background", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"collecting lasing on", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"collecting lasing off", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"analysing image", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"pulse reconstrction", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"saving data ", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"n shots", None))
        self.timeandenergycollib.setTabText(self.timeandenergycollib.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"pulse reconstruction", None))
    # retranslateUi

