class Player():
    def __init__(self, full_name):
        # formats name inputted, capitalises first letter of every word
        self.name = "_".join([name.capitalize() for name in full_name.split()])
        self.balance = 25000
        self.rating = 3
        self.score = 0
        self.stock = []

    # prints all of Player's details
    def display_info(self):
        # calculates Player's score before printing
        # 1 Rating is worth 5000 score, and then Player's balance is added on top of that
        self.score = self.rating * 5000 + self.balance
        print(f"|{self.name}|".center(50).replace(" ", "="))
        print(f" Balance: ${self.balance}")
        print(f" Rating: {self.rating}")
        print(f" Score: {self.score}")
        print("|STOCK|".center(50).replace(" ", "="))
        # if nothing is in stock, prints "You have nothing in stock" instead of leaving an empty line
        if len(self.stock) == 0:
            print(" You have nothing in stock")
        else:
            for index, product in enumerate(self.stock):
                print(f"{index + 1:>2}. {product}")

    def buy_product_from(self, product, customer):
        # adds the Product to the Player's stock
        self.stock.append(product.name)
        # reduces Player's balance by the Product's price
        self.balance -= product.price
        # removes the Product from the Customer's selllist
        customer.selllist.remove(product)
        # creates and adds a receipt to the Customer
        customer.receipts.append(f"You bought {product.name} for ${product.price}")

    def sell_product_to(self, product, customer):
        # removes the Product from the Player's stock
        self.stock.remove(product.name)
        # increases the Player's balance by the Product's price
        self.balance += product.price
        # removes the Product from the Customer's buylist
        customer.buylist.remove(product)
        # creates and adds a receipt to the Customer
        customer.receipts.append(f"You sold {product.name} for ${product.price}")
