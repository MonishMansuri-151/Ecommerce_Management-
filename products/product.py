class Product:
    def __init__(self, product_id, name, category, price, stock, brand, rating):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.__price = price
        self.stock = stock
        self.brand = brand
        self.rating = rating
    def set_price(self, price):
        if price > 0:
            self.__price = price
    def get_price(self):
        return self.__price