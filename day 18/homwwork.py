#1)

numbers = []

for i in range(5):
    number = int(input("Enter your number: "))
    numbers.append(number)
    
print(sum(numbers))

#2)

numbers = [11,12,13,14,15,16,17,18,19,20]
print(numbers[-1])

#3)

numbers = []

for number in range(30,51):
    numbers.append(number)
if number % 2 == 1:
    print(number)

#4)

numbers = []
for i in range(10,51):
    if number % 4 == 0:
        numbers.append(number)
        print(numbers)