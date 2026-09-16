from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SKILLS = [
    "python", "java", "c", "c++", "html", "css",
    "javascript", "sql", "mysql", "flask",
    "django", "machine learning", "data science",
    "git", "github", "excel", "power bi"
]


def extract_text(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def analyze_resume(text):
    text_lower = text.lower()

    found_skills = []
    missing_skills = []

    for skill in SKILLS:
        if skill in text_lower:
            found_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    score = int((len(found_skills) / len(SKILLS)) * 100)

    if score >= 70:
        level = "Excellent"
    elif score >= 40:
        level = "Good"
    else:
        level = "Needs Improvement"

    return found_skills, missing_skills, score, level


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No resume uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a resume."

    if not file.filename.lower().endswith(".pdf"):
        return "Please upload a PDF file."

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    text = extract_text(filepath)

    found_skills, missing_skills, score, level = analyze_resume(text)

    return render_template(
        "result.html",
        skills=found_skills,
        missing=missing_skills,
        score=score,
        level=level
    )


if __name__ == "__main__":
    app.run(debug=True)
