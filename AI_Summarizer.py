from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
from tqdm import tqdm
import time

# Load T5 model (TensorFlow version)
model_name = "t5-base"  # Change to "t5-base" for better quality
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name, from_pt=True)

def show_progress(message):
    print(f"\n{message}")
    for _ in tqdm(range(100), desc="Processing"):
        time.sleep(0.02)  # Simulated progress (2 sec total)

def summarize_text(text, max_length=150, min_length=50):
    show_progress("Preparing input...")
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="tf", max_length=512, truncation=True)

    show_progress("Generating summary...")
    outputs = model.generate(
        input_ids,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def extract_notes(text):
    show_progress("Extracting bullet points...")
    input_ids = tokenizer.encode("summarize as bullet points: " + text, return_tensors="tf", max_length=512, truncation=True)

    outputs = model.generate(
        input_ids,
        max_length=250,
        min_length=30,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    print("================================")
    print("    AI Text Summarizer + Notes ")
    print("      (Local TensorFlow)        ")
    print("================================")

    text = input("\nPaste the text you want to summarize:\n\n")

    summary = summarize_text(text)
    notes = extract_notes(text)

    print("\n========== SUMMARY ==========\n")
    print(summary)
    print("\n========== NOTES ==========\n")
    print(notes)

if __name__ == "__main__":
    main()