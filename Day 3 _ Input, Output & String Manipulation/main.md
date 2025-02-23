🔥 Fantastic job, Taha! You're moving fast. Now, let's step into **Day 3: Input, Output & String Manipulation**.  

---

### **📌 Day 3: Input, Output & String Manipulation**  
#### **📖 Topics to Cover:**  
✅ Taking user input  
✅ Output formatting (f-strings, `.format()`, `% formatting`)  
✅ String operations & methods  
✅ String slicing  

---

### **📂 1. Taking User Input**  
Python allows users to enter data using `input()`.  
```python
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")
```
🔹 **Note:** `input()` always returns a **string** by default. Convert it if needed.  
```python
age = int(input("Enter your age: "))  # Convert input to integer
print("In 5 years, you will be", age + 5)
```

---

### **📂 2. Output Formatting**  
#### **✅ f-strings (Recommended)**
```python
name = "Taha"
age = 17
print(f"My name is {name} and I am {age} years old.")
```
#### **✅ `.format()` Method**
```python
print("My name is {} and I am {} years old.".format(name, age))
```
#### **✅ `% formatting` (Old Method)**
```python
print("My name is %s and I am %d years old." % (name, age))
```

---

### **📂 3. String Operations**  
You can perform operations on strings:  

```python
text = "Python is amazing"
print(text.upper())   # PYTHON IS AMAZING
print(text.lower())   # python is amazing
print(text.title())   # Python Is Amazing
print(text.replace("Python", "Cybersecurity"))  # Cybersecurity is amazing
```

🔹 **Checking for a word in a string**  
```python
print("Python" in text)  # True
```

---

### **📂 4. String Slicing**  
Extracting parts of a string:  
```python
text = "Cybersecurity"
print(text[0:5])   # Cyber
print(text[:5])    # Cyber
print(text[5:])    # security
print(text[-3:])   # ity (last 3 letters)
```

---

### **📝 Daily Task:**  
1️⃣ Take user input for **name, age, and favorite programming language**.  
2️⃣ Print a sentence using an **f-string**.  
3️⃣ Convert the input name to **uppercase**.  
4️⃣ Slice the **first 3 letters** of the programming language and print them.  

**📌 Example Output:**  
```
Enter your name: Taha
Enter your age: 17
Enter your favorite programming language: Python
Hello, Taha! You are 17 years old and love Python.
Your name in uppercase: TAHA
First 3 letters of your favorite language: Pyt
```

---

💬 Let me know once you've completed the task! 🚀