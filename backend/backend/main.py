from fastapi import FastAPI

app = FastAPI(title="LegacyLens AI")

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "LegacyLens AI backend"
    }
