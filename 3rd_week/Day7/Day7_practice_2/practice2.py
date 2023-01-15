# 단어를 구분해서 출력하세요.
# hello python world

string = input('단어를 구분해서 출력하세요.').split()

print(*string, end =' ')