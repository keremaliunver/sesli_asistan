import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Dinleniyor...')
    audio=r.record(source, duration=5)
    try:
        str=r.recognize_google(audio,language="tr-tr")
        print(str)
    except:
        print("Bir hata var :( ")
