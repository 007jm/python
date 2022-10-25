### 제어문 / 조건문 if
# num = 8
# if num ==10:
#     print(f"num은 {num}입니다.")
#     print("지금은 조건문 if 안에 있습니다")
# print("지금은 조건문 if 밖에 있습니다")

# num = int(input("숫자 입력 : "))

# if num > 5:
#     print("입력한 숫자는 5보다 큽니다")
#     if num % 2 == 0:  #num이 짝수 라면
#         print("짝수 입니다")
#     elif num % 2 == 1: #num % 2 != 0 #홀수의 조건
#         print("홀수 입니다.")
#     else:
#         print("0입니다")
# elif num < 5:        #elif : else if 의 약자
#     print("입력한 숫자는 5보다 작습니다.")
#     if num % 2 == 0:
#         print("짝수 입니다")
#     elif num % 2 == 1:
#         print("홀수 입니다")
#     else:
#         print("0입니다")
# else:
#     print("입력하신 숫자는 5 입니다")   #else는 조건에 포함 되지 않은 전부
#     print("홀수 입니다.")
    
# num = int(input("숫자 입력 : "))

# if num > 5:
#     print("입력한 숫자는 5보다 큽니다")
# elif num > 3:
#     print("입력한 숫자는 3보다 큽니다")   #

##  조건문 if 와 논리연산 ( and , or , not )



# num = int(input("숫자 입력 : "))

# if num > 5 and num % 2 == 0:
#     print("입력한 숫자는 5보다 큽니다")
#     print("짝수 입니다")
# elif num > 5 and num % 2 == 1: #num % 2 != 0 #홀수의 조건
#     print("5보다 큽니다")
#     print("홀수 입니다.")

# elif num < 5 and num % 2 == 0:        #elif : else if 의 약자
#     print("입력한 숫자는 5보다 작습니다.")
#     print("짝수 입니다")
# elif num < 5 and num % 2 == 1:
#     print("홀수 입니다")
# elif num < 5 and num == 0:
#     print("0입니다")
# else:
#     print("입력하신 숫자는 5 입니다")   #else는 조건에 포함 되지 않은 전부
#     print("홀수 입니다.")
    
# ### 맴버쉽 연산자
# l = [1,2,3,4,5]
# print(3 in l)
# print(7 in l)

# s = "hello"
# print('e' in s)
# print('a' in s)


###미션
menmer = ["재명, 현수, 서욱"]
ID = input("새로운 아이디를 입력 하세요")
