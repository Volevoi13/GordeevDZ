# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.central = QtWidgets.QWidget(MainWindow)
        self.central.setObjectName("central")

        self.lblTitle = QtWidgets.QLabel(self.central)
        self.lblTitle.setGeometry(QtCore.QRect(250, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("ГОСТ тип А")
        font.setPointSize(16)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")

        self.lbl1 = QtWidgets.QLabel(self.central)
        self.lbl1.setGeometry(QtCore.QRect(150, 100, 200, 30))
        font = QtGui.QFont()
        font.setFamily("ГОСТ тип А")
        font.setPointSize(16)
        self.lbl1.setFont(font)
        self.lbl1.setObjectName("lbl1")

        self.le1 = QtWidgets.QLineEdit(self.central)
        self.le1.setGeometry(QtCore.QRect(370, 100, 200, 30))
        self.le1.setObjectName("le1")

        self.lbl2 = QtWidgets.QLabel(self.central)
        self.lbl2.setGeometry(QtCore.QRect(150, 150, 200, 30))
        font = QtGui.QFont()
        font.setFamily("ГОСТ тип А")
        font.setPointSize(16)
        self.lbl2.setFont(font)
        self.lbl2.setObjectName("lbl2")

        self.le2 = QtWidgets.QLineEdit(self.central)
        self.le2.setGeometry(QtCore.QRect(370, 150, 200, 30))
        self.le2.setObjectName("le2")

        self.btn = QtWidgets.QPushButton(self.central)
        self.btn.setGeometry(QtCore.QRect(300, 220, 200, 50))
        font = QtGui.QFont()
        font.setFamily("ГОСТ тип А")
        font.setPointSize(16)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")

        self.lbl3 = QtWidgets.QLabel(self.central)
        self.lbl3.setGeometry(QtCore.QRect(250, 300, 300, 50))
        font = QtGui.QFont()
        font.setFamily("ГОСТ тип А")
        font.setPointSize(16)
        self.lbl3.setFont(font)
        self.lbl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl3.setObjectName("lbl3")

        MainWindow.setCentralWidget(self.central)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Калькулятор имт"))
        self.lbl1.setText(_translate("MainWindow", "Введите ваш вес"))
        self.lbl2.setText(_translate("MainWindow", "Введите ваш рост"))
        self.btn.setText(_translate("MainWindow", "Вывод"))
        self.lbl3.setText(_translate("MainWindow", ""))
