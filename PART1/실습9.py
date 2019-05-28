# 리스트 내포(List Comprehension) : 리스트 안에 for 문을 사용하여 리스트를 만드는 문법
# 아래 리스트에 모두 3을 곱하여 새로운 리스트를 만드시오.
a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i*3)

print(result)

# 리스트 내포 방법을 이용하기

result = [ num*3 for num in a ]
print(result)

# 실습 9 : 리스트 내포를 사용하여 짝수만 3을 곱하여 새로운 리스트를 만드시오.
