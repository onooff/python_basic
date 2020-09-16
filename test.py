# # 문자열 특정인덱스 교체 되는가
# string = "abcdefg"
# # string[2] = '%'
# print(string[2])
# print(string)


# # 문자열 특정 인덱스 없애기
# string = "abcdefg"  # 길이7
# remove = 2
# string = string[:remove]+string[remove+1:]
# print(string)

# string = "abcdefg"  # 길이7
# remove = 6
# string = string[:remove]+string[remove+1:]
# print(string)

# 리스트끼리 정렬 = 된다
test = [[0, 1, 2], [0, 1, 1], [0, 0, 1]]
test.sort()
print(test)
