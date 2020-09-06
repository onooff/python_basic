# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

menu = dict(menu)  # ??
print(menu, type(menu))
menu = list(menu)  # dict를 리스트로 변경시 키값만 넘어옴
print(menu, type(menu))
