# 문제5

name = (input('이름을 입력하세요 > '))
phone = input('전화번호를 입력하세요 > ')
email = input('이메일알 입력하세요 > ')
address = input('거주지를 입력하세요 > ')

dict_variable = {
    '이름' : { 
        '이메일' : email,
        '전화번호' : phone,
        '거주지' : address,
    },
}
print(dict_variable)

