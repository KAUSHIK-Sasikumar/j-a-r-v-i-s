from assistant.voice import speak, take_command, wish_me
from assistant.commands import handle_command
import threading

def run_jarvis():
    wish_me()
    while True:
        command = take_command()
        if command == "none":
            continue
        if "exit" in command or "stop" in command:
            speak("Goodbye Kaushik!")
            break
        handle_command(command)

if __name__ == "__main__":
    run_jarvis()
