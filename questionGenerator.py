import os
import re
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def build_prompt(sections):
    return f'''
You are a senior tech interviewer.
Based on the candidate's resume, generate 10 **very specific** technical interview questions. 
DO NOT provide generic templates.
DO NOT provide information about what knowledge will each question test.
Add numbering to each question only.

EDUCATION:
{sections.get("education", "")}

EXPERIENCE:
{sections.get("experience", "")}

PROJECTS:
{sections.get("projects", "")}

SKILLS:
{sections.get("skills", "")}

The questions must refer to specific tech, projects, roles, or skills. Avoid vague behavioral templates.
'''

def generate_questions(sections):
    prompt = build_prompt(sections)
    try:
        response = model.generate_content(prompt)
        lines = response.text.strip().split("\n")

        cleaned_questions = []
        for line in lines:
            if "interview questions" in line.lower():
                continue
            if not line.strip(): 
                continue

            question = re.sub(r'^\s*\d+[\.\)]\s*', '', line).strip()
            if question:
                cleaned_questions.append(question)

        return cleaned_questions

    except Exception as e:
        return [f"<b>Error generating questions:</b> {e}"]

