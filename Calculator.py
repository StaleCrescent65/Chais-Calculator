# Chai's calculator - Version 1.0.1

import os
import time

# Calculator

def calc(clear):  # Main input to select the operator you want to use to calculate numbers. 
    opchoose = input(''' 
    Chai's Calculator! - Yes, this is created by Chai himself.

    /---------------------"
    |_____________________|
    |  _________________  |     Choose an operator to begin!
    | | Chai           06 |      
    | |_________________| |     
    |  ___ ___ ___   ___  |     1, +
    | | 7 | 8 | 9 | | + | |     2, -
    | |___|___|___| |___| |     3, *
    | | 4 | 5 | 6 | | - | |     4, /
    | |___|___|___| |___| |     5, %
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    
    
    pointing here! >>>>>>>>> yes. Type it HERE!: ''')

    def option1():  # This function calculates using +
        if opchoose == "1": 
            os.system("cls")
            print("")
            print("  Operator Selected, +")
            print("")
            firnum = int(input("  Enter the first number: "))
            second = int(input("  Enter the second number: "))
            print("")
            print(" Calculating...")
            time.sleep(1)
            print("")
            print("  Your sum is:", firnum + second)
            time.sleep(4)
            os.system("cls")
            print("")
            return calc(os.system("cls"))
        else:
            print("Sorry, numbers only.")


    def option2():  # This function calculates using the - operator
        if opchoose == "2":
            os.system("cls")
            print("")
            print("  Operator Selected, -")
            print("")
            firnum = input("  Enter the first number: ")
            firnum = int(firnum)
            second = input("  Enter the second number: ")
            second = int(second)
            print("")
            print(" Calculating...")
            time.sleep(1)
            print("")
            print("  Your sum is:", firnum - second)
            time.sleep(4)
            os.system("cls")
            print("")
            return calc(os.system("cls"))
        else:
            print("Sorry, numbers only.")

    def option3():  # This function calculates using the x operator (Multiplication)
        if opchoose == "3":
            os.system("cls")
            print("")
            print("  Operator Selected, *")
            print("")
            firnum = input("  Enter the first number: ")
            firnum = int(firnum)
            second = input("  Enter the second number: ")
            second = int(second)
            print("")
            print(" Calculating...")
            time.sleep(1)
            print("")
            print("  Your sum is:", firnum * second)
            time.sleep(4)
            os.system("cls")
            print("")
            return calc(os.system("cls"))
        else:
            print("Sorry, numbers only.")

    def option4():  # This function calculates using the / operator (Division)
        if opchoose == "4":
            os.system("cls")
            print("")
            print("  Operator Selected, / Division")
            print("")
            firnum = input("  Enter the first number: ")
            firnum = int(firnum)
            second = input("  Enter the second number: ")
            second = int(second)
            print("")
            print(" Calculating...")
            time.sleep(1)
            print("")
            print("  Your sum is:", firnum / second)
            time.sleep(4)
            os.system("cls")
            print("")
            return calc(os.system("cls"))
        else:
            print("Sorry, numbers only.")

    def option5():  # This function calculates using the % operator (Modulus)
        if opchoose == "5":
            os.system("cls")
            print("")
            print("  Operator Selected, %")
            print("")
            firnum = input("  Enter the first number: ")
            firnum = int(firnum)
            second = input("  Enter the second number: ")
            second = int(second)
            print("")
            print(" Calculating...")
            time.sleep(1)
            print("")
            print("  Your sum is:", firnum % second)
            time.sleep(4)
            os.system("cls")
            print("")
            return calc(os.system("cls"))
        else:
            print("Sorry, numbers only.")




    if opchoose == "1":
        return option1()

    if opchoose == "2":
        return option2()

    if opchoose == "3":
        return option3()

    if opchoose == "4":
        return option4()

    if opchoose == "5":
        return option5()


calc(os.system("cls"))
