str = input('문자열을 입력하세요 > ')
result=''
for i in str:
    if i ==' ':
        result += '-'
    else:
        result += i

print(result)
