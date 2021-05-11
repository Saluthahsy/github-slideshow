#!pip install SpeechRecognition
import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('D:\\male.wav') 
with harvard as source:
    audio = r.record(source)
audio_data = r.recognize_google(audio)
#print(audio_data)
                       
import re
                       
search_list = ['Kill','Kidnap','Money']
long_string = audio_data
if re.compile('|'.join(search_list),re.IGNORECASE).search(long_string):
                       print('Threaten Content Present In the Audio')
else:
                       print('Not present, Audio is safe')