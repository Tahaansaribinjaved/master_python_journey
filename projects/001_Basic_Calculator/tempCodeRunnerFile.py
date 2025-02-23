while True:
    def get_number(prompt):
        while True:
            user_input = input(prompt)
            if user_input.strip() == "":
                print("Input cannot be empty. Please enter a valid number.")
                continue
            try:
                return float(user_input)
            except ValueError:
                print(f"{user_input} is not a valid number. Please enter a valid number.")

    num1 = get_number("Please Enter first number: ")
    num2 = get_number("Please Enter second number: ")

    def get_operator():
        valid_operators = ['+', '-', '*', '/', '**', '%', '//']
        while True:
            operator = input("Enter an operator in [+,-,*,/,**,%,//]: ")
            if operator.strip() in valid_operators:
                return operator
            else:
                print("Invalid operator. Please enter one of the following: +, -, *, /, **, %, //.")

    operator = get_operator()

    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    elif operator == '//':
        if num2 == 0:
            print("Error: Integer division by zero is not allowed.")
        else:
            result = num1 // num2
    elif operator == '%':
        if num2 == 0:
            print("Error: Modulo by zero is not allowed.")
        else:
            result = num1 % num2

    if result is not None:
        print(f"{num1} {operator} {num2} = {result:.2f}")

    response = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Okay, bye-bye!")
        break
