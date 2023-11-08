# Name: Daniel Aguilar
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats.
# 
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia.
# 
# PET CARE MEDS Pricing
#------------------------------------
# Canine Vaccines:
#  1. Bordatella $30.00
#  2. DAPP $35.00
#  3. Influenza $48.00
#  4. Leptospirosis $21.00
#  5. Lyme Disease $41.00
#  6. Rabies $ 25.00
#  7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, Up to 25 lbs: $9.99
#   Medium-size dogs, 26 to 50 lbs: $11.99
#   Large dogs, 51 to 100 lbs: $13.99

import datetime

##############  define global variables  ############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEPT = 21
PR_LYME = 41
PR_RAB = 25
PR_ALL = 170
PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

# define global variables
pet_name = 0
pet_type = 0
pet_weight = 0

############## define program functions ################
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
            
        askAgain = input("\nWould you like to process another pet (Y/N)?:")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global num_adults, num_children
    num_adults = int(input("Number of adults: "))
    num_children = int(input("Number of children: "))
    pet_weight = int(input("Weight of your pet (in pounds): "))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total, adults_cost, children_cost
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
    

-