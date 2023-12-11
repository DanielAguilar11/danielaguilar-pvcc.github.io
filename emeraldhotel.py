# Name: Daniel Aguilar
# Prog Purpose: This program will create a web page sales report for Emerald Beach Hotel & Resort.
#   The output is sent to an .html file
# SR-SINGLE ROOM: $195 per night
# DR-DOUBLE ROOM: $250 per night
# SU-SUITE: $350 per night

import datetime

########## Variables ######
num_nights = 0

############## TUPLES of constants ############
#          s-tax  occ-tax 
# indexes    0      1      
TAX_RATES = (.065, .1125)

#            sr   dr    su
# indexes    0    1     2   
ROOM_RATES = (195, 250, 350)

# create file variables
infile = 'emerald.csv' 
outfile = 'emerald-web-page.html'

guest = []

##############  define program functions ################
def main():
    read_in_data_file()
    perform_calculations()
    open_out_file()
    create_output_html()

def read_in_data_file():   
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    for i in guest_in:
        guest.append(i.split(","))
    
def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)           
            
def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wb-emerald.png); color: #f8dd61;">\n')

def create_output_html():
    global f
    
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    td = "\t"

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    
    f.write('\n<table border="3"   style ="background-color: #006600;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 7>\n')
    f.write('<h2>Emerald Beach Hotel & Resort</h2></td></tr>')
    titles1 = tr + "\nLast Name" + td + "First Name" + td + "Room Type" + td + "# Nights" + td + "Subtotal" + td + "Sales Tax" + td + "Occ. Tax" + td + "Total" + endtr 
    f.write(titles1)
    for i in range(len(guest)):
        f.write(tr + format(guest[i][0])+ td)
        f.write(format(guest[i][1])+ td)        
        f.write(format(guest[i][2])+ td)
        f.write(format(guest[i][3])+ td)
        f.write(format(guest[i][4], currency)+ td)
        f.write(format(guest[i][5], currency)+ td)
        f.write(format(guest[i][6], currency)+ td)
        f.write(format(guest[i][7], currency)+ '</td></tr>')
                        
 
    titles2 = '<tr><td colspan = 7>' + "\nGrand Total " + td
    f.write(titles2)
    f.write( format(grandtotal, currency))
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')
    

##########  call on main program to execute ############
main()              


