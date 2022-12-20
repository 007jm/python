### 지역변수 & 전역변수
# total = 0

# def add(num):
#     global total    #함수 밖 변수는 원래 함수 안에서 못쓰나 global을 쓰면 쓸 수 있다
#     total+=num
#     print(total)
    
# add(10)
# add(7)


### 클래스
# class Cal:
#     total = 0
#     def add(self,num):
#         self.total += num
#         print(self.total)
# income= Cal()   #클래스 객체선언
# income.add(1000)
# spend= Cal()
# spend.add(100)

## 생성자
# class Cal:
#     def __init__(self):
#         self.total = 0
    
#     def add(self,num):
#         self.total += num
#         print(self.total)
# income=Cal()
# income.add(10000)

## 클래스 상속

class Cal:   # 부모 클래스
    def __init__(self):
        self.total = 0
    
    def add(self,num):
        self.total += num
        print(self.total)

class Cal_ch1(Cal):    # 자녀 클래스
    def sub (self,num):
        self.total -= num
        print(self.total)
    def div(self,num):
        self.total /=num
        print(self.total)
money = Cal_ch1()
money.add(100)
money.sub(1000)


### 오버 라이딩(덮어쓰기)

class Cal_fix(Cal_ch1):
    def div (self,num):
        if num == 0:
            print("존재 없음")
        else:
            self.total/=num
            print(self.total)