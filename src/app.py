import os

from notifications import TelegramNotifier
from tinkoff.controllers.statistic import TinkoffStatisticController


def main() -> None:
    notifier = TelegramNotifier()
    controller = TinkoffStatisticController()

    message = controller.run()

    notifier.notify(message, os.getenv('TELEGRAM_CHAT_ID'))


if __name__ == '__main__':
    main()
