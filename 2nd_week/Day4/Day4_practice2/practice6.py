# 문제6
str = input('문자열 입력하세요 > ')

dic = {}

for i in str:
    if i == ' ':
        continue
    elif i not in dic:
        dic[i] =1
    elif i in dic:
        dic[i] += 1
for key in dic:
    print(key, dic[key])