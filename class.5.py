### 문자열 함수
text = "Hello, World!"

print(text.count("l"))
print(text.count("d"))
print(text.upper())     #대문자
print(text.lower())     #소문자
print(text.replace("World", "hi"))
print(text.isalpha())   #알파벳
print(text.isdigit())   #숫자

text2="hello"
text3="0123456789"
print(text2.isalpha())
print(text3.isdigit())

print(len(text))
print(text.split())    #쪼개기(아무것도 없으면 " "로 인식됨)

phone = "010-1234-1234"
print(phone.split("-"))

###김밥 만들기
아이템 = "김"
아이템2="밥"
아이템3="계란"
아이템4="단무지"
아이템5="햄"

print(아이템,아이템2,아이템3,아이템4,아이템5)

아이템들 = ["김" , "밥" , "단무지" , "계란" , "햄" , "시금치"]
print(type(아이템들))
print(아이템들[4])
print(아이템들[2:5])


###리스트와 인덱스
students = ["현수" , "서욱" , "주원"]
scores = [100, 80, 90]

# print(students + scores)     #병합
# print(students * 3)     #반복

# print(max(scores))
# print(min(scores))
# print(len(students))
# text = "hello"
# print(text, type(text))
# text=list(text)
# print(text, type(text))

# num = int(input("숫자입력: "))
# print(num, type(num))

# print(sum(scores))

students.append("민재")
print(students)
scores.append(70)
print(scores)

students.insert(2, "재명")
print(students)
scores.insert(2,100)
print(scores)

students.pop()
print(students)
scores.remove(70)    #똑같은 수가 있을때 앞에서 부터 실행됨
print(scores)
print(students + scores)
print(students)
print(scores)

students.extend(scores)
print(students)
print(scores)