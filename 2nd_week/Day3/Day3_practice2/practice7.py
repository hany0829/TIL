# 문제7

number_list = [1, 2, 3, 4, 5]
min = number_list[0]
for i in range(1, len(number_list)):
    if min > number_list[i]:
        min = number_list[i]
print(min)

number_list = [5, 5, 5, 2]
min = number_list[0]
for i in range(1, len(number_list)):
    if min > number_list[i]:
        min = number_list[i]
print(min)