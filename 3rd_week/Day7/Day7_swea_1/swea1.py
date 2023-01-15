# 2029 : 몫과 나머지 출력하기

T = int(input())

for t in range(1, T+1):
   a, b = list(map(int,input().split()))
   # print(a, b)
   share = a // b
   remainder = a % b
   print(f'#{t} {share} {remainder}')








