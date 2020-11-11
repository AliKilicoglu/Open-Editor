from PyQt5 import QtCore, QtGui, QtWidgets
from dosyasistemi import DosyaSistemi
from versiyonkontrol  import Versiyon_Kontrol
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ayarlar import Ui_MainWindow
import syntax
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
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 0, 81, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ayarlar)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 601, 491))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.highlighter = syntax.PythonHighlighter(self.plainTextEdit.document())
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
        self.pushButton_4.setText(_translate("Form", "Ayarlar"))


    def yaz(self):
        self.plainTextEdit.clear()
        dosya=open("ayarlar.txt","r")
        font_ad=dosya.readline().replace("FONT_ADI=","")
        font_boy=dosya.readline().replace("FONT_BOYU=","")
        self.plainTextEdit.setFont(QFont(font_ad, int(font_boy)))
        update=Versiyon_Kontrol.kontrol()
        if update =="1":

            msg = QMessageBox()

            msg.setWindowTitle("Günceleme bulundu!")
            #msg.setText("Yeni günceleme bulundu.\na href <'https://tinyurl.com/y2ruqeh4'>aa</a> güncel sürümü burdan indirebilirsiniz")
            msg.setText("Yeni güncelleme bulundu!.Güncelemeyi <a href='https://tinyurl.com/y2ruqeh4'Subject=My%20Subject>burdan</a> indirebilirsiniz")
            msg.setIcon(QMessageBox.Information)


            x = msg.exec_()
        if update=="0":

            pass



        try:
            dosya=DosyaSistemi.yaz(self)
            self.plainTextEdit.insertPlainText(dosya.read())
        except:
            pass
        
    def kaydet(self):
        dosya=DosyaSistemi.kaydet(self)
        dosya.write(self.plainTextEdit.toPlainText())

    def calistir(self):
        DosyaSistemi.calistir(self)
    def ayarlar(self):
        self.pencere=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.pencere)
        self.pencere.show()
        dosya=open("ayarlar.txt","r")
        font_ad=dosya.readline().replace("FONT_ADI=","")

        font_boy=dosya.readline().replace("FONT_BOYU=","")
        self.plainTextEdit.setFont(QFont(font_ad, int(font_boy)))
        text=self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        self.plainTextEdit.insertPlainText(text)





















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
