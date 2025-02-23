
#! 📝 Daily Task:
#! 1️⃣ Write a function multiply() that takes two numbers and returns their product.
#! 2️⃣ Write a function is_even() that checks if a number is even or odd.
#! 3️⃣ Create a function print_table(n) that prints the multiplication table of a given number.
#! 4️⃣ Create a function that converts temperature from Celsius to Fahrenheit.

#! 1️⃣ Write a function multiply() that takes two numbers and returns their product.

def multiply(num1,num2):
    return num1*num2
product = multiply(2,3)
print(f"product of 2,3 is {product}")

#! 2️⃣ Write a function is_even() that checks if a number is even or odd.
def is_even(num):
    if(num==0):
        print("Number is Zero")
    elif(num%2==0):
        print("The given number {} is even".format(num))
    else:
        print("The given number {} is odd".format(num))
        
is_even(3)
#! 3️⃣ Create a function print_table(n) that prints the multiplication table of a given number.
def print_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
n = int(input("Enter a number :"))
print_table(n)

#! 4️⃣ Create a function that converts temperature from Celsius to Fahrenheit.
# °F = °C × (9/5) + 32.
def Celsius_to_Fahrenheit(C):
    F =( C * (9/5) )+ 32
    print(f"°{C} in Fahrenheit is °{F} ")
Celsius_to_Fahrenheit(0)