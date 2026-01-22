from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from file_explainer import explain_code_file
from multi_file_analyzer import analyze_multiple_files

app = FastAPI(title="LegacyLens AI")

class FileExplainRequest(BaseModel):
    file_name: str
    file_content: str

class MultiFileRequest(BaseModel):
    files: Dict[str, str]

@app.get("/")
def health_check():
    return {"status": "running", "service": "LegacyLens AI backend"}

@app.post("/explain-file")
def explain_file(request: FileExplainRequest):
    explanation = explain_code_file(
        request.file_name,
        request.file_content
    )
    return {"explanation": explanation}

@app.post("/analyze-files")
def analyze_files(request: MultiFileRequest):
    analysis = analyze_multiple_files(request.files)
    return {"analysis": analysis}
