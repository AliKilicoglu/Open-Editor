from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("C:\\Users\\Ali\\Desktop\\Open Editor")
from Dosya_Sistemi import DosyaSistemi
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 532)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Ac = QtWidgets.QPushButton(Form)
        self.Ac.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.Ac.setObjectName("Ac")
        self.Ac.clicked.connect(self.Ac)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 601, 491))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Editor"))
        self.Ac.setText(_translate("Form", "Aç"))
    def Ac(self):
        DosyaSistemi.ac("plainTextEdit")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
