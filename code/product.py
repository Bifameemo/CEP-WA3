import random

class Product():
    def __init__(self, name):
        self.name = name
        # sets a random price in the given range
        self.price = random.choice(range(100, 9999))
