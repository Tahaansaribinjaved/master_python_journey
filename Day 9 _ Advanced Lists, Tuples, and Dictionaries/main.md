### **📅 Day 9 - Advanced Lists, Tuples, and Dictionaries**  

Today, we’ll dive deeper into **Lists, Tuples, and Dictionaries**, followed by **a daily task** to strengthen your understanding.  

---

## **📚 Lesson: Advanced Lists, Tuples, and Dictionaries**  

### **🔹 1️⃣ Lists: Dynamic Collections**  
Lists are **mutable** (can be changed) and used to store multiple items.  

#### **📌 Common List Operations**  
```python
numbers = [4, 2, 8, 2, 9]

numbers.append(10)  # Adds 10 at the end
numbers.remove(2)   # Removes first occurrence of 2
numbers.sort()      # Sorts list in ascending order
numbers.reverse()   # Reverses the list
numbers.pop()       # Removes the last element

print(numbers)  
```
✅ **Use Case:** Managing a list of student scores dynamically.  

---

### **🔹 2️⃣ Tuples: Immutable Sequences**  
Tuples are **fixed** once created and are more memory-efficient than lists.  

#### **📌 Tuple Example**
```python
subjects = ("Math", "Physics", "Computer Science")

print(subjects.count("Math"))  # Counts occurrences of "Math"
print(subjects.index("Physics"))  # Finds index of "Physics"
```
✅ **Use Case:** Storing unchangeable data like months of the year.  

---

### **🔹 3️⃣ Dictionaries: Key-Value Pairs**  
Dictionaries store data as `{key: value}` pairs.  

#### **📌 Dictionary Operations**
```python
student = {"name": "Taha", "age": 17, "city": "Karachi"}

print(student.keys())    # Prints all keys
print(student.values())  # Prints all values
print(student.items())   # Prints key-value pairs

# Using .get() to avoid KeyErrors
print(student.get("age", "Not Found"))  # Returns 17
print(student.get("country", "Not Found"))  # Returns "Not Found"

# Updating dictionary
student.update({"age": 18, "country": "Pakistan"})
print(student)
```
✅ **Use Case:** Storing and managing user data in web applications.  

---

### **🔹 4️⃣ List & Dictionary Comprehensions**
💡 **A short and fast way to create lists and dictionaries.**  

#### **📌 List Comprehension Example**  
```python
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, ... 20]
```

#### **📌 Dictionary Comprehension Example**  
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
✅ **Use Case:** Efficiently transforming or filtering data.  

---

## **📝 Daily Task (Day 9)**
1️⃣ **Remove duplicates from a list** and print the unique elements.  
2️⃣ **Find the second-largest number** in a given list.  
3️⃣ Use **dictionary comprehension** to create a dictionary where **keys are numbers (1-5) and values are their squares**.  
4️⃣ Given a dictionary, **sort it by values in ascending order**.  

💬 **Let me know once you've completed the task!**  

---

## **🚀 Next Step: Mini Project**
Once you complete the daily task, you'll move on to a **mini project** that applies what you've learned!  

🎯 **Project Idea:**  
**Build a Contact Book in Python**  
✅ Add, delete, and search contacts  
✅ Store names, phone numbers, and emails in a dictionary  
✅ Save contacts to a file for future use  

---

Let me know when you're ready to start! 🚀