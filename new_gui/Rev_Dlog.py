from PyQt5 import QtCore, QtWidgets


class UiDialogRev(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 324)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 270, 361, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 40, 471, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 461, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 150, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 220, 201, 26))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 60, 16))
        self.label_4.setObjectName("label_4")

        self.retranslate_ui(Dialog)
        self.buttonBox.accepted.connect(self.add_revenue_to_wallet) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Revenue:"))
        self.label_2.setText(_translate("Dialog", "Amount:"))
        self.label_3.setText(_translate("Dialog", "Description:"))
        self.label_4.setText(_translate("Dialog", "Category: "))

    def combo_update(self, categories):
        for category in categories:
            self.comboBox.addItem(category.name, category)

    def add_revenue_to_wallet(self):
        amount = self.lineEdit.text()
        item = self.lineEdit_2.text()
        if amount == "":
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter an amount.")
        else:
            try:
                amount = float(amount)
                if amount <= 0:
                    QtWidgets.QMessageBox.warning(None, "Error", "Amount must be a positive number.")
                else:
                    # if the amount is pos adds item and $ to wallet for selected category
                    selected_drop = self.comboBox.currentData()
                    selected_cat = selected_drop if selected_drop is not None else None
                    selected_cat.add_revenue(amount, item)
                    QtWidgets.QMessageBox.information(None, "Success", "Revenue added successfully.")
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
                    #print(selected_cat.wallet)
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Error", "Invalid amount entered. Please enter a positive number.")