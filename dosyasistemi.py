
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import sys
import subprocess
import os
class DosyaSistemi:


    def ac(self):
        filename = QFileDialog.getOpenFileName()

        self.path = filename[0]

        return self.path
    def yaz(self):
        try:
            self.path=DosyaSistemi.ac(self)

            dosya=open(self.path,"r")

            return dosya
        except:
            pass
    def dosya_adi(self):
        return self.path
        pass

    def yeni(self):
        file = str(QFileDialog.getExistingDirectory(None, "Klasör Seç"))
        os.chdir(file)
        self.path=file+"untitled.py"
        dosya=open("untitled.py","w")
        dosya.close()
        dosya=open("untitled.py","r")
        return dosya



    def kaydet(self):

        dosya=open(self.path,"w")
        return dosya
    def calistir(self):



        output = subprocess.check_output([sys.executable, self.path]).decode('utf-8').rstrip()

        msg = QMessageBox()
        msg.setWindowTitle("Code running")
        msg.setText("Code running you can see output pressing 'Show Details'")
        msg.setIcon(QMessageBox.Question)
        msg.setDetailedText(output)
        x = msg.exec_()
