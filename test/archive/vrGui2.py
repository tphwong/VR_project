import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)	# (x1, y1, x2, y2)
		self.setWindowTitle("VR Test")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

		
		# add a text label as placeholder for language choice, hide the text on widget
		self.languageChoice = QtGui.QLabel("en-US", self)
		self.languageChoice.hide()
		# add a drop-down box for language choice
		languageList = ["en-US", "fr-CA", "es-MX"]
		self.languageBox = QtGui.QComboBox(self)
		self.languageBox.addItems(languageList)
		self.languageBox.move(20, 50)
		self.languageBox.activated[str].connect(self.language_choice)
		
		# add a text label as placeholder for category choice, hide the text on widget
		self.categoryChoice = QtGui.QLabel("Navigation", self)
		self.categoryChoice.hide()
		# add a drop-down box for category choice
		categoryList = ["Navigation", "Phone", "Radio"]
		self.categoryBox = QtGui.QComboBox(self)
		self.categoryBox.addItems(categoryList)
		self.categoryBox.move(120, 50)
		self.categoryBox.activated[str].connect(self.category_choice)
		
		#add a text label as placeholder for command choice, hide the text on widget
		self.cmdChoice = QtGui.QLabel("Address book", self)
		self.cmdChoice.hide()
		# add a drop-down box for category choice
		self.cmdBox = QtGui.QComboBox(self)
		list = ["Address book", "Cancel route", "Change home", "Change work", 
				"Destination information", "Find 46501 Commerce Center Dr, Plymouth, Michigan",
				"Find Starbucks", "Frequently visited points", "Go home", "Go to work",
				"Pause route", "Previous destinations", "Previous points", 
				"Previous starting points", "Resume route", "Route options", "Show route",
				"Traffic information", "Turn guidance off", "Turn guidance on", 
				"Zoom in", "Zoom out"]
		self.cmdBox.addItems(list)
		self.cmdBox.move(220, 50)
		self.cmdBox.activated[str].connect(self.cmd_choice)
		
		# add Run button to send the command
		self.runButton = QtGui.QPushButton('Run', self)
		self.runButton.clicked.connect(self.run_button)
		self.runButton.move(320, 50)
		
		
		self.show()
	
	# set text for language choice
	def language_choice(self, text):
		self.languageChoice.setText(text)
		
	
	# set text for category choice
	# also determine the contents in cmdBox, depending on the contents in languageBox and categoryBox
	def category_choice(self, text):
		self.categoryChoice.setText(text)
		
		if self.languageBox.currentText() == "en-US":
			if self.categoryBox.currentText() == "Navigation":
				self.cmdBox.clear()
				list = ["Address book", "Cancel route", "Change home", "Change work", 
						"Destination information", "Find 46501 Commerce Center Dr, Plymouth, Michigan",
						"Find Starbucks", "Frequently visited points", "Go home", "Go to work",
						"Pause route", "Previous destinations", "Previous points", 
						"Previous starting points", "Resume route", "Route options", "Show route",
						"Traffic information", "Turn guidance off", "Turn guidance on", 
						"Zoom in", "Zoom out"]
				self.cmdBox.addItems(list)
				
			elif self.categoryBox.currentText() == "Phone":				
				self.cmdBox.clear()
				list = ["Call", "Call John Smith", "Call John Smith on mobile", "Change Bluetooth device",
						"Dial 2486626203", "Dial number", "Send message to John Smith"]
				self.cmdBox.addItems(list)
				
			elif self.categoryBox.currentText() == "Radio":
				self.cmdBox.clear()
				list = ["AM 1080", "Channel 144", "FM 97.1", "SiriusXM 67"]
				self.cmdBox.addItems(list)
				
		elif self.languageBox.currentText() == "fr-CA":
			if self.categoryBox.currentText() == "Navigation":
				self.cmdBox.clear()
				list = ["Chercher l'adresse en Quebec", "Trouver les banque", "Trajet en pause", "Continuer trajet",
						"Annuler l'itineraire", "Informations de destination", "Points Precedents",
						"Destinations precedentes", "Points de depart precedentes", "Points frequentes",
						"Info. Trafic", "Aller a la Maison", "Modifier Maison", "Aller au travail", "Modifier travail",
						"Options itineraire", "Afficher l'itineraire", "Zoom avant", "Zoom arriere", 
						"Services d'urgences", "Poste de police", "Hopital", "Concession automobile", "Carnet d'Adresses",
						"Assistance routiere", "Navigation vocale activee", "Navigation vocale desactivee"]
				self.cmdBox.addItems(list)
				
			elif self.categoryBox.currentText() == "Phone":
				self.cmdBox.clear()
				list = ["Appeler", "Composer un numero", "Appeler Pierre Durand", "Appeler PierDurand sur cellulaire",
						"Composer 2486626203", "Changer l'appareil Bluetooth"]
				self.cmdBox.addItems(list)
				
			elif self.categoryBox.currentText() == "Radio":
				self.cmdBox.clear()
				list = ["AM 1080", "Canal 144", "FM 97.1", "SiriusXM 144"]
				self.cmdBox.addItems(list)
	
	# set text for command choice
	def cmd_choice(self, text):
		self.cmdChoice.setText(text)
		#print(self.languageChoice.text(), "	", self.categoryChoice.text(), "	", self.cmdChoice.text())
		
	# Run button clicked response
	def run_button(self):
		# English - Navigation
		if self.cmdBox.currentText() == "Address book":
			print("addressBook")
		elif self.cmdBox.currentText() == "Cancel route":
			print("cancelRoute")
		elif self.cmdBox.currentText() == "Change home":
			print("changeHome")
		elif self.cmdBox.currentText() == "Change work":
			print("changeWork")
		elif self.cmdBox.currentText() == "Destination information":
			print("destinationInformation")
		elif self.cmdBox.currentText() == "Find 46501 Commerce Center Drm Plymouth, Michigan":
			print("find46501CommerceCenterDrPlymouthMichigan")
		elif self.cmdBox.currentText() == "Find Starbucks":
			print("findStarbucks")
		elif self.cmdBox.currentText() == "Frequently visited points":
			print("frequentlyVisitedPoints")
		elif self.cmdBox.currentText() == "Go home":
			print("goHome")
		elif self.cmdBox.currentText() == "Go to work":
			print("goToWork")
		elif self.cmdBox.currentText() == "Pause route":
			print("pauseRoute")
		elif self.cmdBox.currentText() == "Previous destinations":
			print("previousDestinations")
		elif self.cmdBox.currentText() == "Previous points":
			print("previousPoints")
		elif self.cmdBox.currentText() == "Previous starting points":
			print("previousStartingPoints")
		elif self.cmdBox.currentText() == "Resume route":
			print("resumeRoute")
		elif self.cmdBox.currentText() == "Route Options":
			print("routeOptions")
		elif self.cmdBox.currentText() == "Show route":
			print("showRoute")
		elif self.cmdBox.currentText() == "Traffic information":
			print("trafficInformation")
		elif self.cmdBox.currentText() == "Turn guidance off":
			print("turnGuidanceOff")
		elif self.cmdBox.currentText() == "Turn guidance on":
			print("turnGuidanceOn")
		elif self.cmdBox.currentText() == "Zoom in":
			print("zoomIn")
		elif self.cmdBox.currentText() == "Zoom out":
			print("zoomOut")
		# English - Phone
		elif self.cmdBox.currentText() == "Call":
			print("call")
		elif self.cmdBox.currentText() == "Call John Smith":
			print("callJohnSmith")
		elif self.cmdBox.currentText() == "Call John Smith on mobile":
			print("callJohnSmithOnMobile")
		elif self.cmdBox.currentText() == "Change Bluetooth Device":
			print("changeBluetoothDevice")
		elif self.cmdBox.currentText() == "Dial 2486626203":
			print("dial2486626203")
		elif self.cmdBox.currentText() == "Dial number":
			print("dialNumber")
		elif self.cmdBox.currentText() == "Send message to John Smith":
			print("sendMessageToJohnSmith")
		# English - Radio
		elif self.cmdBox.currentText() == "AM 1080":
			print("am1080")
		elif self.cmdBox.currentText() == "Channel 144":
			print("channel144")
		elif self.cmdBox.currentText() == "FM 97.1":
			print("fm97.1")
		elif self.cmdBox.currentText() == "SiriusXM 67":
			print("siriusXM67")
		
		# French - Navigation
		elif self.cmdBox.currentText() == "Chercher l'adresse en Quebec":
			print("chercherLadresseEnQuebec")
		elif self.cmdBox.currentText() == "Trouver les banque":
			print("trouverLesBanque")
		elif self.cmdBox.currentText() == "Trajet en pause":
			print("trajetEnPause")
		elif self.cmdBox.currentText() == "Continuer trajet":
			print("continuerTrajet")
		elif self.cmdBox.currentText() == "Annuler l'itineraire":
			print("annulerLitineraire")
		elif self.cmdBox.currentText() == "Informations de destination":
			print("informationsDeDestination")
		elif self.cmdBox.currentText() == "Points Precedents":
			print("pointsPrecedents")
		elif self.cmdBox.currentText() == "Destinations precedentes":
			print("destinationsPrecedentes")
		elif self.cmdBox.currentText() == "Points de depart precedentes":
			print("pointsDeDepartPrecedents")
		elif self.cmdBox.currentText() == "Points frequentes":
			print("pointsFrequentes")
		elif self.cmdBox.currentText() == "Info. Trafic":
			print("")
		elif self.cmdBox.currentText() == "Aller a la Maison":
			print("allerALaMaison")
		elif self.cmdBox.currentText() == "Modifier Maison":
			print("")
		elif self.cmdBox.currentText() == "Info. Trafic":
			print("infoTrafic")
		elif self.cmdBox.currentText() == "Modifier Maison":
			print("modifierMaison")
		elif self.cmdBox.currentText() == "Aller au travail":
			print("allerAuTravail")
		elif self.cmdBox.currentText() == "Modifier Travail":
			print("modifierTravail")
		elif self.cmdBox.currentText() == "Options itineraire":
			print("optionsItineraire")
		elif self.cmdBox.currentText() == "Afficher l'itineraire":
			print("afficherLitineraire")
		elif self.cmdBox.currentText() == "Zoom avant":
			print("zoomAvant")
		elif self.cmdBox.currentText() == "Zoom arriere":
			print("zoomArriere")
		elif self.cmdBox.currentText() == "Services d'urgences":
			print("servicesDurgences")
		elif self.cmdBox.currentText() == "Poste de police":
			print("posteDePolice")
		elif self.cmdBox.currentText() == "Hopital":
			print("hopital")
		elif self.cmdBox.currentText() == "Concession automobile":
			print("concessionAutomobile")
		elif self.cmdBox.currentText() == "Carnet d'Adresses":
			print("carnetDadresse")
		elif self.cmdBox.currentText() == "Assistance routiere":
			print("assistanceRoutiere")
		elif self.cmdBox.currentText() == "Navigation vocale activee":
			print("navigationVocaleActivee")
		elif self.cmdBox.currentText() == "Navigation vocale desactivee":
			print("navigationVocaleDesactivee")
		# French - Phone
		elif self.cmdBox.currentText() == "Appeler":
			print("appeler")
		elif self.cmdBox.currentText() == "Composer un numero":
			print("")
		elif self.cmdBox.currentText() == "Appeler Pierre Durand":
			print("appelerPierreDurand")
		elif self.cmdBox.currentText() == "Appeler PierDurand sur cellulaire":
			print("appelerPierreDurandSurCellulaire")
		elif self.cmdBox.currentText() == "Composer 2486626203":
			print("composer2486626203")
		elif self.cmdBox.currentText() == "Changer l'appareil Bluetooth":
			print("changerLappareilBluetooth")
		# French - Radio
		elif self.cmdBox.currentText() == "AM 1080":
			print("am1080")
		elif self.cmdBox.currentText() == "Canal 144":
			print("canal144")
		elif self.cmdBox.currentText() == "FM 97.1":
			print("fm97.1")
		elif self.cmdBox.currentText() == "SiriusXM 144":
			print("siriusXM144")
		
			
def run():
	app = QtGui.QApplication(sys.argv)	# think of this as the frame of the window
	GUI = Window()
	sys.exit(app.exec_())
	
run()