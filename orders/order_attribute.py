class Order:
    def __init__(self,order_id,customer_id,products,total_amount,order_date,payment_status):
        self.order_id = order_id
        self.customer_id= customer_id
        self.products = products
        self.total_amount = total_amount
        self.order_date = order_date
        self.payment_status = payment_status
        