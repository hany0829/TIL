num = int(input('양의 정수를 입력하세요 > '))
sum = 0
if num < 0:
    print(-1)
else:
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    print(sum)

    # 이해안됨