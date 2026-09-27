# infrastructure/notifier.py
# Реализации NotificationSender

from interfaces.services import NotificationSender


class EmailSender:  # Уведомление по email
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL → {recipient}] {message}")


class SmsSender:  # Уведомление по SMS
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS → {recipient}] {message}")