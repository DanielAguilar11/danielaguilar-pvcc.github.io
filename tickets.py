# Name: Daniel Aguilar 
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Price of popcorn: $8.99
#   Price of a drink: $4.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables  ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 8.99
PR_DRINK = 4.99

# define global variables
num_tickets = 0
ticket_cost = 0
num_popcorn = 0
popcorn_cost = 0
num_drinks = 0
drink_cost = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ################
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nwould you like to order again (Y or N)?: ")
        if askAgain.upper()== "N" or askAgain == "n":
            more_tickets = False
            print("Thank you for order. Enjoy your movie!")   

def get_user_data():
    global num_tickets, num_popcorn, num_drinks
    num_tickets = int(input("Number of movies tickets: "))
    num_popcorn = int(input("Number of buckets of popcorn: "))
    num_drinks = int(input("Number of drinks: "))

def perform_calculations():
    global subtotal, sales_tax, total, ticket_cost, popcorn_cost, drink_cost
    ticket_cost = num_tickets * PR_TICKET
    popcorn_cost = num_popcorn * PR_POPCORN
    drink_cost = num_drinks * PR_DRINK
    subtotal = ticket_cost + popcorn_cost + drink_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    greetings = "Hello There!"
    print(greetings)
    
def display_results():
    
    moneyformat = '8,.2f'
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('------------------------------')
    print('Tickets      $ ' + format(ticket_cost, moneyformat))
    print('Popcorn      $ ' + format(popcorn_cost, moneyformat))
    print('Drinks       $ ' + format(drink_cost, moneyformat))
    print('------------------------------')
    print('Subtotal     $ ' + format(subtotal, moneyformat))
    print('Sales Tax    $ ' + format(sales_tax, moneyformat))
    print('Total        $ ' + format(total, moneyformat))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
    
