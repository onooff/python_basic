from random import *

# 반복문 아직 안가르쳐줬으니까 안씀
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
users = range(1, 21)  # 1~20까지 들어잇는 range생성
list = list(users)
shuffle(list)

get_chicken_man = list.pop()
get_coffee_men = [list.pop(), list.pop(), list.pop()]

print("치킨맨 :", get_chicken_man)
print("커피맨 :", get_coffee_men)

print(list)
print(sample(list, 10))  # 샘플은 해도 리스트에서 값이 사라지지는 않는디
print(list)
