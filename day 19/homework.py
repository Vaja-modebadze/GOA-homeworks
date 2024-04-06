#1)
list = []
for i in range(1,5):
    i = i * (1,5)
    list.append(i)
    print(i)

print(i)

#2)
negative_numbers = []

for i in range(-3,3):
    if i * -1 > 0:
        negative_numbers.append(i)
        print(i)

#3)
list = []
for i in range(1,5):
    i = (1 + 2 + 3 + 4)

print(i / 4)
    
#4)
list1 = []
list2 = []
list3 = []

for i in range(1,5):
    list1.append(i)
for x in range(5,10):
    list2.append(x)
            
list3.append(list1 and list2)
print(list3)
    