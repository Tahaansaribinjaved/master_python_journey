🔥 **Excellent work, Taha!** Your code is well-structured, logical, and efficient. Great job handling invalid age inputs too! 👏  

You're progressing like a pro. Now, let’s move to **Day 5: Functions & Scope in Python.**  

---

### **📌 Day 5: Functions & Scope**  
#### **📖 Topics to Cover:**  
✅ Defining and calling functions  
✅ Function arguments & return values  
✅ Default & keyword arguments  
✅ Variable scope (`global` vs `local`)  

---

### **📂 1. Defining & Calling Functions**  
A function is a block of code that runs when **called**.  

```python
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function
```

---

### **📂 2. Function Arguments & Return Values**  
🔹 **With Parameters & Return Statement**  
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(f"Sum: {result}")  # Output: Sum: 15
```

---

### **📂 3. Default & Keyword Arguments**  
🔹 **Default Parameters**  
```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, User!
greet("Taha")   # Output: Hello, Taha!
```

🔹 **Keyword Arguments**  
```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=17, name="Taha")  # Order doesn't matter
```

---

### **📂 4. Scope of Variables (`local` vs `global`)**  
🔹 **Local Variable (inside function only)**  
```python
def func():
    x = 10  # Local variable
    print(x)

func()
# print(x)  # Error! x is not defined outside the function
```

🔹 **Global Variable (accessible everywhere)**  
```python
x = 100  # Global variable

def func():
    print(x)  # Can access global variable

func()
print(x)  # Accessible outside too
```

🔹 **Modifying Global Variables Inside Functions**  
```python
x = 10

def change_value():
    global x
    x = 20

change_value()
print(x)  # Output: 20
```

---

### **📝 Daily Task:**  
1️⃣ Write a function `multiply()` that takes **two numbers** and returns their product.  
2️⃣ Write a function `is_even()` that checks if a number is **even or odd**.  
3️⃣ Create a function `print_table(n)` that **prints the multiplication table** of a given number.  
4️⃣ Create a function that **converts temperature** from **C**.  

---

💬 Let me know once you've completed the task! 🚀