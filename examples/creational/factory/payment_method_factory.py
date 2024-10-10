# Payment Interface
class Payment:
    def pay(self, amount):
        pass

# Concrete Classes
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."

class BitcoinPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Bitcoin."

# Payment Factory
class PaymentFactory:
    @staticmethod
    def create_payment(method):
        if method == "creditcard":
            return CreditCardPayment()
        elif method == "paypal":
            return PayPalPayment()
        elif method == "bitcoin":
            return BitcoinPayment()
        else:
            raise ValueError(f"Unknown payment method: {method}")

# Example usage
if __name__ == "__main__":
    method = input("Choose a payment method (creditcard, paypal, bitcoin): ").lower()
    payment = PaymentFactory.create_payment(method)
    print(payment.pay(100))
