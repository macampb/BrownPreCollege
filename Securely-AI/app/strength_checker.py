import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import os
from tensorflow.keras.preprocessing.text import tokenizer_from_json

# Dynamically set paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, '..', 'models')
MODEL_PATH = os.path.join(MODELS_DIR, 'strength_model.h5')
TOKENIZER_PATH = os.path.join(MODELS_DIR, 'tokenizer.json')

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Load tokenizer (as raw string, not dict)
with open(TOKENIZER_PATH, 'r') as f:
    tokenizer_json = f.read()
tokenizer = tokenizer_from_json(tokenizer_json)

# Max password length used in training
max_len = 20

def predict_strength(password):
    seq = tokenizer.texts_to_sequences([password])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    pred = model.predict(padded, verbose=0)
    classes = ['Weak', 'Medium', 'Strong']
    return classes[np.argmax(pred)]

# Test block
if __name__ == "__main__":
    test_passwords = ["12345", "Password123", "Blu3P@nda2025"]
    for pwd in test_passwords:
        print(f"{pwd} → {predict_strength(pwd)}")
