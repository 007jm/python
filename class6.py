###   리스트 함수2

score = [80, 90, 100, 70, 100]

##리스트 정보 관련 메소드
#.index() :특정 갚의 인덱스를 반환
print(score.index(90))
#.count() : 특정 갚의 갯수
print(score.count(100))
list.index
list.count

##리스트 정렬 관한 메소드
score.reverse()    # .reverse() : 리스트 안에있는 데이터의 순서를 역순으로 정렬
print(score)
score.sort()    # .sort() : 리스트 안에 있는 데이터를 작은 값부터 큰 값 순으로로 정렬
print(score)
score.sort(reverse=True)    # 내림차순 : 큰 값부터 작은 값 순으로 정렬
print(score)

## 활용
name = ["나", "현수", "서욱", "민재", "주원"]
print(name[2])
en_score = [1, 2, 3, 4, 5]
ma_score = [5, 4, 3, 2, 1]

print(name)
print(score)

student = []

student.append(name)     #append : 중간에 넣기
student.append(ma_score)
student.append(en_score)
print(student)

print(student[0][0],student[1][0],student[2][0])
print(student[0][3],student[1][3],student[2][3])


### 튜플 (tuple)
num = (10, 20, 30, 40, 50)
print(num, type(num))

##튜플의 연산
print(num+num)      #곱셈과 덧셈만 가능
print(num*4)

##튜플 & 인덱스
print(num[2])
print(num[1:4])

##리스트 vs 튜플
#리스트 : 복사 기능 / 위,변조 가능
l1 = [1, 2, 3]
l2 = l1[:]   # [:] : 전체를 의미 / 전체값 복사
print(l1)
print(l2)

l2.append(4)
print(l1)
print(l2)
print(l1 is l2)    #is : 객체가 같은 지 비교

##튜플 : 위변조 불가
t1 = (1, 2, 3)
t2 = t1[:]

print(t1==t2)
print(t1 is t2)