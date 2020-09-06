# 리스트[]

# # ex) 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 박명수 몇번째칸??
# print(subway.index("박명수"))

# # 하하가 탑승
# subway.append("하하")
# print(subway)

# # 정형돈이 유재석,조세호사이에 탑승
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철 사람들 뒤에서부터 한명씩 내림 pop
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# # 정렬
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()
# print(num_list)

num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]  # 리스트에 여러가지 타입 넣을 수 있따?!!?
print(mix_list)

num_list.extend(mix_list)  # 리스트 합치기
print(num_list)
