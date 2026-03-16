from fastapi import APIRouter
import os

from backend.utils.parsers.log_parser import read_log_file
from backend.agents.autonomous_soc_agent import autonomous_investigation

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.get("/autonomous-investigate/{filename}")
def autonomous_investigate(filename: str):

    filepath = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(filepath):
        return {"error": "File not found"}

    log_content = read_log_file(filepath)

    result = autonomous_investigation(log_content)

    return {
        "filename": filename,
        "result": result
    }