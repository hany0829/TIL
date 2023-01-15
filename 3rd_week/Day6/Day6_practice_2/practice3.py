string = input('문자열을 입력하세요 > ')
result = ''
for char in string:
    if char != 'e':
       result += char
print(result)