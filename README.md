langchain_chaining
A beginner-level LangChain project demonstrating LCEL (LangChain Expression Language) by chaining two LLM calls — one to explain a concept, and another to translate the explanation to Japanese.
What it does

Takes a concept as input from the terminal
Chain 1 — explains the concept in one sentence
Chain 2 — translates that explanation to Japanese

Tech Stack

LangChain — chaining framework
Groq — LLM provider
llama-3.3-70b-versatile — model used
python-dotenv — for managing API keys

Setup

Clone the repo

bash   git clone https://github.com/yourusername/langchain_chaining.git
   cd langchain_chaining

Install dependencies

bash   pip install langchain langchain-groq langchain-core python-dotenv

Create a .env file in the root directory

   GROQ_API_KEY=your_api_key_here

Run

bash   python main.py
Example
You: photosynthesis
Chain 1 (English): Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into glucose and oxygen.
Chain 2 (Japanese): 光合成とは、植物が太陽光、水、二酸化炭素をブドウ糖と酸素に変換するプロセスです。
Concepts Covered

LangChain basics
LCEL (| pipe syntax)
PromptTemplate
StrOutputParser
Sequential chaining
