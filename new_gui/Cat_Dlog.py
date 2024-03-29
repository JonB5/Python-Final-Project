# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cat_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject


class UiDialog(QObject, object):
    category_added = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.categories = []

    def setup_ui(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(405, 190)
        dialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 281, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.line = QtWidgets.QFrame(dialog)
        self.line.setGeometry(QtCore.QRect(20, 110, 371, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 30, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslate_ui(dialog)
        self.buttonBox.accepted.connect(self.accepted_action) # type: ignore
        self.buttonBox.rejected.connect(dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def accepted_action(self):
        text = self.lineEdit.text()
        self.categories.append(text)
        self.category_added.emit(text)
        #print(f"Saved text: {text}")
        self.buttonBox.parent().accept()

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label.setText(_translate("dialog", "Add Category:"))

