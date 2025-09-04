import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from config import GEMINI_API_KEY
from openai import OpenAI
from typing import List, Dict

app = FastAPI(title="Gemini Chatbot with Memory")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": "You are a helpful assistant."}]

def save_memory(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

# Request body model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Load past memory
        messages = load_memory()

        # Add new user message
        messages.append({"role": "user", "content": req.message})

        # Send to Gemini
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=messages
        )

        reply = response.choices[0].message.content

        # Save assistant reply into memory
        messages.append({"role": "assistant", "content": reply})
        save_memory(messages)

        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
