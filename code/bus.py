import os
os.system("color")
# to print colored text later

class Bus():
    def __init__(self):
        self.customers = []

    # prints all Customers in the Bus
    def display_customers(self):
        print("|CUSTOMERS|".center(50).replace(" ", "="))
        for index, customer in enumerate(self.customers):
            print(f"{index + 1:>2}. {customer.name}")

    # prints all Customers in the Bus according to page along with their buylist and selllist
    def display_customer_info(self, page):
        # sets scope of Customers to only Customers on the page 
        customers = self.customers[5 * (page - 1):5 * page]
        # prints all Customers' names in a row
        for customer in customers:
            print(f"|{customer.name:^29}", end = "")
        print("|")
        print("|BUYING|".center(len(customers) * 30 + 1).replace(" ", "="))
        # method to find matching Products in buylists and selllists
        all_lists = []
        common_products = []
        for customer in self.customers:
            for product in customer.buylist + customer.selllist:
                all_lists.append(product.name)
        # if a Product appears multiple times in all_lists, then it is considered matching and added to common_products
        for product in all_lists:
            if all_lists.count(product) > 1:
                common_products.append(product)
        # loops through index based on the longest buylist
        for index in range(max([len(customer.buylist) for customer in customers])):
            for customer in customers:
                # try except is used to avoid "list index out of range" errors
                # if the index is in the range, it prints the Product details at that index
                # if the index is out of the range, then there are no more Products to be printed, so it prints an empty column
                try:
                    product = customer.buylist[index]
                    # if the Product is in the common_products, it is considered matching and then printed in yellow
                    # this makes it easier for Players to find common Products between Customers' buylsits and selllists
                    # otherwise, the Product's details are printed normally
                    if product.name in common_products:
                        print(f"|\033[1;33;40m{index + 1:>2}. {product.name:<16}\033[1;37;40m | ${product.price:<4} ", end = "")
                    else:
                        print(f"|{index + 1:>2}. {product.name:<16} | ${product.price:<4} ", end = "")
                except:
                    print(f"|{' ' * 29}", end = "")
            print("|")
        print("|SELLING|".center(len(customers) * 30 + 1).replace(" ", "="))
        # loops through and prints the same thing as the loop above, except for Customers' selllist instead of buylist
        for index in range(max([len(customer.selllist) for customer in customers])):
            for customer in customers:
                try:
                    product = customer.selllist[index]
                    if product.name in common_products:
                        print(f"|\033[1;33;40m{index + 1:>2}. {product.name:<16}\033[1;37;40m | ${product.price:<4} ", end = "")
                    else:
                        print(f"|{index + 1:>2}. {product.name:<16} | ${product.price:<4} ", end = "")
                except:
                    print(f"|{' ' * 29}", end = "")
            print("|")
        # prints the current page number out of the total number of pages
        print(f"|Page-{page}/{int(-(-len(self.customers) / 5 // 1))}|".center(len(customers) * 30 + 1).replace(" ", "="))
