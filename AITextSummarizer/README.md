# AI Text Summarizer + Note Taker (Local TensorFlow)

A local AI-powered summarizer and note-taker built using TensorFlow and Hugging Face Transformers.  
This tool summarizes text into a concise paragraph and extracts key bullet points 
[**offline**— no API key or internet required after initial setup.]

---

## Features
- Summarizes long text into short, clear summaries.
- Choose summary length: Short (~50 words), Medium (~100 words), Long (~150 words)
- Upload .txt files for automatic summarization
- Download options: Export results as TXT or PDF
- Extracts bullet-point notes from text.
- 100% local (no API costs, no rate limits).

---

## Tech Stack
- Language: Python
- Frameworks/Libraries:
  - TensorFlow
  - Hugging Face Transformers
  - tqdm (for progress bar)
  - Flask
- Model: Hugging Face `facebook/bart-large-cnn` (or `sshleifer/distilbart-cnn-12-6` for speed)

---

## Project Structure
FinalProject/
│
├── app.py # Flask application 
├── summarizer_model.py 
├── templates/
│ └── index.html 


---

## Installation

### 1. Clone or download this project
git clone <https://github.com/mcampb30/AITextSummarizer>
cd FinalProject

### 2. Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### 3. Install dependencies
pip install flask transformers torch reportlab
 
### 4. How to Run
python3 AI_Summarizer_Local.py
# Paste the text you want to summarize when prompted.

### Example Output:
================================
    AI Text Summarizer + Notes 
      (Local TensorFlow)        
================================

Paste the text you want to summarize:

[User pastes text here]

Generating summary...
Processing: 100%|████████████████████████████████| 100/100 [00:02<00:00, 50.00it/s]

========== SUMMARY ==========
[Generated summary here]

========== NOTES ==========
[Generated bullet points here]

----

## What is Hugging Face Transformers?
Hugging Face Transformers is a library that provides state-of-the-art NLP models like T5, BERT, GPT, etc., making it easy to use advanced AI models for tasks like summarization, translation, and question answering.

----
# Author 
Developed by: Mikhala Campbell, ChatGPT
Course: Making AI with AI
Instructor: Samuel Musker 


