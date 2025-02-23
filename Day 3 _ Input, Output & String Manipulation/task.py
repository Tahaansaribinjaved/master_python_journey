# 📝 Daily Task:
# 1️⃣ Take user input for name, age, and favorite programming language.
# 2️⃣ Print a sentence using an f-string.
# 3️⃣ Convert the input name to uppercase.
# 4️⃣ Slice the first 3 letters of the programming language and print them.

# 📌 Example Output:

# Enter your name: Taha
# Enter your age: 17
# Enter your favorite programming language: Python
# Hello, Taha! You are 17 years old and love Python.
# Your name in uppercase: TAHA
# First 3 letters of your favorite language: Pyt

name = input("Enter your name :")
age = int(input("Enter your age :"))
favorite_programming_language = input("Enter your favorite programming language :")

print(f"Hello, {name}! You are {age} years old and love {favorite_programming_language}.")
name = name.upper()
print(f" Your name in uppercase: {name}")
print(f" First 3 letters of your favorite language: {favorite_programming_language[0:3]}")
