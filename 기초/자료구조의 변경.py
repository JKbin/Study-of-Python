menu = {"커피","우유","주스"}
#print(menu,type(menu))

# 리스트로 변경
menu = list(menu)
#print(menu,type(menu))

# 튜플로 변경
menu = tuple(menu)
#print(menu,type(menu))

# 세트로 변경
menu = set(menu)
#print(menu,type(menu))

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# 출력 예제
# --당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
#-- 축하합니다--

from random import *

# id 값 1~20까지 리스트에 저장
list_id = list(range(1,21))
shuffle(list_id)
chicken_id = sample(list_id,1)
# 치킨 당첨자 발표
list_id = set(list_id)
chicken_id = set(chicken_id)
diff_id = list_id.difference(chicken_id)
diff_id = list(diff_id)
# 커피 당첨자 발표
coffee_id = sample(diff_id,3)
chicken_id = list(chicken_id)

print("--당첨자 발표--")
print(f"치킨 당첨자 : {chicken_id}")
print(f"커피 당첨자 : {coffee_id}")
print("--축하합니다--")








