import random

from customer import Customer

names = ["Leam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia"]

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

    def show_customers_info(self):
        for customer in self.passengers:
            print(f"|{customer.name:^20}", end = "")
        print("|")
        print(f"{'FULFILLED'}".center(len(self.passengers) * 21 + 1).replace(" ", "="))
        for index in range(max([len(customer.fulfilled) for customer in self.passengers]) + 1):
            for customer in self.passengers:
                try:
                    print(f"|{str(customer.fulfilled[index]):<20}", end = "")
                except:
                    print(f"|{' ' * 20}", end = "")
            print("|")
        print(f"{'BUYING'}".center(len(self.passengers) * 21 + 1).replace(" ", "="))
        for index in range(max([len(customer.buylist) for customer in self.passengers]) + 1):
            for customer in self.passengers:
                try:
                    print(f"|{str(customer.buylist[index]):<20}", end = "")
                except:
                    print(f"|{' ' * 20}", end = "")
            print("|")
        print(f"{'SELLING'}".center(len(self.passengers) * 21 + 1).replace(" ", "="))
        for index in range(max([len(customer.selllist) for customer in self.passengers]) + 1):
            for customer in self.passengers:
                try:
                    print(f"|{str(customer.selllist[index]):<20}", end = "")
                except:
                    print(f"|{' ' * 20}", end = "")
            print("|")

    def display_bankruptcy(self):
        print(f"{'BANKRUPTCY':^50}".replace(" ", "="))
        print("YOU RAN OUT OF MONIES!!")
        print()

    def display_negligence(self):
        print(f"{'NEGLIGENCE':^50}".replace(" ", "="))
        print("You ngelected your customers too much...")
        print()

    def display_score_success(self):
        print(f"{'SUCCESS':^50}".replace(" ", "="))
        print("You started up a successful business!! CONGRATULATIONS")
        print()
        
        
