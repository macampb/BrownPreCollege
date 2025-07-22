# train_strength_model.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from data_preprocessing import load_and_preprocess

# Load data
passwords, labels = load_and_preprocess('data/rockyou.txt')

# Tokenize
tokenizer = Tokenizer(char_level=True)  # char-level because passwords are short
tokenizer.fit_on_texts(passwords)
sequences = tokenizer.texts_to_sequences(passwords)
max_len = max([len(p) for p in passwords])
X = pad_sequences(sequences, maxlen=max_len, padding='post')
y = np.array(labels)

# Model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=16, input_length=max_len),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')  # Weak, Medium, Strong
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=3, batch_size=256, validation_split=0.1)

# Save model
model.save('models/strength_model.h5')

import json
# Save tokenizer
tokenizer_json = tokenizer.to_json()
with open('models/tokenizer.json', 'w') as f:
    f.write(tokenizer_json)

