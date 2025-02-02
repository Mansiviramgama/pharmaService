from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddMedicine(object):
    def __init__(self, _id):
        self.id = _id

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, -10, 911, 71))
        self.widget_2.setStyleSheet("background-color: rgb(57, 66, 148);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 16, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(780, 20, 81, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(39, 24, 106);\n"
                                      "border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(150, 90, 630, 676))
        self.widget_3.setStyleSheet("background-color: rgb(57, 66, 148);\n"
                                    "border-radius:15px;")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 228, 29))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(100, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.medicine_name = QtWidgets.QLineEdit(self.widget_3)
        self.medicine_name.setGeometry(QtCore.QRect(80, 200, 455, 51))
        self.medicine_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius:5px;\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "padding: 2px 4px;")
        self.medicine_name.setObjectName("medicine_name")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.add_button = QtWidgets.QPushButton(self.widget_3)
        self.add_button.setGeometry(QtCore.QRect(240, 590, 145, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius:5px;\n"
                                      "color: rgb(57, 66, 148);")
        self.add_button.setObjectName("add_button")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(300, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.description = QtWidgets.QTextEdit(self.widget_3)
        self.description.setGeometry(QtCore.QRect(80, 310, 451, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius:5px;\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "padding: 4px 6px\n"
                                       "")
        self.description.setObjectName("description")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(90, 460, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.medicine_quantity = QtWidgets.QLineEdit(self.widget_3)
        self.medicine_quantity.setGeometry(QtCore.QRect(390, 460, 111, 41))
        self.medicine_quantity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius:5px;\n"
                                             "color: rgb(0, 0, 0);\n"
                                             "padding: 2px 4px;")
        self.medicine_quantity.setObjectName("medicine_quantity")
        self.medicine_price = QtWidgets.QLineEdit(self.widget_3)
        self.medicine_price.setGeometry(QtCore.QRect(150, 460, 111, 41))
        self.medicine_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius:5px;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "padding: 2px 4px;")
        self.medicine_price.setObjectName("medicine_price")
        self.error_message = QtWidgets.QLabel(self.widget_3)
        self.error_message.setGeometry(QtCore.QRect(180, 550, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.error_message.setFont(font)
        self.error_message.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_message.setText("")
        self.error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.error_message.setObjectName("error_message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "MedAlthea"))
        self.pushButton.setText(_translate("Dialog", "Back"))
        self.label_3.setText(_translate("Dialog", "Add  New Medicines"))
        self.label_4.setText(_translate("Dialog", "Medicine Name:"))
        self.label_5.setText(_translate("Dialog", "Description:"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.label_6.setText(_translate("Dialog", "Quantity"))
        self.description.setHtml(_translate("Dialog", ""))
        self.label_7.setText(_translate("Dialog", "Price"))

    def checkFields(self):
        valid = False
        medicineName_text = self.medicine_name.text()
        medicinePrice_text = self.medicine_price.text()
        medicineDescription_text = self.description.toPlainText()
        medicineQuantity_text = self.medicine_quantity.text()
        medicineDetails = {}
        if (len(medicineName_text.replace(' ', '')) == 0) or (len(medicineQuantity_text.replace(' ', '')) == 0) or len(
                medicinePrice_text.replace(' ', '')) == 0 or len(medicineDescription_text.replace(' ', '')) == 0:
            self.error_message.setText("All fields are required")
            valid = False

        else:
            valid = True
            medicineDetails = {
                'medicalId': self.id,
                'name': medicineName_text,
                'description': medicineDescription_text,
                'price': medicinePrice_text,
                'quantity': medicineQuantity_text
            }
            self.error_message.setText("")

        return valid, medicineDetails
