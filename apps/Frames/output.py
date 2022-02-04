from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 649)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 901, 711))
        self.widget.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(260, 360, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(370, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 801, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(252, 209, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QlineEdit"
                                    "*{background-color:rgb(208, 211, 255);"
                                    "border-radius:50px;"
                                    "border:2px solid black;}"
                                    "*::placeholder{"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 310, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QlineEdit" +
                                      "*{background-color:rgb(208, 211, 255);" +
                                      "border-radius:50px;" +
                                      "border:2px solid black;};" +
                                      "*::placeholder{" +
                                      "color:rgb(0, 0, 0)" +
                                      "}"
                                      )

        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(250, 420, 351, 41))
        self.pushButton.setStyleSheet("border-radius:25px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(85, 0, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog",
                                        "Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in "
                                        "laying out print, graphic or web designs. The passage is attributed to an "
                                        "unknown typesetter in the 15th century who is thought to have scrambled "
                                        "parts of Cicero\'s De Finibus Bonorum et Malorum for use in a type specimen "
                                        "book. It usually begins with:"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Email:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "SIGN IN"))
