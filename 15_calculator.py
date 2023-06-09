# Form implementation generated from reading ui file '15_calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 60, 385, 184))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_one = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_one.setFont(font)
        self.lineEdit_one.setObjectName("lineEdit_one")
        self.horizontalLayout.addWidget(self.lineEdit_one)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_second = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_second.setFont(font)
        self.lineEdit_second.setObjectName("lineEdit_second")
        self.horizontalLayout_2.addWidget(self.lineEdit_second)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.clicked.connect(self.add)
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_sub = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_sub.clicked.connect(self.subtract)
        self.horizontalLayout_3.addWidget(self.pushButton_sub)
        self.pushButton_multi = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_multi.setFont(font)
        self.pushButton_multi.setObjectName("pushButton_multi")
        self.pushButton_multi.clicked.connect(self.multiply)
        self.horizontalLayout_3.addWidget(self.pushButton_multi)
        self.pushButton_divide = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_divide.clicked.connect(self.divide)
        self.horizontalLayout_3.addWidget(self.pushButton_divide)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_result = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("QLabel{\n"
"color:green\n"
"}")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #addition function
    def add(self):
        first_number = int(self.lineEdit_one.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number + second_number
        self.label_result.setText("Addition: {}".format(result))
    
    #subtraction function
    def subtract(self):
        first_number = int(self.lineEdit_one.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number - second_number
        self.label_result.setText("Subtraction: {}".format(result))
    
    #multiplication function
    def multiply(self):
        first_number = int(self.lineEdit_one.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number * second_number
        self.label_result.setText("Multiplication: {}".format(result))
    
    #division function
    def divide(self):
        first_number = int(self.lineEdit_one.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number / second_number
        self.label_result.setText("Division: {}".format(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number"))
        self.lineEdit_one.setPlaceholderText(_translate("Form", "Please Enter First Number"))
        self.label_2.setText(_translate("Form", "Second Number"))
        self.lineEdit_second.setPlaceholderText(_translate("Form", "Please Enter Second Number"))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.pushButton_sub.setText(_translate("Form", "Sub"))
        self.pushButton_multi.setText(_translate("Form", "Multiply"))
        self.pushButton_divide.setText(_translate("Form", "Divide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
