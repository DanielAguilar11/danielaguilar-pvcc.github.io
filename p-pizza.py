# Name: Felix Barrientos
# Program Purpose: This program allows (nonexistent) customers to order from, the nonexistent, Palermo's Pizza
# Palermo's Pizza
import datetime
now = datetime.datetime.now
# GLOBAL VARIABLES #
S_pizza = 9.99
M_pizza = 12.99
L_pizza = 17.99
X_pizza = 21.99
Drink = 3.99
Breadsticks = 6.99

#sales 5.5% (number*.945)

def main():
    more = True
    while more:
        get_user_data()

        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to process another order? (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for choosing Palermos Pizza, have a nice day!.')

def get_user_data():
    global pizza_num, breadsticks_num, drinks_num, pizza_size, pizza_yn, breadsticks_yn, drinks_yn
    
    pizza_yn = input("Would you like to add Pizza to your order? (Y/N): ")
    if pizza_yn.upper() == "Y" :
            pizza_data()
    breadsticks_yn = input("Would you like to add any breadsticks to your order? (Y/N): ")
    if breadsticks_yn.upper() == "Y" :
        breadsticks_data()
    else:
        breadsticks_num = 0
    drinks_yn = input("Would you to add any drinks to your order? (Y/N): ")
    if drinks_yn.upper() == "Y" : 
            drinks_data()

def pizza_data():
    global pizza_size, pizza_num
    pizzasizes = "\n** Pizza sizes: \n\tSmall: 9.99 \n\tMedium: 12.99 \n\tLarge: 17.99 \n\tXLarge: 21.99"
    pizza_size = input(pizzasizes + "\n**Enter the name of the size you would like to order?: ")
    pizza_num = int(input("How many of this size pizza would you like to order?: "))

def breadsticks_data():
    global breadsticks_num
    breadsticks_num = int(input("How many orders of breadsticks would you like to add? "))

def drinks_data():
    global drinks_num
    drinks_num = int(input("How many drinks would you like to add? "))

def perform_calculations():
    global pizza_total, breadsticks_total, drinks_total, total, subtotal
    if pizza_size.upper() == "SMALL":
        pizza_cost = S_pizza
    elif pizza_size.upper() == "MEDIUM":
        pizza_cost = M_pizza
    elif pizza_size.upper() == "LARGE":
        pizza_cost = L_pizza
    elif pizza_size.upper() == "XLARGE":
        pizza_cost = X_pizza
    
    pizza_total = pizza_cost * pizza_num
    breadsticks_total = breadsticks_num * Breadsticks
    drinks_total = drinks_num * Drink

    subtotal = pizza_total + breadsticks_total + drinks_total
    total = subtotal + (subtotal * .055)

def display_results():
    print("")
    print("Palermo's Pizza")
    print(f"Current Time: {current_time}")
    print("")
    print(str(pizza_num) + "x Pizza(s) Cost: $" + str(pizza_total))
    print(str(breadsticks_num) + "x Breadsticks Order Cost: $" + str(breadsticks_total))
    print(str(drinks_num) + "x Drink(s) Cost: $" + str(drinks_total))
    print("")
    print("Subtotal: $" + str(subtotal))
    print("Total: $" + str(total))


main()