
#* 📝 Daily Task (Day 9)
#* 1️⃣ Remove duplicates from a list and print the unique elements.
#* 2️⃣ Find the second-largest number in a given list.
#* 3️⃣ Use dictionary comprehension to create a dictionary where keys are numbers (1-5) and values are their squares.
#* 4️⃣ Given a dictionary, sort it by values in ascending order.

#* 1️⃣ Remove duplicates from a list and print the unique elements.
numbers = [1,23,1,3,4]
unumbers = list(set(numbers))
print(unumbers)

#* 2️⃣ Find the second-largest number in a given list.
list = [1,23,14,3,4]
list.sort()
print(list[-2])

#* 3️⃣ Use dictionary comprehension to create a dictionary where keys are numbers (1-5) and values are their squares.
squares = {x:x**2 for x in range(1,6)}
print(squares)

#* 4️⃣ Given a dictionary, sort it by values in ascending order.
student_marks = {"Alice": 85, "Bob": 78, "Charlie": 92}
sorted_marks = dict(sorted(student_marks.items(), key=lambda item: item[1]))
print(sorted_marks)  
# Output: {'Bob': 78, 'Alice': 85, 'Charlie': 92}
