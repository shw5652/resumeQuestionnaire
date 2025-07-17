import os
from flask import Flask, render_template, request
from questionGenerator import generate_questions
from resumeParser import extract_resume_sections
from resumeFileParser import parse_resume_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    questions = []
    resume_text = ""

    if request.method == 'POST':
        # Handle file upload
        if 'resume_file' in request.files and request.files['resume_file'].filename != '':
            resume_text = parse_resume_file(request.files['resume_file'])
        else:
            resume_text = request.form.get('resume_text', '')

        sections = extract_resume_sections(resume_text)
        questions = generate_questions(sections)

    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)