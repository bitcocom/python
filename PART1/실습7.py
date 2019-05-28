# 반복문(for, while)
'''
   for 변수 in  여러개의자료형(리스트,문자열) :
       반복할 문장 1
       반복할 문장 2
'''

aList = "Hello Python"
for s in aList :
    print(s, end='')

print()

bList = ['blue', 'red' ,'green', 'yellow']
for color in bList :
    print("color는 %s 입니다." %color)
    if color=='red' :
        print("내가 가장 좋아하는 색상입니다.")

# 실습 7 : 위에 있는 bList 원소들의 길이를 각각 구하여 출력하시오.
