# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\findDialog.ui'
#
# Created: Mon Jul 03 15:52:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_findDialog(object):
    def setupUi(self, findDialog):
        findDialog.setObjectName("findDialog")
        findDialog.resize(406, 298)
        self.buttonBox = QtGui.QDialogButtonBox(findDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 200, 201, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtGui.QComboBox(findDialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 60, 151, 21))
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(20)
        self.comboBox.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(findDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), findDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), findDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(findDialog)

    def retranslateUi(self, findDialog):
        findDialog.setWindowTitle(QtGui.QApplication.translate("findDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setCurrentText(QtGui.QApplication.translate("findDialog", "CTR:  GoodCRC", None, QtGui.QApplication.UnicodeUTF8))

