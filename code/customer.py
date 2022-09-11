import random
from product import Product

class Customer():
    def __init__(self, name, products, difficulty):
        self.name = name
        self.receipts = []
        # generates list of Products with a random name picked from "products"
        # number of Products in each list ranges from a minimum of 1 to a maximum that scales with the day Players are on, ie. difficulty
        self.buylist = [Product(name) for name in random.sample(products, random.randint(1, 5 + difficulty))]
        self.selllist = [Product(name) for name in random.sample(products, random.randint(1, 5 + difficulty))]

    # prints out all of Customer's past transactions as saved in self.receipts
    def display_receipts(self):
        print(f"|{self.name}|".center(50).replace(" ", "="))
        for index, receipt in enumerate(self.receipts):
            print(f"{index + 1:>2}. {receipt}")
        if len(self.receipts) == 0:
            print(f" You didn't interact with {self.name}...")

    # prints out Customer's buylist, ie. what Players can sell to the Customer
    def display_buylist(self):
        print(f"|{self.name}|".center(50))
        print("|BUYING|".center(50).replace(" ", "="))
        for index, product in enumerate(self.buylist):
            print(f"{index + 1:>2}. {product.name:<16} {'|':>22} {f'${product.price}':>4}")

    # prints out Customer's selllist, ie. what Players can buy from the Customer
    def display_selllist(self):
        print(f"|{self.name}|".center(50))
        print("|SELLING|".center(50).replace(" ", "="))
        for index, product in enumerate(self.selllist):
            print(f"{index + 1:>2}. {product.name:<16} {'|':>22} {f'${product.price}':>4}")
