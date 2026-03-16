from fastapi import FastAPI
from fastapi.responses import FileResponse


from backend.api.upload_logs import router as upload_router
from backend.api.analyze_logs import router as analyze_router
from backend.api.investigate import router as investigate_router
from backend.api.timeline import router as timeline_router
from backend.api.autonomous_investigate import router as autonomous_router

app = FastAPI(title="NovaSOC AI Analyst")

app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(investigate_router)
app.include_router(timeline_router)
app.include_router(autonomous_router)

@app.get("/")
def home():
    return FileResponse("frontend/dashboard.html")

@app.get("/status")
def status():
    return {"message": "NovaSOC API Running"}