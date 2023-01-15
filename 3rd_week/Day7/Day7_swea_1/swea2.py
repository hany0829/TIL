# 2071 평균값 구하기

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    avg = sum(numbers) / len(numbers)
    avg = round(avg)
    print(f'#{t} {avg}')