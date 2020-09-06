from random import *

ox = ""
time = 0
count = 0
for guest in range(1, 51):
    time = randrange(5, 51)
    if time <= 15:
        ox = "O"
        count += 1
    else:
        ox = " "
    print(f"[{ox}] {guest}번째 손님 (소요시간 : {time}분)")

print(f"\n총 탑승 승객 : {count} 분")
