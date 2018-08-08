import pyaudio
import wave
import speech_recognition as sr

CHUNK = 1024

# obtain audio from microphone

r = sr.Recognizer()

#with sr.Microphone() as source:
source = sr.Microphone(device_index: Union[int, None] = None, sample_rate: int = 16000, chunk_size: int = CHUNK)
	print("Calibrating mic...")
	
	# listen for 5 seconds and create ambient noise energy level
	r.adjust_for_ambient_noise(source, duration=5)
	
	print("Say something...")
	audio = r.listen(source)
	
# recognize speech using Sphinx
try:
	print("Sphinx thinks you said ' " + r.recognize_sphinx(audio) + "'")
except sr.UnknownValueError:
	print("Sphinx could not understand audio")
except sr.RequestError as e:
	print("Sphinx error; {0}".format(e))