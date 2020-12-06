# # 마린 : 공격 유닛, 군인, 총을 쏜다.

# # 탱크 : 공격 유닛, 탱크, 포를 쏜다, 일반 모드 / 시즈모드가 있다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력{self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
