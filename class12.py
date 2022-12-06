###중간평가

## 1
# i=input("숫자 입력:")
# p=input("문자 입력:")
# print(i+p)

## 2
# print("과천코딩2022"[2:6])

## 3
# a = input("과일 이름 : ")
# b = input("과일 갯수 : ")
# print(f"{a}과일을 {b}개만큼 먹었다")

## 4
# j=int(input("숫자 입력1 : "))
# m=int(input("숫자 입력2 : "))
# print(j+m)
# print(j-m)
# print(j*m)
# print(j/m)

## 5
# f =  int(input("숫자 입력 3 : "))
# if f%2==0:
#     print("짝수")
# elif f%2==1:
#     print("홀수")

## 6
# count= 1
# c = int(input("숫자입력: "))
# while count<=c:
#     if c%count==0:
#         print(count)
#     count+=1

#for문
    
## 7
# d = 0
# count=1
# c = int(input("숫자 입력 : "))
# while count<=c:
#     if c%count==0:
#         print(count)
#         d+=1
#     count+=1
# if d >2:
#     print("false")
# else:
#     print("true")

#for 문
## 8
# count=1
# g = int(input("구구단 숫자 입력: "))
# while count<10:
#     print(f"{g}*{count}={g*count}")
#     count+=1

#for문
# 9
#while시도
# c =1
# d = 0
# h=int(input("숫자 입력: "))
# while h>=c:
#     d+=(1+c)
#     c+=1
# print(d-h)

# 9
#range시도
# c=0
# h=int(input("dlqfur: "))
# for i in range(1,h+1):
#     c+=i
# print(c)



# ## 10
# w= int(input("숫자입력:"))
# c =0
# while c<=w:
#     print (c)
#     c+=1
    
# for i in range(0,10,3):
#     print("x")

# if ##나머지 연산중요

# 10
# j = 0
# c = 0
# m = int(input("입력: "))
# while j<=m:
#     while c<=10:
#         if c==3:
#             print("*")
#             c+=1
#             j+=1
#         elif c==6:
#             print("*")
#             c+=1
#             j+=1
#         elif c==9:
#             print("*")
#             c+=1
#             j+=1
#         else:
#             print(c)
#             c+=1
#             j+=1
#         c-=10
        
        
        
##3,6,9
# num = int(input("숫자입력: "))

# for i in range(1, num+1):
#     if i % 10 == 3 or i%10==6 or i %10==9:
#         print("X")
#     elif i // 10==3 or i// 10 == 6 or i //10== 9 :
#         print("X")
#     else:
#         print(i)


##두가지 주사위
k=[]
for i in range(1,7):
    for g in range(1,7):
        print(i,g)
        
###
