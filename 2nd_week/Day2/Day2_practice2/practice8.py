a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
else:
    for c in range(max(a,b) - min(a,b) - 1):
        c += 1
        print(max(a,b) - c,end=' ')