# 문제3

dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

### 이하 문제 해결 코드 작성

if "나이" not in dict_variable:
    dict_variable["나이"] = "24세"
print(f"나이 : {dict_variable['나이']}")
