a = list(input('문자열을 입력하세요 > ').split())

dic = {}


for i in a:
    if i not in dic:
        dic[i] = 1
    else:

        dic[i] = dic[i] + 1
for key in dic:
    
    print(key, dic[key])

# dic[i] = dic.get (k, 0)