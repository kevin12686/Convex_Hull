# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConvexHullGui(object):
    def setupUi(self, ConvexHullGui):
        ConvexHullGui.setObjectName("ConvexHullGui")
        ConvexHullGui.setWindowModality(QtCore.Qt.WindowModal)
        ConvexHullGui.setEnabled(True)
        ConvexHullGui.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConvexHullGui.sizePolicy().hasHeightForWidth())
        ConvexHullGui.setSizePolicy(sizePolicy)
        ConvexHullGui.setMinimumSize(QtCore.QSize(800, 600))
        ConvexHullGui.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        ConvexHullGui.setFont(font)
        ConvexHullGui.setMouseTracking(False)
        ConvexHullGui.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConvexHullGui.setWindowIcon(icon)
        self.graphicsView = QtWidgets.QGraphicsView(ConvexHullGui)
        self.graphicsView.setGeometry(QtCore.QRect(20, 80, 761, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.runbutton = QtWidgets.QPushButton(ConvexHullGui)
        self.runbutton.setGeometry(QtCore.QRect(690, 30, 93, 31))
        self.runbutton.setObjectName("runbutton")
        self.groupBox = QtWidgets.QGroupBox(ConvexHullGui)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName("groupBox")
        self.inputbox = QtWidgets.QSpinBox(self.groupBox)
        self.inputbox.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.inputbox.setAlignment(QtCore.Qt.AlignCenter)
        self.inputbox.setMinimum(3)
        self.inputbox.setMaximum(500)
        self.inputbox.setSingleStep(5)
        self.inputbox.setProperty("value", 10)
        self.inputbox.setObjectName("inputbox")
        self.vertexconfirm = QtWidgets.QPushButton(self.groupBox)
        self.vertexconfirm.setGeometry(QtCore.QRect(120, 21, 93, 28))
        self.vertexconfirm.setAutoDefault(False)
        self.vertexconfirm.setDefault(False)
        self.vertexconfirm.setObjectName("vertexconfirm")

        self.retranslateUi(ConvexHullGui)
        QtCore.QMetaObject.connectSlotsByName(ConvexHullGui)

    def retranslateUi(self, ConvexHullGui):
        _translate = QtCore.QCoreApplication.translate
        ConvexHullGui.setWindowTitle(_translate("ConvexHullGui", "Convex Hull"))
        self.runbutton.setText(_translate("ConvexHullGui", "RUN"))
        self.groupBox.setTitle(_translate("ConvexHullGui", "Vertex"))
        self.vertexconfirm.setText(_translate("ConvexHullGui", "Confirm"))

