class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self.__price = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")

        self.__stock = value

    def __str__(self):
        return f"Name : {self.__name} | Price : {self.__price} | Stock :{self.__stock}"

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False
