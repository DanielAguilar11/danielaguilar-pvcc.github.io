# Name: Daniel Aguilar
# Prog Purpose: This program display a tax bill for personal poroperty vehicles in Charlottesville.
#   TAX_RATE: $4.20 per $100 of vehicle value (4.20% per year) 
# Note: Paid every 6 months, so bill should be for 6 months, not for the entire year.   
#   PP_TAX_RELIEF: 33%

import datetime

##############  define global variables  ############
# define tax rate 
TAX_RATE = 0.042
TAX_RELIEF = 0.33

# define global variables
assessed_value = 0
pers_vehicle = 0
tax_rate = 0
tax_relief = 0
tax_due = 0
annual_tax = 0
full_tax = 0
total_tax = 0

############## define program functions ################
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()
            
        askAgain = input("\nWould you like to process another vehicle (Y or N): ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you, have a good day!')

def get_user_data():
    global pers_vehicle, assessed_value
    assessed_value = int(input("What is the assessed value of the vehicle: "))
    pers_vehicle = input("Is this a personal Vehicle (Y or N): ")

def perform_calculations():
    global assessed_value, pers_vehicle, tax_rate, tax_relief, tax_due, annual_tax, full_tax
    annual_tax = assessed_value * TAX_RATE
    full_tax = annual_tax / 2

    if pers_vehicle.upper() == "Y":
        tax_relief = full_tax * TAX_RELIEF
    else :  
        tax_relief = 0

    tax_due = full_tax - tax_relief
    total_tax = tax_due

def display_results():
    
    moneyformat = '11,.2f'
    line = '------------------------------'
    print(line)
    print('**** City of Charlottesville ****')
    print('--- Personal Property Tax ---')
    print(line)
    print('Assessed Value   $ ' + format(assessed_value, moneyformat))
    print('Full Tax Amount  $ ' + format(full_tax, moneyformat))
    print('Relief           $ ' + format(tax_relief, moneyformat))
    print('Tax Due by Dec 5 $ ' + format(tax_due, moneyformat))
    print()
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
