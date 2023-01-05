# 문제5

dict_variable = {
    '이름' : '정우영',
    '이메일' : 'beemo@hphk.kr',
    '전화번호' : '010-1234-5678',
    '거주지' : '서울시'
}

input('이름을 입력하세요 >')
input('전화번호를 입력하세요 >')
input('이메일을 입력하세요 >')
input('거주지를 입력하세요 >')


for key, value in dict_variable.items():
    print(value, end='')