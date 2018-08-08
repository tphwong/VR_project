import pyaudio
import wave
import speech_recognition as sr

CHUNK = 1024

r = sr.Recognizer()
r.energy_threshold = 4000

# obtain audio from microphone
#source = sr.Microphone(device_index=None, sample_rate=16000, chunk_size=CHUNK)
#with source:
with sr.Microphone() as source:
	#print("Calibrating mic...")
	# listen for 5 seconds and create ambient noise energy level
	#r.adjust_for_ambient_noise(source, duration=2)
	
	print("Spit some fiyah...")
	audio = r.listen(source)
	
# recognize speech using Sphinx
try:
	print("Sphinx thinks you said '" + r.recognize_sphinx(audio_data=audio, language="en-US") + "'")
except sr.UnknownValueError:
	print("Sphinx could not understand audio")
except sr.RequestError as e:
	print("Sphinx error; {0}".format(e))