### for 활용
## 자료형변환 ## 중첩 for문
# num= input ("원하는 숫자 입력 : ")
# print(num, type(num))
# num = num.split()   ##split 뜨어쓰기마다 끊어준다
# print(num, type(num))

# num= input ("원하는 숫자 입력 : ")
# num  = num.split()
# num = list(int(i) for i in num)
# print(num, type(num))

# num= input ("원하는 숫자 입력 : ").split
# num = list(int(i) for i in num)
# print(num, type(num))

# num = list(int(i) for i in input ("원하는 숫자 입력 : ").split)
# print(num, type(num))

# num = [(int(i) for i in input ("원하는 숫자 입력 : ").split)]
# print(num, type(num))

### 이메일 주소록

# email = input ("이메일 주소 입력 : ").split()
# email1=email
# email2=email1.split("@")
# id=[]                               ###내 시도
# id= email
# print(id)
# id1 = []
# id1=id[0]
# print(id1)
# host=[]
# host = [1]
# print(host)

### 별찍기
# count= int(input("별갯수 입력 : "))
# for i in range(1,count+1):
#     print("*"*i)

# count= int(input("별개수 입력 : "))
# for i in range(count):
#     print(" "*i , end='')
#     print("*")
##   역 삼각형
# count = int(input("별의 갯수 입력 : "))
# for i in range(1, count+1):
#     for g in range(count-i,0,-1):
#         print(" ",end="")
#     print("*"*i)


# count = int(input("별의 갯수 입력 : "))
# for i in range ()
   ##트리
count = int(input("별의 갯수 입력 : "))
for i in range(1, count+1):
    for g in range(count-i,0,-1):
        print(" ",end="")
    print("*"*(i+(i-1)))

