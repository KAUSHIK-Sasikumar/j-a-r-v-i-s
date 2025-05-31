import pyttsx3, speech_recognition as sr, datetime

engine = pyttsx3.init()
engine.setProperty('voice', pyttsx3.init().getProperty('voices')[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning, Kaushik.")
    elif hour < 18:
        speak("Good afternoon, Kaushik.")
    else:
        speak("Good evening, Kaushik.")
    speak("Jarvis is now online.")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"User: {command}")
        return command.lower()
    except:
        speak("Sorry, please say that again.")
        return "none"
