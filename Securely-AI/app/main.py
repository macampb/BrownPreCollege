# app/main.py
from flask import Flask, request, jsonify, render_template
from strength_checker import predict_strength
from generator import personalized_password
from breach_checker import check_breach
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


# Check Password Strength + Breach Status 
@app.route('/check_strength', methods=['POST'])
def check_strength():
    data = request.json
    password = data.get('password', '')
    strength = predict_strength(password)
    breached = check_breach (password)
    return jsonify({
        'password': password, 
        'strength': strength,
        'breached': breached 
        })

# Endpoint: Generate Personalized Password 
@app.route('/generate_password', methods=['POST'])
def generate_password():
    answers = request.json  # Expect keys: color, animal, year, symbol
    new_password = personalized_password(answers)
    return jsonify({'generated_password': new_password})

if __name__ == '__main__':
    app.run(debug=True)
