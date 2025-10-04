from fastapi import FastAPI

app = FastAPI(title="Radcliffe API")


@app.get("/health")
def health():
    return {"status": "ok"}
