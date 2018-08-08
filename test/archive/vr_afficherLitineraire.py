import os
import pyaudio
import wave
import speech_recognition as sr
import time

CHUNK = 1024

# initiate voice recognition on HU through ADB
ADB_DEVICE = "ABC-0123456789"
cmd = "adb -s " + ADB_DEVICE + " shell input keyevent KEYCODE_SHORTCUT_PTT"
os.system(cmd)
time.sleep(3)

# ==========================================
# VR input from PC to HU

# prepare to play .wav file
wf = wave.open("Z:/Projects/VR_project/audio_files/French/Navigation/afficherLitineraire.wav", 'rb')

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

# ==========================================
# VR output from HU to PC

r = sr.Recognizer()
r.energy_threshold = 4000

# obtain audio from microphone
with sr.Microphone() as source:
	print("Spit some fiyah...")
	audio = r.listen(source)
	
# recognize speech using Google
try:
	print("Google thinks you said '" + r.recognize_google(audio_data=audio, language="fr-CA") + "'")
except sr.UnknownValueError:
	print("Google could not understand audio")
except sr.RequestError as e:
	print("Google error; {0}".format(e))