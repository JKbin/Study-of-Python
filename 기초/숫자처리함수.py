# 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : xx 행 열차가 들어오고 있습니다.


station =["사당","신도림","인천공항"]

# for i in station:
#     print(f"{i}행 열차가 들어오고 있습니다.")


# 절댓값 abs()
print(abs(-5))      # 5
# 제곱 pow()
print(pow(2,10))    # 2^10 = 1024
# 최댓값 max() , 최솟값 min()
print(max(5,12))    # 12
print(min(5,12))    # 5
# 반올림 round()
print(round(3.14))  # 3
print(round(4.99))  # 5

# math 라이브러리를 모두 사용하겠다.
from math import *
# 내림 floor(), 올림 ceil(), 제곱근 sqrt()
print(floor(4.99))  # 4
print(ceil(3.14))   # 4
print(sqrt(16))     # 4.0

