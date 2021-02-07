######################
# Name: Darren Bowers
# Coding 03
# Purpose: In this assignment we ask the user for multiple inputs, and make a decision and calculations based on that input.
######################


USER_CHOICE = input("Enter \n 1) Convert Fahrenheit to Celsius \n 2) Convert Celsius to Fahrenheit \n")
if USER_CHOICE == "1":
    USER_FAH_TEMP = (input("Enter a Fahrenheit tempature: "))
    try:
        USER_FAH_TEMP = float(USER_FAH_TEMP)
        CELSIUS = (5.0/9.0)*((USER_FAH_TEMP)-32.0)
        print("{:.1f}" .format(USER_FAH_TEMP), 'F =', CELSIUS, 'C',)
    except:
        print("That is an ivalid tempature.")
elif USER_CHOICE == "2":
    USER_CEL_TEMP = input("Enter a Celsius tempature: ")
    try:
        USER_CEL_TEMP = float(USER_CEL_TEMP)
        FAHRENHEIT = ((9.0/5.0)*float(USER_CEL_TEMP)+32.0)
        print("{:.1f}" .format(USER_CEL_TEMP), 'C =', FAHRENHEIT, 'F',)
    except:
        print("That is an ivalid tempature.")
else:
    print("That is an invalid choice.")
