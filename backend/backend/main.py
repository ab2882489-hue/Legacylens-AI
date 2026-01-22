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
from impact_analysis import impact_analysis
from pydantic import BaseModel
from typing import Dict

class ImpactAnalysisRequest(BaseModel):
    target_file: str
    files: Dict[str, str]

@app.post("/impact-analysis")
def analyze_impact(request: ImpactAnalysisRequest):
    result = impact_analysis(request.target_file, request.files)
    return {"impact_analysis": result}
from dependency_visualizer import generate_dependency_graph
from pydantic import BaseModel
from typing import Dict

class DependencyGraphRequest(BaseModel):
    files: Dict[str, str]

@app.post("/dependency-graph")
def dependency_graph(request: DependencyGraphRequest):
    graph = generate_dependency_graph(request.files)
    return {"dependency_graph": graph}
from auto_documentation import generate_technical_documentation
from pydantic import BaseModel
from typing import Dict

class DocumentationRequest(BaseModel):
    files: Dict[str, str]

@app.post("/auto-documentation")
def auto_documentation(request: DocumentationRequest):
    doc = generate_technical_documentation(request.files)
    return {"documentation": doc}
from repo_question_answer import answer_repo_question
from pydantic import BaseModel
from typing import Dict

class RepoQuestionRequest(BaseModel):
    question: str
    files: Dict[str, str]

@app.post("/ask-repo")
def ask_repo(request: RepoQuestionRequest):
    answer = answer_repo_question(request.question, request.files)
    return {"answer": answer}
from risk_analyzer import analyze_system_risks
from pydantic import BaseModel
from typing import Dict

class RiskAnalysisRequest(BaseModel):
    files: Dict[str, str]

@app.post("/risk-analysis")
def risk_analysis(request: RiskAnalysisRequest):
    result = analyze_system_risks(request.files)
    return {"risk_report": result}
