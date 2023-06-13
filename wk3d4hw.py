class Cart:
    def __init__(self, name):
        self.cart = {}
        self.name = name

    def add(self, item, quantity):
        self.cart[item.upper()] = self.cart.get(item.upper(), 0) + quantity

    def remove(self, item, quantity):
        item = item.upper()
        if item not in self.cart:
            return "This item does not exist in your cart."
        self.cart[item] -= quantity
        if self.cart[item] == 0:
            del self.cart[item]

    def show(self):
        if not self.cart:
            return "Your cart is currently empty"
        output = "\n{}'s SHOPPING CART".format(self.name)
        for item, quantity in self.cart.items():
            output += "\nItem: {} - Quantity: {}".format(item, quantity)
        return output
