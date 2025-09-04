import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API key from Google AI Studio
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
