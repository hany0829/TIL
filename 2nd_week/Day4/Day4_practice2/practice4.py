# 문제4

dict_variable = {
    '이름' : '정우영',
    '전화번호' : '010-1234-5678',
    '거주지' : '서울시'
}

name = input('이름을 입력하세요 >')
phone = input('전화번호를 입력하세요 >')
address = input('거주지를 입력하세요 >')

# for k, v in dict_variable.items():
#     print('{} : {}'.format(k, v))

dict_variable = {}
dict_variable['이름'] = name
dict_variable['전화번호'] = phone
dict_variable['거주지'] = address
print(dict_variable)

for key in dict_variable:
    print(f'{key} : {dict_variable[key]}')