#  1. 모듈을 가져오는 것!
import random

menu = ['햄버거', '국밥', '초밥']
print(random.choice(menu))

numbers = range(1,46)
lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))

for i in range(5):
    numbers = range(1,46)
    lucky_numbers = random.sample(numbers, 6)
    print(sorted(lucky_numbers))

students = ['', '', '', '']
print(students)
random.suffle(students)
print(students)

# .sort() : 매서드 
# return : None
# 해당 리스트 자체를 정렬!
numbers = [10, 2, 5]
result = numbers.sort()

numbers =[10, 2, 5]
numbers.sort()
print(numbers)


# sorted() : 함수
# return : 정렬된 리스트
numbers = [10, 2, 5]
result = sorted(numbers)
print(result) # [2, 5, 10]

import datetime

# print(datetime.datetime.now())
# print(datetime.date(2023, 1, 5))

today = datetime.date(2023, 1, 5)
print(today)
print(type(today))
print(today.year)
print(today.day)

end = datetime.date(2023, 6, 14)
print(end - today)