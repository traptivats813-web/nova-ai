from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


def ChatBot(chat_history):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_history,
            temperature=0.6,
            max_tokens=200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
