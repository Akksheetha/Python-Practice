from typing import Protocol


class PaymentMethod(Protocol):

    def authorize_payment(self, amount: float) -> bool:
        ...

    def process_payment(self, amount: float) -> bool:
        ...


class CreditCardPayment:

    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorizing credit card payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True


class PayPalPayment:

    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorizing PayPal payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True


def make_payment(payment: PaymentMethod, amount: float):

    if payment.authorize_payment(amount):
        payment.process_payment(amount)


cc = CreditCardPayment()
pp = PayPalPayment()

make_payment(cc, 500)
make_payment(pp, 1000)