**ChatBot OpenAI Wrapper with Gemini**

This project is a basic chatbot built using FastAPI and the OpenAI Python wrapper (with Gemini support).
It demonstrates how to integrate OpenAI models into a backend API while keeping track of conversation memory in a memory.json file, enabling the chatbot to provide context-aware responses like ChatGPT.

🚀 Features

⚡ FastAPI backend for handling chat requests

🔗 OpenAI Wrapper integration with Gemini API endpoint

💾 Persistent memory with memory.json for storing past chats

📜 Custom system prompts via system_prompt.txt

🔒 Secure API key management using .env

**📂 Project Structure**

ChatBot_OpenAI_Wrapper_Gemini-/

│── app.py                # FastAPI backend

│── config.py             # API key / config management

│── system_prompt.txt     # Custom chatbot instructions

│── memory.json           # Persistent chat history (auto-created)

│── requirements.txt      # Python dependencies

│── .env                  # API key (ignored in Git)

│── .gitignore            # Ignore sensitive/unnecessary files

**🛠️ Setup & Installation**
1. Clone the Repository
git clone https://github.com/Chakradhar080/ChatBot_OpenAI_Wrapper_Gemini-.git
cd ChatBot_OpenAI_Wrapper_Gemini-

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_or_gemini_api_key

**▶️ Running the Backend**

**Start the FastAPI server:**

uvicorn app:app --reload


API will be available at:
👉 http://127.0.0.1:8000/docs
 (interactive Swagger UI)

**💬 Example Usage**

Send a POST request to /chat:

Request
{
  "message": "Hello, who are you?"
}

Response
{
  "reply": "I am your AI assistant powered by OpenAI wrapper with Gemini."
}


Since memory is stored in memory.json, the bot will remember previous conversations.

**🔒 Security**

.env file ensures your API keys are never exposed in GitHub.

.gitignore excludes memory.json and sensitive files.

**📌 Future Improvements**

🌐 Add Streamlit frontend for user-friendly chat UI

🧠 Improve long-term memory with vector database

🛠️ Extend support for multiple models
