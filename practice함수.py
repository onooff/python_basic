# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):
#     print("입금 완료. 잔액 {0}원".format(balance+money))
#     return balance+money


# def withdraw(balance, money):
#     if balance >= money:
#         print("출금 완료. 잔액 {0}원".format(balance-money))
#         return balance-money
#     else:
#         print("잔액 부족. 잔액 {0}원".format(balance))
#         return balance


# def withdraw_night(balance, money):
#     commission = 100  # 수수료 100원
#     return commission, balance-money-commission


# b = 0
# b = deposit(b, 1000)
# # b = withdraw(b, 5000)
# # b = withdraw(b, 500)
# c, b = withdraw_night(b, 500)
# print(b)
# print("수수료 {0}원, 잔액 {1}원".format(c, b))

##################################################################
# # 함수 기본값 설정
# def profile(name, age, main_lang):
#     print("이름:{0}  나이:{1}  주력언어:{2}".format(name, age, main_lang))


# profile("유재석", 10, "파이썬")
# profile("김태호", 15, "자바")


# def profile_default(name, age=17, main_lang="파이썬"):
#     print("이름:{0}  나이:{1}  주력언어:{2}".format(name, age, main_lang))


# profile_default("유재석")
# profile_default("김태호")

################################################################
# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")
#가변 인자###############################################################
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름:{0}  나이:{1}  ".format(name, age), end="")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *lang):
#     print("이름:{0}  나이:{1}  ".format(name, age), end="")
#     for l in lang:
#         print(l, end=" ")
#     print()


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Go")
# profile("김태호", 23, "Kotlin", "Swift")


#지역변수,전역변수###############################################################
gun = 10  # 전역변수


def checkpoint(soldiers):  # 경계근무
    # gun = 15 # 지역변수
    global gun  # 함수내에서 전역변수 사용하겠다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 두명 근무투입
gun = checkpoint_ret(gun, 2)  # 두명 근무투입
print("전체 총 : {0}".format(gun))
