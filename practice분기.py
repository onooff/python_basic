# # whether = "몰라"
# whether = input("오늘 날씨는 어때요 ?")

# # if 조건:
# #     실행할 명령
# if whether == "비" or whether == "눈":
#     print("우산 챙기세유")
# elif whether == "미세먼지":
#     print("마스크 쓰십쇼")
# else:
#     print("날씨굿~")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무더엉")
elif 10 <= temp and temp < 30:
    print("조와용")
elif 0 <= temp < 10:
    print("추버")
else:
    print("너무추버~")
