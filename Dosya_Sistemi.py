from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
class DosyaSistemi:

	def ac():
		filename = QFileDialog.getOpenFileName()
		path = filename[0]
		return path




		
    	