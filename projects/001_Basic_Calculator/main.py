
# def calculation():
while True:
        
    # 📌 Steps to Build a Basic Calculator

    # * 1️⃣ Ask the user for two numbers

    #^ Take input from the user (remember to convert it to a number).

    def get_number(prompt):
        while True:
            user_input = input(prompt)
            if(user_input.strip()==""):
                print("Input cannot be empty. Please enter a valid number.")
                continue
            try :
                return float(user_input)
            except ValueError:  
                print(f"{user_input} is not a valid number. Please enter a valid number.")  
            
        

    num1 = get_number("Please Enter first number ")
    num2 = get_number("Please Enter second number")

    # * 2️⃣ Ask the user for an operation

    #^ Let the user choose from:
    #^ ➕ Addition
    #^ ➖ Subtraction
    #^ ✖️ Multiplication
    #^ ➗ Division

    def get_operator():
        valid_operators = ['+','-','/','*','**','%','//']
        while True:        
            operator = input("Enter an operator in [+,-,*,/,**,%,//]: ")  
            if operator.strip() in valid_operators:  
                return operator  
            else:  
                print("Invalid operator. Please enter one of the following: +, -, *, /,**,%,//.")  


    operator = get_operator()





        # *3️⃣ Perform the calculation
        #^ Use conditions (if-else) to check the chosen operation and apply the correct formula.

    result = None
    if(operator== '+'):
        result = num1 + num2     
    elif(operator == '-'):
        result = num1 - num2     
    elif(operator == '*'):
        result = num1 * num2   
    elif(operator == '**'):
        result = num1 ** num2   
    elif(operator == '%'):
        result = num1 % num2   
    elif(operator == '//'):
        result = num1 // num2   
    elif(operator == '/'):
        if(num2 == 0 ):
            print(f"you cannot divide {num1} by {num2}")
            result = ""
        else:
            result = num1 / num2     

    # *4️⃣ Display the result
    # ^ Print the final answer nicely.
    if result is not None:
        print(f"{num1} {operator} {num2} = {result:.2f}")
        response =  input("Do you want to perform another calculation? (yes/no)")
        if response.strip().lower() == 'yes'or response.strip().lower() =='y':
            # calculation()
            continue
        else :
            print(" okay bye bye ")
            break


    # *5️⃣ Handle errors

    # ^ What if the user enters invalid input?
    # ^ What if they try to divide by zero?
    # ^ Add checks to handle these situations.
# calculation()