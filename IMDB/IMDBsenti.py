# sentiment_imdb_tf.py
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random

# ----------------------------
# 1. Hyper-parameters
# ----------------------------
VOCAB_SIZE = 30000          
MAX_LEN    = 300           # pad / truncate length
EMB_DIM    = 256
BATCH_SIZE = 128
EPOCHS     = 20
SEED       = 42

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# ----------------------------
# 2. Load IMDB (already split)
# ----------------------------
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=VOCAB_SIZE)

# 👇 convert the NumPy arrays of object-dtype sequences into plain Python lists
x_train = list(x_train)
x_test  = list(x_test)

# Optional: restore original words to peek at samples
word_index   = imdb.get_word_index()
index_to_word = {v+3: k for k, v in word_index.items()}
index_to_word.update({0:'<PAD>', 1:'<START>', 2:'<UNK>', 3:'<UNUSED>'})

# ----------------------------
# 3. Simple in-place augmentation
# ----------------------------
def augment_sequence(seq, prob_drop=0.1, prob_swap=0.1):
    seq = seq.copy()
    # random deletion
    seq = [w for w in seq if random.random() > prob_drop or w < 4]  # keep special tokens
    # random swap (two positions)
    if len(seq) > 2 and random.random() < prob_swap:
        i, j = random.sample(range(1, len(seq)), 2)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

augmented_x_train = [augment_sequence(s) for s in x_train]
# combine original + augmented for larger effective set
x_train_full = x_train + augmented_x_train
y_train_full = np.concatenate([y_train, y_train])

# ----------------------------
# 4. Pad / truncate
# ----------------------------
x_train_padded = pad_sequences(x_train_full, maxlen=MAX_LEN, padding='post', truncating='post')
x_test_padded  = pad_sequences(x_test,        maxlen=MAX_LEN, padding='post', truncating='post')

# ----------------------------
# 5. Build model (1-D CNN example)
#    Swap for LSTM by uncommenting alt block
# ----------------------------
model = models.Sequential([

layers.Input(shape=(MAX_LEN,)),      
layers.Embedding(VOCAB_SIZE, EMB_DIM),
layers.Conv1D(128, 5, activation='relu'),
layers.GlobalMaxPooling1D(),
layers.Dense(64, activation='relu'),
layers.Dropout(0.5),
layers.Dense(1, activation='sigmoid')

])

# -----  LSTM variant (comment out CNN above to try)  -----
# model = models.Sequential([
#     layers.Embedding(VOCAB_SIZE, EMB_DIM, input_length=MAX_LEN),
#     layers.LSTM(64, return_sequences=False),
#     layers.Dropout(0.5),
#     layers.Dense(1, activation='sigmoid')
# ])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()

# ----------------------------
# 6. Train
# ----------------------------
early_stop = callbacks.EarlyStopping(
    monitor='val_accuracy', patience=2, restore_best_weights=True)

history = model.fit(
    x_train_padded, y_train_full,
    validation_split=0.2,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks=[early_stop],
    verbose=1
)

# ----------------------------
# 7. Evaluate
# ----------------------------
test_loss, test_acc = model.evaluate(x_test_padded, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc:.3f}")
