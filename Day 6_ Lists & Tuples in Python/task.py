
#^ 📝 Daily Task:
#^ 1️⃣ Create a list of five favorite movies and print them.
#^ 2️⃣ Create a list of numbers, sort them in ascending & descending order.
#^ 3️⃣ Create a tuple with 3 subjects and print each using a loop.
#^ 4️⃣ Use list comprehension to generate a list of even numbers from 1 to 20.

#^ 1️⃣ Create a list of five favorite movies and print them.
movies = ["JAwani phir nahi aani","3idiots ","batrangi bhai jan ","wrong number","Teefaa"]
for movie in movies:
    print(f"My favorate movie is {movie}")

#^ 2️⃣ Create a list of numbers, sort them in ascending & descending order.
list = [1,24,324,3,4,566,65,3]
list.sort()
print(list)
list.reverse()
print(list)

#^ 3️⃣ Create a tuple with 3 subjects and print each using a loop.
subjects = ("Computer","Physics","Math")
for subject in subjects:
    print(f"My subject is {subject} ")
    
#^ 4️⃣ Use list comprehension to generate a list of even numbers from 1 to 20.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

