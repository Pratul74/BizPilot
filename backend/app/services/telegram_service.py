from httpx import AsyncClient

class TelegramService:

    def __init__(self, token: str):
        self.base_url = f"https://api.telegram.org/bot{token}"

    async def send_message(self, chat_id: int, text: str):
        async with AsyncClient() as client:
            await client.post(
                f"{self.base_url}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": text
                }
            )

