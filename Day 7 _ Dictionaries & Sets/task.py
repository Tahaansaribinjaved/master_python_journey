
#* 📝 Daily Task:
#* 1️⃣ Create a dictionary with your name, age, and favorite programming language. Print each value.
#* 2️⃣ Update the dictionary to include your favorite hobby.
#* 3️⃣ Create two sets of numbers and perform union, intersection, and difference.
#* 4️⃣ Check if a value exists in a dictionary before accessing it.

#* 1️⃣ Create a dictionary with your name, age, and favorite programming language. Print each value.
my_dict = {"name":"Taha","age":17,"fpl":"Python"}
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["fpl"])

#* 2️⃣ Update the dictionary to include your favorite hobby.
my_dict["mfh"] = "coding"
print(my_dict["mfh"])

#* 3️⃣ Create two sets of numbers and perform union, intersection, and difference.
a = {1,2,3,4}
b= {3,4,5,6}
print(a|b)
print(a&b)
print(a-b)

#* 4️⃣ Check if a value exists in a dictionary before accessing it.
if "age" in my_dict:
    print("My age exists:", my_dict["age"])
