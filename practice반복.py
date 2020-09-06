# for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for wating_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(wating_no))

# for wating_no in range(5):
#     print("대기번호 : {0}".format(wating_no))
# for wating_no in range(1, 6):
#     print("대기번호 : {0}".format(wating_no))

# caffe = ["아이언맨", "토르", "그루트"]
# for customer in caffe:
#     print("{0}님 커피 받아가세요".format(customer))


# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님 커피 가져가세요 기회{1}번 남았습니다".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피 버림~")

# c = "토르"
# p = "?"

# while p != c:
#     print("{}님 커피가져가세요".format(c))
#     p = input("이름이 어떻게 되세요?")
#     if p == c:
#         print("맛커~")
#     else:
#         print("꺼지쇼")


# continue, break
# absent = [2, 5]  # 결석한학생
# no_book = [7]
# for student in range(1, 11):  # 1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("도랏나? 수업끝. {0}번 교무실로 따라와".format(student))
#         break
#     print("{0}번아 책읽어라".format(student))


# for한줄로조지기
# 출석번호가 1,2,3,4였는데 101,102,103,104로 만들기
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["IronMan", "Thor", "Cap", "BlackWidow", ]
students = [i.upper() for i in students]
print(students)
students = [len(i) for i in students]
print(students)
