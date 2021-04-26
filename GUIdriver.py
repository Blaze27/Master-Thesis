import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
 
qtCreatorFile = "design.ui" # Enter file here.
global ImageFile
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.browse.clicked.connect(self.Test)
		self.close.clicked.connect(self.Close)

	def Test(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		ImageFile = QFileDialog.getOpenFileName(self,"Select Image To Process", "","All Files (*);;Image Files(*.jpg *.gif)",options=options)	
		exec(open('main.py').read())
		

	def Close(self):
		self.destroy()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())


