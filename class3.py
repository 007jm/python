###변수 복습
num=0
num+=1       #num=num+1변수num에 1을 더해서 num에 대입
print(num)
num*=12  #num=num * 12
print(num)
# 복합 대입 연산자

balance=100
balance*=2
print(balance)
# 비교 연산자

a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#논리 연산자

print(a<b and a == 10)
print(a<b or a==20)
print(not a>b)

# 포맷팅

name="jm"
age= 14
height= 170.5
print("이름: %s, 나이: %d, 키: %f"%(name,age,height))  # 포맷기호
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))  #포맷함수 , f-string
print(f"이름:{name}, 나이:{age}, 키:{height}")  #f-string
print("이름: %s, 나이: %d, 키: %.1f"%(name,age,height))
#bin : 2진수 함수
#oct : 8진수 함수
#hex : 16진수 함수

n=10
print("%s"%(bin(n)))