

# ! 📝 Daily Task:
# ! 1️⃣ Take user input for age and print whether they are an adult or minor.
# ! 2️⃣ Write a program that prints numbers from 1 to 10, skipping number 5.
# ! 3️⃣ Write a program to print even numbers from 1 to 20 using a loop.
# ! 4️⃣ Print "Python is fun!" 5 times using a loop.



# ! 1️⃣ Take user input for age and print whether they are an adult or minor.

age = int(input("Enter your age :"))
if(age<0):
    print("invalid age ! please enter a valid age")
else:
    if(age<18):
        print("You are minor!")
    else:
        print("you are adult")
        
# ! 2️⃣ Write a program that prints numbers from 1 to 10, skipping number 5.
for i in range(1,11):
    if(i==5):
        continue
    print(f"count {i}")
# ! 3️⃣ Write a program to print even numbers from 1 to 20 using a loop.
for i in range(1,21):
    if(i%2==0):
        print(f"even number {i}")    
# ! 4️⃣ Print "Python is fun!" 5 times using a loop.
times = 0
while(times<5):
    print("Python is fun")
    times+=1

