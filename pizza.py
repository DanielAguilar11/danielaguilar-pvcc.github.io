# Name: Daniel Aguilar and Felix Barrientos
# Prog Purpose: This program display a receipt for Palermo Pizza.
#   Price for S Pizza: $ 9.99
#   Price for M Pizza: $ 12.99 
#   Price for L Pizza: $ 17.99 
#   Price for XL Pizza: $21.95
#   Drink: $ 3.99
#   Order of breadsticks: $6.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables  ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_S_PIZZA = 9.99
PR_M_PIZZA = 12.99
PR_L_PIZZA = 17.99
PR_XL_PIZZA = 21.99
Drink = 3.99
Order_beadsticks = 6.99

# define global variables
num_pizzas = 0
pizza_size = 0
small_pizza = 0
medium_pizza = 0
large_pizza = 0
xlarge_pizza = 0
num_drinks = 0
num_breadsticks = 0
sales_tax = 0
subtotal = 0
total = 0

############## define program functions ################
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()
        

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper()== "N" or askAgain.upper()== "NO":
            more = False
            print("Thank you for order. Enjoy your meal!")   

def get_user_data():
    global num_pizzas, num_
    num_pizzas = int(input("Number of Pizzas: "))
    pizza_size = int(input("What sizes of pizza would you like(S, M, L, XL): "))
    askAgain = input("\nWould you like to order again (Y or N)?: ")
    
        if askAgain.upper()== "N" or askAgain.upper()== "NO":
            more = False
            print("Thank you for order. Enjoy your meal!") 
    askAgain = input("What sizes would you like for your pizzas (S, M, L, XL): ")
    
    if askAgain.upper() == "S" or askAgain.upper()== "M" or askAgain.upper()== "L" or askAgain.upper()== "XL"
    more = print(
                    
    drinks = int(input("Number of Drinks: " ))
    num_breadsticks = int(input("Number of Breadsticks: "))



def perform_calculations():
    global subtotal, sales_tax, total, num_pizzas, num_drinks, num_breadsticks, pizza_size, small_pizza, medium_pizza, large_pizza, xlarge_pizza
    adults_cost = num_adults * PR_ADULTS
    children_cost = num_children * PR_CHILDREN
    subtotal = adults_cost + children_cost
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax + service_fee
    
def display_results():
    
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** BRANCH BARBECUE BUFFET ****')
    print('--- Your neighborhood branch ---')
    print(line)
    print('Adults       $ ' + format(adults_cost, moneyformat))
    print('Children     $ ' + format(children_cost, moneyformat))
    print(line)
    print('Subtotal     $ ' + format(subtotal, moneyformat))
    print('Service Fee  $ ' + format(service_fee, moneyformat))
    print('Sales Tax    $ ' + format(sales_tax, moneyformat))
    print('Total        $ ' + format(total, moneyformat))
    print()
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
    

