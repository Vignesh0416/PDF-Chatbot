# 📄 PDF Chatbot using LangChain & OpenRouter

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) based PDF chatbot.

Users can ask questions about a PDF document, and the chatbot retrieves the most relevant information using embeddings and FAISS before generating an answer with an LLM.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- OpenRouter
- OpenAI Embeddings
- FAISS
- PyPDF
- dotenv

---

## ✨ Features

- Load PDF documents
- Split documents into chunks
- Generate embeddings
- Store vectors in FAISS
- Semantic search
- GPT-powered answers
- Streamlit interface

---

## 📂 Project Structure

```
PDF-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/PDF-Chatbot.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENROUTER_API_KEY=your_api_key
```

Run

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Place screenshots inside the **assets** folder.

Example:

- Home Screen
- Chat Response

---

## 📌 Future Improvements

- Upload multiple PDFs
- Conversation memory
- ChromaDB support
- AI Agents