import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception:
        return "Sorry, I couldn't connect to ChatGPT."
