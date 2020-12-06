# 지역변수 : 함수 내에서만 사용할 수 있는 변수
# 전역변수 : 모든 부분에서 사용할 수 있는 변수
# 일반적으로 지역변수로 사용한다.
gun = 10

def checkpoint(soldiers):
    global gun # 전역 변수인 gun을 사용하겠다.
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))

