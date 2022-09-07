import random

from product import Product

products = [[chr(i).upper(), range(10, 10000)] for i in range(97, 110)]

class Customer():
    def __init__(self, name):
        self.name = name
        self.fulfilled = []
        self.buylist = [Product(item[0], random.choice(item[1])) for item in random.sample(products, random.randint(1, len(products)))]
        self.selllist = [Product(item[0], random.choice(item[1])) for item in random.sample(products, random.randint(1, len(products)))]

    def __repr__(self):
        return self.name

    def get_buylist(self):
        print(f"{'BUYING':^50}".replace(" ", "="))
        for index, item in enumerate(self.buylist):
            print(f"{index + 1}. {item}")

    def get_selllist(self):
        print(f"{'SELLING':^50}".replace(" ", "="))
        for index, item in enumerate(self.selllist):
            print(f"{index + 1}. {item}")

    def get_fulfilled(self):
        print(f"{f'{self.name}':^50}".replace(" ", "="))
        for index, item in enumerate(self.fulfilled):
            print(f"{index + 1}. {item}")

    def get_info(self):
        print(self.name)
        print(f"{'DONE':^50}".replace(" ", "="))
        for item in self.fulfilled:
            print(item)
        print()
        self.get_buylist()
        print()
        self.get_selllist()
        print()
