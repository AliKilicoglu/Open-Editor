from PyQt5 import QtCore, QtGui, QtWidgets
from dosyasistemi import DosyaSistemi

from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 532)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 0, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.calistir)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 601, 491))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton.clicked.connect(self.yaz)
        self.pushButton_2.clicked.connect(self.kaydet)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Editor"))
        self.pushButton_2.setText(_translate("Form", "Kaydet"))
        self.pushButton.setText(_translate("Form", "Aç"))
        self.pushButton_3.setText(_translate("Form", "Çalıştır"))

    def yaz(self):
        self.plainTextEdit.clear()
        dosya=DosyaSistemi.yaz(self)

        self.plainTextEdit.insertPlainText(dosya.read())
    def kaydet(self):
        dosya=DosyaSistemi.kaydet(self)
        dosya.write(self.plainTextEdit.toPlainText())

    def calistir(self):
        DosyaSistemi.calistir(self)





















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
