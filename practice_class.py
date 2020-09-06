# # 스타크래프트를 예로 들어 설명함
# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "marine"  # 유닛 이름
# hp = 40  # 유닛 체력
# damage = 5  # 유닛 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")

# # 탱크 : 공격 유닛, 탱크, 포을 쏠 수 있음, 일반/시즈모드
# tank_name = "tank"  # 유닛 이름
# tank_hp = 150  # 유닛 체력
# tank_damage = 35  # 유닛 공격력

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")


# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}\n")


# marine1 = Unit("마린", 40, 5)
# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 3
# 멤버변수
# 레이스 : 공중유닛 클로킹 가능
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True  # 객체에 멤버변수 확장 가능

# if wraith2.clocking == True:
#     print(f"{wraith2.name}는 현재 클로킹 상태입니다.")

########################################################
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : 데미지를 {damage} 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
