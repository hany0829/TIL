n = int(input('정수를 입력하세요 >'))
if n < 0 or n > 100:
    print('Error')
elif n >= 60:
    print('합격')
else:
    print('불합격')