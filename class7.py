# ### 딕셔너리 (dictionary)
# dic = {"name": "JM", "age":14, "school":"문원중"}
# print(dic, type(dic))

# print(dic["name"])
#    #추가
# dic["grade"] = 1
# print(dic)
#    #수정
# dic["name"] = "유재명"
# print(dic)
#    #삭제
# del dic["school"]
# print(dic)

# fruit = {"apple":500,"banana":2500,"mango":2000}
# print(fruit)

# print("망고의 가격은 1개 당 %d입니다" %fruit["mango"])  # 포맷 기호
# print("망고는 개당{}원 입니다".format(fruit["mango"]))  # 포맷 함수
# print(f"망고는 개당 {fruit['mango']}원 입니다")       # f 스트링

# fruit["apple"] = 700
# print(fruit)

# fruit["산딸기"] = 10000
# print(fruit)

# del fruit["banana"]
# print(fruit)


## 딕셔너리 함수
# d.keys()
score = {"ma":100, "en": 80, "sc":90, "ko":70}
print(score.keys())
# d.values
print(type(score.keys()))
print(score.values(), type(score.values()))
#
print(score.items)
#
print(score.get("ma"))
#
score.update({"ma":90, "hs": 80})
print(score)

score.clear()
print(score)