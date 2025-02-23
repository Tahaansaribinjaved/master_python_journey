# 📌 Steps to Build a Basic Calculator  

# * 1️⃣ Ask the user for two numbers  
def get_number(prompt):  
    while True:  
        user_input = input(prompt)  
        if user_input.strip() == "":  
            print("Input cannot be empty. Please enter a number.")  
            continue  
        try:  
            return float(user_input)  # Using float to allow decimal numbers  
        except ValueError:  
            print(f"{user_input} is not a valid number. Please enter a valid number.")  

num1 = get_number("Please enter the first number: ")  
num2 = get_number("Please enter the second number: ")  

# * 2️⃣ Ask the user for an operation  
def get_operator():  
    valid_operators = ['+', '-', '*', '/']  
    while True:  
        operator = input("Enter an operator in [+,-,*,/]: ")  
        if operator.strip() in valid_operators:  
            return operator  
        else:  
            print("Invalid operator. Please enter one of the following: +, -, *, /.")  

operator = get_operator()  

# *3️⃣ Perform the calculation  
result = None  

if operator == '+':  
    result = num1 + num2  
elif operator == '-':  
    result = num1 - num2  
elif operator == '*':  
    result = num1 * num2  
elif operator == '/':  
    if num2 == 0:  
        print(f"You cannot divide {num1} by {num2}.")  
    else:  
        result = num1 / num2  

# *4️⃣ Display the result  
if result is not None:  
    print(f"{num1} {operator} {num2} = {result}")  

# *5️⃣ Handle errors  
# ^ The error handling for invalid inputs is integrated into the get_number and get_operator functions.
