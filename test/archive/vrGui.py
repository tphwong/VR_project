import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)	# (x1, y1, x2, y2)
		self.setWindowTitle("VR Test")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

		self.home()	# use self.home() instead of self.show() directly; see home() definition
		
	# define a home() function so that we don't have to use __init__() as a home method
	# this allows us to not have to reset all other application changes when returning to home
	def home(self):	
		# add a text label as placeholder for language choice, hide the text on widget
		self.languageChoice = QtGui.QLabel("en-US", self)
		self.languageChoice.hide()
		# add a drop-down box for language choice
		languageBox = QtGui.QComboBox(self)
		languageBox.addItem("en-US")
		languageBox.addItem("fr-CA")
		languageBox.addItem("es-MX")
		languageBox.move(50, 250)
		languageBox.activated[str].connect(self.language_choice)
		
		# add a text label as placeholder for category choice, hide the text on widget
		self.categoryChoice = QtGui.QLabel("Navigation", self)
		self.categoryChoice.hide()
		# add a drop-down box for category choice
		categoryBox = QtGui.QComboBox(self)
		categoryBox.addItem("Navigation")
		categoryBox.addItem("Phone")
		categoryBox.addItem("Radio")
		categoryBox.move(150, 250)
		categoryBox.activated[str].connect(self.category_choice)
		
		
		
		
		self.cmdChoice = QtGui.QLabel("Address book", self)
		self.cmdChoice.hide()
		cmdBox = QtGui.QComboBox(self)
		cmdBox.addItem("Address book")
		
		if self.languageChoice.text() == "en_US":
			if self.categoryChoice.text() == "Phone":
				cmdBox.clear()
				cmdBox.addItem("Call")
				cmdBox.update()
				
		cmdBox.move(250, 250)
		cmdBox.activated[str].connect(self.cmd_choice)
		
		if self.languageChoice.text() == "en_US":
			print('1')
			if self.categoryChoice.text() == "Phone":
				print('2')
				cmdBox.clear()
				cmdBox.addItem("Call")
				cmdBox.update()
		
		self.show()
	
	def language_choice(self, text):
		self.languageChoice.setText(text)
		print(self.languageChoice.text())
		
	def category_choice(self, text):
		self.categoryChoice.setText(text)
		print(self.categoryChoice.text())
		
		
				
		
		
	def cmd_choice(self, text):
		self.cmdChoice.setText(text)
		print(self.cmdChoice.text())
		
		
				

		
def run():
	app = QtGui.QApplication(sys.argv)	# think of this as the frame of the window
	GUI = Window()
	sys.exit(app.exec_())
	
run()