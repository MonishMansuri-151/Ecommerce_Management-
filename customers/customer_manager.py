from customers.customer import Customers_Detail
from customers.customer_inventory import Customer_Inventory

class Customer_Manager:
    def __init__(self):
        pass

    def add_customer(self):
        customer_id = int(input("Enter a customer iD :"))
        customer_name = input("Enter customer name :")
        email_id = input("Enter email id: ")
        phone_no = int(input("Enter a phone number :"))
        customer_address = input("Enter a customer address:")
        add_detail = Customers_Detail(
            customer_id, customer_name, email_id, phone_no, customer_address)
        Customer_Inventory.customer_Dict[customer_id] = add_detail

        print("\nSUCCESSFULL ADD CUSTOMER DETAIL:==")

    def viwe_customer(self):
        print("\n" + "=" * 75)

        print(f"{'ID':<6}{'Name':<15}{'Email_id':<28}{'Phone_no':<16}{'Address':<8}")

        print("=" * 75)

        if not Customer_Inventory.customer_Dict:

            print("Customer Detail Not  Available!")

        else:
            for customer_id, val in Customer_Inventory.customer_Dict.items():
                print(
                    f"{customer_id:<6}"
                    f"{val.customer_name:<15}"
                    f"{val.email_id:<28}"
                    f"{val.phone_no:<16}"
                    f"{val.customer_address:<8}"
                )

        print("=" * 75)

    def search_customer(self):
        search = int(input("Enter a Customer ID :-"))
        get_customer = Customer_Inventory.customer_Dict.get(search)
        if get_customer ==  None:
            print("Customer detail not found :")
        else:
            print("\n" + "=" * 90)

            print(
                f"{'ID':<6}{'Name':<15}{'Email_id':<28}{'Phone_no':<16}{'Address':<18}"
            )
            print("=" * 90)
            print(
                f"{get_customer.customer_id:<6}"
                f"{get_customer.customer_name:<15}"
                f"{get_customer.email_id:<28}"
                f"{get_customer.phone_no:<16}"
                f"{get_customer.customer_address:<18}"
            )

    def update_customer(self):
        try:
            update = int(input("Enter customer ID :"))
            id_get = Customer_Inventory.customer_Dict.get(update)
            if id_get == None:
                print("Customer id not found ")
            new_email_id = input("Enter new email id :")
            new_phone_no = int(input("Enter new phone number :"))
            new_customer_address = input("Enter new customer address")
            id_get.email_id = new_email_id
            id_get.phone_no = new_phone_no
            id_get.customer_address = new_customer_address
            print()
            print("update successfull:-")

        except ValueError as e:
            print("value error ", e)

    def delete_customer(self):
        try:
            customer_id = int(input("Enter product_id : "))
            get_id = Customer_Inventory.customer_Dict.get(customer_id)
            if get_id is None:
                print("Invalid Product Id")
            else:
                del Customer_Inventory.customer_Dict[customer_id]
                print("Delete customer  Successfully ")
        except ValueError:
            print("Please enter a valid customer  ID.")
