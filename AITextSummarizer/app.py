from flask import Flask, render_template, request, send_file
from summarizer_model import summarize_text, extract_notes
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    notes = ""
    text = ""
    selected_length = "medium"  # Default option
    if request.method == "POST":
        selected_length = request.form.get("summary_length", "medium")

        if "input_text" in request.form and request.form["input_text"].strip():
            text = request.form["input_text"]
        elif "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".txt"):
                text = file.read().decode("utf-8")

        if text:
            summary = summarize_text(text, length_choice=selected_length)
            notes = extract_notes(text)
    return render_template("index.html", summary=summary, notes=notes, text=text, selected_length=selected_length)

@app.route("/download", methods=["POST"])
def download():
    summary = request.form["summary"]
    notes = request.form["notes"]
    file_format = request.form["format"]

    file_path = "output." + file_format
    if file_format == "txt":
        with open(file_path, "w") as f:
            f.write("Summary:\n" + summary + "\n\nNotes:\n" + notes)
    elif file_format == "pdf":
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        c = canvas.Canvas(file_path, pagesize=letter)
        text_object = c.beginText(40, 750)
        text_object.textLine("Summary:")
        for line in summary.split("\n"):
            text_object.textLine(line)
        text_object.textLine("")
        text_object.textLine("Notes:")
        for line in notes.split("\n"):
            text_object.textLine(line)
        c.drawText(text_object)
        c.save()

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)