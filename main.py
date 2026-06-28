from customers.customer_manager import Customer_Manager
from products.product_manager import Product_manager
from orders.cart_manager import Cart_Manager



obj_manager = Product_manager()
cust_manager = Customer_Manager()
obj_cart_manager = Cart_Manager()
while True:
    print("\n===== E-Commerce System =====")
    print("1. Product Management")
    print("2. Customer Management")
    print("3. Shopping Cart System")
    print("4. Exit")
    

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
            print("3.Sum of total price of product :-  ")
            print("4. Exit")
            print("\n")
            
            choice = input("Enter your choice :")
            if choice == "1":
                obj_cart_manager.add_cart()
            elif choice == "2":
                obj_cart_manager.remove_cart()
            elif choice == "3":
                obj_cart_manager.total_sum()
            elif choice == "4":
                print("Exit:-")
                break
            else:
                print("invalid choice :")
                
    elif Choice  == 4:
           print("exit !")
           break     
    else:
        print("Invalid choice !-") 