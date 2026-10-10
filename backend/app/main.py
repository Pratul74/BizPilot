from fastapi import FastAPI

app = FastAPI(
    title="BizPilot",
    version="1.0.0"
)

@app.get("/health")
async def health():
    return {"status": "ok"}