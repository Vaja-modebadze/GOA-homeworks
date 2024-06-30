# 1
def is_even(n): 
    return n % 2 == 0
# თუ რაიმე რიცხვს რომელსაც ვყოფთ 2-ზე გვრჩება ნაშთი ნული ამ შემთხვევაში უცნობი რიცხვი არის ლუწი.
# 2
def difference_in_ages(ages):
    youngest = min(ages)
    oldest = max(ages)
    
    return youngest, oldest, oldest - youngest
# ამ kata-ში უნდა გამოგვეტანა სიიდან ყველაზე მცირე, დიდი და მათ შორის მყოფი სხვაობა.
# 3
def find_average(numbers):
    summary = sum(numbers)
    amount = len(numbers)
    
    if amount > 0:
        return summary / amount
    else:
        return 0
# ამ kata-ში უნდა გამოგვეთვალა საშუალო არეთმეტიკული და თუ სია იქნებოდა ცარიელი უნდა გამოგვეტანა 0.
# 4
def make_upper_case(s):
    return s.upper()
# ამ kata-ში უნდა გადაგვეყვანა სტრინგი uppercase-ში.
# 5