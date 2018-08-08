import os
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
				
	# Run button clicked response
	def run_button(self):
		cmd = ""
		# English - Navigation
		if self.cmdBox.currentText() == "Address book":
			print("addressBook")
			cmd = "python addressBook.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Cancel route":
			print("cancelRoute")
			cmd = "python cancelRoute.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Change home":
			print("changeHome")
			cmd = "python changeHome.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Change work":
			print("changeWork")
			cmd = "python changeWork.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Destination information":
			print("destinationInformation")
			cmd = "python destinationInformation.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Find 46501 Commerce Center Drm Plymouth, Michigan":
			print("find46501CommerceCenterDrPlymouthMichigan")
			cmd = "python find46501CommerceCenterDrPlymouthMichigan.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Find Starbucks":
			print("findStarbucks")
			cmd = "python findStarbucks.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Frequently visited points":
			print("frequentlyVisitedPoints")
			cmd = "python frequentlyVisitedPoints.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Go home":
			print("goHome")
			cmd = "python goHome.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Go to work":
			print("goToWork")
			cmd = "python goToWork.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Pause route":
			print("pauseRoute")
			cmd = "python pauseRoute.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Previous destinations":
			print("previousDestinations")
			cmd = "python previousDestinations.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Previous points":
			print("previousPoints")
			cmd = "python previousPoints.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Previous starting points":
			print("previousStartingPoints")
			cmd = "python previousStartingPoints.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Resume route":
			print("resumeRoute")
			cmd = "python resumeRoute.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Route Options":
			print("routeOptions")
			cmd = "python routeOptions.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Show route":
			print("showRoute")
			cmd = "python showRoute.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Traffic information":
			print("trafficInformation")
			cmd = "python trafficInformation.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Turn guidance off":
			print("turnGuidanceOff")
			cmd = "python turnGuidanceOff.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Turn guidance on":
			print("turnGuidanceOn")
			cmd = "python turnGuidanceOn.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Zoom in":
			print("zoomIn")
			cmd = "python zoomIn.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Zoom out":
			print("zoomOut")
			cmd = "python zoomOut.py"
			os.system(cmd)
		# English - Phone
		elif self.cmdBox.currentText() == "Call":
			print("call")
			cmd = "python call.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Call John Smith":
			print("callJohnSmith")
			cmd = "python callJohnSmith.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Call John Smith on mobile":
			print("callJohnSmithOnMobile")
			cmd = "python callJohnSmithOnMobile.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Change Bluetooth Device":
			print("changeBluetoothDevice")
			cmd = "python changeBluetoothDevice.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Dial 2486626203":
			print("dial2486626203")
			cmd = "python dial2486626203.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Dial number":
			print("dialNumber")
			cmd = "python dialNumber.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Send message to John Smith":
			print("sendMessageToJohnSmith")
			cmd = "python sendMessageToJohnSmith.py"
			os.system(cmd)
		# English - Radio
		elif self.cmdBox.currentText() == "AM 1080":
			print("am1080en")
			cmd = "python am1080en.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Channel 144":
			print("channel144en")
			cmd = "python channel144en.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "FM 97.1":
			print("fm97.1en")
			cmd = "python fm97.1en.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "SiriusXM 67":
			print("siriusXM67en")
			cmd = "python siriusXM67en.py"
			os.system(cmd)
		
		# French - Navigation
		elif self.cmdBox.currentText() == "Chercher l'adresse en Quebec":
			print("chercherLadresseEnQuebec")
			cmd = "python chercherLadresseEnQuebec.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Trouver les banque":
			print("trouverLesBanque")
			cmd = "python trouverLesBanque.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Trajet en pause":
			print("trajetEnPause")
			cmd = "python trajetEnPause.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Continuer trajet":
			print("continuerTrajet")
			cmd = "python continuerTrajet.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Annuler l'itineraire":
			print("annulerLitineraire")
			cmd = "python annulerLitineraire.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Informations de destination":
			print("informationsDeDestination")
			cmd = "python informationsDeDestination.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Points Precedents":
			print("pointsPrecedents")
			cmd = "python pointsPrecedents.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Destinations precedentes":
			print("destinationsPrecedentes")
			cmd = "python destinationsPrecedentes.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Points de depart precedentes":
			print("pointsDeDepartPrecedents")
			cmd = "python pointsDeDepartPrecedents.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Points frequentes":
			print("pointsFrequentes")
			cmd = "python pointsFrequentes.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Aller a la Maison":
			print("allerALaMaison")
			cmd = "python allerALaMaison.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Info. Trafic":
			print("infoTrafic")
			cmd = "python infoTrafic.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Modifier Maison":
			print("modifierMaison")
			cmd = "python modifierMaison.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Aller au travail":
			print("allerAuTravail")
			cmd = "python allerAuTravail.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Modifier Travail":
			print("modifierTravail")
			cmd = "python modifierTravail.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Options itineraire":
			print("optionsItineraire")
			cmd = "python optionsItineraire.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Afficher l'itineraire":
			print("afficherLitineraire")
			cmd = "python afficherLitineraire.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Zoom avant":
			print("zoomAvant")
			cmd = "python zoomAvant.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Zoom arriere":
			print("zoomArriere")
			cmd = "python zoomArriere.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Services d'urgences":
			print("servicesDurgences")
			cmd = "python servicesDurgences.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Poste de police":
			print("posteDePolice")
			cmd = "python posteDePolice.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Hopital":
			print("hopital")
			cmd = "python hopital.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Concession automobile":
			print("concessionAutomobile")
			cmd = "python concessionAutomobile.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Carnet d'Adresses":
			print("carnetDadresse")
			cmd = "python carnetDadresse.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Assistance routiere":
			print("assistanceRoutiere")
			cmd = "python assistanceRoutiere.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Navigation vocale activee":
			print("navigationVocaleActivee")
			cmd = "python navigationVocaleActivee.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Navigation vocale desactivee":
			print("navigationVocaleDesactivee")
			cmd = "python navigationVocaleDesactivee.py"
			os.system(cmd)
		# French - Phone
		elif self.cmdBox.currentText() == "Appeler":
			print("appeler")
			cmd = "python appeler.py"
			os.system(cmd)
		
		#elif self.cmdBox.currentText() == "Composer un numero":
		#	print("")
		
		elif self.cmdBox.currentText() == "Appeler Pierre Durand":
			print("appelerPierreDurand")
			cmd = "python appelerPierreDurand.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Appeler PierDurand sur cellulaire":
			print("appelerPierreDurandSurCellulaire")
			cmd = "python appelerPierreDurandSurCellulaire.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Composer 2486626203":
			print("composer2486626203")
			cmd = "python composer2486626203.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Changer l'appareil Bluetooth":
			print("changerLappareilBluetooth")
			cmd = "python changerLappareilBluetooth.py"
			os.system(cmd)
		# French - Radio
		elif self.cmdBox.currentText() == "AM 1080":
			print("am1080fr")
			cmd = "python am1080fr.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Canal 144":
			print("canal144fr")
			cmd = "python canal144fr.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "FM 97.1":
			print("fm97.1fr")
			cmd = "python fm97.1fr.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "SiriusXM 144":
			print("siriusXM144fr")
			cmd = "python siriusXM144fr.py"
			os.system(cmd)
		
		# Spanish - Navigation
		elif self.cmdBox.currentText() == "Encontrar direccion en California":
			print("encountrarDireccionEnCalifornia")
			cmd = "encountrarDireccionEnCalifornia.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Encontrar Bancos":
			print("encontrarBancos")
			cmd = "python encontrarBancos.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Reanudar ruta":
			print("reanudarRuta")
			cmd = "python reanudarRuta.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Pausar ruta":
			print("pausarRuta")
			cmd = "python pausarRuta.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Cancelar ruta":
			print("cancelarRuta")
			cmd = "python cancelarRuta.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Ir a Casa":
			print("irACasa")
			cmd = "python irACasa.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Cambiar Casa":
			print("cambiarCasa")
			cmd = "python cambiarCasa.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Ir al trabajo":
			print("irAlTrabajo")
			cmd = "python irAlTrabajo.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Cambiar Trabajo":
			print("cambiarTrabajo")
			cmd = "python cambiarTrabajo.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Puntos previos":
			print("puntosPrevios")
			cmd = "python puntosPrevios.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Destinos anteriores":
			print("destinosAnteriores")
			cmd = "python destinosAnteriores.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Puntos de inicio anteriores":
			print("puntosDeInicioAnteriores")
			cmd = "python puntosDeInicioAnteriores.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Puntos frecuentados":
			print("puntosFrecuentados")
			cmd = "python puntosFrecuentados.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Opciones de Ruta":
			print("opcionesDeRuta")
			cmd = "python opcionesDeRuta.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Liberta de direccion":
			print("libertaDeDireccion")
			cmd = "python libertaDeDireccion.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Acercar":
			print("acercar")
			cmd = "python acercar.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Alejar":
			print("alejar")
			cmd = "python alejar.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Informacion de destino":
			print("informacionDeDestino")
			cmd = "python informacionDeDestino.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Informacion del trafico":
			print("informacionDelTrafico")
			cmd = "python informacionDelTrafico.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Servicios de Emergencia":
			print("serviciosDeEmergencia")
			cmd = "python serviciosDeEmergencia.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Estacion de Policia":
			print("estacionDePolicia")
			cmd = "python estacionDePoliciapy"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Hospital":
			print("hospital")
			cmd = "python hospital.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Concesionaria":
			print("concesionaria")
			cmd = "python concesionaria.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Asistencia en carretera":
			print("asistenciaEnCarretera")
			cmd = "python asistenciaEnCarretera.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Activar Guia":
			print("activarGuia")
			cmd = "python activarGuia.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Desactivar Guia":
			print("desactivarGuia")
			cmd = "python desactivarGuia.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Mostrar Ruta":
			print("mostrarRuta")
			cmd = "python mostrarRuta.py"
			os.system(cmd)
		# Spanish - Phone
		elif self.cmdBox.currentText() == "Llamar":
			print("llamar")
			cmd = "python llamar.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Marcar numero":
			print("marcarNumero")
			cmd = "python marcarNumero.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Llamar a Juan Garcia":
			print("llamarAJuanGarcia")
			cmd = "python llamarAJuanGarcia.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Llamar a Juan Garcia al movil":
			print("llamarAJuanGarciaAlMovil")
			cmd = "python llamarAJuanGarciaAlMovil.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Marcar 2486626203":
			print("marcar2486626203")
			cmd = "python marcar2486626203.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Cambiar dispositivo Bluetooth":
			print("cambiarDispositivoBluetooth")
			cmd = "python cambiarDispositivoBluetooth.py"
			os.system(cmd)
		# Spanish - Radio
		elif self.cmdBox.currentText() == "AM 1080":
			print("am1080es")
			cmd = "python am1080es.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "Canal 144":
			print("canal144es")
			cmd = "python canal144es.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "FM 97.1":
			print("fm97.1es")
			cmd = "python fm97.1es.py"
			os.system(cmd)
		elif self.cmdBox.currentText() == "SiriusXM 144":
			print("siriusXM144es")
			cmd = "python siriusXM144es.py"
			os.system(cmd)
			
def run():
	app = QtGui.QApplication(sys.argv)	# think of this as the frame of the window
	GUI = Window()
	sys.exit(app.exec_())
	
run()