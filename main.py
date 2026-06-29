from customers.customer_manager import Customer_Manager
from products.product_manager import Product_manager
from shoping_cart.cart_manager import Cart_Manager
from orders.order_manager import Order_Manage
from sampal_data_for_testing import load_sample_data


obj_manager = Product_manager()
cust_manager = Customer_Manager()
obj_cart_manager = Cart_Manager()
obj_order = Order_Manage()

load_sample_data()
while True:
    print("\n===== E-Commerce System =====")
    print("1. Product Management")
    print("2. Customer Management")
    print("3. Shopping Cart System")
    print("4.Order Management ")
    print("5. Exit")
    

    Choice = int(input("Enter your Choices :- "))

    if Choice == 1:
        while True:
            print("\n===== Product Management =====")
            print("1. Add Product")
            print("2. View Products")
            print("3. Search Product")
            print("4. Update Product")
            print("5. Delete Product")
            print("6. Exit")
            print()

            choice = input("Enter your choice :")
            if choice == "1":
                obj_manager.add_product()
            elif choice == "2":
                obj_manager.viwe_product()
            elif choice == "3":
                obj_manager.search_product()
            elif choice == "4":
                obj_manager.update_product()
            elif choice == "5":
                obj_manager.delete_product()
            elif choice == "6":
                break
            else:
                print("invalid choice :")

    elif Choice == 2:
        while True:
            print("\n===== Customer Management =====")
            print("1. Add Customer :-")
            print("2. View  Customer:-")
            print("3. Search Customer:-")
            print("4. Update Customer:-")
            print("5. Delete Customer:-")
            print("6. Exit")
            print("\n")

            choice = input("Enter your choice :")
            if choice == "1":
                cust_manager.add_customer()
            elif choice == "2":
                cust_manager.viwe_customer()
            elif choice == "3":
                cust_manager.search_customer()
            elif choice == "4":
                cust_manager.update_customer()
            elif choice == "5":
                cust_manager.delete_customer()
            elif choice == "6":
                break
            else:
                print("invalid choice :")
                
    elif Choice == 3:
        while True:
            print("\n===== ADD TO CART  =====")
            print("1.Add Cart Items :-  ")
            print("2.Remove itmes from Cart :- ")
            print("3.view product :-")
            print("4.Sum of total price of product :-  ")
            print("5. Exit")
            print("\n")
            
            choice = input("Enter your choice :")
            if choice == "1":
                obj_cart_manager.add_cart()
            elif choice == "2":
                obj_cart_manager.remove_cart()
            elif choice == "3":
                obj_cart_manager.view_product()    
            elif choice == "4":
                obj_cart_manager.total_sum()
            elif choice == "5":
                print("Exit:-")
                break
            else:
                print("invalid choice :")
                
    elif Choice == 4:
         while True:
            print("\n===== ORDER  =====")
            print("1.Place Order ")
            print("2.Cancel Order ")
            print("3.view Order ")
            print("\n")
            
            choice = input("Enter your choice :")
            if choice == "1":
                obj_order.place_order()
            elif choice == "2":
                obj_order.cancel_order()
            elif choice == "3":
                obj_order.view_order()    
            elif choice == "4":
                print("Exit:-")
                break
            else:
                print("invalid choice :")
        
                
    elif Choice  == 5:
           print("exit !")
           break     
    else:
        print("Invalid choice !-") 