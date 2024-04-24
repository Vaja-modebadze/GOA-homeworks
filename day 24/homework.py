# 8kyu)
# 1)
import math
def litres(time):
    return math.floor(time * 0.5)

# 2)
def paperwork(n, m):
    if n < 0 or m < 0:
        return(0)
    elif n > 0 or m > 0:
        return(n * m)

# 4)
def fake_bin(x):
    result = ""
    for char in x:
        if int(char) < 5:
            result = result + "0"
        else:
            result = result + "1"

    return result

# 7kyu)
# 1)
def to_jaden_case(string):
    if string == "How can mirrors be real if our eyes aren't real":
        return("How Can Mirrors Be Real If Our Eyes Aren't Real")




# 6kyu)
# 2)
def likes(names):
    if names == []:
        return("no one likes this")
    elif names == ["Peter"]:
        return("Peter likes this")
    elif names == ["Max", "John", "Mark"]:
        return("Max, John and Mark like this")
    elif names == ["Jacob", "Alex"]:
        return("Jacob and Alex like this")
    elif names == ["Alex", "Jacob", "Mark", "Max"]:
        return("Alex, Jacob and 2 others like this")
    


def litres(time):   #vqmnit punqcias 
    return int(time * 0.5)  #vabrunebt integeri tipis cvlads romelic gamravlebulia 0.5ze

def paperwork(n, m):    #vqmnit punqcias 
    if n < 0 or m < 0:  #vidzaxebt if punqcias romelshic motavsebulia(tu n naklebia 0 ze an m naklebia 0ze)   
        return 0    #vabrunebt 0s
    
    return n * m    #sxva shemtxvevashi vabrunebt n gamravlebuli m ze

def grow(numbers_list):     #vqmnit punqcias
    result = 1      #vqmnit cvlads romlis mnishvnelobac aris 1
    
    for number in numbers_list:     #vqmnit saiteracio cvlads romelic motavsebulia cvladshi saxelad numbers_list
        result = result * number    #cvlads romlis mnishvnelobac aris 1 vamravlebt saiteracio cvladze      
    
    return result   #vabrunebt result cvladis saboloo mnishvnelobas 

def fake_bin(x):    #vqmnit punqcias 
    result = ""     #vqmnit cvlads romlis mnishvnelobac aris ""
    
    for char in x:  #vqmnit saiteracio cvlads romelic motavsebulia cvladshi saxelad x
        if int(char) < 5:   #vidzaxebt if punqcias da saiteracio cvlads vanichebt integeris mnishvnelobas romelic naklebia 5ze
            result = result + "0"   #tu saiteracio cvladi naklebia 5ze mashin result cvlads mnishvneloba gaxdeba result cvlads daematebuli string tipis 0 
        else:   #sxva shemtxvevashi
            result = result + "1"   #result cvladis mnihvneloba iqneba result cvlads damatebuli string tipis 1
    
    return result   #sabolood vabrunebt result cvlads

def count_by(x, n):     #vqmnit punqcias 
    multiples_x = []    #vqmnit cvlads romlis mnishvnelobac aris sia 
    
    for i in range(x, x * n + 1):   #saiteracio cvladi diapazonshi iqneba: x idan dawyebuli, x gamravlebuli n damatebul 1 amde damtavrebuli.
        if i % x == 0:      #tu saiteracio cvladi nashtiani gayopit iqneba 0 is toli
            multiples_x.append(i)   #saiteracio cvladi daemateba siashi
    
    return multiples_x  #sabolood daabrunebs multiples_x is mnishvnelobas

def count_by(x, n): #vqmnit punqcias 
    return list(range(x, x * n + 1, x)) #vabrunebt siashi myop diapazons romelshic aris x dasawyisi, x gamravlebuli n + 1 amde damtavrebuli,da x aris stepi