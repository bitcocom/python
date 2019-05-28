# 순서가있는 자료형(시퀀스 자료형)
# 1. 문자열(str)
#    0123456789......index(순서)
s = 'Hello Python'
# 인텍싱
print(s[0])
print(s[1])
print(s[2])
print(s[3])

# 슬라이싱
print(s[0:2])
print(s[3:5])
print(s[6:])

# 문자열 관련 함수
print(s.upper())
print(s.lower())
print(s.count('o'))
print(s.startswith("H"))
print(s.find('P'))
print(s.split(" ")[0])
print(s.split(" ")[1])

# 실습 4 : ssn 문자열 변수에서 - 을 기준으로 두부분으로 나누어서 출력하시오.
ssn = '710210-1622481'

