# 1)
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age in range(18,65):
    print("You are an adult.")
else:
    age >= 65
    print("You are a senior citizen.")

# 2)
for i in range(5):
    num = int(input("Enter your number: "))
    
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd")

# 3)
grade = input("Enter your grade: ")

if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("You passed.")
elif grade == "D":
    print("You can do better.")
elif grade == "F":
    print("You failed.")

# 4)
num = 1

while num < 10:
    print(num)
    num = num + 1

# 5)
num = 4
number = 0
count = 0

while number != num:
    number = int(input("Please enter number from (1-10): "))
    if number == num:
        print("You guessed number ip",count,"try")

# 6)
for i in range (5, 55, 5):
    print(i)

# 7)
for i in range (10,1,-1):
    print(i)