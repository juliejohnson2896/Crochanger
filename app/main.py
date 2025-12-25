from fastapi import FastAPI

app = FastAPI(title="Crochet Pattern Manager")

@app.get("/health")
def health():
    return {"status": "ok"}
