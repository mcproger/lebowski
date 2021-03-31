from __future__ import annotations

import os

from telegram.bot import Bot

from notifications.base import BaseNotifier


class TelegramNotifier(BaseNotifier):
    def __init__(self) -> None:
        self.bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

    def notify(self, message: str = None, chat_id: str = None) -> None:  # type: ignore
        if chat_id is None:
            return

        self.bot.send_message(chat_id=chat_id, text=message)
