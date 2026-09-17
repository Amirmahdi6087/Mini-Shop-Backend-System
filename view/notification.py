from typing import Protocol


class NotificationProtocol(Protocol):
    def send(self, message: str) -> str:
        ...


class EmailNotification:
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSNotification:
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


class PushNotification:
    def send(self, message: str) -> str:
        return f"Push notification sent: {message}"


def notify(service: NotificationProtocol, message: str) -> None:
    print(service.send(message))
