from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import firebase
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 253)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.create_account)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create your account"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Create My Acount!"))
    def create_account(self):
        data="""
        Username: {}
        Password: {}



        """.format(self.lineEdit.text(),self.lineEdit_2.text())
        firebase_ = firebase.FirebaseApplication('https://openeditor-7924c.firebaseio.com/Users', None)
        result = firebase_.get('https://openeditor-7924c.firebaseio.com/Users/', '')
        result=list(result.values())
        for i in range(0,len(result)):
            text=result[i]
            if self.lineEdit.text() in text:

                msg = QMessageBox()

                msg.setWindowTitle("Error!")
        
                msg.setText("This username is already taken")
                msg.setIcon(QMessageBox.Information)


                x = msg.exec_()
                a=1
            else:
                a=0
        if a==1:
            pass
        else:


            firebase_ = firebase.FirebaseApplication('https://openeditor-7924c.firebaseio.com', None)

            result = firebase_.post('https://openeditor-7924c.firebaseio.com/Users/',data)

            msg = QMessageBox()

            msg.setWindowTitle("Created!")
        
            msg.setText("Your account  created                        \n Thanks for joining                 ")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())