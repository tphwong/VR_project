import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)	# (x1, y1, x2, y2)
		self.setWindowTitle("VR Test")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		
		# add menu bar by building status bars and then putting them together as menu bar
		# put these in __init__() instead of home() because they stay the same everywhere
		
		# add an openFile item as a status bar entry for text editing
		openFile = QtGui.QAction("&Open File", self)
		openFile.setShortcut("Ctrl+O")
		openFile.setStatusTip('Open File')
		openFile.triggered.connect(self.file_open)
		
		# add a saveFile item as a status bar entry for text editing
		saveFile = QtGui.QAction("&Save File", self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.file_save)
		
		# add a peaceOut item as a status bar entry for quit function
		peaceOut = QtGui.QAction("&Peace out.", self)
		peaceOut.setShortcut("Ctrl+Q")
		peaceOut.setStatusTip('Ima bounce.')
		peaceOut.triggered.connect(self.close_application)
		
		# add an openEditor item as a status bar entry for text editor function
		openEditor = QtGui.QAction('&Editor', self)
		openEditor.setShortcut('Ctrl+E')
		openEditor.setStatusTip('Open Editor')
		openEditor.triggered.connect(self.editor)
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		
		# create File menu bar and add items
		fileMenu = mainMenu.addMenu("&File")
		fileMenu.addAction(openFile)
		fileMenu.addAction(saveFile)
		fileMenu.addAction(peaceOut)

		# create Editor menu bar and add items
		editorMenu = mainMenu.addMenu("&Editor")
		editorMenu.addAction(openEditor)
		
		# show everything
		self.home()	# use self.home() instead of self.show() directly; see home() definition
		
	# define a home() function so that we don't have to use __init__() as a home method
	# this allows us to not have to reset all other application changes when returning to home
	def home(self):
		# "Quit" button
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0, 100)
		
		# add tool bar 
		# for now just put it in home(); it could either be same or different on each page
		
		# add a tool bar item for quit function
		peaceOut = QtGui.QAction(QtGui.QIcon('deuces.jpg'), 'Flee the Scene', self)
		peaceOut.triggered.connect(self.close_application)
		self.toolBar = self.addToolBar("Peace Out.")
		self.toolBar.addAction(peaceOut)
		
		# add a tool bar item for font choices
		fontChoice = QtGui.QAction('Font', self)
		fontChoice.triggered.connect(self.font_choice)
		#self.toolBar = self.addToolBar("Font")
		self.toolBar.addAction(fontChoice)
		
		# add a check box for enlarging window
		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100, 20)
		checkBox.stateChanged.connect(self.enlarge_window)
		checkBox.toggle()	# set the box on, otherwise default is off
		
		# add progress bar and "download" button
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)
		self.btn = QtGui.QPushButton("Cops dat stuff", self)
		self.btn.move(200, 120)
		self.btn.clicked.connect(self.download)
		
		# add a text label and drop down button for style choices
		self.styleChoice = QtGui.QLabel("Windows Vista", self)
		self.styleChoice.move(50, 200)
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")
		comboBox.move(50, 250)
		comboBox.activated[str].connect(self.style_choice)
		
		self.show()
	
	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)
	
	def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)
	
	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
		
	def font_choice(self):
		font, valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)
	
	def editor(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		
	def file_open(self):
		# get file name as whatever is selected in the selector
		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		# read file into memory
		file = open(name, 'r')
		
		# call the editor, since it is not up by default
		self.editor()
		
		# populate the editor with data read from file
		with file:
			text = file.read()
			self.textEdit.setText(text)
			
	def file_save(self):
		name = QtGui.QFileDialog.getSaveFileName(self, 'SaveFile')
		file = open(name, 'w')
		text = self.textEdit.toPlainText()
		file.write(text)
		file.close()
	
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Hold up!', "You tryna bounce?",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Peacing out...")
			sys.exit("Smell ya later.")
		else:
			pass
		
	
def run():
	app = QtGui.QApplication(sys.argv)	# think of this as the frame of the window
	GUI = Window()
	sys.exit(app.exec_())
	
run()