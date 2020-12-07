# 자식클래스에서 정의한 메서드를 쓰고싶을 때
# Unit의 기본정보 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

# 공격할 수 있는 Unit 클래스
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        #self.name = name
        #self.hp = hp
        Unit.__init__(self, name, hp, speed)   # Unit의 name과 hp를 상속받음.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 : {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. 속도 [{self.flying_speed}]")

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        # 초기화
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

    # 메서드 오버라이딩 move 함수를 재정의 하였다.
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
# 배틀크루저 : 공중 공격 유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 메서드 오버라이딩 전
#vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")

# 메서드 오버라이딩 후
vulture.move("11시")
battlecruiser.move("9시")
