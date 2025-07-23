from transformers import AutoTokenizer, BartForConditionalGeneration

# Load BART model
bart_model_name = "sshleifer/distilbart-cnn-12-6"
bart_tokenizer = AutoTokenizer.from_pretrained(bart_model_name)
bart_model = BartForConditionalGeneration.from_pretrained(bart_model_name)

# Length presets
LENGTH_OPTIONS = {
    "short": (60, 30),
    "medium": (100, 50),
    "long": (140, 70)
}

def summarize_text(text, length_choice="medium"):
    """Generate summary with user-selected length."""
    max_length, min_length = LENGTH_OPTIONS.get(length_choice, (120, 60))

    inputs = bart_tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = bart_model.generate(
        inputs["input_ids"],
        num_beams=4,
        length_penalty=2.0,
        max_length=max_length,
        min_length=min_length,
        early_stopping=True
    )
    summary = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
    return summary

def extract_notes(text):
    """Generate bullet points using BART with custom prompt + post-processing."""
    prompt = "Extract key points as bullet points: " + text
    inputs = bart_tokenizer([prompt], max_length=1024, return_tensors="pt", truncation=True)
    note_ids = bart_model.generate(
        inputs["input_ids"],
        num_beams=4,
        length_penalty=2.0,
        max_length=150,
        early_stopping=True
    )
    raw_notes = bart_tokenizer.decode(note_ids[0], skip_special_tokens=True).strip()

    # Convert to bullet points
    sentences = [s.strip() for s in raw_notes.replace("•", "").split(".") if s.strip()]
    bullets = ["- " + s[0].upper() + s[1:] for s in sentences]
    return "\n".join(bullets)
