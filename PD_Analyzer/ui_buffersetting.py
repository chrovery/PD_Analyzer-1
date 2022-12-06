# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\buffersetting.ui'
#
# Created: Tue Mar 14 16:56:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_bufferSetting(object):
    def setupUi(self, bufferSetting):
        bufferSetting.setObjectName("bufferSetting")
        bufferSetting.resize(406, 298)
        self.buttonBox = QtGui.QDialogButtonBox(bufferSetting)
        self.buttonBox.setGeometry(QtCore.QRect(80, 200, 201, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bufferSettingSlider = QtGui.QSlider(bufferSetting)
        self.bufferSettingSlider.setGeometry(QtCore.QRect(120, 50, 160, 19))
        self.bufferSettingSlider.setMinimum(1)
        self.bufferSettingSlider.setMaximum(100)
        self.bufferSettingSlider.setPageStep(5)
        self.bufferSettingSlider.setProperty("value", 10)
        self.bufferSettingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bufferSettingSlider.setObjectName("bufferSettingSlider")
        self.bufferSettingSpinBox = QtGui.QSpinBox(bufferSetting)
        self.bufferSettingSpinBox.setGeometry(QtCore.QRect(120, 120, 81, 16))
        self.bufferSettingSpinBox.setMinimum(1)
        self.bufferSettingSpinBox.setMaximum(100)
        self.bufferSettingSpinBox.setProperty("value", 10)
        self.bufferSettingSpinBox.setObjectName("bufferSettingSpinBox")
        self.label = QtGui.QLabel(bufferSetting)
        self.label.setGeometry(QtCore.QRect(210, 120, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(bufferSetting)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), bufferSetting.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), bufferSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(bufferSetting)

    def retranslateUi(self, bufferSetting):
        bufferSetting.setWindowTitle(QtGui.QApplication.translate("bufferSetting", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("bufferSetting", "MB", None, QtGui.QApplication.UnicodeUTF8))

