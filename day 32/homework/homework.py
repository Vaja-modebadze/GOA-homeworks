# 8 kyu:
# 1)
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    return "green"

# 2)
def find_difference(a, b):
    multiply_a = a[0] * a[1] * a[2]
    multiply_b = b[0] * b[1] * b[2]
    
    if multiply_a > multiply_b:
        return multiply_a - multiply_b
    else:
        return multiply_b - multiply_a

# 3)
def triple_trouble(one, two, three):
    result = ""
    for i in range(len(one)):
        result += one[i]
        result += two[i]
        result += three[i]
    
    return result

# 7 kyu:
# 1)
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    return a / b

# 2)
def in_asc_order(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# 3)
def show_sequence(n):
    if n < 0 :
        return str(n)+"<0"
    elif n == 0:
        return "0=0"
    sum = 0
    string_result = []
    for i in range(n+1):
        sum += i
        string_result.append(str(i))
    return "+".join(string_result)+" = " + str(sum)


# 6 kyu:
# 1)

# 2)
def data_reverse(data):
    res = []
    while len(data) != 0:
        res += data[-8:]
        data = data[0:-8]
    return res
