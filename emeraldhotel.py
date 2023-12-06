# Name: Daniel Aguilar
# Prog Purpose: This program will create a web page sales report for Emerald Beach Hotel & Resort.
#   The output is sent to an .html file
# SR-SINGLE ROOM: $195 per night
# DR-DOUBLE ROOM: $250 per night
# SU-SUITE: $350 per night

import datetime

############## Lists of Data #################


##############  define global variables ############
# define tax rate and prices


# define global variables
num_nights = 0
single_cost = 0
double_cost = 0
suite_cost = 0

subtotal = 0
sales_tax = 0
occupancy_tax = 0
total = 0
grand_total = 0

guest = []

############## TUPLES of constants ############
#          s-tax  occ-tax 
# indexes    0      1      
TAX_RATE = (.065, .1125)

#            sr   dr    su
# indexes    0    1     2   
ROOM_RATE = (195, 250, 350)

# create file variables
infile = 'emerald.csv' 
outfile = 'hotelsalesrep.html'

##############  define program functions ################
def main():
    read_in_data_file()

def read_in_data_file():   
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    for i in guest_in:
        guest.append(i.split(","))
    
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-cinema.png); color: #f8dd61;">\n')
    
def get_user_data():
    global num_tickets,num_popcorn, num_drinks
    num_tickets = int(input('Number of movie tickets: '))
    num_popcorn = int(input('Number of buckets of popcorn: '))
    num_drinks =  int(input('Number of drinks: '))    

def perform_calculations():
    global cost_tickets, cost_popcorn, cost_drinks, subtotal, sales_tax, total
    cost_tickets = num_tickets * PR_TICKET
    cost_popcorn= num_popcorn * PR_POPCORN
    cost_drinks = num_drinks * PR_DRINK

    subtotal = cost_tickets + cost_popcorn + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>CINEMA HOUSE MOVIES</h2></td></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('*** Your neighborhood movie house ***\n')
    
    f.write(tr + 'Tickets' + endtd + str(num_tickets) + endtd + format(cost_tickets,currency) + endtr)
    f.write(tr + 'Popcorn' + endtd + str(num_popcorn) + endtd + format(cost_popcorn,currency) + endtr)
    f.write(tr + 'Drinks ' + endtd + str(num_drinks) + endtd +  format(cost_drinks,currency)  + endtr)

    f.write(tr + 'Subtotal' +  endtd + sp + endtd + format(subtotal,currency)  + endtr)     
    f.write(tr + 'Sales Tax' + endtd + sp + endtd + format(sales_tax,currency) + endtr)
    f.write(tr + 'TOTAL' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write('<tr><td colspan= "3">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')


##########  call on main program to execute ############
main()              


