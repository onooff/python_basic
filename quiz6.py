def std_weight(height, gender):
    ret = 0
    if gender == "남자":
        ret = (height/100)*(height/100)*22
    elif gender == "여자":
        ret = (height/100)*(height/100)*21
    else:
        return
    print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, round(ret, 2)))


std_weight(175, "남자")
