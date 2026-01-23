from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(0, 0, 531, 611))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("bg.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 70, 251, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.temp_property = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.temp_property.setContentsMargins(0, 0, 0, 0)
        self.temp_property.setObjectName("temp_property")
        self.cityName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cityName.setStyleSheet("font: 20pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255)")
        self.cityName.setAlignment(QtCore.Qt.AlignCenter)
        self.cityName.setObjectName("cityName")
        self.temp_property.addWidget(self.cityName)
        self.temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.temp.setStyleSheet("font: 28pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255)")
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.temp_property.addWidget(self.temp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.high_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.high_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Sans Serif\";")
        self.high_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.high_temp.setObjectName("high_temp")
        self.horizontalLayout.addWidget(self.high_temp)
        self.low_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.low_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Sans Serif\";")
        self.low_temp.setObjectName("low_temp")
        self.horizontalLayout.addWidget(self.low_temp)
        self.temp_property.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cityName.setText(_translate("MainWindow", "NameHere!"))
        self.temp.setText(_translate("MainWindow", "tempHere!"))
        self.high_temp.setText(_translate("MainWindow", "H Here!"))
        self.low_temp.setText(_translate("MainWindow", "L Here!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
