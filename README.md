```t 
# AI Securely - AI-Powered password Strength Checker & Generator 


## Overview 
AI Securely is an AI-powered tool that:
- Evaluates password strength using a trained LSTM model. 
- Checks if a password has been compromised in data breaches via HaveIBeenPwned API. 
- Generates personalized strong passwords based on user input for easy memorization. 
- Exposes functionality through a Flask REST API for easy integration 
# This AI tool can be integrated into a web app, mobile app, or browser extension

---
## Features 
- AI Strength Prediction: Weak, Medium, Strong
- Breach Checks: Uses HaveIBeenPwned API [secure k-anonymity method/ privacy technique]
- Smart Personalized Password Generator 
- Flask REST API for integration into apps or browsers

---
## Tech Stack 
- Language: Python 3.11.9
- Framework: Flask
- AI Model: TensorFlow (LSTM-based model)
- Libraries: 'tensorflow', 'flask', 'requests', 'numpy'
---

## Project Structure 
AI_Securely/
├── app/
│   ├── main.py             # Flask API endpoints
│   ├── strength_checker.py # Password strength prediction
│   ├── generator.py        # Personalized password generator
│   ├── breach_checker.py   # Breach check using HIBP API
├── models/
│   ├── strength_model.h5   # Trained LSTM model
│   ├── tokenizer.json      # Tokenizer for password encoding
├── data/
│   └── rockyou.txt      
├── train_strength_model.py # Model training script'
├── test_api.py               # Script to test API endpoints
└── README.md

---
## Setup Instructions 

### 1. Clone the Repository
git clone <your-repo-url>
cd AI_Securely 

### 2. Create Virtual Environment & Activate 
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

### 3. Install Requirements 
pip install -r requirements.txt 

### 4. Run the Flask API
cd AI_Securely
python app/main.py
- SERVER STARTS AT: http://127.0.0.1:5000

---
# API Endpoints 

## Check Password Strength + Breach 
**Input:**
{
    "password": "Blu3P@nda2023"
}
**Output**: {
    "password": "Blu3P@nda2025",
    "strength": "Strong",
    "breached": false
}

## Generate Personalized Password 
**Input:**
{
  "color": "blue",
  "animal": "panda",
  "year": "2031",
  "symbol": "@"
}
**Output:**
{
  "generated_password": "BluePanda2031@X9"
}

----

# How to Test 
You can test using: 
- **cURL Commands:** 
curl -X POST http://127.0.0.1:5000/check_strength \
-H "Content-Type: application/json" \
-d '{"password":"Blu3P@nda2025"}'

curl -X POST http://127.0.0.1:5000/generate_password \
-H "Content-Type: application/json" \
-d '{"color":"blue","animal":"panda","year":"2031","symbol":"@"}'

- **Or Python Script:**
import requests

# Test strength check
response = requests.post("http://127.0.0.1:5000/check_strength", json={"password": "Blu3P@nda2025"})
print(response.json())

# Test personalized password generator
answers = {"color": "blue", "animal": "panda", "year": "2031", "symbol": "@"}
response = requests.post("http://127.0.0.1:5000/generate_password", json=answers)
print(response.json())

----
# Author 
Developed by: Mikhala Campbell, ChatGPT
Course: Making AI with AI
Instructor: Samuel Musker 
