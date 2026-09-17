from typing import Protocol


class PaymentProtocol(Protocol):
    def pay(self, amount: int) -> str:
        ...


class CashPayment:
    def pay(self, amount: int) -> str:
        return f"Paid {amount} with cash"


class CardPayment:
    def pay(self, amount: int) -> str:
        return f"Paid {amount} with card"


class WalletPayment:
    def pay(self, amount: int) -> str:
        return f"Paid {amount} with wallet"


def process_payment(payment: PaymentProtocol, amount: int) -> None:
    print(payment.pay(amount))
