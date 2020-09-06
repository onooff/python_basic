# 셋 ; 중복 없고 순서 없음
# list[] dict{key:value} tuple() set{}

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}  # 셋선언1
python = set(["유재석", "박명수"])  # 셋선언2

# 셋끼리 교집합 확인
print(java & python)
print(java.intersection(python))

# 합집합 확인
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 할줄아는사람추가(값추가)
python.add("김태호")

# java 까먹음(값삭제)
java.remove("김태호")

print(python)
print(java)
