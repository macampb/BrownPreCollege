# data_preprocessing.py
import pandas as pd
import numpy as np

def load_and_preprocess(filepath, max_len=20):
    passwords = []
    with open(filepath, 'r', encoding='latin-1') as f:
        for line in f:
            pwd = line.strip()
            if 6 <= len(pwd) <= max_len:
                passwords.append(pwd)
    
    # Create strength labels (based on entropy or length)
    labels = []
    for pwd in passwords:
        if len(pwd) < 8:
            labels.append(0)  # weak
        elif len(pwd) < 12:
            labels.append(1)  # medium
        else:
            labels.append(2)  # strong
    
    return passwords, labels
