# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()

# 전달값 , 반한값
# def 함수명(전달값)
def deposit(balance,money):
    print("입급이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money

def withdraw(balance,money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance,money):
    commision = 100
    return commision, balance-money-commision




balance = 0
balance = deposit(balance,10000)
#balance = withdraw(balance,12000)
commision, balance = withdraw_night(balance,500)
print("수수료는 {0}원이고, 잔액은 {1}원 입니다.".format(commision,balance))



