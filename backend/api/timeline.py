from fastapi import APIRouter
import os

from backend.utils.parsers.log_parser import read_log_file
from backend.utils.timeline_generator import generate_timeline

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.get("/timeline/{filename}")
def timeline(filename: str):

    filepath = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(filepath):
        return {"error": "File not found"}

    content = read_log_file(filepath)

    timeline = generate_timeline(content)

    return {
        "filename": filename,
        "timeline": timeline
    }