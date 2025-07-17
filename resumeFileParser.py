import PyPDF2
import docx

def parse_resume_file(file_storage):
    filename = file_storage.filename.lower()

    if filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file_storage)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()

    elif filename.endswith('.docx'):
        doc = docx.Document(file_storage)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""]).strip()

    return "Unsupported file type. Please upload PDF or DOCX only."
