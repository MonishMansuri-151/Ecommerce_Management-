from products.inventory import Inventory
from customers.customer_inventory import Customer_Inventory
from orders.order_inventory import Order_Inventory
class Report_Manager:
    def __init__(self):
        pass
    def product_report(self):
        # Total Products
        # Most Expensive Product
        # Cheapest Product
        # Out Of Stock Products
        if not Inventory.products:
            print("Inventory Empty ")
            return 
        print("Total Products => ",len(Inventory.products))
        print()
        most_expensive = None
        for product in Inventory.products.values():
            # check most expensive price 
            if most_expensive is None:
               most_expensive = product
            elif product.price > most_expensive.price:
                most_expensive = product
            
        print("-----------------------------------------------------")    
        print("Most Expensive Product name => ",most_expensive.name,)
        print("Most Expensive Product Price => ",most_expensive.price)
        print("------------------------------------------------------")
        print()
        # most cheapest product
        most_cheapest = None 
        for item in Inventory.products.values():
            if most_cheapest is None:
                most_cheapest = item
            if item.price < most_cheapest.price:
                most_cheapest = item
        print("---------------------------------------------------")
        print("Most Cheapest Product name =>",most_cheapest.name)
        print("Most Cheapest Product Price =>",most_cheapest.price)
        print("----------------------------------------------------")
        # check product out of stock or not 
        print()
        found = False
        for pro in Inventory.products.values():
            if pro.stock == 0:
                found = True
                print("=======================")
                print("Out Of Stock Products !")
                print("=========================")
                print("Product Name is :-",pro.name)
                print(f"Out Of Stock Products {pro.name} ",pro.stock)
        if found == False:
            print("========================")
            print("No Out Of Stock Products")
                
    
    def customer_report(self):
        # customer report 
        # print the Total customers
        print("===== Customer Report ======")
        print("Total Customers = ",len(Customer_Inventory.customer_Dict))
        print()
        # active customers and inactive customer 
        count = 0
        count2 =0
        for customer in Customer_Inventory.customer_Dict.values():
                found = False
                for order in Order_Inventory.order.values():
                    if customer.customer_id == order.customer_id:
                      found = True
                      count +=1
                      print("=======Active Customers====== ")
                      print(customer.customer_name)
                      break
                if found == False:
                    count2 +=1
                    print("========Inactive Customer========")
                    print(customer.customer_name)
                
        print()
        print("Active Customer :-",count)   
        print("Inactive Customer:-",count2)          
        
    def sales_report(self):
        # Sales Report
        # # Display:
        # # Total Orders
        # # Total Revenue
        # # Average Order Value
        # # Highest Order Value
        print("=====Total Order=====")
        print()
        print("Total Order:",len(Order_Inventory.order))
        print()
        print("=====Total Revenue=====")
        print()
        total =0
        for amount in Order_Inventory.order.values():
            total = total + amount.total_amount 
        print("Total Reveneue :",total)
        print()
        print("==========Average Order Value==========")
        print()
        if not Order_Inventory.order:
            print("No Orders Found")
            return

        average_order = total/len(Order_Inventory.order) 

        print("Average Order Value : ",average_order)
        print()
        print("===========Highest Order value==========")
        print()
        highest = None
        for item in Order_Inventory.order.values():
            if highest is None:
                highest = item
            elif item.total_amount > highest.total_amount:
                highest = item
        print("Highest Order ID :", highest.order_id)
        print()
        print("Customer ID :", highest.customer_id)
        print()
        print("Highest Order Value :", highest.total_amount)
        
        
        