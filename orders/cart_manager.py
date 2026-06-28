from orders.cart import Add_Cart
from products.inventory import Inventory
from customers.customer_inventory import Customer_Inventory

obj_add = Add_Cart()

class Cart_Manager:
    def __init__(self):
        pass
    def add_cart (self):
        get_search = int(input("Customer id :- "))
        user_get = Customer_Inventory.customer_Dict.get(get_search)
        if user_get is None:
            print("Customer is not Available ! :- ")
            return
            
        search_product = int(input("Enter product id :- "))
        
        get_product = Inventory.products.get(search_product)
        # get the product id from the user 
        if get_product is None:
            print("Product id is not avilable :-")  
            return 
        # get input form user quntity 
        quntitiy = int(input("Enter the quntitity :-"))
        # check quntitiy of the product 
        if quntitiy > get_product.stock:
            print("Stoke is not available : ")
            return 
            
        item = (get_product,quntitiy)
        obj_add.cart_list.append(item)
        print("Added to cart successfully!")
            
    def remove_cart (self):
        pass
    def total_sum(self):
        pass