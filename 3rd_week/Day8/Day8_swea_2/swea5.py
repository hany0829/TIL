n = int(input())
total = 0
while n > 0:
    r = n % 10
    n = n //  10
    total += r
print(total)

# a = list(input())
# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)