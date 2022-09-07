# Development Log
> A successful final project is built slowly over many weeks and not thrown together at the last minute. To incentivize good project pacing and to let your project mentor stay informed about the status of your work, each week you should add an entry to your devlog.md file in the development directory.

> Each entry should describe:

> - What goals you had set for the week and whether they were accomplished or not
> - What problems you encountered (if any) that prevented you from meeting your goals
> - What you plan to accomplish or attempt next week

> The development log will be graded for completion, detail, and honesty – not progress. It is much better to truthfully evaluate the work you completed in a week than lie to make the project sound further along than it really is. It is totally acceptable to have an entry that says you tried nothing and accomplished nothing. However if every week starts to say that, both yourself and your project mentor will be able to identify the issue before it becomes impossible to fix.

## Week 5 (26 Jul - 1 Aug)
> Goals accomplished:
> - list out candidate ideas to work on
> - single one out and develop it into a workable project
> - complete proposal.md

> Problems encountered:
> - most ideas I came up with were either too boring or did not utilise OOP

> Future goals:
> - begin creating Player and Customer constructors
> - begin creating Product constructor and list possible products

## Week 6 (2 Aug - 8 Aug)
> Goals accomplished:
> - Player()
>   - stock and balance system
>   - BUYing and SELLing methods
> - Customer()
>   - implemented random generation of items with random pricings to BUY and SELL
> - Product()
>   - name and price
>   - could parody IKEA furniture (SONGESAND, HEMNES, etc)

> Problems encountered:
> - it was difficult to find time during the week to work on the project, thanks to OBS and double LIT WA submission
> - I ended up only having one uninterrupted day to work on it

> Future goals:
> - implement score system
> - make Bus contructor
> - begin implementing actual gameplay

## Week 7 (9 Aug - 15 Aug)
> Goals accomplished:
> - created Bus() constructor
>   - keeps track of
>       - day, which will later affect the how the difficulty scales
>       - Customers in the store, also referred to as passengers
>   - method to calculate overall profits at the end of the day
>   - creates new passengers / Customers every new day
> - basic gameplay
>   - loop through 5 key interactions
>     1. View your info
>     2. View a Customer's shopping list
>     3. Buy a Product from a Customer
>     4. Sell a Product to a Customer
>     5. End the day
>   - input checking to ensure all user inputs are valid
> - Player() update
>   - added name, score and rating
>   - created get_info() method to print name, balance, rating, score and available stock
> - Customer() update
>   - created methods to print their wishlists
> - implemented os.system("CLS") at certain points to make the game more readable when played in Command Prompt

> Problems encountered:
> - I was too focused on actually coding instead of finishing this devlog.md update
> - initially learning how to implement user input validation needed some Googling to understand try: and except:

> Future goals:
> - increase code readability by separating it into separate files
> - implement win and lose conditions + daily rent / tax deduction
> - implement rating system that checks if each Customer as interacted with
> - balance values + create a formula to calculate score
> - find a way to print all passengers' wishlists at once in page format (?)

## Week 8 (16 Aug - 22 Aug)
> Goals accomplished:
> - separated code into 5 separate files
> - player.py
> - customer.py
> - product.py
> - bus.py
> - main.py

> Problems encountered:
> - since it was my first time using multiple files in one project, deciding what to separate into individual files and what to keep together took time
> - I was also unfamiliar with how to import functions from other files

> Future goals:
> - implement win and lose conditions + daily rent / tax deduction
> - implement rating system that checks if each Customer as interacted with
> - balance values + create a formula to calculate score
> - find a way to print all passengers' wishlists at once in page format (?)
> - create .txt files and file handling to store and read Customer and Product details

## Week 9 (23 Aug - 29 Aug)
> Goals accomplished:
> - implemented proper rating system
>   - checks if every customer was interacted with and increments / decrements Player's rating
> - implemented win / lose conditions
>   - bankruptcy: when Player's balance falls below 0
>   - negligence: when Player's rating falls below 0
>   - success: when Player's score exceeds a certain point, to be determined

> Problems encountered:
> - Nil

> Future goals:
> - balance values + create a formula to calculate score
> - find a way to print all passengers' wishlists at once in page format (?)
> - create .txt files and file handling to store and read Customer and Product details

## Week 10 (30 Aug - 5 Sep)
> Goals accomplished:
> - added a method to print all passengers' wishlists at once in one page

> Problems encountered:
> - Nil

> Future goals:
> - balance values + create a formula to calculate score
> - create .txt files and file handling to store and read Customer and Product details

## Sep Holiday (5 Sep - 10 Sep) **Submission date is 10 Sep**
