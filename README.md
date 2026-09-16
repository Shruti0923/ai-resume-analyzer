# AI Resume Analyzer

An ATS-style Resume Analyzer built using Python and Flask.

## 📌 Project Description

AI Resume Analyzer is a web-based application that analyzes a user's resume PDF and identifies technical skills present in the resume.

The application extracts text from the uploaded PDF and compares it with a predefined list of technical skills.

It displays:

- Skills found in the resume
- Skills that can be added
- ATS-style skill score
- Resume analysis level

## 🚀 Features

- Upload resume in PDF format
- Extract text from PDF
- Detect technical skills
- Calculate ATS-style skill score
- Display missing skills
- Simple and responsive user interface

## 🛠️ Technologies Used

- Python
- Flask
- PyPDF2
- HTML
- CSS
- Jinja2
- GitHub

## 📂 Project Structure

```text
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
