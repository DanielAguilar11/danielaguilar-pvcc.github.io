# Name:  Daniel Aguilar and Abigail Bang
# Prog Purpose: This program computes PVCC college tuition & fees based ond number of credits
# PVCC fee rates are from: https://www.pvcc.edu/tuition-and-fees
# Rates are: per credit

import datetime
# dafine tuition and fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT =  336.21 
RATE_CAPITAL_FEE = 23.50 
RATE_INSTITUTION_FEE = 1.75 
RATE_ACTIVITY_FEE = 2.90 

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

tuition_amt = 0
cap_fee_amt = 0
inst_fee_amt = 0
act_fee_amt = 0
total_amt = 0
balance_amt = 0 

########### define program functions #######
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to calculate tuition and fees for another student (Y/N) :")
        if yesno == "n" or yesno == "N" :
            another_student = False

def get_user_data():
    global inout,numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for : "))
    scholarshipamt = float(input("Scholarship amount recived : "))

def perform_calculations():
    global total, balance, in_state, out_state, tuition_amt, inst_fee_amt, cap_fee_amt, act_fee_amt, total_amt, balance_amt 
    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee_amt = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee_amt = numcredits * RATE_CAPITAL_FEE
    
    inst_fee_amt = numcredits * RATE_INSTITUTION_FEE
    act_fee_amt = numcredits * RATE_INSTITUTION_FEE
    total_amt =  tuition_amt + cap_fee_amt + inst_fee_amt + act_fee_amt
    balance_amt = total_amt - scholarshipamt
    
def display_results():
    
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** Piedmont Virginia Community College ****')
    print(line)
    print('Tuition Fee       $ ' + format(tuition_amt, moneyformat))
    print(line)
    print('Capital Fee       $ ' + format(cap_fee_amt, moneyformat))
    print('Institution Fee   $ ' + format(inst_fee_amt, moneyformat))
    print('Activity Fee      $ ' + format(act_fee_amt, moneyformat))
    print('Total             $ ' + format(total_amt, moneyformat))
    print('Balance           $ ' + format(balance_amt, moneyformat))
    print()
    print(str(datetime.datetime.now()))

########## call on main program to execute ########
main()
    
        
