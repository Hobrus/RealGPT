from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':
    print(TELEGRAM_TOKEN, OPENAI_API_KEY)
