import pyaudio
import wave
import speech_recognition as sr
import time
import os
import sys
import codecs
from PyQt4 import Qt, QtGui, QtCore

ADB_DEVICE = "ABC-0123456789"
WAV_PATH_NAME = "Z:/Projects/VR_project/audio_files/"
EXPECTED_OUTPUT_FILE_PATH = "Z:/Projects/VR_project/expected_output_files/"
CHUNK = 1024

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)	
		self.setWindowTitle("VR Test")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

		# add a text label as placeholder for mode choice, hide the text on widget
		self.modeChoice = QtGui.QLabel("Local", self)
		self.modeChoice.hide()
		# add a drop-down box for mode choice
		modeList = ["Local", "Server"]
		self.modeBox = QtGui.QComboBox(self)
		self.modeBox.addItems(modeList)
		self.modeBox.move(20, 30)
		self.modeBox.activated[str].connect(self.mode_choice)
		
		# add a text label as placeholder for language choice, hide the text on widget
		self.languageChoice = QtGui.QLabel("en-US", self)
		self.languageChoice.hide()
		# add a drop-down box for language choice
		languageList = ["en-US", "fr-CA", "es-MX"]
		self.languageBox = QtGui.QComboBox(self)
		self.languageBox.addItems(languageList)
		self.languageBox.move(20, 80)
		self.languageBox.activated[str].connect(self.language_choice)
		
		# add a text label as placeholder for category choice, hide the text on widget
		self.categoryChoice = QtGui.QLabel("Navigation", self)
		self.categoryChoice.hide()
		# add a drop-down box for category choice
		categoryList = ["Navigation", "Phone", "Radio"]
		self.categoryBox = QtGui.QComboBox(self)
		self.categoryBox.addItems(categoryList)
		self.categoryBox.move(120, 80)
		self.categoryBox.activated[str].connect(self.category_choice)
		
		# add a text label as placeholder for command choice, hide the text on widget
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
		self.cmdBox.resize(260, 30)
		self.cmdBox.move(220, 80)
		self.cmdBox.activated[str].connect(self.cmd_choice)
		
		# add Run button to send the command
		self.runButton = QtGui.QPushButton('Run', self)
		self.runButton.clicked.connect(self.run_button)
		self.runButton.move(200, 130)
			
		self.show()
	
	# set text for mode choice
	def mode_choice(self, text):
		self.modeChoice.setText(text)
		self.handle_dropdown()
		
	# set text for language choice
	# also determine the contents in cmdBox, depending on the contents in languageBox and categoryBox
	def language_choice(self, text):
		self.languageChoice.setText(text)
		self.handle_dropdown()
	
	# set text for category choice
	# also determine the contents in cmdBox, depending on the contents in languageBox and categoryBox
	def category_choice(self, text):
		self.categoryChoice.setText(text)
		self.handle_dropdown()
		
	# set text for command choice
	def cmd_choice(self, text):
		self.cmdChoice.setText(text)
	
	# handle dropdown by assigning text to cmdBox, depending on current texts in other boxes
	def handle_dropdown(self):
		if self.modeBox.currentText() == "Local":
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
					
			elif self.languageBox.currentText() == "es-MX":
				if self.categoryBox.currentText() == "Navigation":
					self.cmdBox.clear()
					list = ["Encontrar direccion en California", "Encontrar Bancos", "Reanudar ruta", "Pausar ruta",
							"Cancelar ruta", "Ir a Casa", "Cambiar Casa", "Ir al trabajo", "Cambiar Trabajo",
							"Puntos previos", "Destinos anteriores", "Puntos de inicio anteriores", "Puntos frecuentadoes",
							"Opciones de Ruta", "Liberta de direccion", "Acercar", "Alejar", "Informacion de destino",
							"Informacion del trafico", "Servicios de Emergencia", "Estacion de Policia", "Hospital",
							"Concesionaria", "Asistencia en carretera", "Activar Guia", "Desactivar Guia", "Monstar Ruta"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Phone":
					self.cmdBox.clear()
					list = ["Llamar", "Marcar numero", "Llamar a Juan Garcia", "Llamar a Juan Garcia al movil",
							"Marcar 2486626203", "Cambiar dispositivo Bluetooth"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Radio":
					self.cmdBox.clear()
					list = ["AM 1080", "Canal 144", "FM 97.1", "SiriusXM 144"]
					self.cmdBox.addItems(list)

		elif self.modeBox.currentText() == "Server":
			if self.languageBox.currentText() == "en-US":
				if self.categoryBox.currentText() == "Navigation":
					self.cmdBox.clear()
					list = ["server english navigation"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Phone":				
					self.cmdBox.clear()
					list = ["server english phone"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Radio":
					self.cmdBox.clear()
					list = ["server english radio"]
					self.cmdBox.addItems(list)
					
			elif self.languageBox.currentText() == "fr-CA":
				if self.categoryBox.currentText() == "Navigation":
					self.cmdBox.clear()
					list = ["server french navigation"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Phone":
					self.cmdBox.clear()
					list = ["server french phone"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Radio":
					self.cmdBox.clear()
					list = ["server french radio"]
					self.cmdBox.addItems(list)
					
			elif self.languageBox.currentText() == "es-MX":
				if self.categoryBox.currentText() == "Navigation":
					self.cmdBox.clear()
					list = ["server spanish navigation"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Phone":
					self.cmdBox.clear()
					list = ["server spanish phone"]
					self.cmdBox.addItems(list)
					
				elif self.categoryBox.currentText() == "Radio":
					self.cmdBox.clear()
					list = ["server spanish radio"]
					self.cmdBox.addItems(list)
		
	# Run button clicked response
	def run_button(self):
		print("==================================================================")
		print("Running test case...")
		cmd = ""
		
		result = ""
		
		if self.languageBox.currentText() == "en-US":
		# English - Navigation
			if self.cmdBox.currentText() == "Address book":
				print("addressBook")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/addressBook")
			elif self.cmdBox.currentText() == "Cancel route":
				print("cancelRoute")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/cancelRoute")
			elif self.cmdBox.currentText() == "Change home":
				print("changeHome")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/changeHome")
			elif self.cmdBox.currentText() == "Change work":
				print("changeWork")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/changeWork")
			
			# HU RESPONSE DEPENDS ON LOCATION... FIND SOME WAY TO NOTIFY USER
			elif self.cmdBox.currentText() == "Destination information":
				print("destinationInformation")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/destinationInformation")
			
			
			elif self.cmdBox.currentText() == "Find 46501 Commerce Center Drm Plymouth, Michigan":
				print("find46501CommerceCenterDrPlymouthMichigan")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/find46501CommerceCenterDrPlymouthMichigan")
			elif self.cmdBox.currentText() == "Find Starbucks":
				print("findStarbucks")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/findStarbucks")
			elif self.cmdBox.currentText() == "Frequently visited points":
				print("frequentlyVisitedPoints")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/frequentlyVisitedPoints")
			elif self.cmdBox.currentText() == "Go home":
				print("goHome")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/goHome")
			elif self.cmdBox.currentText() == "Go to work":
				print("goToWork")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/goToWork")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Pause route":
				print("pauseRoute")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/pauseRoute")
			
			
			elif self.cmdBox.currentText() == "Previous destinations":
				print("previousDestinations")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/previousDestinations")
			elif self.cmdBox.currentText() == "Previous points":
				print("previousPoints")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/previousPoints")
			elif self.cmdBox.currentText() == "Previous starting points":
				print("previousStartingPoints")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/previousStartingPoints")
			
			#NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Resume route":
				print("resumeRoute")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/resumeRoute")
			
			
			elif self.cmdBox.currentText() == "Route Options":
				print("routeOptions")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/routeOptions")
			elif self.cmdBox.currentText() == "Show route":
				print("showRoute")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/showRoute")
			elif self.cmdBox.currentText() == "Traffic information":
				print("trafficInformation")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/trafficInformation")
			elif self.cmdBox.currentText() == "Turn guidance off":
				print("turnGuidanceOff")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/turnGuidanceOff")
			elif self.cmdBox.currentText() == "Turn guidance on":
				print("turnGuidanceOn")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/turnGuidanceOn")
			elif self.cmdBox.currentText() == "Zoom in":
				print("zoomIn")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/zoomIn")
			elif self.cmdBox.currentText() == "Zoom out":
				print("zoomOut")
				result = vrTest(ADB_DEVICE, "en-US", "Navigation/zoomOut")
			# English - Phone
			elif self.cmdBox.currentText() == "Call":
				print("call")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/call")
			elif self.cmdBox.currentText() == "Call John Smith":
				print("callJohnSmith")
				result = vvrTest(ADB_DEVICE, "en-US", "Phone/callJohnSmith")
			elif self.cmdBox.currentText() == "Call John Smith on mobile":
				print("callJohnSmithOnMobile")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/callJohnSmithOnMobile")
			elif self.cmdBox.currentText() == "Change Bluetooth Device":
				print("changeBluetoothDevice")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/changeBluetoothDevice")
			elif self.cmdBox.currentText() == "Dial 2486626203":
				print("dial2486626203")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/dial2486626203")
			elif self.cmdBox.currentText() == "Dial number":
				print("dialNumber")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/dialNumber")
			elif self.cmdBox.currentText() == "Send message to John Smith":
				print("sendMessageToJohnSmith")
				result = vrTest(ADB_DEVICE, "en-US", "Phone/sendMessageToJohnSmith")
			# English - Radio
			elif self.cmdBox.currentText() == "AM 1080":
				print("am1080en")
				result = vrTest(ADB_DEVICE, "en-US", "Radio/am1080en")
			elif self.cmdBox.currentText() == "Channel 144":
				print("channel144en")
				result = vrTest(ADB_DEVICE, "en-US", "Radio/channel144enen")
			elif self.cmdBox.currentText() == "FM 97.1":
				print("fm97.1en")
				result = vrTest(ADB_DEVICE, "en-US", "Radio/fm97.1en")
			elif self.cmdBox.currentText() == "SiriusXM 67":
				print("siriusXM67en")
				result = vrTest(ADB_DEVICE, "en-US", "Radio/siriusXM67en")
		
		# French - Navigation
		elif self.languageBox.currentText() == "fr-CA":
			if self.cmdBox.currentText() == "Chercher l'adresse en Quebec":
				print("chercherLadresseEnQuebec")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/chercherLadresseEnQuebec")
			elif self.cmdBox.currentText() == "Trouver les banque":
				print("trouverLesBanque")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/trouverLesBanque")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Trajet en pause":
				print("trajetEnPause")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/trajetEnPause")
			elif self.cmdBox.currentText() == "Continuer trajet":
				print("continuerTrajet")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/continuerTrajet")
			
			# RE-RECORD annulerLitineraire.wav
			elif self.cmdBox.currentText() == "Annuler l'itineraire":
				print("annulerLitineraire")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/annulerLitineraire")
			
			# HU RESPONSE DEPENDS ON LOCATION... FIND SOME WAY TO NOTIFY USER
			elif self.cmdBox.currentText() == "Informations de destination":
				print("informationsDeDestination")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/informationsDeDestination")
			
			
			elif self.cmdBox.currentText() == "Points Precedents":
				print("pointsPrecedents")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/pointsPrecedents")
			elif self.cmdBox.currentText() == "Destinations precedentes":
				print("destinationsPrecedentes")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/destinationsPrecedentes")
			elif self.cmdBox.currentText() == "Points de depart precedentes":
				print("pointsDeDepartPrecedents")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/pointsDeDepartPrecedents")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Points frequentes":
				print("pointsFrequentes")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/pointsFrequentes")
			
			
			elif self.cmdBox.currentText() == "Aller a la Maison":
				print("allerALaMaison")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/allerALaMaison")
			elif self.cmdBox.currentText() == "Info. Trafic":
				print("infoTrafic")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/infoTrafic")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Modifier Maison":
				print("modifierMaison")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/modifierMaison")
			
			
			elif self.cmdBox.currentText() == "Aller au travail":
				print("allerAuTravail")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/allerAuTravail")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Modifier travail":
				print("modifierTravail")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/modifierTravail")
			
			
			elif self.cmdBox.currentText() == "Options itineraire":
				print("optionsItineraire")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/optionsItineraire")
			elif self.cmdBox.currentText() == "Afficher l'itineraire":
				print("afficherLitineraire")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/afficherLitineraire")
			elif self.cmdBox.currentText() == "Zoom avant":
				print("zoomAvant")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/zoomAvant")
			elif self.cmdBox.currentText() == "Zoom arriere":
				print("zoomArriere")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/zoomArriere")
			elif self.cmdBox.currentText() == "Services d'urgences":
				print("servicesDurgences")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/servicesDurgences")
			elif self.cmdBox.currentText() == "Poste de police":
				print("posteDePolice")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/posteDePolice")
			elif self.cmdBox.currentText() == "Hopital":
				print("hopital")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/hopital")
			elif self.cmdBox.currentText() == "Concession automobile":
				print("concessionAutomobile")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/concessionAutomobile")
			elif self.cmdBox.currentText() == "Carnet d'Adresses":
				print("carnetDadresse")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/carnetDadresse")
			elif self.cmdBox.currentText() == "Assistance routiere":
				print("assistanceRoutiere")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/assistanceRoutiere")
			elif self.cmdBox.currentText() == "Navigation vocale activee":
				print("navigationVocaleActivee")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/navigationVocaleActivee")
			elif self.cmdBox.currentText() == "Navigation vocale desactivee":
				print("navigationVocaleDesactivee")
				result = vrTest(ADB_DEVICE, "fr-CA", "Navigation/navigationVocaleDesactivee")
			# French - Phone
			elif self.cmdBox.currentText() == "Appeler":
				print("appeler")
				result = vrTest(ADB_DEVICE, "fr-CA", "Phone/appeler")
		
			
			elif self.cmdBox.currentText() == "Composer un numero":
				print("ASDFS BAFDG")
			
			
			elif self.cmdBox.currentText() == "Appeler Pierre Durand":
				print("appelerPierreDurand")
				result = vrTest(ADB_DEVICE, "fr-CA", "Phone/appelerPierreDurand")
			elif self.cmdBox.currentText() == "Appeler PierDurand sur cellulaire":
				print("appelerPierreDurandSurCellulaire")
				result = vrTest(ADB_DEVICE, "fr-CA", "Phone/appelerPierreDurandSurCellulaire")
			elif self.cmdBox.currentText() == "Composer 2486626203":
				print("composer2486626203")
				result = vrTest(ADB_DEVICE, "fr-CA", "Phone/composer2486626203")
			elif self.cmdBox.currentText() == "Changer l'appareil Bluetooth":
				print("changerLappareilBluetooth")
				result = vrTest(ADB_DEVICE, "fr-CA", "Phone/changerLappareilBluetooth")
			# French - Radio
			elif self.cmdBox.currentText() == "AM 1080":
				print("am1080fr")
				result = vrTest(ADB_DEVICE, "fr-CA", "Radio/am1080fr")
			elif self.cmdBox.currentText() == "Canal 144":
				print("canal144fr")
				result = vrTest(ADB_DEVICE, "fr-CA", "Radio/canal144fr")
			elif self.cmdBox.currentText() == "FM 97.1":
				print("fm97.1fr")
				result = vrTest(ADB_DEVICE, "fr-CA", "Radio/fm97.1fr")
			elif self.cmdBox.currentText() == "SiriusXM 144":
				print("siriusXM144fr")
				result = vrTest(ADB_DEVICE, "fr-CA", "Radio/siriusXM144fr")
		
		# Spanish - Navigation
		elif self.languageBox.currentText() == "es-MX":
			if self.cmdBox.currentText() == "Encontrar direccion en California":
				print("encontrarDireccionEnCalifornia")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/encontrarDireccionEnCalifornia")
			elif self.cmdBox.currentText() == "Encontrar Bancos":
				print("encontrarBancos")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/encontrarBancos")
			
			# NEED RESPONSE FROM NEW SW
			elif self.cmdBox.currentText() == "Reanudar ruta":
				print("reanudarRuta")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/reanudarRuta")
			elif self.cmdBox.currentText() == "Pausar ruta":
				print("pausarRuta")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/pausarRuta")
			
			
			elif self.cmdBox.currentText() == "Cancelar ruta":
				print("cancelarRuta")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/cancelarRuta")
			elif self.cmdBox.currentText() == "Ir a Casa":
				print("irACasa")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/irACasa")
			elif self.cmdBox.currentText() == "Cambiar Casa":
				print("cambiarCasa")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/cambiarCasa")
			elif self.cmdBox.currentText() == "Ir al trabajo":
				print("irAlTrabajo")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/irAlTrabajo")
			elif self.cmdBox.currentText() == "Cambiar Trabajo":
				print("cambiarTrabajo")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/cambiarTrabajo")
			elif self.cmdBox.currentText() == "Puntos previos":
				print("puntosPrevios")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/puntosPrevios")
			elif self.cmdBox.currentText() == "Destinos anteriores":
				print("destinosAnteriores")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/destinosAnteriores")
			elif self.cmdBox.currentText() == "Puntos de inicio anteriores":
				print("puntosDeInicioAnteriores")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/puntosDeInicioAnteriores")
			elif self.cmdBox.currentText() == "Puntos frecuentados":
				print("puntosFrecuentados")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/puntosFrecuentados")
			elif self.cmdBox.currentText() == "Opciones de Ruta":
				print("opcionesDeRuta")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/opcionesDeRuta")
			elif self.cmdBox.currentText() == "Liberta de direccion":
				print("libertaDeDireccion")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/libertaDeDireccion")
			elif self.cmdBox.currentText() == "Acercar":
				print("acercar")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/acercar")
			elif self.cmdBox.currentText() == "Alejar":
				print("alejar")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/alejar")
			
			# HU RESPONSE DEPENDS ON LOCATION... FIND SOME WAY TO NOTIFY USER
			elif self.cmdBox.currentText() == "Informacion de destino":
				print("informacionDeDestino")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/informacionDeDestino")
			
			
			elif self.cmdBox.currentText() == "Informacion del trafico":
				print("informacionDelTrafico")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/informacionDelTrafico")
			elif self.cmdBox.currentText() == "Servicios de Emergencia":
				print("serviciosDeEmergencia")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/serviciosDeEmergencia")
			elif self.cmdBox.currentText() == "Estacion de Policia":
				print("estacionDePolicia")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/estacionDePolicia")
			elif self.cmdBox.currentText() == "Hospital":
				print("hospital")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/hospital")
			elif self.cmdBox.currentText() == "Concesionaria":
				print("concesionaria")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/concesionaria")
			elif self.cmdBox.currentText() == "Asistencia en carretera":
				print("asistenciaEnCarretera")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/asistenciaEnCarretera")
			elif self.cmdBox.currentText() == "Activar Guia":
				print("activarGuia")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/activarGuia")
			elif self.cmdBox.currentText() == "Desactivar Guia":
				print("desactivarGuia")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/desactivarGuia")
			elif self.cmdBox.currentText() == "Mostrar Ruta":
				print("mostrarRuta")
				result = vrTest(ADB_DEVICE, "es-MX", "Navigation/mostrarRuta")
			# Spanish - Phone
			elif self.cmdBox.currentText() == "Llamar":
				print("llamar")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/llamar")
			elif self.cmdBox.currentText() == "Marcar numero":
				print("marcarNumero")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/marcarNumero")
			elif self.cmdBox.currentText() == "Llamar a Juan Garcia":
				print("llamarAJuanGarcia")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/llamarAJuanGarcia")
			elif self.cmdBox.currentText() == "Llamar a Juan Garcia al movil":
				print("llamarAJuanGarciaAlMovil")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/llamarAJuanGarciaAlMovil")
			elif self.cmdBox.currentText() == "Marcar 2486626203":
				print("marcar2486626203")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/marcar2486626203")
			elif self.cmdBox.currentText() == "Cambiar dispositivo Bluetooth":
				print("cambiarDispositivoBluetooth")
				result = vrTest(ADB_DEVICE, "es-MX", "Phone/cambiarDispositivoBluetooth")
			# Spanish - Radio
			elif self.cmdBox.currentText() == "AM 1080":
				if self.languageBox.currentText() == "es-MX":
					print("am1080es")
					result = vrTest(ADB_DEVICE, "es-MX", "Radio/am1080es")
			elif self.cmdBox.currentText() == "Canal 144":
				if self.languageBox.currentText() == "es-MX":	
					print("canal144es")
					result = vrTest(ADB_DEVICE, "es-MX", "Radio/canal144es")
			elif self.cmdBox.currentText() == "FM 97.1":
				if self.languageBox.currentText() == "es-MX":
					print("fm97.1es")
					result = vrTest(ADB_DEVICE, "es-MX", "Radio/fm97.1es")
			elif self.cmdBox.currentText() == "SiriusXM 144":
				if self.languageBox.currentText() == "es-MX":	
					print("siriusXM144es")
					result = vrTest(ADB_DEVICE, "es-MX", "Radio/siriusXM144es")
	
		print(result)
		
		# display test results using popup
		resultPopup = QtGui.QMessageBox()
		resultPopup.setWindowTitle("VR Test Result")
		resultPopup.setText(result)
		resultPopup.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		resultPopup.exec_()
		
		print("==================================================================")	
		
		
# execute the VR test
def vrTest(ADB_DEVICE, lang, testCase):
	print("vrStart")
	vrStart(ADB_DEVICE)
	print("vrInput")
	vrInput(WAV_PATH_NAME, lang, testCase)
	print("vrOutput")
	vrOutput(lang)
	expectedOutputFile = EXPECTED_OUTPUT_FILE_PATH + testCase + "_out.txt"
	result = checkOutput('out.txt', expectedOutputFile)
	return result

# initiate voice recognition on HU through ADB	
def vrStart(ADB_DEVICE):
	cmd = "adb -s " + ADB_DEVICE + " shell input keyevent KEYCODE_SHORTCUT_PTT"
	os.system(cmd)
	time.sleep(3)
		
# WAV_PATH_NAME is the path name of the directory where .wav files are saved
# lang is the current language
# testCase is a string in the form of [category]/[command]
def vrInput(WAV_PATH_NAME, lang, testCase):
	# VR input from PC to HU
	
	file = ""
	if lang == "en-US":
		file = WAV_PATH_NAME + "English/" + testCase + ".wav"
	elif lang == "fr-CA":
		file = WAV_PATH_NAME + "French/" + testCase + ".wav"
	elif lang == "es-MX":
		file = WAV_PATH_NAME + "Spanish/" + testCase + ".wav"
	
	# prepare to play .wav file
	wf = wave.open(file, 'rb')

	# instantiate PyAudio
	p = pyaudio.PyAudio()

	# open stream
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), 
					channels=wf.getnchannels(), 
					rate=wf.getframerate(), 
					output=True)

	data = wf.readframes(CHUNK)

	while len(data) > 0:
		stream.write(data)
		data = wf.readframes(CHUNK)

	# stop stream
	stream.stop_stream()
	stream.close()

	# close PyAudio
	p.terminate()

# VR output from HU to PC	
def vrOutput(lang):
	r = sr.Recognizer()		# create an instance of Recognizer object from speech_recognition
	r.energy_threshold = 4000	# for handling noise
	f = codecs.open('out.txt', 'w', encoding = 'utf8')
	# obtain audio from microphone
	with sr.Microphone() as source:
		print("Listening...")
		audio = r.listen(source)
	
	# open file to write results; change encoding to UTF-8 to accommodate French and Spanish chars
	f = codecs.open('out.txt', 'w', encoding = 'utf8')	 
	
	# recognize speech using Google
	try:
		print("Writing results to <out.txt>...")
		# print("Google thinks you said '" + r.recognize_google(audio_data=audio, language=lang) + "'")
		f.write(r.recognize_google(audio_data=audio, language=lang))
		print("Done.")
	except sr.UnknownValueError:
		print("Google could not understand audio")
		f.write("Google could not understand audio")
	except sr.RequestError as e:
		print("Google error; {0}".format(e))
		f.write("Google error; {0}".format(e))
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# check VR output by comparing string from output file against that from expected output file
def checkOutput(outputFile, expectedOutputFile):
	f = codecs.open(outputFile, 'r', encoding = 'utf8')
	output = f.readline()
	#output = output.replace(" ", "")	# remove space characters for comparison
	#output = output.lower()			# change all characters to lower case for comparison
			
	f = codecs.open(expectedOutputFile, 'r', encoding = 'utf8')
	expectedOutput = f.readline()
	#expectedOutput = expectedOutput.replace(" ", "")	# remove space characters for comparison
	#expectedOutput = expectedOutput.lower()			# change all characters to lower case for comparison
	
	result = ""
	if output == expectedOutput:
		result = "VR output matches expected output. \n\nPASS"
	else:
		result = "VR output does not match expected output. \n(Make sure test conditions are correct, and minimize surrounding noise.) \n\nFAIL"
	
	return result
	
# a high-level function for running the GUI		
def run():
	# os.system("chcp 65001")	# change the active code page in order to display foreign chars on Windows command line
	app = QtGui.QApplication(sys.argv)	# think of app object as the frame of the window
	GUI = Window()
	sys.exit(app.exec_())
	
run()