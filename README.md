```t 
# Securely AI - AI-Powered password Strength Checker & Generator 


## Overview 
Securely AI is an AI-powered tool that:
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
    - Customizable with user inputs
    - Advanced Mode for extra randomization and enhanced security
- Flask REST API for integration into apps or browsers
- Real-time password feedback + Security checklist
- Password history (last 3 generated passwords)
- Light/Dark theme toggle

---
## Tech Stack 
- Language: Python 3.11.9
- Framework: Flask
- AI Model: TensorFlow (LSTM-based model)
- Libraries: 'tensorflow', 'flask', 'requests', 'numpy'
- Frontend: HTML, CSS, JavaScript
---

## Project Structure 
AI_Securely/
├── app/
│   ├── main.py             # Flask API endpoints
│   ├── strength_checker.py # Password strength prediction
│   ├── generator.py        # Personalized password generator
│   ├── breach_checker.py   # Breach check using HIBP API
|   └── templates/
│       └── index.html      # Modern UI
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
cd AI_Securely 

### 2. Create Virtual Environment & Activate 
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

### 3. Install Requirements 
pip install 

### 4. Run the Flask API
cd AI_Securely
python app/main.py
- SERVER STARTS AT: http://127.0.0.1:5000
----
# Author 
Developed by: Mikhala Campbell, ChatGPT
Course: Making AI with AI
Instructor: Samuel Musker
© 2025 | M.C
