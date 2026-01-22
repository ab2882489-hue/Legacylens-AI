from fastapi import FastAPI
from pydantic import BaseModel
from file_explainer import explain_code_file

app = FastAPI(title="LegacyLens AI")

class FileExplainRequest(BaseModel):
    file_name: str
    file_content: str

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
