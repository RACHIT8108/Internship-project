# Internship-project

# 🚀 Simple AI Q&A Chatbot (Meta LLaMA 3.1 8B via Groq API)

A tiny command-line chatbot that answers your questions using **Meta LLaMA 3.1 8B** through the **Groq API**.  
This project is part of the *Intern Assignment: Build a Tiny AI-Powered App*.  

---

## 📌 Features
- Simple **command-line Q&A chatbot**.  
- Uses **Groq API** with Meta LLaMA 3.1 8B model.  
- Conversation memory (remembers previous messages in the chat).  
- Exit anytime by typing `quit`, `exit`, `bye`, or `q`.  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-qa-chatbot.git
cd ai-qa-chatbot
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

GROQ_API_KEY=your_actual_key_here

python chatbot.py
```

