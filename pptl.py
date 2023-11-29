# Name: Daniel Aguilar
# Program Purpose: This program uses lists to find the personal property tax  for vehicles in Charlottesville
#   and produces a report which displays all data and the total tax value
#
# Personal property tax in Charlottesville:
#   TAX_RATE: $4.20 per $100 of vehicle value (4.20% per year) 
#   --- Paid every 6 months
# Personal Property Tax Relief (PPTR):
#   --- Eligibility: Owned or leased vehicles which are predominately used for non-bussiness purposes & have passenger license plates
#   PP_TAX_RELIEF: 33%

import datetime

##############  define global variables  ############
# define tax rate 
PPT_RATE = 0.042
RELIEF_RATE = 0.33

############## create list data ################
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus ",]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y", ]

owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jeniffer  ", 


############# define program functions #############

def main():
        perform_calculations()
        display_results()

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
