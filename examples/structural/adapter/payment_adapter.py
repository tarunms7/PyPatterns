# Target Interface (Expected by the client)
class PaymentGateway:
    def make_payment(self, amount):
        pass


# Adaptee 1: Stripe Payment Gateway
class StripePayment:
    def stripe_charge(self, amount):
        print(f"Charging ${amount} using Stripe.")

# Adaptee 2: PayPal Payment Gateway
class PayPalPayment:
    def paypal_send(self, amount):
        print(f"Sending ${amount} using PayPal.")


# Adapter 1: Stripe Adapter
class StripeAdapter(PaymentGateway):
    def __init__(self, stripe_payment):
        self.stripe_payment = stripe_payment

    def make_payment(self, amount):
        self.stripe_payment.stripe_charge(amount)


# Adapter 2: PayPal Adapter
class PayPalAdapter(PaymentGateway):
    def __init__(self, paypal_payment):
        self.paypal_payment = paypal_payment

    def make_payment(self, amount):
        self.paypal_payment.paypal_send(amount)


# Client code
class ECommercePlatform:
    def process_payment(self, payment_gateway: PaymentGateway, amount):
        payment_gateway.make_payment(amount)


# Example Usage
if __name__ == "__main__":
    # Using Stripe
    stripe_payment = StripePayment()
    stripe_adapter = StripeAdapter(stripe_payment)

    # Using PayPal
    paypal_payment = PayPalPayment()
    paypal_adapter = PayPalAdapter(paypal_payment)

    # Processing payments through ECommerce platform
    platform = ECommercePlatform()
    platform.process_payment(stripe_adapter, 100)  # Charging $100 using Stripe
    platform.process_payment(paypal_adapter, 200)  # Sending $200 using PayPal

# OUTPUT:
# Charging $100 using Stripe.
# Sending $200 using PayPal.
