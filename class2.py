###연산기호
print(1+9) #덧샘
print(1-9) #뺄샘
print(1*9) #곱샘
print(1/9) #나눗샘
print(1//9) #몫
print(1%9) #나머지
print(9**2) #제곱근

###자료형 (Data Type)
##type() : 자료형의 타입을 반환해주는 함수
print(type("hello,world"))   #str:string (문자열)
print(type(10))   #int : integer(정수) / ..-3,-2,-1,0,1,2,3...
print(type(10/3))  #float : 실수 / 소수점을 가진 숫자
print(type(1//9))
print(type(1%9))
print(type(1**9))

print("안녕하세요.제 이름은 %s이구요,나이는 %d살 입니다.키는 %fcm 입니다"%('재명',14,170.5)) #str : s/int : d / float : f



### 변수
name = "재명"
age = 14
height = 170.5
print(name, type(name))
print(age, type(age))
print(height, type(height))
print("안녕하세요.제 이름은 %s이구요,나이는 %d살 입니다.키는 %fcm 입니다"%(name,age,height))