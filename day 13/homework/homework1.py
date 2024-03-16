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

while num <= 10 and num >= 1:
    num = num + 1
    print(num)


# 7)
for i in range (10,0):
    i = 10 - 1
    print(i)