import re

def extract_resume_sections(resume_text):
    text = resume_text.lower()

    def extract_section(section_name, next_sections):
        pattern = rf"{section_name}\s*(.*?)(?=" + '|'.join([rf"{s}" for s in next_sections]) + r"|$)"
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ""

    sections = {
        "education": extract_section("education", ["experience", "projects", "skills", "achievement", "activities", "certification", "contact"]),
        "experience": extract_section("experience", ["projects", "skills", "education", "achievement", "activities", "certification", "contact"]),
        "projects": extract_section("projects", ["experience", "skills", "education", "achievement", "activities", "certification", "contact"]),
        "skills": extract_section("skills", ["experience", "projects", "education", "achievement", "activities", "certification", "contact"]),
    }

    return sections
