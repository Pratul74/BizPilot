from fastapi import FastAPI

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(update: dict):
    print(update)
    return {"ok": True}