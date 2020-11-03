from PyQt5 import QtCore, QtGui, QtWidgets
from DosyaSistemi import DosyaSistemi
import sys
import subprocess
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 532)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Ac)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Kaydet)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 0, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Calistir)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 601, 491))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Editor"))
        self.pushButton_2.setText(_translate("Form", "Kaydet"))
        self.pushButton.setText(_translate("Form", "Aç"))
        self.pushButton_3.setText(_translate("Form", "Çalıştır"))
    def Ac(self):
        self.dosya_konumu=DosyaSistemi.ac()
        print(self.dosya_konumu)
        dosya=open(self.dosya_konumu,"r")
        self.plainTextEdit.insertPlainText(dosya.read())
    def Kaydet(self):
        dosya=open(self.dosya_konumu,"w")
        dosya.write(self.plainTextEdit.toPlainText())
    def Calistir(self):

            output = subprocess.check_output([sys.executable, self.dosya_konumu]).decode('utf-8').rstrip()
            print(output)
            msg = QMessageBox()
            msg.setWindowTitle("Kod Derleniyor")
            msg.setText("Kod Derleniyor")
            msg.setIcon(QMessageBox.Question)
            msg.setDetailedText(output)
            x = msg.exec_()





        


        
        
    	

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())