# 1)
def odd(numbers):
    num = 0
    for i in numbers:
        if (numbers % 2) != 0:
            num += i
        return num
print(odd([1,3,4,5,6])+ 5)
# 2)     
def calculation():
    num1 = 15
    num2 = int(input("Enter your number: "))
    x = input("Choose +, -, *, /: ")
    if x == "/":
        print(num1 / num2)
    elif x == "+":
        print(num1 + num2)
    elif x == "*":
        print(num1 * num2)
    elif x == "-":
        print(num1 - num2)
    else:
        print("incorrect")
    print(x)
# 3)
def hashtag_generator():
    sentence = input("Enter your sentence: ")
    if sentence != "#":
        return("#" + sentence)
    print(sentence)
