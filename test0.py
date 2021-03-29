import speech_recognition as sr
import pyaudio
import pyttsx3

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Wait a sec...")
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Okay! Say something!")
    audio = r.listen(source, timeout=3)

result=""
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    result = r.recognize_google(audio).lower()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    result = ""
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    result = ""

response = ""

if result == "hello":
    response = "Hi there"
elif result == "what's your name" or result == "who are you":
    response = "I am Lenny, your virtual assistant"
else:
    response = "sorry, i don't understand that... yet"

speaker = pyttsx3.init()
speaker.say(response)
speaker.runAndWait()

