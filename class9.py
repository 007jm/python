### 제어문 반복문 while

# while 조건 :
    # 명령

# count = 0

# while count<10:
#     count += 1
#     print(f"나무를 {count}번 찍었습니다")


### 계정 생성 프로그램 업그레이드 -> 로그인 프로그램
count = 3
while count > 0:
    member = ["재명", "현수", "서욱"]
    newpw = ''
    newID = input("새로운 아이디를 입력 하세요 : ")
    
    if newID in member:
        print("이미 가입된 아이디 입니다")
        count -= 1
    else:
        member.append(newID)
        newpw = input("pw 입력하세요 : ")
        print(f"가입완료! {newID}님, 환영 합니다")
        break
    print("다시 시도해 주세요")

### 로그인 프로그램
# count1 = 0
# while count1 == 0:
#     id= input("회원가입 아이디를 입력해 주세요 : ")
#     if id in member:
#         print(f"{id}님 로그인이 됬습니다")
#         count1 += 1
#     else:
#         print("없는 아이디 입니다")

# # while true (무한 반복)

# while True:
#     id= input("로그인 아이디를 입력해 주세요 : ")
#     if id in member:
#         print(f"{id}님 로그인이 됬습니다")
#         break
#     else:
#         print("없는 아이디 입니다")


while True:
    id = input("회원가입 아이디를 입력해 주세요 : ")
    
    if id in member:
        pw = input("pw를 입력해 주세요 : ")
        if pw ==newpw:
            print(f"{id}님 로그인이 됬습니다")
            break
        #pw 틀렸을 경우
    else:
        print("없는 아이디 입니다")
