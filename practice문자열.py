# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """나는 소년이고,
# 파이썬은 쉽다!"""
# print(sentence3)


# 슬라이싱
# jumin = "910822-1234567"
# print("성별 : "+(jumin[7]))
# print("생년 : "+(jumin[0:2]))
# print("월 : "+(jumin[2:4]))
# print("일 : "+(jumin[4:6]))

# print("생년월일 : "+(jumin[:6])) #첫자리는 생략하면 처음(0)부터
# print("뒤 7자리 : "+(jumin[7:])) #7부터 끝까지
# print("뒤 2자리 : "+(jumin[-2:])) #뒤 2자리

# 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "C++"))

# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# print(index)

# print(python.find("is"))
# print(python.index("is"))

# print(python.find("Java"))  # 없는 문자열 검색시 -1반환
# # print(python.index("Java"))  # 없는 문자열 인덱스 요청시 에러

# print(python.count("n"))  # 파라미터 문자열 몇개 포함됐는지 세기


# 문자열 포맷
# print("a"+"b")
# print("a", "b")
# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아합니다." % "파이썬")
# print("Apple은 %c로 시작합니다" % "A")
# print("나는 %s살입니다." % 20)  # %s쓰면 저절로 str() 됨
# print("%s %s" % ("파란", "빨간")) #여러개 사용
# 방법 2
# print("나는 {}살입니다.".format(20))
# print("{} {}".format("파란", "빨간"))  # 여러개 사용
# print("{1} {0}".format("파란", "빨간"))  # 여러개 사용 순서지정 가능한~
# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해유".format(age=20, color="빨간"))
# 방법 4(3.6이상에서만 가넝)
# age = 20
# color = "파란"
# print(f"나는 {age}살이며, {color}색을 좋아해유") #f로 시작

# 탈출 문자
# \n 줄바꿈
print("백문이 불여일견,\n백견이 불여일타")
# 저는 "한정훈"입니다 = 따옴표 \", \'
print('저는 "한정훈"입니다')
print("저는 \"한정훈\"입니다")
# \\ 문장내에서 \출력
print("\\")
# \r : 커서를 맨 앞으로 이동
print("red apple\rpine")
# \b : 백스페이스 한글자 삭제
print("redd\bapple")
# \t : 탭 입력
print("red\tapple")
