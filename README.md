```markdown
# langchain_chaining

A simple LangChain LCEL demo that chains two prompts sequentially — one to explain a concept, and one to translate the explanation to Japanese.

## What it does

1. Takes a concept as input from the terminal
2. Chain 1 explains the concept in one sentence
3. Chain 2 translates that explanation to Japanese

## Tech stack

- [LangChain](https://www.langchain.com/) (LCEL)
- [Groq](https://groq.com/) (llama-3.3-70b-versatile)
- Python

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install langchain langchain-groq langchain-core python-dotenv
   ```
3. Create a `.env` file in the root folder:
   ```
   GROQ_API_KEY=your_key_here
   ```
4. Run:
   ```bash
   python main.py
   ```

## Usage

```
You: photosynthesis
Chain 1 (English): Photosynthesis is the process by which plants convert sunlight into energy.
Chain 2 (Japanese): 光合成とは、植物が太陽光をエネルギーに変換するプロセスです。
```

Type `exit` to quit.
```
