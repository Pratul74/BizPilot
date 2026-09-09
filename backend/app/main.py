from fastapi import FastAPI
from services import TelegramService
from core import settings

app = FastAPI()

telgram_service= TelegramService(settings.TELEGRAMBOT_TOKEN)

@app.post("/webhook")
async def telegram_webhook(update: dict):
    chat_id = update["message"]["chat"]["id"]
    print(update["message"]["text"])
    await telgram_service.send_message(
        chat_id=chat_id,
        text="Good to hear from you :)"
    )
    return {"ok": True}