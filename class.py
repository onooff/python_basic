class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 다중상속시는 super 사용 제한됨(맨 앞 부모클래스 한개만 호출된다)
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()
