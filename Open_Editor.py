from PyQt5 import QtCore, QtGui, QtWidgets
from dosyasistemi import DosyaSistemi
from versiyonkontrol  import Versiyon_Kontrol
from PyQt5.QtWidgets import QMessageBox,QTabWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QTextCursor
from ayarlar import Ui_MainWindow
import syntax
import os
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 532)


        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.yeni)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 0, 81, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 0, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 0, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.calistir)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 0, 81, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ayarlar)


        self.pushButton.clicked.connect(self.yaz)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 601, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))

        #self.tab = QtWidgets.QWidget()
        #self.tab.setObjectName("tab")

        #self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tabWidget.addTab(self.tab_2, "")









        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Editor"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.pushButton.setText(_translate("Form", "Open"))
        self.pushButton_3.setText(_translate("Form", "Run"))
        self.pushButton_4.setText(_translate("Form", "Settings"))
        self.pushButton_5.setText(_translate("Form", "New"))
        self.pushButton.setIcon(QIcon('Images/Aç.png'))
        self.pushButton_2.setIcon(QIcon('Images/Kaydet.png'))
        self.pushButton_3.setIcon(QIcon('Images/Çalıştır.png'))

        self.pushButton_4.setIcon(QIcon('Images/Ayarlar.png'))
        self.pushButton_5.setIcon(QIcon('Images/Yeni.png'))



    def add_indent(self):
        cursor = self.QTextCursor()
        line = cursor.blockNumber()
        split = self.toPlainText().split("\n")
        last = split[line-1]
        count = last.count("\t")

        if last.endswith(":") and self.key == Qt.Key_Return:
            self.key = None
            self.insertPlainText("\t"*(count+1))

        elif self.key == Qt.Key_Return:
            self.key = None
            count = last.count("\t")
            self.insertPlainText("\t"*(count))
    def yaz(self):

        dosya=open("ayarlar.txt","r")
        font_ad=dosya.readline().replace("FONT_ADI=","").replace("\n", "")

        font_boy=dosya.readline().replace("FONT_BOYU=","").replace("\n", "")

        dosya.close()

        update=Versiyon_Kontrol.kontrol()
        if update =="1":

            msg = QMessageBox()

            msg.setWindowTitle("Update!")
            #msg.setText("Yeni günceleme bulundu.\na href <'https://tinyurl.com/y2ruqeh4'>aa</a> güncel sürümü burdan indirebilirsiniz")
            msg.setText("A new update found!.You can dowland from <a href='https://tinyurl.com/y2ruqeh4'Subject=My%20Subject> here</a> ")
            msg.setIcon(QMessageBox.Information)


            x = msg.exec_()
        if update=="0":

            pass




        dosya=DosyaSistemi.yaz(self)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)

        self.tabWidget.addTab(self.tab, str(DosyaSistemi.dosya_adi(self)))
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 600, 490))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.highlighter = syntax.PythonHighlighter(self.plainTextEdit.document())

        self.plainTextEdit.clear()
        self.plainTextEdit.setFont(QFont(font_ad, int(font_boy)))
        self.plainTextEdit.insertPlainText(dosya.read())




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

    def yeni(self):
        dosya=open("ayarlar.txt","r")
        font_ad=dosya.readline().replace("FONT_ADI=","").replace("\n", "")
        font_boy=dosya.readline().replace("FONT_BOYU=","").replace("\n", "")
        dosya.close()
        self.dosya_konumu = DosyaSistemi.yeni(self)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)


        self.tabWidget.addTab(self.tab, "untitled.py")
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 600, 490))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.highlighter = syntax.PythonHighlighter(self.plainTextEdit.document())

        self.plainTextEdit.clear()
        self.plainTextEdit.setFont(QFont(font_ad, int(font_boy)))
        self.plainTextEdit.insertPlainText(self.dosya_konumu.read())
        self.dosya_konumu=str(self.dosya_konumu)










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()

    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())









