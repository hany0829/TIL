# 문제2

# a = input('문자열을 입력하세요>')
# n = 0

# for element in a:
#     if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element ==  'u' or element =='A' or element == 'E' or element == 'I' or element == 'O' or element == 'U' :
#         n += 1    
# print(n)

str = input('문자열을 입력하세요 > ').lower()
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in str:
    if i in vowel:
         cnt += 1
print(cnt)