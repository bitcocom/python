#리스트 구조 만들기
x=list()
print(type(x))

x.append(10)
x.append(20)
x.append(30)
print(x) # [10,20,30]

x=list([10,30,30])
print(x) # [10,20,30]

x=[10,20,30]
print(x) # [10,20,30]

# range(start, stop, step) : 범위함수 사용
x=list(range(10,40,10)) # start~stop 까지 step 씩 증가하는 수 [10,20,30]
print(x)

#리스트에 저장된 데이터 출력
for data in x :
    print(data)

for i in  range(0, len(x)):
    print(x[i])