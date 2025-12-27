import pdfplumber
from docx import Document
import os

def parse_file(file_path: str) -> str:
    if file_path.lower().endswith(".pdf"):
        text = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n".join(text)

    if file_path.lower().endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs if p.text)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
