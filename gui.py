# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main
class Ui_RunWindow(object):
    def setupUi(self, RunWindow):
        RunWindow.setObjectName("RunWindow")
        RunWindow.resize(1792, 982)
        RunWindow.setAutoFillBackground(True)
        self.groupBox = QtWidgets.QGroupBox(RunWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 931, 631))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330, 911, 271))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(80, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 70, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(2, "")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(320, 50, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(320, 70, 161, 21))
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(550, 50, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(160, 140, 31, 16))
        self.label_14.setObjectName("label_14")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 160, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(2, "")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(280, 160, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(2, "")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(290, 140, 31, 16))
        self.label_15.setObjectName("label_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 160, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 240, 91, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(430, 10, 111, 16))
        self.label_29.setObjectName("label_29")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_23.setGeometry(QtCore.QRect(230, 240, 91, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 240, 91, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(350, 110, 31, 16))
        self.label_32.setObjectName("label_32")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 70, 161, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 461, 311))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(170, 10, 111, 16))
        self.label.setObjectName("label")
        self.RunListTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.RunListTable.setGeometry(QtCore.QRect(10, 50, 371, 151))
        self.RunListTable.setColumnCount(3)
        self.RunListTable.setObjectName("RunListTable")
        self.RunListTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable.setItem(2, 1, item)
        self.RunListTable.horizontalHeader().setDefaultSectionSize(117)
        self.Add = QtWidgets.QPushButton(self.groupBox_3)
        self.Add.setGeometry(QtCore.QRect(300, 210, 75, 23))
        self.Add.setObjectName("Add")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(260, 80, 25, 19))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/play.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/play.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_4.setGeometry(QtCore.QRect(300, 80, 25, 19))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/pause.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/pause.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_5.setGeometry(QtCore.QRect(340, 80, 25, 19))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/stop.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/stop.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_6.setGeometry(QtCore.QRect(340, 110, 25, 19))
        self.toolButton_6.setIcon(icon2)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_2.setGeometry(QtCore.QRect(260, 110, 25, 19))
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_7.setGeometry(QtCore.QRect(300, 110, 25, 19))
        self.toolButton_7.setIcon(icon1)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_8.setGeometry(QtCore.QRect(340, 140, 25, 19))
        self.toolButton_8.setIcon(icon2)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_3.setGeometry(QtCore.QRect(260, 140, 25, 19))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_9 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_9.setGeometry(QtCore.QRect(300, 140, 25, 19))
        self.toolButton_9.setIcon(icon1)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_10.setGeometry(QtCore.QRect(300, 170, 25, 19))
        self.toolButton_10.setIcon(icon1)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_11.setGeometry(QtCore.QRect(260, 170, 25, 19))
        self.toolButton_11.setIcon(icon)
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_12.setGeometry(QtCore.QRect(340, 170, 25, 19))
        self.toolButton_12.setIcon(icon2)
        self.toolButton_12.setObjectName("toolButton_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(480, 10, 441, 311))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 311, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(50, 110, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 151, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(50, 170, 71, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(220, 160, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(380, 160, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(200, 190, 21, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(50, 230, 141, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 270, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_4.clicked.connect(lambda: main.saveConfigurationRun(self))
        self.textEdit_12 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_12.setGeometry(QtCore.QRect(220, 40, 151, 21))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_13.setGeometry(QtCore.QRect(220, 70, 151, 21))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_14.setGeometry(QtCore.QRect(220, 100, 151, 21))
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_15.setGeometry(QtCore.QRect(220, 130, 151, 21))
        self.textEdit_15.setObjectName("textEdit_15")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_22.setGeometry(QtCore.QRect(360, 230, 71, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.textEdit_16 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_16.setGeometry(QtCore.QRect(200, 230, 151, 21))
        self.textEdit_16.setObjectName("textEdit_16")
        self.groupBox_6 = QtWidgets.QGroupBox(RunWindow)
        self.groupBox_6.setGeometry(QtCore.QRect(940, 10, 851, 961))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 831, 311))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.RunListTable_2 = QtWidgets.QTableWidget(self.groupBox_7)
        self.RunListTable_2.setGeometry(QtCore.QRect(220, 40, 361, 181))
        self.RunListTable_2.setColumnCount(3)
        self.RunListTable_2.setObjectName("RunListTable_2")
        self.RunListTable_2.setRowCount(5)
        self.pushButton_4.clicked.connect(lambda: main.saveConfigurationRun(self))
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RunListTable_2.setItem(4, 0, item)
        self.RunListTable_2.horizontalHeader().setDefaultSectionSize(117)
        self.label_30 = QtWidgets.QLabel(self.groupBox_7)
        self.label_30.setGeometry(QtCore.QRect(370, 20, 111, 16))
        self.label_30.setObjectName("label_30")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_9.setGeometry(QtCore.QRect(460, 60, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_10.setGeometry(QtCore.QRect(460, 90, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 120, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 150, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 180, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_20.setGeometry(QtCore.QRect(250, 920, 113, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_21.setGeometry(QtCore.QRect(440, 920, 113, 32))
        self.pushButton_21.setObjectName("pushButton_21")
        #self.pushButton_21.clicked.connect(self.updateToolListAddedTool)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 330, 391, 581))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_21 = QtWidgets.QLabel(self.groupBox_9)
        self.label_21.setGeometry(QtCore.QRect(140, 10, 151, 16))
        self.label_21.setObjectName("label_21")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 90, 151, 21))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_22 = QtWidgets.QLabel(self.groupBox_9)
        self.label_22.setGeometry(QtCore.QRect(160, 60, 81, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_9)
        self.label_23.setGeometry(QtCore.QRect(140, 120, 131, 16))
        self.label_23.setObjectName("label_23")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_7.setGeometry(QtCore.QRect(120, 150, 151, 21))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_24 = QtWidgets.QLabel(self.groupBox_9)
        self.label_24.setGeometry(QtCore.QRect(160, 180, 81, 16))
        self.label_24.setObjectName("label_24")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_8.setGeometry(QtCore.QRect(120, 210, 151, 21))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setGeometry(QtCore.QRect(130, 240, 131, 16))
        self.label_25.setObjectName("label_25")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_9.setGeometry(QtCore.QRect(120, 270, 151, 21))
        self.textEdit_9.setObjectName("textEdit_9")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 270, 71, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_17.setGeometry(QtCore.QRect(290, 210, 71, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        self.label_26.setGeometry(QtCore.QRect(120, 300, 161, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setGeometry(QtCore.QRect(180, 380, 60, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_9)
        self.label_28.setGeometry(QtCore.QRect(130, 420, 141, 16))
        self.label_28.setObjectName("label_28")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_10.setGeometry(QtCore.QRect(120, 460, 151, 21))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_11.setGeometry(QtCore.QRect(120, 330, 151, 21))
        self.textEdit_11.setObjectName("textEdit_11")
        self.pushButton_21.clicked.connect(lambda: main.saveToolSpecification(self))  
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_18.setGeometry(QtCore.QRect(290, 320, 71, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 450, 71, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_10.setGeometry(QtCore.QRect(410, 330, 431, 581))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 120, 104, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_16 = QtWidgets.QLabel(self.groupBox_10)
        self.label_16.setGeometry(QtCore.QRect(170, 100, 131, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_10)
        self.label_17.setGeometry(QtCore.QRect(170, 150, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_10)
        self.label_18.setGeometry(QtCore.QRect(170, 200, 61, 16))
        self.label_18.setObjectName("label_18")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_14.setGeometry(QtCore.QRect(180, 270, 81, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 340, 361, 81))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_19 = QtWidgets.QLabel(self.groupBox_10)
        self.label_19.setGeometry(QtCore.QRect(40, 310, 181, 16))
        self.label_19.setObjectName("label_19")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_6.setGeometry(QtCore.QRect(170, 170, 104, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_31 = QtWidgets.QLabel(self.groupBox_10)
        self.label_31.setGeometry(QtCore.QRect(170, 50, 131, 16))
        self.label_31.setObjectName("label_31")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_15.setGeometry(QtCore.QRect(170, 440, 113, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(150, 10, 151, 16))
        self.label_20.setObjectName("label_20")
        self.textEdit_17 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_17.setGeometry(QtCore.QRect(170, 220, 101, 21))
        self.textEdit_17.setObjectName("textEdit_17")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_7.setGeometry(QtCore.QRect(170, 70, 104, 26))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(RunWindow)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 640, 931, 331))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(60, 10, 781, 131))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_4)
        self.tabWidget.setGeometry(QtCore.QRect(180, 160, 491, 101))
        self.tabWidget.setObjectName("tabWidget")
        self.scan_1 = QtWidgets.QWidget()
        self.scan_1.setObjectName("scan_1")
        self.tabWidget.addTab(self.scan_1, "")
        self.scan_2 = QtWidgets.QWidget()
        self.scan_2.setObjectName("scan_2")
        self.tabWidget.addTab(self.scan_2, "")

        self.retranslateUi(RunWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RunWindow)

    def retranslateUi(self, RunWindow):
        _translate = QtCore.QCoreApplication.translate
        RunWindow.setWindowTitle(_translate("RunWindow", "Form"))
        self.label_10.setText(_translate("RunWindow", "Report Name"))
        self.comboBox_2.setItemText(0, _translate("RunWindow", "Test"))
        self.comboBox_2.setItemText(1, _translate("RunWindow", "Test1"))
        self.label_13.setText(_translate("RunWindow", "Report Description"))
        self.label_11.setText(_translate("RunWindow", "Run"))
        self.label_14.setText(_translate("RunWindow", "Run"))
        self.comboBox_3.setItemText(0, _translate("RunWindow", "Test"))
        self.comboBox_3.setItemText(1, _translate("RunWindow", "Test1"))
        self.comboBox_4.setItemText(0, _translate("RunWindow", "Test"))
        self.comboBox_4.setItemText(1, _translate("RunWindow", "Test1"))
        self.label_15.setText(_translate("RunWindow", "Scan"))
        self.pushButton_5.setText(_translate("RunWindow", "Remove"))
        self.pushButton_7.setText(_translate("RunWindow", "Generate"))
        self.label_29.setText(_translate("RunWindow", "XML Report"))
        self.pushButton_23.setText(_translate("RunWindow", "Add"))
        self.pushButton_8.setText(_translate("RunWindow", "Cancel"))
        self.label_32.setText(_translate("RunWindow", "OR"))
        self.label.setText(_translate("RunWindow", "Run List "))
        self.RunListTable.setSortingEnabled(True)
        item = self.RunListTable.horizontalHeaderItem(0)
        item.setText(_translate("RunWindow", "Name of Run"))
        item = self.RunListTable.horizontalHeaderItem(1)
        item.setText(_translate("RunWindow", "Description of Run"))
        item = self.RunListTable.horizontalHeaderItem(2)
        item.setText(_translate("RunWindow", "Control"))
        __sortingEnabled = self.RunListTable.isSortingEnabled()
        self.RunListTable.setSortingEnabled(False)
        item = self.RunListTable.item(0, 0)
        row_value = main.getNewToolNameConfigurationRun(0)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable.item(0, 1)
        description_value = main.getDescriptionConfigRun(self, 0)
        item.setText(_translate("RunWindow", description_value)) 
        item = self.RunListTable.item(1, 0)
        row_value = main.getNewToolNameConfigurationRun(1)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable.item(1, 1)
        description_value = main.getDescriptionConfigRun(self, 1)
        item.setText(_translate("RunWindow", description_value))
        item = self.RunListTable.item(2, 0)
        row_value = main.getNewToolNameConfigurationRun(2)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable.item(2, 1)
        description_value = main.getDescriptionConfigRun(self, 2)
        item.setText(_translate("RunWindow", description_value))
        #item = self.RunListTable.item(3, 0)
        #row_value = self.getNewToolNameConfigurationRun(self, 3)
        #item.setText(_translate("RunWindow", row_value))
        self.RunListTable.setSortingEnabled(__sortingEnabled)
        self.Add.setText(_translate("RunWindow", "Add"))
        self.toolButton.setText(_translate("RunWindow", "..."))
        self.toolButton_4.setText(_translate("RunWindow", "..."))
        self.toolButton_5.setText(_translate("RunWindow", "..."))
        self.toolButton_6.setText(_translate("RunWindow", "..."))
        self.toolButton_2.setText(_translate("RunWindow", "..."))
        self.toolButton_7.setText(_translate("RunWindow", "..."))
        self.toolButton_8.setText(_translate("RunWindow", "..."))
        self.toolButton_3.setText(_translate("RunWindow", "..."))
        self.toolButton_9.setText(_translate("RunWindow", "..."))
        self.toolButton_10.setText(_translate("RunWindow", "..."))
        self.toolButton_11.setText(_translate("RunWindow", "..."))
        self.toolButton_12.setText(_translate("RunWindow", "..."))
        self.label_2.setText(_translate("RunWindow", "Configuration of Selected Run Area"))
        self.label_3.setText(_translate("RunWindow", "Run Name"))
        self.label_4.setText(_translate("RunWindow", "Run Description"))
        self.label_5.setText(_translate("RunWindow", "Whitelisted IP Target"))
        self.label_6.setText(_translate("RunWindow", "Blacklisted IP Target"))
        self.label_7.setText(_translate("RunWindow", "Scan Type"))
        self.comboBox.setItemText(0, _translate("RunWindow", "Test"))
        self.comboBox.setItemText(1, _translate("RunWindow", "Test1"))
        self.pushButton.setText(_translate("RunWindow", "Add"))
        self.label_8.setText(_translate("RunWindow", "OR"))
        self.label_9.setText(_translate("RunWindow", "Run Configuration File"))
        self.pushButton_3.setText(_translate("RunWindow", "Cancel"))
        self.pushButton_4.setText(_translate("RunWindow", "Save"))
        self.pushButton_22.setText(_translate("RunWindow", "Browse"))
        self.pushButton_22.clicked.connect(lambda: main.getFilePath(self, 22))
        self.RunListTable_2.setSortingEnabled(True)
        item = self.RunListTable_2.horizontalHeaderItem(0)
        item.setText(_translate("RunWindow", "Name of Tool"))
        item = self.RunListTable_2.horizontalHeaderItem(1)
        item.setText(_translate("RunWindow", "Description of Tool"))
        item = self.RunListTable_2.horizontalHeaderItem(2)
        item.setText(_translate("RunWindow", "Remove"))
        __sortingEnabled = self.RunListTable_2.isSortingEnabled()
        self.RunListTable_2.setSortingEnabled(False)
        item = self.RunListTable_2.item(0, 0)
        row_value = main.getNewToolNameToolSpecification(0)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable_2.item(0, 1)
        description_value = main.getDescriptionToolSpecification(self, 0)
        item.setText(_translate("RunWindow", description_value)) 
        item = self.RunListTable_2.item(1, 0)
        row_value = main.getNewToolNameToolSpecification(1)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable_2.item(1, 1)
        description_value = main.getDescriptionToolSpecification(self, 1)
        item.setText(_translate("RunWindow", description_value)) 
        item = self.RunListTable_2.item(2, 0)
        row_value = main.getNewToolNameToolSpecification(2)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable_2.item(2, 1)
        description_value = main.getDescriptionToolSpecification(self, 2)
        item.setText(_translate("RunWindow", description_value)) 
        item = self.RunListTable_2.item(3, 0)
        row_value = main.getNewToolNameToolSpecification(3)
        item.setText(_translate("RunWindow", row_value))
        item = self.RunListTable_2.item(4, 0)
        row_value = main.getNewToolNameToolSpecification(4)
        item.setText(_translate("RunWindow", row_value))
        self.RunListTable_2.setSortingEnabled(__sortingEnabled)
        self.label_30.setText(_translate("RunWindow", "Tool List"))
        self.pushButton_9.setText(_translate("RunWindow", "Remove"))
        self.pushButton_9.clicked.connect(lambda: main.removeToolList(self, 0))
        self.pushButton_9.clicked.connect(lambda: main.showDialog(self))
        self.pushButton_10.setText(_translate("RunWindow", "Remove"))
        self.pushButton_10.clicked.connect(lambda: main.removeToolList(self, 1))
        self.pushButton_10.clicked.connect(lambda: main.showDialog(self))
        self.pushButton_11.setText(_translate("RunWindow", "Remove"))
        self.pushButton_11.clicked.connect(lambda: main.removeToolList(self, 2))
        self.pushButton_11.clicked.connect(lambda: main.showDialog(self))
        self.pushButton_12.setText(_translate("RunWindow", "Remove"))
        self.pushButton_12.clicked.connect(lambda: main.removeToolList(self, 3))
        self.pushButton_12.clicked.connect(lambda: main.showDialog(self))
        self.pushButton_13.setText(_translate("RunWindow", "Remove"))
        self.pushButton_13.clicked.connect(lambda: main.removeToolList(self, 4))
        self.pushButton_13.clicked.connect(lambda: main.showDialog(self))
        self.pushButton_20.setText(_translate("RunWindow", "Cancel"))
        self.pushButton_21.setText(_translate("RunWindow", "Save"))
        self.label_21.setText(_translate("RunWindow", "Tool Specification"))
        self.label_22.setText(_translate("RunWindow", "Tool Name"))
        self.label_23.setText(_translate("RunWindow", "Tool Description"))
        self.label_24.setText(_translate("RunWindow", "Tool Path"))
        self.label_25.setText(_translate("RunWindow", "Option and Argument"))
        self.pushButton_16.setText(_translate("RunWindow", "Add"))
        self.pushButton_17.setText(_translate("RunWindow", "Browse"))
        self.pushButton_17.clicked.connect(lambda: main.getFilePath(self, 17))
        self.label_26.setText(_translate("RunWindow", "Output Data Specification"))
        self.label_27.setText(_translate("RunWindow", "OR"))
        self.label_28.setText(_translate("RunWindow", "Tool Specification File"))
        self.pushButton_18.setText(_translate("RunWindow", "Add"))
        self.pushButton_19.setText(_translate("RunWindow", "Browse"))
        self.pushButton_19.clicked.connect(lambda: main.getFilePath(self, 19))
        self.comboBox_5.setItemText(0, _translate("RunWindow", ""))
        #self.comboBox_5.setItemText(1, _translate("RunWindow", "Test1"))
        self.label_16.setText(_translate("RunWindow", "Dependent Data"))
        self.label_17.setText(_translate("RunWindow", "Operator"))
        self.label_18.setText(_translate("RunWindow", "Value"))
        self.pushButton_14.setText(_translate("RunWindow", "Remove"))
        self.pushButton_14.clicked.connect(lambda: main.removeTooldependency(self))
        self.label_19.setText(_translate("RunWindow", "Dependency Expression"))
        self.comboBox_6.setItemText(0, _translate("RunWindow", ""))
        #self.comboBox_6.setItemText(1, _translate("RunWindow", ""))
        self.pushButton_15.setText(_translate("RunWindow", "Add"))
        self.pushButton_15.clicked.connect(lambda: main.addTooldependency(self)) 
        self.label_20.setText(_translate("RunWindow", "Tool Dependency"))
        main.refreshToolDependecy(self)
        self.comboBox_7.setItemText(0, _translate("RunWindow", ""))
        #self.comboBox_7.setItemText(1, _translate("RunWindow", "Test1"))
        self.label_31.setText(_translate("RunWindow", "Tool Name"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RunWindow", "Scan"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RunWindow", "Execution Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RunWindow", "Start time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RunWindow", "End Time "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("RunWindow", "Success/Failure"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("RunWindow", "Control"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_1), _translate("RunWindow", "Scan 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_2), _translate("RunWindow", "Scan 2"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RunWindow = QtWidgets.QWidget()
    ui = Ui_RunWindow()
    ui.setupUi(RunWindow)
    RunWindow.show()
    sys.exit(app.exec_())
