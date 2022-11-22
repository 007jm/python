# ### for 반복문 
# student = ["현수","서욱","재명",]

# count = 0
# while count < len (student) :
#     print(student[count])
#     count += 1

# for c in student:
#     print(c)

##for 와 딕셔너리
# dic = {"ma":90, "en":100, "ss":80, "sc":70, "pt":90}          #딕셔너리를 for 문으로 쓰면 열쇠 갚이 나온다
# point = 0
# for d in dic:
#     if dic[d] < 90:
#         continue
#     else:
#         print("축하합니다. 1000코인 플러스")
#         point += 1000
# print (f"총 {point} 적립되었습니다")
    

    # print(dic[d])
    # if dic[d] >= 90:
    #     print(f"{d} 축하")
    # else :
    #     print(f"{d}노력하세요")                 #90이상일시 축하
    

##range()
# for i in range(5):       #기본형          #하나의 인자값: 횟수 의미< 0 ~ (입력갑 -1) 생성
#     print(i)

## 확장1
# for i in range(1,6):          #두개의 인자값: (시작값, 끝값), 시작값 ~ (끝값-1) 생성
#     print(i)

# ## 확장 2
# for i in range(1, 10 ,2):
#     #하나의 인자값: (시작값,끝값,간격), ~ (끝값-1)까지 간격만큼 건너서 생성
#     print(i,end = " ")                #end = " " 은 옆으로 적입



### range() 활용
# j = int(input("숫자 입력 :"))
# j+=1
# for l in range(j):
#     print(j)
    
    
j = int(input("숫자 입력 :"))
k = int(input("숫자를 입력 :"))
for l in range(j,k+1):
    print(l)


##1~100까지 3의 배수출력

count = 0
for i in range (3,101,3):
    print(i, end=" ")
    count += 1
    if count == 10:
        count=0
        print()
        