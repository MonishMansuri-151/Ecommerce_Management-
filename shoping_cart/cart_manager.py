from shoping_cart.cart import Add_Cart
from products.inventory import Inventory
from customers.customer_inventory import Customer_Inventory

class Cart_Manager:
    def __init__(self):
        pass
    def add_cart (self):
    
        get_search = int(input("Customer id :- "))
        user_get = Customer_Inventory.customer_Dict.get(get_search)
        if user_get is None:
            print("Customer is not Available ! :- ")
            return
        while True:   
            search_product = int(input("Enter product id :- "))
                
            get_product = Inventory.products.get(search_product)
            # get the product id from the user 
            if get_product is None:
                    print("Product id is not avilable :-")  
                    continue
            # get input form user quntity 
            quntitiy = int(input("Enter the quntitity :-"))
            # check quntitiy of the product 
            if quntitiy > get_product.stock:
                print("Stoke is not available : ")
                continue
            
            item = (get_product,quntitiy)
            Add_Cart.cart_list.append(item)
                
            print("Added to cart successfully!")
            choice = input("Do you want to add another product? (y/n): ")

            if choice.lower() != "y":
                break
            
    def remove_cart (self):
        # remove product to cart 
        product_id = int(input("Enter product  Id : "))
        for item in Add_Cart.cart_list:
            product = item[0]
            if product.product_id == product_id:
                Add_Cart.cart_list.remove(item)
                
                print("Product Remove Successfully :- ")
                return
        print("Product not found in Cart  :")  
        
    def view_product(self):
        
        if not  Add_Cart.cart_list :
            print("Cart is Empty : ")
            return
        print("product Add Cart :-")
        print("\nName\t\tQuantity")
        print("-" * 25)
        for item in Add_Cart.cart_list:
            product = item[0]
            quantity= item[1]
            print(f"{product.name}\t\t{quantity}")
                    
       
    def total_sum(self):
        total =0
        for item in Add_Cart.cart_list:
            product = item[0]
            quntitiy = item[1]
            total += product.price * quntitiy
            print()
        print("--Total Price of Product:--",total)
            
                
            