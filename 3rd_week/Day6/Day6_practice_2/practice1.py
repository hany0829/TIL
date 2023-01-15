a = list(input('문자열을 입력하세요 > '))

for i in a:
    if i =='e':
        print (a.index(i))

if 'e' not in a:
      print ('=-1')

a = list(input())
for i in range(len(a)):
    if i =='e':
        print (i)
        break

if 'e' not in a:
      print ('=-1')