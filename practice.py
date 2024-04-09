# from art import logo

# from replit import clear

import math

# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

def sqrt(n1,_):
    return math.sqrt(n1)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "sqrt": sqrt
}

# Recursion: Creating a function which calls itself and has no inputs or outputs. Calling a function inside a function
def calculator():
    # print(logo)
    
    num1 = float(input("What's the first number?: "))
    print("")
    for operator in operations:
        print(operator)
        
    should_continue = True
    
    while should_continue:
        select_operator = input("\nPick an operator: ")
        if select_operator != "sqrt":
            num2 = float(input("What's the next number?: "))
        else:
            num2 = None
        
        calculation_function = operations[select_operator]
    
        #Here the code will be: (When selected multiply first and then add operator)
        #answer = multiply(multiply(num1, num2), num3)
        # answer = calculation_function(calculation_function(num1, num2), num3)
        #answer = 2 * 3 * 3 = 18
        #To fix this bug we need to change the code on line 42 to:
        answer = calculation_function(num1, num2)
        if select_operator == "sqrt":
            print(f"The square root of {num1} is {answer}")
        else:
            print(f"{num1} {select_operator} {num2} = {answer}")
        continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    
        if continue_cal == "y":
            num1 = answer
        elif continue_cal == "n":
            should_continue = False
            # clear()
            calculator()
    
calculator()







   