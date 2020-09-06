# 피클이 뭔가? 프로그램상에서 사용하는 데이터를 파일로 저장?
import pickle
# profile_file = open("profile.pickle", "wb") #피클은 인코딩 필요없지만 타입에 b필요 binary?
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close

# with 는 close 자동으로 됨
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
