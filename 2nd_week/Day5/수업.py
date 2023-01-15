my_list = ['서울', '서울', '대전', '광주' , 
'서울', '대전', '부산', '부산' ]
li =[]
# 지역을 하나씩 반복
for i in my_list:
    # 만약에 결과 통에 없다면,
    if i not in li:
        # 결과 통에 추가
        li.append(i)
print(li)
print(len(li))
print(set(li))
print(len(set(li)))

# dictionary : 키와 값의 모음