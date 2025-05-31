import webbrowser, os, datetime
import wikipedia
from assistant.voice import speak
from assistant.chatgpt import chat_with_gpt
from assistant.emailer import send_email
from assistant.weather import get_weather

def handle_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "play music" in command:
        music_dir = "C:\\Users\\Kaushik\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif "weather" in command:
        city = command.replace("weather in", "").strip()
        weather_info = get_weather(city)
        speak(weather_info)

    elif "email" in command:
        speak("What should I say?")
        content = take_command()
        send_email(content)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn’t fetch the Wikipedia data.")

    else:
        # Fallback to GPT
        response = chat_with_gpt(command)
        speak(response)
