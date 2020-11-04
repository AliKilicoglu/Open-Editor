
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

		dosya_konumu=DosyaSistemi.ac(self)
		print(dosya_konumu)
		dosya=open(dosya_konumu,"r")
		print(dosya)
		return dosya

	def kaydet(self):
		dosya_konumu = DosyaSistemi.ac(self)
		dosya=open(dosya_konumu,"w")
		return dosya
	def calistir(self):
		dosya_konumu=DosyaSistemi.ac(self)
		output = subprocess.check_output([sys.executable, dosya_konumu]).decode('utf-8').rstrip()
		print(output)
		msg = QMessageBox()
		msg.setWindowTitle("Kod Derleniyor")
		msg.setText("Kod Derleniyor")
		msg.setIcon(QMessageBox.Question)
		msg.setDetailedText(output)
		x = msg.exec_()
                                                     print('ali babapro')
