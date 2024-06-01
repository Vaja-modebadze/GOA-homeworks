# 2.
def numbers(rounding):
    X = []
    for i in range(0, -1):
        i = round(i)
        return(i)
# 3.
x = [1, 2, 3]
if x[0] <= 1 :
    print(x[0])
else:
    print((False))
if x[1] == 2 :
    print(True)
else:
    print(False)
if x[2] == 3:
    print(True)
else:
    print(False)
# 4.
def find_largest(a, b, c):
    first, second, third = float('-inf'), float('-inf'), float('-inf')

    if a > first:
        third = second
        second = first
        first = a
    elif b > second and b != first:
        third = second
        second = b
    elif c > third and c != second and c != first:
        third = c

    print(f"Three largest elements {first}, {second}, {third}")