import os

from player import Player
from bus import Bus

def show_interactions():
    print(f"{'INTERACTIONS':^50}".replace(" ", "="))
    print("""1. View your info
2. View your Customers' shopping lists
3. Buy a Product from a Customer
4. Sell a Product to a Customer
5. End the day
""")

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
            bus.show_customers_info()
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

            all_fulfilled = True
            for customer in bus.passengers:
                if len(customer.fulfilled) == 0:
                    all_fulfilled = False
                customer.get_fulfilled()
                print()
            print("=" * 50)
            print()
            if all_fulfilled == True:
                player.rating += 1
                print("You interacted with everyone today!")
                print("Rating increased by 1.")
            else:
                player.rating -= 1
                print("You neglected some Customers today...")
                print("Rating fell by 1.")

            print()
            print("You pay $1000 in rent to your landlord.")
            player.balance -= 1000
            print()
            player.get_info()
            input()
            break

    os.system("CLS")
    if player.balance < 0:
        bus.display_bankruptcy()
    elif player.rating < 0:
        bus.display_negligence()
    elif player.score >= 100000:
        bus.display_score_success()

    if player.balance < 0 or player.rating < 0 or player.score >= 100000:
        print(f"{'FINAL-STATS':^50}".replace(" ", "="))
        player.get_info()
        input()
        exit()
