# AITextSummarizer
A Python-based AI Text Summarizer and Note Taker built using TensorFlow and Hugging Face Transformers. This tool summarizes up to 250 characters [can be adjusted] and extracts key bullet points, without requiring any API key or internet connection after setup. 

---

## Features
- Summarize text into VERY concise paragraphs.
- Extract key points as bullet notes.
- 100% Local (No API cost or rate limits).

---

## Tech Stack
- Language: Python
- Libraries:
  - TensorFlow
  - Transformers (Hugging Face)
  - tqdm (for progress bars)
- Model: T5-small (default), T5-base (optional for better quality)

---

## Installation
1. Clone the repository or download the script.
2. Create and activate a virtual environment:
  python3 -m venv venv
    source venv/bin/activate   # (Mac/Linux)
    venv\Scripts\activate      # (Windows)
3. Install dependencies
   pip install tensorflow transformer sentencepiece tqdm

---
## How to Run 
- python3 AI_Summarizer_Local.py
- Then: Paste the text you want to summarize when prompted.

---
## Author 
- Developed by: Mikhala Campbell, ChatGPT
- Course: Making AI with AI
- Instructor: Samuel Musker 


