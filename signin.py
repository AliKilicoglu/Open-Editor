
from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import firebase
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 205)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.signin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
    def signin(self):
            firebase_ = firebase.FirebaseApplication('https://openeditor-7924c.firebaseio.com/Users', None)
            result = firebase_.get('https://openeditor-7924c.firebaseio.com/Users/', '')
            result=list(result.values())
            for i in range(0,len(result)):
                text=result[i]
                if self.lineEdit.text() in text and self.lineEdit_2.text() in text:
                    file=open("account.txt", "w")
                    file.write(self.lineEdit.text())
                    file.close()

                    msg = QMessageBox()

                    msg.setWindowTitle("Sing in!")

                    msg.setText("Sign in successful")
                    msg.setIcon(QMessageBox.Information)


                    x = msg.exec_()
                    a=1
                else:
                    a=0
            if a==0:
                msg = QMessageBox()

                msg.setWindowTitle("Sign in!")

                msg.setText("Username or password false")
                msg.setIcon(QMessageBox.Information)


                x = msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
