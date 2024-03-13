#1

num = int(input("Enter your number: "))
if num == 0:
    print(0)
if num >= 0:
    print("True")
else :
    print("False")

#2 

mile = int(input("Enter number: "))
kilometer = int(input("Enter number: "))

if mile >= 0:
    print("Correct decision")
else:
    print("Wrong decision")

if kilometer >= 0:
    print("Correct decision")
else:
    print("Wrong decision")

#3

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
mail = input("Enter your mail: ")
print(name, surname, age, mail)

#4

i = int(input("Enter your number: "))
for i in range(3):
    i = i // 3
    print(i)

#5
    
num = int(input("Enter your number: "))
if num >= 10:
    print (num in range(1,50))
else:
    print("False")

#7
num = int(input("Enter your number: "))
num1 = int(input("Enter your number: "))
print(num + num1)