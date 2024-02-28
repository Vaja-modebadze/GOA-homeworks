required_weight = 50
required_height = 170

weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

print(weight == required_weight and height == required_height)
print(weight >= required_weight and height < required_height)