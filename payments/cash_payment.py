from payments.payment import Payment
class CashPayment(Payment):
    def pay(self):
        print("Cash Payment Successful")