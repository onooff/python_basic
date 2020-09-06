for i in range(1, 51):
    with open(f"./file_out/{i}주차.txt", "w", encoding="utf8") as file:
        file.write(f"- {i} 주차 주간보고 -\n")
        file.write("부서 :\n")
        file.write("이름 :\n")
        file.write("업무 요약 :")
