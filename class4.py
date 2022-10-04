# # ### input () 함수
# # print(input("작성하시요"))
# # name = input("작성하시요")
# # print(name)

# # num = input("숫자를 입력")
# # print(num, type(num))    #input은 문자열로 저장

# # num2 = input("숫자")

# # print(f"{num} + {num2} = {num+num2}")

# # int(input("숫자 입력"))

# #name = int(input("작성하시요"))   #문자열을 숫자로 바꾸려면 int()로 감싼다.
# #print(name, type(name))

# #int() : 정수형 함수
# #float() : 실수형 함수
# #str() : 문자열 함수
# #list() : 리스트형 함수
# #tuple() : 튜플형 함수
#                             #계정생성 프로그램
id = input("아이디를 입력하시요 : ")
pw = input("pw를 입력 하시요")
print(f"ID:{id} / PW:{pw}")

print(len(pw))
print(f"ID:{id} / PW:{pw}")
#len()   #길이(갯수)를 반환해 주는 함수
#[숙제]
print(len(pw) * ("*"))    # 해결

# ### 문자열

# #변수이름 = '원하는 문자열'
# text = 'He said, "Hello"'

# fruit1 = "블루베리"
# fruit2 = "산딸기"

# print(fruit1+ fruit2)  #문자열 덧셈은 병합
# # print(fruit1- fruit2) # 문자열과 문자열은 뺄수 없다
# print(fruit1*5)  #문자열과 숫자는 곱할수 있다. (반복)


###인덱스(index)

# hello = "hello, world!"
# # print(hello[7])
# # print(hello[-1])

# # ### 인데스 슬라이싱
# # print(hello[0:4])   # [] 뒤에 있는 숫자는 끝나는 숫자보다 1더 해 줘야 한다
# print(hello[:5])

### 이스케이프 코드
text = "\t\"There is no one \nwho loves pain itself, \nwho seeks after it \nand wants to have it, \nsimply because it is pain...\""

print(text)

#\n  문자열 안에서 줄 바꿈
