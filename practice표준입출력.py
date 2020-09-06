# # 세퍼레이터(구분자)지정가넝, 문자열끝지정가넝(줄바꿈안하기가능한)
# print("python", "Java", sep=",", end="?")

# print("무엇이 더 재밌을까요??")
###################################################
# import sys
# print("Python", "java", file=sys.stdout)
# print("Python", "java", file=sys.stderr)
###################################################

# # 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호 : "+str(num).zfill(3))  # zero fill

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))  # input으로 받으면 숫자 받아도 문자열 형태로 받아짐.
# print("입력하신 값은 "+answer+"입니다.")


###################################################
# 출력포맷
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0:>10}".format(500))
# 양수에는+음수에는-표시
print("{0:>+10}".format(500))
# 왼쪽정렬, 빈칸을 밑줄로채우고, +-부호표시
print("{0:_<+10}".format(500))
# 3자리마다 ,찍기
print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
# 3자리마다 ,찍고 부호도 붙이고 자릿수도 확보하고 빈자리^로 채우기
print("{0:^<+20,}".format(100000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지 출력
print("{0:.3f}".format(5/3))
