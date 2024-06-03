# 8KYU
# 1)

# 2)
def make_negative( number ):
    if number != 0:
        return number
    else:
        return 0

# 3)
def str_count(strng, letter):
    return strng.count(letter)

# 7KYU
# 1)
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0