######################
# Name: Darren Bowers
# Coding 03
# Purpose: In this assignment we ask the user for multiple inputs, and make a decision and calculations based on that input.
######################


user_choice = input("Enter \n 1) Convert Fahrenheit to Celsius \n 2) Convert Celsius to Fahrenheit \n")
if user_choice == "1":
    user_fah_temp = (input("Enter a Fahrenheit tempature: "))
    try:
        user_fah_temp = float(user_fah_temp)
        celsius = (5.0/9.0)*((user_fah_temp)-32.0)
        print("{:.1f}" .format(user_fah_temp), 'F = ', "{:.1f}" .format(celsius), 'C', sep="")
    except:
        print("That is an invalid tempature.")
elif user_choice == "2":
    user_cel_temp = input("Enter a Celsius tempature: ")
    try:
        user_cel_temp = float(user_cel_temp)
        fahrenheit = ((9.0/5.0)*(user_cel_temp)+32.0)
        print("{:.1f}" .format(user_cel_temp), 'C = ', "{:.1f}" .format(fahrenheit), 'F', sep="")
    except:
        print("That is an invalid tempature.")
else:
    print("That is an invalid choice.")
