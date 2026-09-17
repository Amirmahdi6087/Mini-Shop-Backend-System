class Order:
    def __init__(self):
        self.shopping_cart = list()

    def add_product(self, product):
        self.shopping_cart.append(product)

    def total_price(self) -> int:
        total = 0
        for item in self.shopping_cart:
            total += (item.price * item.stock)
        return total

    def __len__(self) -> int:
        return len(self.shopping_cart)

    def __str__(self) -> str:
        result = "Order:\n"

        for item in self.shopping_cart:
            result += f"{item}\n"

        return result
