🔥 Perfect, Taha! You're coding like a pro already. Your code is clean and correctly formatted. Keep up this momentum! 🚀  

Now, let’s move on to **Day 4: Control Flow (if-else & Loops)**.  

---

### **📌 Day 4: Control Flow (if-else & Loops)**  
#### **📖 Topics to Cover:**  
✅ `if-else` conditions  
✅ Logical and comparison operators  
✅ `for` and `while` loops  
✅ Loop control (`break`, `continue`, `pass`)  

---

### **📂 1. `if-else` Statements**  
Used for decision-making in Python.  

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

🔹 **Multiple Conditions (`elif`)**
```python
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")
```

---

### **📂 2. Loops in Python**
Loops allow us to execute a block of code multiple times.

#### **✅ `for` Loop** (Iterates over a sequence)  
```python
for i in range(1, 6):  
    print(f"Count: {i}")  
```
🔹 Output:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

#### **✅ `while` Loop** (Repeats while condition is `True`)  
```python
x = 1
while x <= 5:
    print(f"Number: {x}")
    x += 1  # Increase x to avoid infinite loop
```

---

### **📂 3. Loop Control (`break`, `continue`, `pass`)**
🔹 **`break`** → Stops the loop  
```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)  # Stops at 4
```

🔹 **`continue`** → Skips current iteration  
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Skips 3
```

🔹 **`pass`** → Placeholder (does nothing)  
```python
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
```

---

### **📝 Daily Task:**  
1️⃣ Take user input for **age** and print whether they are an **adult or minor**.  
2️⃣ Write a program that prints **numbers from 1 to 10**, skipping number `5`.  
3️⃣ Write a program to **print even numbers** from `1 to 20` using a loop.  
4️⃣ Print `"Python is fun!"` **5 times** using a loop.  

---

💬 Let me know once you've completed the task! 🚀