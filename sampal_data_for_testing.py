from products.product import Product
from products.inventory import Inventory

from customers.customer import Customers_Detail
from customers.customer_inventory import Customer_Inventory


def load_sample_data():

    # Products
    Inventory.products[101] = Product(
        101, "Laptop", "Electronics", 55000, 10, "Dell", 4.5
    )

    Inventory.products[102] = Product(
        102, "Mouse", "Electronics", 800, 50, "Logitech", 4.2
    )
    
    Inventory.products[103] = Product(
        103, "phone", "Electronics", 40000, 10, "vivo", 4.3
    )
    Inventory.products[104] = Product(
        104, "Fan", "Electronics", 5000, 20, "Bjaj", 3.2
    )
    Inventory.products[105] = Product(
        105, "AC", "Electronics", 30000, 50, "sumsung", 4.5
    )
    Inventory.products[106] = Product(
        106, "Table", "furniture", 4000, 30, "Wood", 2.4
    )

    # Customers
    Customer_Inventory.customer_Dict[1] = Customers_Detail(
        1, "Monish", "monish@gmail.com", 9876543210, "Jaipur"
    )

    Customer_Inventory.customer_Dict[2] = Customers_Detail(
        2, "Rahul", "rahul@gmail.com", 9876543211, "Ajmer"
    )