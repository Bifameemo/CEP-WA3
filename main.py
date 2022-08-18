import random
import os

class Player():
    def __init__(self, name):
        self.name = name.capitalize()
        self.balance = 5000
        self.rating = 0
        self.score = 0
        self.stock = []

    def get_info(self):
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
            self.score += product.price / 10
            customer.selllist.remove(product)
            customer.fulfilled.append(f"You bought {product.name} for ${product.price}")

    def sell(self, product, customer):
        if product.name in self.stock:
            self.stock.remove(product.name)
            self.balance += product.price
            self.score += product.price / 5
            customer.buylist.remove(product)
            customer.fulfilled.append(f"You sold {product.name} for ${product.price}")
        else:
            print("You don't have that!")
            input()

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

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Bus():
    def __init__(self):
        self.day = 0
        self.passengers = []
        self.profits = 0

    def get_info(self):
        for passenger in self.passengers:
            print(f"{self.passengers.index(passenger) + 1}. {passenger}")
        print()

    def get_profits(self):
        self.profits = 0
        for customer in self.passengers:
            for product in customer.fulfilled:
                if product.split()[1] == "bought":
                    self.profits -= int(product.split()[-1][1:])
                elif product.split()[1] == "sold":
                    self.profits += int(product.split()[-1][1:])
        if self.profits > 0:
            print(f"Today, you made a net profit of ${self.profits}")
        elif self.profits < 0:
            print(f"Today, you made a net loss of ${-self.profits}")
        else: print("Nothing much happened today...")
        print()

    def start_new_day(self):
        self.day += 1
        self.passengers = [Customer(name) for name in random.sample(names, 4 + self.day // 2)]
        print(f"{f'DAY-{self.day}':^50}".replace(" ", "="))
        self.get_info()

    def welcome_passengers(self, choices):
        self.passengers = [self.passengers[index - 1] for index in choices]

    def show_customers(self):
        print(f"{'CUSTOMERS':^50}".replace(" ", "="))
        self.get_info()

def show_interactions():
    print(f"{'INTERACTIONS':^50}".replace(" ", "="))
    print("""1. View your info
2. View a Customer's shopping list
3. Buy a Product from a Customer
4. Sell a Product to a Customer
5. End the day
""")

names = ["Leam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia"]

products = [[chr(i).upper(), range(10, 10000)] for i in range(97, 107)]

os.system("CLS")
print("This is a game.")
input()
print("In this game, you manage a store.")
input()
print("Your task is to buy and sell Products from and to Customers.")
input()
print("Don't go bankrupt and keep on trading.")
input()

name = input("Give yourself a name, and you may begin!\n>> ")
while True:
    if name == "":
        name = input("Enter a name!\n>>")
    else:
        break

player = Player(name)
bus = Bus()

while True:
    os.system("CLS")
    bus.start_new_day()
    print("=" * 50)
    while True:
        try:
            choice = list(map(int, input("\nWho would you like to let into your store? Pick at least 3. (eg. 1 3 4)\n>> ").split()))
            if list(set(choice)) != sorted(choice) or min(choice) < 1 or len(choice) < 3:
                raise Exception
            bus.welcome_passengers(choice)
        except:
            print("Please enter a valid input.")
        else:
            break

    while True:
        os.system("CLS")
        bus.show_customers()
        show_interactions()
        print("=" * 50)
        while True:
            try:
                choice = int(input("\nWhat would you like to do? (eg. 3)\n>> "))
                if choice < 1 or choice > 5:
                    raise Exception
            except:
                print("Please enter a valid input.")
            else:
                break

        if choice == 1:
            os.system("CLS")
            player.get_info()
            input()
            
        elif choice == 2:
            os.system("CLS")
            bus.show_customers()
            print("=" * 50)
            while True:
                try:
                    choice = int(input("\nWhich Customer's shopping list would you like to view? (eg. 3)\n>> "))
                    if choice < 1 or choice > len(bus.passengers):
                        raise Exception
                except:
                    print("Please enter a valid input.")
                else:
                    break

            os.system("CLS")
            bus.passengers[choice - 1].get_info()
            print("=" * 50)
            input()
            
        elif choice == 3:
            os.system("CLS")
            bus.show_customers()
            print("=" * 50)
            while True:
                try:
                    choice = int(input("\nWhich Customer would you like to buy from? (eg. 3)\n>> "))
                    if choice < 1 or choice > len(bus.passengers):
                        raise Exception
                except:
                    print("Please enter a valid input.")
                else:
                    break

            customer = bus.passengers[choice - 1]
            os.system("CLS")
            print(customer.name)
            customer.get_selllist()
            print("=" * 50)
            while True:
                try:
                    choice = int(input("\nWhich Product would you like to buy? (eg. 3)\n>> "))
                    if choice < 1 or choice > len(customer.selllist):
                        raise Exception
                except:
                    print("Please enter a valid input.")
                else:
                    break

            player.buy(customer.selllist[choice - 1], customer)
            
        elif choice == 4:
            os.system("CLS")
            bus.show_customers()
            print("=" * 50)
            while True:
                try:
                    choice = int(input("\nWhich Customer would you like to sell to? (eg. 3)\n>> "))
                    if choice < 1 or choice > len(bus.passengers):
                        raise Exception
                except:
                    print("Please enter a valid input.")
                else:
                    break

            customer = bus.passengers[choice - 1]
            os.system("CLS")
            print(customer.name)
            customer.get_buylist()
            print("=" * 50)
            while True:
                try:
                    choice = int(input("\nWhich Product would you like to sell? (eg. 3)\n>> "))
                    if choice < 1 or choice > len(customer.buylist):
                        raise Exception
                except:
                    print("Please enter a valid input.")
                else:
                    break

            player.sell(customer.buylist[choice - 1], customer)
            
        elif choice == 5:
            os.system("CLS")
            print(f"{f'DAY-{bus.day}-SUMMARY':^50}".replace(" ", "="))
            bus.get_profits()
            for customer in bus.passengers:
                customer.get_fulfilled()
                print()
            print("=" * 50)
            print()
            player.get_info()
            input()
            break
    
    if player.balance >= 0:
        pass
    elif player.score >= 0:
        pass
    elif player.score < 100000:
        pass
