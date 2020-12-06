# __init__ : 생성자
# self를 제외한 나머지 값들을 넣어줘야한다.
class Unit:
    def __init__(self, name, hp, damage):
        # 멤버 변수 : 클래스 내의 변수 (name, hp, damage)
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력{self.damage}")

#marine1 = Unit("마린", 40, 5)
#marine2 = Unit("마린", 40, 5)
#tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)     # wraith1 객체 생성
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))


# 마인드 컨트롤 스킬
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))



