
#* 📝 Daily Task:
#* 1️⃣ Create a function subtract(a, b) that returns a - b.
#* 2️⃣ Write a function greet_user(name, age) that prints "Hello, {name}! You are {age} years old."
#* 3️⃣ Write a function that accepts multiple numbers and returns their product.
#* 4️⃣ Use **kwargs to create a function that accepts a person's details (name, age, city) and prints them.


#* 1️⃣ Create a function subtract(a, b) that returns a - b.
def subtract(a, b):
    return a-b
print(subtract(3,2))

#* 2️⃣ Write a function greet_user(name, age) that prints "Hello, {name}! You are {age} years old."
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet_user("Taha",17)

#* 3️⃣ Write a function that accepts multiple numbers and returns their product.
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product
print(multiply(2, 3, 4))  # Output: 24


#* 4️⃣ Use **kwargs to create a function that accepts a person's details (name, age, city) and prints them.
def display_info(**kwargs):  # Accepts key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Taha", age=17, city="Karachi")

