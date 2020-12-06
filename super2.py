class Unit:
    def __init__(self):
        print("Unit 생성자")

class flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, flyable):
    def __init__(self):
        # super를 사용하면 맨 처음 상속받은 class의 생성자만 생성된다.
        # super().__init__()
        Unit.__init__(self)
        flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()