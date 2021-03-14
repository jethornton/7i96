# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sun Aug 12 12:18:13 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(about)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(about)
        self.label.setGeometry(QtCore.QRect(100, 20, 161, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.versionLB = QtWidgets.QLabel(about)
        self.versionLB.setGeometry(QtCore.QRect(150, 50, 59, 15))
        self.versionLB.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLB.setObjectName("versionLB")
        self.label_2 = QtWidgets.QLabel(about)
        self.label_2.setGeometry(QtCore.QRect(98, 70, 161, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(about)
        self.label_3.setGeometry(QtCore.QRect(108, 100, 131, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(about)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 371, 81))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.systemLB = QtWidgets.QLabel(self.groupBox)
        self.systemLB.setObjectName("systemLB")
        self.gridLayout.addWidget(self.systemLB, 0, 0, 1, 1)
        self.releaseLB = QtWidgets.QLabel(self.groupBox)
        self.releaseLB.setObjectName("releaseLB")
        self.gridLayout.addWidget(self.releaseLB, 1, 0, 1, 1)
        self.bitsLB = QtWidgets.QLabel(self.groupBox)
        self.bitsLB.setObjectName("bitsLB")
        self.gridLayout.addWidget(self.bitsLB, 1, 1, 1, 1)
        self.machineLB = QtWidgets.QLabel(self.groupBox)
        self.machineLB.setObjectName("machineLB")
        self.gridLayout.addWidget(self.machineLB, 2, 0, 1, 1)

        self.retranslateUi(about)
        self.buttonBox.accepted.connect(about.accept)
        self.buttonBox.rejected.connect(about.reject)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About"))
        self.label.setText(_translate("about", "7i96 Configuration Tool"))
        self.versionLB.setText(_translate("about", "TextLabel"))
        self.label_2.setText(_translate("about", "Author John Thornton"))
        self.label_3.setText(_translate("about", "Licence GPL3"))
        self.groupBox.setTitle(_translate("about", "PC Information"))
        self.systemLB.setText(_translate("about", "TextLabel"))
        self.releaseLB.setText(_translate("about", "TextLabel"))
        self.bitsLB.setText(_translate("about", "TextLabel"))
        self.machineLB.setText(_translate("about", "TextLabel"))

