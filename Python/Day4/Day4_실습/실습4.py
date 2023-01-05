# 문제4

dict_variable = {
    '이름' : '정우영',
    '전화번호' : '010-1234-5678',
    '거주지' : '서울시'
}

input('이름을 입력하세요 >')
input('전화번호를 입력하세요 >')
input('거주지를 입력하세요 >')

for k, v in dict_variable.items():
    print('{} : {}'.format(k, v))

