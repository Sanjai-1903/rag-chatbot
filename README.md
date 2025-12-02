RAG Chatbot

A smart, context-aware chatbot built using RAG (Retrieval-Augmented Generation) workflow, designed to provide accurate and knowledge-driven responses. The project leverages LangChain for orchestration, Pinecone as a vector database, and OpenAI GPT/LLMs for generation.

🌟 Features

Retrieval-Augmented Generation (RAG) workflow

Vector-based search using Pinecone for fast retrieval of relevant information

LangChain integration for chaining prompts and orchestrating queries

Custom knowledge base to answer domain-specific questions

Interactive chat interface with responsive frontend

🛠 Tech Stack

Python – backend logic

Flask / FastAPI – API serving the chatbot

OpenAI GPT / LLMs – for generating intelligent responses

Pinecone – vector database for embedding search

LangChain – orchestrating retrieval and generation

HTML / CSS / JS – frontend chat interface

📂 Project Structure
rag-chatbot/
├── app.py                  # Main backend application
├── backend.py              # Backend logic for chatbot
├── document.py             # Document processing & embedding
├── data/                   # Knowledge base text files
│   ├── faq.txt
│   ├── insurance-info.txt
│   ├── locations.txt
│   ├── tech-specs.txt
│   └── terms-of-use.txt
├── images/                 # Screenshots / UI images
├── templates/
│   └── index.html          # Frontend chat interface
├── __pycache__/            # Compiled Python files
└── .gitignore              # Files/folders to ignore in Git

⚡ Installation & Setup

Clone the repo

git clone https://github.com/Sanjai-1903/rag-chatbot.git
cd rag-chatbot


Create a virtual environment

python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Set up API keys / environment variables

Create a .env file (if needed) and add your OpenAI API key and Pinecone key:

OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=your_environment


Run the app

python app.py


Open http://localhost:5000 in your browser to access the chatbot.

💬 Usage

Type your queries in the chat interface.

The bot will retrieve relevant documents and generate context-aware responses.

Ideal for FAQ answering, knowledge base assistance, or domain-specific chatbots.

📝 Future Improvements

Multi-modal RAG (text + images + audio)

Integration with enterprise knowledge bases

Personalized AI assistants based on user context

Enhanced UI/UX with avatars, typing indicators, and dark/light modes

📄 License

This project is open source and available under the MIT License.

👨‍💻 Author

[Sanjai Murugan](https://github.com/Sanjai-1903/)
GitHub Profile
