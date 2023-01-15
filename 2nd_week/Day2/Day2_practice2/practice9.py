a = int(input('정수를 입력하세요 > '))

if a < 1:
    print(False)
else:
    for b in range(a):
        if b % 2 == 0:
            continue
        print(b)