# 사전? 키:밸류 형태 자료형? map이랑 머가 다르노
# cabinet = {3: "유재석", 100: "김태호"}  # 선언 {}안에 키:밸류
# print(cabinet)
# print(cabinet[3])
# print(cabinet.get(100))
# # print(cabinet[5]) #대괄호로 없는 키에 접근시 오류
# print(cabinet.get(5))  # get으로 없는 키에 접근시 none
# print(cabinet.get(5, "비어 있음"))  # 뒤에 none말고 출력값 지정 가능

# print(3 in cabinet)  # true
# print(5 in cabinet)  # false

cabinet = {"A-3": "유재석", "B-100": "김태호"}  # 선언 {}안에 키:밸류
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
