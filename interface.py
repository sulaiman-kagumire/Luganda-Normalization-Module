'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

INTERFACE.PY
============

HOW IT WORKS:
-------------
This module creates a GUI for users to normalise text files or inserted text using the detection and conversion module (detection.py).
It is the module that is run to perform the normalisation
'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QWidget, QMessageBox, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDesktopWidget, QFileDialog
import sys, re, subprocess
import detection

class SimpleGui(QWidget):
	"""docstring for SimpleGui"""
	def __init__(self):
		super().__init__()
		self.initUI()
#opens dialog for file selection	
	def openFileDialog(self):
		fname = QFileDialog.getOpenFileName(self, 'Open text file', '', 'Text files (*.txt)')
		if fname[0]:
			# print(self.fname[0])
			self.fname = fname[0]
			self.filepath.setText(self.fname)
			# with open(self.fname[0], 'r') as f:
			# 	self.data = f.read()
				
#gets the path of text file selected
	def get_path_leaf(self, path):
		import ntpath
		head, tail = ntpath.split(path)
		return tail or ntpath.basename(head)

#normalises text file selected by calling detection.py 
	def normalize_text(self):
		txt = self.selText.text()
		if (txt != ""):
			#result = subprocess.check_output(['python', 'detection.py', 't', txt])
			#result = str(result, 'utf-8')
			result = detection.start(False, txt)
			print(type(result))
			import re
			resultRE = re.compile(r'>>>>>>>>>>>.*')
			groups = resultRE.findall(result)
			print(groups[0])
			self.txtNORMRESULTLabel.setText(groups[0])
		else:
			#result = subprocess.check_output(['python', 'detection.py', 'f', self.fname])
			#result = str(result, 'utf-8')
			result = detection.start(True, self.fname)
			import os.path
			dest_dir = os.path.dirname(self.fname)
			src_file = self.get_path_leaf(self.fname)
			p=os.path.join(dest_dir, 'normalised-'+src_file+"-log.txt")
			f = open(p, 'w+', errors="ignore")
			f.write(result)
			print(result)
			self.txtNORMDONELabel.setText("Normalisation Done")
		"""
		try:
			'''result = '''
			subprocess.check_output(['python', 'detection.py', self.fname])
			# result = str(result, 'utf-8')
			
		except AttributeError as e:
			subprocess.check_output(['python', 'detection.py', self.selText.text()])"""
#defines interface layout
	def initUI(self):
		#Layout Manager and Items
		self.filepath = QLineEdit("")

		openBtn = QPushButton("SELECT TEXT FILE TO NORMALISE", self)
		openBtn.clicked.connect(self.openFileDialog)
		openBtn.resize(openBtn.sizeHint())
		
		filebox = QHBoxLayout()
		filebox.addWidget(self.filepath)
		filebox.addWidget(openBtn)
		filebox.setAlignment(Qt.AlignCenter)
		filebox.setContentsMargins(90, 0, 90, 0)

		selLabel = QLabel("PASTE TEXT HERE (NOT MORE THAN 30 WORDS)")
		selLabel.setStyleSheet("{ color: white }")
		self.selText = QLineEdit("")
		textbox = QHBoxLayout()
		textbox.addWidget(selLabel)
		textbox.addWidget(self.selText)
		textbox.setAlignment(Qt.AlignCenter)
		textbox.setContentsMargins(90, 0, 90, 0)

		normalizeFileBtn = QPushButton("NORMALISE TEXT FILE", self)
		normalizeFileBtn.clicked.connect(self.normalize_text)
		normalizeFileBtn.resize(normalizeFileBtn.sizeHint())

		normalizeTxtBtn = QPushButton("NORMALISE PASTED TEXT", self)
		normalizeTxtBtn.clicked.connect(self.normalize_text)
		normalizeTxtBtn.resize(normalizeTxtBtn.sizeHint())

		closeBtn = QPushButton("CLOSE", self)
		closeBtn.clicked.connect(QApplication.instance().quit)
		closeBtn.resize(closeBtn.sizeHint())

		buttonbox = QHBoxLayout()
		buttonbox.addWidget(normalizeFileBtn)
		buttonbox.addWidget(normalizeTxtBtn)
		buttonbox.addWidget(closeBtn)
		buttonbox.setAlignment(Qt.AlignCenter)

		self.txtNORMDONELabel = QLabel("")
		self.txtNORMDONELabel.setStyleSheet("{ color: white }")
		donebox = QHBoxLayout()

		
		donebox.addWidget(self.txtNORMDONELabel)
		donebox.setAlignment(Qt.AlignCenter)

		self.txtNORMRESULTLabel = QLabel("")
		self.txtNORMRESULTLabel.setStyleSheet("{ color: white }")
		resultbox = QHBoxLayout()
		resultbox.addWidget(self.txtNORMRESULTLabel)
		resultbox.setAlignment(Qt.AlignCenter)

		mainlayout = QVBoxLayout()
		mainlayout.addLayout(filebox)
		mainlayout.addLayout(donebox)
		mainlayout.addLayout(textbox)
		mainlayout.addLayout(resultbox)
		mainlayout.addLayout(buttonbox)
		mainlayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(mainlayout)
		self.resize(600, 500)
		self.center()
		self.setWindowTitle("Luganda Text Normalization Tool")
		self.show()
# centers the interface in the middle of the screen
	def center(self):
		windowFrame = self.frameGeometry()
		windowCenter = QDesktopWidget().availableGeometry().center()
		windowFrame.moveCenter(windowCenter)
		self.move(windowFrame.topLeft())

	def function_one(self):
		pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	sgui = SimpleGui()
	sys.exit(app.exec_())