class Player():
    def __init__(self, name):
        self.name = name.capitalize()
        self.balance = 500000
        self.rating = 3
        self.score = 0
        self.stock = []

    def get_info(self):
        self.score = self.rating * 1000 + self.balance
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance}")
        print(f"Rating: {self.rating}")
        print(f"Score: {self.score}")
        print(f"{'STOCK':^50}".replace(" ", "="))
        print()
        for item in self.stock:
            print(item)
        print("=" * 50)

    def buy(self, product, customer):
            self.stock.append(product.name)
            self.balance -= product.price
            customer.selllist.remove(product)
            customer.fulfilled.append(f"You bought {product.name} for ${product.price}")

    def sell(self, product, customer):
        if product.name in self.stock:
            self.stock.remove(product.name)
            self.balance += product.price
            customer.buylist.remove(product)
            customer.fulfilled.append(f"You sold {product.name} for ${product.price}")
        else:
            print("You don't have that!")
            input()
