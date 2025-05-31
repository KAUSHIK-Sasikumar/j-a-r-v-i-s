import smtplib
from config import EMAIL, EMAIL_PASSWORD
from assistant.voice import speak

def send_email(content):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, EMAIL_PASSWORD)
            server.sendmail(EMAIL, EMAIL, content)
        speak("Email has been sent.")
    except Exception:
        speak("Failed to send email.")
