import pyaudio
import wave
import speech_recognition as sr

CHUNK = 1024

r = sr.Recognizer()
r.energyy_threshold = 4000

# obtain audio from microphone
#source = sr.Microphone(device_index=None, sample_rate=16000, chunk_size=CHUNK)
#with source:
with sr.Microphone() as source:
	#print("Calibrating mic...")
	# listen for 5 seconds and create ambient noise energy level
	#r.adjust_for_ambient_noise(source, duration=2)
	
	print("Spit some fiyah...")
	audio = r.listen(source)
	
# open file for writing results
f = open("vr_out.txt", "w+")
	
# recognize speech using Google
try:
	outStr = r.recognize_google(audio_data=audio, language="fr-CA")
	print("Google thinks you said '" + outStr + "'")
	# f.write("Google thinks you said '" + outStr + "'")
	
except sr.UnknownValueError:
	print("Google could not understand audio")
	# f.write("Google could not understand audio")
except sr.RequestError as e:
	print("Google error; {0}".format(e))
	# f.write("Google error; {0}".format(e))