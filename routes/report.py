from fastapi import APIRouter, UploadFile, File
import shutil
import os
from uuid import uuid4

from services import parser, analyzer, fixer

router = APIRouter()

UPLOAD_DIR = "temp"

@router.post("/analyze")
async def analyze_report(file: UploadFile = File(...)):
    # Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Generate safe filename
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Parse content
    text = parser.parse_file(file_path)

    # AI processing
    analysis = analyzer.analyze_report(text)
    fixed = fixer.fix_report(text, analysis)

    return {
        "analysis": analysis,
        "fixed_report": fixed
    }
