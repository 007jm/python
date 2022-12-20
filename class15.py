### 함수
## 사용자 정의 함수  :매개 변수

# def add():    #함수 정의
#     print("더하기 함수")
    
# add()       #함수 호출

# ##매개변수만 있는 함수
# def add(n1,n2):                        #n1, n2는 인자값 을 전달 받는 매개변수
#     total=n1+n2
#     print(total)
    
# add(10,5)

# ##전달값만 있는 함수
# def add():
#     return "더하기 함수"

# print(add())

# #매개변수와 전달값 둘다 있는 함수
# def add(n1,n2):     #매개변수
#     total = n1+n2
#     return total   #전달값

# print(add(10,5))


##응용

# def cal(f1,f2):
#     a=(f1+f2)
#     b=(f1-f2)
#     c=(f1*f2)
#     d=(f1/f2)
#     return a,b,c,d

# j=int(input("1 : "))
# m=int(input("2 : "))
# cal(j,m)


# def add(n):
#     total=0
#     for i in n:
#         total+=i
#     return i
# num=1
# num_l= []
# while num !=0:
#     num=int(input("1 : "))
#     num_l.append(num)

# print(add(num_l))

# num = [int(i) for i in input("숫자입력")]



###명함
# def namecard(*argm):
#     print("===============")
#     for i in argm:
#         print(i)
#     print("===============")       ##딕셔너리쓸때 개수가 정해져있지 않을때 **argm
    
# namecard("재명","010-****-****","myungwith")


# def tri(b,h):
#     area=b*h*0.5
#     return area

# def rect(b,h):
#     area = b*h
#     return area

# def circle(r):
#     area=r*r*3.14
#     return area

# order = input("어떤 도형의 넓이를 구하시겠습니까? : ")
# if