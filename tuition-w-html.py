# Name:  Daniel Aguilar
# Prog Purpose: This program computes PVCC college tuition & fees based ond number of credits
# PVCC fee rates are from: https://www.pvcc.edu/tuition-and-fees
# Rates are: per credit

import datetime

############ define global variables ###########
# define tuition and fee rates
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

# create output file
outfile = 'tuition-webpage.html'

########### define program functions ###########
def main():
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to calculate tuition and fees for another student (Y/N) :")
        if yesno == "n" or yesno == "N" :
            another_student = False
            print('\n** Open this file in the browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close
            
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC College Tuitions </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #ffffff; background-image: url(wp-tuition.png); color: #8d8d8d;">\n')
    
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
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</tr><tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #ffffff;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 2>\n')
    f.write('<h2>PVCC COLLEGE TUITIONS</h2></td></tr>')
    f.write('<tr><td colspan = 2>\n')
    f.write('*** Piedmont Virginia Community College ***\n')

    f.write(tr + 'Tuition Fee' + endtd + str(numcredits) + endtd + format(tuition_amt,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + str(scholarshipamt) + endtd + format(cap_fee_amt,currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + sp + endtd +  format(inst_fee_amt,currency)  + endtr)
    f.write(tr + 'Activity Fee' + endtd + sp + endtd +  format(inst_fee_amt,currency)  + endtr)
    f.write(tr + 'Total' + endtd + sp + endtd + format(total_amt,currency) + endtr)
    f.write(tr + 'Balance' + endtd + sp + endtd + format(balance_amt,currency) + endtr)
    
    f.write('<tr><td colspan= "2">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')

########## call on main program to execute ########
main()
    
        
