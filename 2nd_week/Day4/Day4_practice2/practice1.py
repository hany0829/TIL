# 문제1

# a = input('문자열을 입력하세요>')
# n = 0
# word = ['h', 'e', 'l', 'l', 'o','h' ,'y' , 'p', 'E', 'r', 'g', 'r', 'o', 't', 'h']

# for element in word:
#     if element == 'e':
#             n += 1    
# print(n)

str = input('문자열을 입력하세요 > ')

count =0
for i in str:
    if i == 'e' :
        count += 1
print(count)
