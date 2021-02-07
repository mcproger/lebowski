import os
from notifications.base import BaseNotifier

from telegram.bot import Bot


class TelegramNotifier(BaseNotifier):
    def __init__(self) -> None:
        self.bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

    def notify(self, message: str, chat_id: int) -> None:
        self.bot.send_message(chat_id=chat_id, text=message)
