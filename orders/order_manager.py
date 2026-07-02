# manage all order method 
from customers.customer_inventory import Customer_Inventory
from shoping_cart.cart import Add_Cart
from orders.order_attribute import Order
from orders.order_inventory import Order_Inventory
from datetime import datetime
class Order_Manage:
    def __init__(self):
        pass
    def place_order(self):
        # 1. Select Customer
        # 2. Add Products To Cart
        # 3. Calculate Total
        # 4. Apply Discount
        # 5. Process Payment
        # 6. Generate Order
    # search order id 
        order_id = input("Enter order Id :")
    # Date of order place 
        order_date = datetime.now().date()
    # searh customer id 
        customer_id = int(input("Enter Customer iD :"))
        get_id_customer = Customer_Inventory.customer_Dict.get(customer_id)
        if get_id_customer is None:
            print("Customer Not Found: ")
            return
    # check cart is empty or not 
        if not Add_Cart.cart_list:
            print(" Cart is empty : ")
            return
    # calculate the total amount 
        total =0
        print()
        for item in Add_Cart.cart_list:
            product = item[0]
            quantity = item[1]
            total += product.price * quantity
        print ("--Total Amount --",total)
        print()
    # apply the discount 
        if total < 5000:
            print("No Discount :")
            print()
        elif total >= 15000:
            print("10% Discount Total price  :-")
            print()
            # calculate the discount 
            discount = total * 10 /100
            discount_amount = total-discount
            print("----Discountd Price---- ",discount_amount)
            print()
            print()
        print("====Please Slect payment method====: ")
        print()
        print("1. UPI :-")
        print("2.CASH ON DELIVERY :-")
        print("3.DEBIT/CREDIT CARD :-")
        print()
        choice = int(input("Enter your choice :-"))
        print()
        if choice == 1:
            status = "paid"
            payment = "UPI"
            print("Payment confirm by UPI:-",status,payment)
        elif choice == 2:
            status = "panding"
            payment = "COD"
            print("payment pending : ",status,payment)
        elif choice == 3:
            status = "paid"
            payment = "CREDID/DEBIT CARD"
            print("payment confirm by Credit/Debit Card : ",status,payment)
        else:
            print("Invalid choice :")
    # generate the order 
        print()
        generate_order = Order(order_id,customer_id,Add_Cart.cart_list.copy(),discount_amount,order_date,status)
        Order_Inventory.order[order_id] = generate_order
        print("Order Generated Successfully!")
        print()
        print()
        
        # update stock
        for item in Add_Cart.cart_list:
            product = item[0]
            quantity = item[1]
            product.stock = product.stock - quantity 
        # clear cart 
        Add_Cart.cart_list.clear()
        
        print("================================")
        print("Order Placed Successfull!")
        print("================================")   
        
    def cancel_order(self):
        order_id = int (input("Enter order id :- "))
        order = Order_Inventory.order.get(order_id)
        if order is None:
            print("Order is Not Found :")
            return
        
        # order restore 
        print()
        for item in order.products:
            product = item[0]
            quantity = item[1]
            product.stock += quantity
        # and delete order 
        Order_Inventory.order.pop(order_id)
        print("Order Cancelled Successfully")
        
    def view_order(self):
        # discount amount view
        # discount = order.total_amount * 10 /100
        # viwe product
        if not Order_Inventory.order:
            print("Order Not Found")
            return
        print("=================ORDERS===================")
        for order in Order_Inventory.order.values():
            print("Order ID :-",order.order_id)
            print("Customer ID :-",order.customer_id)
            print("Order Date:-",order.order_date)
            print("Payment:-",order.payment_status)
            print("Total :-",order.total_amount)
            print()
            print()
            print("PRODUCTS : ")
            print()
            for item in order.products:
                product =item[0]
                quantity = item[1]
                print(product.name ,quantity)
                
                
            