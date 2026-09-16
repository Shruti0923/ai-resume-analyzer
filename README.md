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

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Go into the project folder
cd ai-resume-analyzer
3. Install required packages
pip install -r requirements.txt

▶️ Run the Application

Run the following command:

python app.py

Then open your browser and visit:
http://127.0.0.1:5000

📄 How It Works
User uploads a resume PDF.
Flask receives the uploaded file.
PyPDF2 extracts text from the PDF.
The application checks the extracted text for predefined technical skills.
An ATS-style skill score is calculated.
The results are displayed on the result page.

🔮 Future Improvements
Machine Learning based resume classification
NLP-based skill extraction
Job description matching
Resume improvement suggestions
Resume keyword recommendations
Database integration
User authentication
Cloud deployment

👩‍💻 Author
Shruti
GitHub: Shruti0923
