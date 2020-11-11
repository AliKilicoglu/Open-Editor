
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import sys
import subprocess
class DosyaSistemi:


    def ac(self):
        filename = QFileDialog.getOpenFileName()
    
        self.path = filename[0]

        return self.path
    def yaz(self):
        try:
            self.dosya_konumu=DosyaSistemi.ac(self)

            dosya=open(self.dosya_konumu,"r")

            return dosya
        except:
            pass
    def dosya_adi(self):
        return self.path
        pass




    def kaydet(self):

        dosya=open(self.dosya_konumu,"w")
        return dosya
    def calistir(self):


        output = subprocess.check_output([sys.executable, self.dosya_konumu]).decode('utf-8').rstrip()

        msg = QMessageBox()
        msg.setWindowTitle("Kod Derleniyor")
        msg.setText("Kod Derleniyor")
        msg.setIcon(QMessageBox.Question)
        msg.setDetailedText(output)
        x = msg.exec_()
