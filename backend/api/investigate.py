from fastapi import APIRouter
import os

from backend.utils.parsers.log_parser import read_log_file
from backend.utils.ioc_extractor import extract_iocs
from backend.agents.investigation_agent import investigate_incident

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.get("/investigate/{filename}")
def investigate(filename: str):

    filepath = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(filepath):
        return {"error": "File not found"}

    content = read_log_file(filepath)

    iocs = extract_iocs(content)

    investigation = investigate_incident(iocs,content)

    return {
        "filename": filename,
        "iocs": iocs,
        "investigation": investigation
    }