from payments.payment import Payment
class CardPayment(Payment):
    def pay(self):
        print("Card Payment Successful")