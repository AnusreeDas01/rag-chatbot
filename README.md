# 🤖 RAG Chatbot – Chat with Your Documents

A conversational AI chatbot powered by **LLMs + RAG (Retrieval-Augmented Generation)** that allows you to upload documents and ask natural questions — and it answers using only the content of the files you uploaded.

🚀 **Live Demo**: [rag-chatbot-01.streamlit.app](https://rag-chatbot-01.streamlit.app/)

---

## 📌 Overview

The RAG Chatbot is a smart document-based Q&A assistant. Upload PDFs, DOCX, or TXT files — then ask questions in natural language and get answers with references to the document content.

---

## ✨ Features

- 📁 Upload `.pdf`, `.docx`, or `.txt` files
- 🔍 Retrieves relevant chunks using semantic search
- 🧠 Uses LLMs (OpenAI / Flan-T5) to answer based on file content
- 📎 Source references included in responses
- 💬 Chat-style UI with streamlit
- 💾 Download chat history anytime
- 🧹 One-click clear chat + file reset
- 📱 Fully responsive and mobile-ready

---

## 🛠️ Tech Stack

| Layer        | Tools / Libraries |
|--------------|-------------------|
| **Frontend** | Streamlit, streamlit-lottie |
| **Backend**  | Python, LangChain, FAISS |
| **LLM**      | OpenAI GPT-3.5 / Flan-T5 |
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Vector DB** | FAISS (in-memory) |
| **Deployment** | Streamlit Cloud |

---

## 📂 Folder Structure

rag-chatbot/
│
├── app.py # Streamlit UI
├── main/
│ ├── utils.py # Embeddings & parsing
│ ├── rag_engine.py # RAG answer engine
│ └── uploads/ # Uploaded files folder
├── assets/
│ └── virtual_assistant.json # Lottie animation
├── requirements.txt # Project dependencies
└── README.md # This file 😉


---

## ⚙️ How to Run Locally

### 1. Clone the project:

```bash
git clone https://github.com/AnusreeDas01/rag-chatbot.git
cd rag-chatbot

2. (Optional) Create virtual env:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install required packages:
pip install -r requirements.txt

4. Run the app:
streamlit run streamlit_app.py

🔐 Environment Setup
For OpenAI (Optional):
In .streamlit/secrets.toml or in Streamlit Cloud settings:
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxx"

🌐 Streamlit Deployment
App is deployed here 👉 https://rag-chatbot-01.streamlit.app/
Hosted via Streamlit Cloud with public access. You can upload files, ask questions, download history, and reset everything cleanly.

🧠 Use Cases
. Summarize HR or legal documents
. Chat with your academic PDFs
. Ask questions about internal process docs
. Personal knowledge base assistant

📸 Screenshots
Add custom screenshots here if needed (e.g., chat, upload, UI)

👩‍💻 Author
Made with 💜 by Anusree Das

🔗 GitHub: AnusreeDas01
💼 LinkedIn: Anusree Das
🌐 Live App: rag-chatbot-01.streamlit.app

