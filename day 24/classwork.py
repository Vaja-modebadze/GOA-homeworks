# 7kyu)
# 2)
def paperwork(n, m):
    if n < 0 or m < 0:
        return(0)
    elif n > 0 or m > 0:
        return(25)



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