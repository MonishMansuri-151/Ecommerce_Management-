from payments.payment import Payment
class UPIpayment (Payment):
    def pay(self):
        print("UPI Payment Successful ")
        