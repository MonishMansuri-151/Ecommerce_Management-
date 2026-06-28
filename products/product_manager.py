from products.inventory import Inventory
from products.product import Product


class Product_manager:
    def __init__(self):
        pass

    def add_product(self):

        # Inventory.products[user_product.product_id] = user_product
        # print("inside the manager", Inventory.products)
        product_id = int(input("Enter product iD : "))
        name = input("Enter product name : ")
        category = input("Enter Category of product : ")
        price = float(input("Enter price of product : "))
        stock = int(input("Enter stock : "))
        brand = input("Enter the Brande of product : ")
        rating = float(input("Enter rating of product :"))
        add = Product(product_id, name, category, price, stock, brand, rating)
        Inventory.products[add.product_id] = add

        print(" PRODUCT ADD DICTIONARY --------- : ")
        # print(Inventory.products)

    def viwe_product(self):
        # back \t ki  wjha se ye nya approch use kar rhe he kyunki usme product shi view nhi aa rha tha islye use kar rhe he
        print("\n" + "=" * 90)

        print(
            f"{'ID':<6}{'Name':<15}{'Category':<18}{'Price':<12}{'Stock':<8}{'Brand':<15}{'Rating'}"
        )

        print("=" * 90)

        if not Inventory.products:
            print("No Products Available!")

        else:
            for product_id, val in Inventory.products.items():
                print(
                    f"{product_id:<6}"
                    f"{val.name:<15}"
                    f"{val.category:<18}"
                    f"{val.price:<12}"
                    f"{val.stock:<8}"
                    f"{val.brand:<15}"
                    f"{val.rating}"
                )

        print("=" * 90)

    def search_product(self):
        search = int(input("Enter product iD.."))

        user_get = Inventory.products.get(search)

        if user_get is None:
            print(" USER NOT FOUND... ")
        else:
            print("\n" + "=" * 90)

            print(
                f"{'ID':<6}{'Name':<15}{'Category':<18}{'Price':<12}{'Stock':<8}{'Brand':<15}{'Rating'}"
            )
            print("=" * 90)
            print(
                f"{user_get.product_id:<6}"
                f"{user_get.name:<15}"
                f"{user_get.category:<18}"
                f"{user_get.price:<12}"
                f"{user_get.stock:<8}"
                f"{user_get.brand:<15}"
                f"{user_get.rating}"
            )

    def update_product(self):
        try:
            product_id = int(input("Enter a product Id : "))
            get_id = Inventory.products.get(product_id)
            if get_id == None:
                print("PRODUCT NOT FOUND ")

            new_price = int(input("Enter new price : "))
            new_stock = int(input("Enter new stock : "))
            new_rating = float(input("Enter new rating : "))
            get_id.price = new_price
            get_id.stock = new_stock
            get_id.rating = new_rating
            print("Product Update Successfully :-")
        except ValueError as e:
            print("value not match ", e)

    def delete_product(self):
        # perform delete opreations
        try:
            product_id = int(input("Enter product_id : "))
            get_id = Inventory.products.get(product_id)
            if get_id is None:
                print("Invalid Product Id")
            else:
                del Inventory.products[product_id]
                print("Delete Product Successfully ")
        except ValueError:
            print("Please enter a valid Product ID.")
