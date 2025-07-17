# 1-Click Interview Question Generator

A Flask-based web app that generates customized interview questions based on your resume!

## 💡 Features
- Accepts resume text or uploaded PDF/DOCX
- Uses Google Gemini to generate questions based on your work
- Clean UI and instant question generation

## 🧠 Powered By:
- Flask
- PyMuPDF / python-docx
- Google Generative AI
- HTML + CSS

## 📦 Local Setup

```bash
git clone git remote add origin https://github.com/shw5652/resumeQuestionnaire
cd resumeQuestionnaire
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
