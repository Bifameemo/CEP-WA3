import os
# running os.system("CLS") clears the screen
# always run before printing a new screen
import random
from player_copy import Player
from customer_copy import Customer
from bus_copy import Bus

# file handling to extract all names from customer_names.txt
customer_names = open("customer_names.txt", "r")
line = customer_names.readline()
names = []
while line != "":
    names.append(line[:-1])
    line = customer_names.readline()
customer_names.close()

# file handling to extract all IKEA Product names from product_names.txt
product_names = open("product_names.txt", "r")
line = product_names.readline()
all_products = []
while line != "":
    if len(line) > 3:
        index = 0
        while line[index].isupper() == True:
            index += 1
        all_products.append(line[:index])
    line = product_names.readline()
product_names.close()
# sets the scope to just 50 random Products
# if all 1300+ Products were included from the start,
# the chances of finding matches in Products would be very low...
products = random.sample(all_products, 50)

# introduction sequence
os.system("CLS")
print()
print(" This is a game that is best played in fullscreen.", end = "")
input()
print(" In this game, you manage a store.", end = "")
input()
print(" Your task is to buy and sell Products from and to Customers.", end = "")
input()
print(" Don't go bankrupt, don't neglect any Customers, and keep on trading.", end = "")
input()
print(" Give yourself a name, and you may begin!")
# Players can have any name they want except for an empty string
while True:
    name = input(" >>> ")
    if name == "":
        print(" Enter a name!")
    else:
        break
player = Player(name)
bus = Bus()
day = 0

while True:
    day += 1
    # every day, a maximum of 10 new Products are added to the pool
    # increases the difficulty as days pass
    for product in random.sample(all_products, 10):
        if product not in products:
            products.append(product)
    # fills the Bus with Customers whose names are taken from the list of all names
    # number of Customers increases as days pass, defined by number of Customers = 4 + day // 2
    bus.customers = [Customer(name, products, day) for name in random.sample(names, 4 + day // 2)]
    os.system("CLS")
    print(f"|DAY-{day}|".center(50))
    bus.display_customers()
    print("=" * 50)
    print()
    # minimum required Customers also scales linearly with the day, defined by minimum = 3 + day // 3
    print(f" Who would you like to let into your store today? Pick at least {3 + day // 3}. (eg. 1 4 3)")
    while True:
        try:
            # formats the string from "1 4 3" to a list of numbers, [1, 4, 3]
            choices = list(map(int, input(" >>> ").split()))
            # if there are duplicate entries, invalid numbers that are outside the allowed range, or less numbers than the minimum allows
            # the Exception is raised and Players have to input another input
            if sorted(list(set(choices))) != sorted(choices) or min(choices) < 1 or max(choices) > len(bus.customers) or len(choices) < 3 + day // 3:
                raise Exception
        except:
            print(" Please enter a valid input.")
        else:
            break
    # removes all non-selected Customers from the Bus
    bus.customers = [bus.customers[index - 1] for index in choices]
    while True:
        # main select scren
        # Players select which interaction they wish to do
        os.system("CLS")
        print("|INTERACTIONS|".center(50).replace(" ", "="))
        print(""" 1. View your info
 2. View your Customers' shopping lists
 3. Buy a Product from a Customer
 4. Sell a Product to a Customer
 5. End the day
 6. Quit the game""")
        print("=" * 50)
        print()
        print(" What would you like to do? (eg. 3)")
        # input verification to make sure only one valid integer from 1 to 6 is inputted
        while True:
            try:
                choice = int(input(" >>> "))
                if choice not in range(1, 7):
                    raise Exception
            except:
                print(" Please enter a valid input.")
            else:
                break
        # if Players choose to view their info
        # prints their details and all Customers' receipts
        if choice == 1:
            os.system("CLS")
            player.display_info()
            print("|RECEIPTS|".center(50).replace(" ", "="))
            all_receipts = []
            for customer in bus.customers:
                for receipt in customer.receipts:
                    all_receipts.append(f"{receipt} from {customer.name}")
            if len(all_receipts) == 0:
                print(" Nothing much has happened today...")
            else:
                for index, receipt in enumerate(all_receipts):
                    print(f"{index + 1:>2}. {receipt}")
            print("=" * 50)
            print()
            print(" Type 'esc' to go back.")
            while True:
                choice = input(" >>> ")
                if choice != "esc":
                    print(" Please enter a valid input.")
                else:
                    break
        # if Players choose to view Customers' shopping lists
        # prints all Customer's buylist and selllist in column format
        elif choice == 2:
            os.system("CLS")
            # defaults to page 1
            bus.display_customer_info(1)
            while True:
                print()
                # asks Players what page they wish to see
                print(" Which page would you like to go to? (eg. 3) Type 'esc' to go back.")
                # input verification to make sure only one valid integer from 1 to the max number of pages or "esc" is inputted
                while True:
                    try:
                        page = input(" >>> ")
                        if page == "esc" or int(page) in range(1, int(-(-len(bus.customers) / 5 // 1) + 1)):
                            break
                        else:
                            raise Exception
                    except:
                        print(" Please enter a valid input.")
                # goes back to the interaction screen if "esc" is inputted
                if page == "esc":
                    break
                else:
                    # prints the page inputted
                    os.system("CLS")
                    bus.display_customer_info(int(page))
        # if Players choose to buy a Product from a Customer
        # prints all Customers
        elif choice == 3:
            os.system("CLS")
            bus.display_customers()
            print("=" * 50)
            print()
            # asks Players which Customer they wish to buy from
            print(" Which Customer would you like to buy from? (eg. 3) Type 'esc' to go back.")
            # input verification to make sure only one valid integer from 1 to the max number of Customers or "esc" is inputted
            while True:
                try:
                    choice = input(" >>> ")
                    if choice == "esc" or int(choice) in range(1, len(bus.customers) + 1):
                        break
                    else:
                        raise Exception
                except:
                    print(" Please enter a valid input.")
            # goes back to the interaction screen if "esc" is inputted
            if choice == "esc":
                pass
            else:
                customer = bus.customers[int(choice) - 1]
                # if the Customer's selllist is empty
                if len(customer.selllist) == 0:
                    os.system("CLS")
                    print()
                    # informs the Player that the Customer cannot sell them anything
                    print(f" {customer.name} has nothing to sell...")
                    input()
                else:
                    os.system("CLS")
                    # prints all Products in the Customers selllist
                    customer.display_selllist()
                    print("=" * 50)
                    print()
                    # asks Players which Product in the Customers selllist they wish to buy
                    print(" Which Product would you like to buy? (eg. 3) Type 'esc' to go back.")
                    # input verification to make sure only one valid integer from 1 to the max number of Products in the Customer's selllist
                    # or "esc" is inputted
                    while True:
                        try:
                            choice = input(" >>> ")
                            if choice == "esc" or int(choice) in range(1, len(customer.selllist) + 1):
                                break
                            else:
                                raise Exception
                        except:
                            print(" Please enter a valid input.")
                    # goes back to the interaction screen if "esc" is inputted
                    if choice == "esc":
                        pass
                    else:
                        # allows Players to "buy" the Product from the specified Customer
                        player.buy_product_from(customer.selllist[int(choice) - 1], customer)
        # if Players choose to sell a Product to a Customer
        # prints all Customers
        elif choice == 4:
            os.system("CLS")
            bus.display_customers()
            print("=" * 50)
            print()
            # asks Players which Customer they wish to sell to
            print(" Which Customer would you like to sell to? (eg. 3) Type 'esc' to go back.")
            # input verification to make sure only one valid integer from 1 to the max number of Customers or "esc" is inputted
            while True:
                try:
                    choice = input(" >>> ")
                    if choice == "esc" or int(choice) in range(1, len(bus.customers) + 1):
                        break
                    else:
                        raise Exception
                except:
                    print(" Please enter a valid input.")
            # goes back to the interaction screen if "esc" is inputted
            if choice == "esc":
                pass
            else:
                customer = bus.customers[int(choice) - 1]
                # if the Customer's buylist is empty
                if len(customer.buylist) == 0:
                    os.system("CLS")
                    print()
                    # informs the Player that thet cannot sell anything to that Customer
                    print(f" {customer.name} doesn't want to buy anything...")
                    input()
                else:
                    os.system("CLS")
                    # prints all Products in the Customers selllist
                    customer.display_buylist()
                    print("=" * 50)
                    print()
                    # asks Players which Product in the Customers buylist they wish to sell
                    print(" Which Product would you like to sell? (eg. 3) Type 'esc' to go back.")
                    # input verification to make sure only one valid integer from 1 to the max number of Products in the Customer's buylist
                    # or "esc" is inputted
                    while True:
                        try:
                            choice = input(" >>> ")
                            if choice == "esc" or int(choice) in range(1, len(customer.buylist) + 1):
                                break
                            else:
                                raise Exception
                        except:
                            print(" Please enter a valid input.")
                    # goes back to the interaction screen if "esc" is inputted
                    if choice == "esc":
                        pass
                    # if the Player doesn't have the Product in stock
                    elif customer.buylist[int(choice) - 1].name not in player.stock:
                        os.system("CLS")
                        print()
                        # informs the Player that they don't have the specified Product
                        print(" You don't have that!")
                        input()
                    else:
                        # allows Players to "sell" the Product to the specified Customer
                        player.sell_product_to(customer.buylist[int(choice) - 1], customer)
        # if Players choose to end the day
        # gives them a summary and overview of what happened that day
        elif choice == 5:
            os.system("CLS")
            print(f"|DAY-{day}-SUMMARY|".center(50).replace(" ", "="))
            # calculates the overall profit made from all the Customers' receipts
            profits = 0
            for customer in bus.customers:
                for receipt in customer.receipts:
                    # none of the Products have the phrase "bought" or "sold" in them
                    # otherwise, this method of checking receipts would be inaccurate
                    if "bought" in receipt:
                        profits -= int(receipt.split()[-1][1:])
                    elif "sold" in receipt:
                        profits += int(receipt.split()[-1][1:])
            # prints out the overall profit made by the Player
            if profits > 0:
                print(f" Today, you made a net profit of ${profits}. Good work!")
            elif profits < 0:
                print(f" Today, you made a net loss of ${-profits}. Oh no!")
            # if the Player made no profits or losses
            else:
                # informs the Player that their balance did not change
                print(" Your balance remained unchanged today...")
            print()
            # calculates number of Customers not interacted with
            # if they have no receipts, then that Customer was not interacted with
            neglected_count = 0
            for customer in bus.customers:
                if len(customer.receipts) == 0:
                    neglected_count += 1
                # prints all Customers' receipts
                customer.display_receipts()
                print()
            print("=" * 50)
            # if the Player interacted with all their Customers
            # awards them rating based on how many Customers they interacted with
            # rating awarded = number of Customers interacted with // 2
            if neglected_count == 0:
                player.rating += len(bus.customers) // 2
                print(" You interacted with everyone today!")
                print(f" Rating increased by {len(bus.customers) // 2}.")
            # if at least one Customer was not interacted with
            # the Player gains 0 rating, and instead loses rating based on how many Customers were neglected
            # rating taken away = number of Customers neglected
            # one bad experience overshadows all good ones
            else:
                player.rating -= neglected_count
                print(f" You neglected {neglected_count} Customers today...")
                print(f" Rating fell by {neglected_count}.")
            print()
            # daily tax that scales with the day to add extra difficulty to the game
            # daily tax = day * 1000
            print(f" You pay ${1000 * day} in rent to your landlord.")
            player.balance -= 1000 * day
            print()
            # prints the Player's details
            player.display_info()
            print("=" * 50)
            input()
            break
        # if the Player chooses to quit the game D:
        # prints their details at the time of quitting
        # before ending the program
        elif choice == 6:
            os.system("CLS")
            print()
            print("It's sad to see you go so soon...")
            print()
            print("|FINAL-STATS|".center(50))
            # prints the Player's details at the time of quitting
            player.display_info()
            print("=" * 50)
            input()
            # ends the program D:
            exit()

    os.system("CLS")
    # checks Player's balance, rating and score at the end of the day
    # if the Player's balance falls below 0
    # informs the Player that they have gone bankrupt, BAD ENDING
    if player.balance < 0:
        print("|BANKRUPTCY|".center(50).replace(" ", "="))
        print(" YOU RAN OUT OF MONIES!!")
    # if the Player's rating falls below 0
    # informs the Player that they did not interact with their Customers enough, BAD ENDING
    elif player.rating < 0:
        print("|NEGLIGENCE|".center(50).replace(" ", "="))
        print(" You ngelected your customers too much...")
    # if the Player's score exceeds 100000
    # informs the Player that they have beaten the game, GOOD ENDING!
    elif player.score >= 100000:
        print("|SUCCESS|".center(50).replace(" ", "="))
        print(" You started up a successful business!! CONGRATULATIONS")
    # if any of the above clauses were met
    # prints the Player their details
    # before ending the program
    if player.balance < 0 or player.rating < 0 or player.score >= 100000:
        print()
        print("=" * 50)
        print()
        print("|FINAL-STATS|".center(50))
        # prints the Player their details
        player.display_info()
        print("=" * 50)
        input()
        # ends the program
        exit()
