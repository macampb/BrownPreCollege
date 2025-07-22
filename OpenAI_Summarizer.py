# ==============================
# Project: AI Text Summarizer + Note Taker using OpenAI API with Flask
# ==============================

# -------- summarizer_model.py --------
import openai
import os

# Set your OpenAI API key as an environment variable before running
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text in a concise paragraph:\n{text}"}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

def extract_notes(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts key points from text."},
            {"role": "user", "content": f"Extract the key points from the following text as bullet points:\n{text}"}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

# -------- app.py (Flask API) --------
from flask import Flask, request, jsonify
from summarizer_model import summarize_text, extract_notes

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarize_text(text)
    notes = extract_notes(text)

    return jsonify({"summary": summary, "notes": notes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# -------- requirements.txt --------
flask
openai
