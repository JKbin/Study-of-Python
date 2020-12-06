# dictionary
# key와 value 형태의 자료형
# key는 중복이 안된다.

cabinet = {3:"유재석",100:"김태호"}
#print(cabinet[3])
#print(cabinet.get(3))
#print(cabinet.get(5)) # 값이 없으면 none
#print(cabinet.get(5,"디폴트값"))    # 5가 없으면 디폴트값 출력
#print(cabinet[100])
#print(3 in cabinet)     # True
#print(5 in cabinet)     # False

# key 추가
cabinet = {"A-3":"유재석","B-100":"김태호"}
#print(cabinet)
cabinet["A-3"] = "김종국"       # Update
cabinet["C-20"] = "조세호"      # Insert
#print(cabinet)

# key 제거
#print(cabinet)
del cabinet["A-3"]
#print(cabinet)

# key 들만 출력     keys()
print(cabinet.keys())
# Value 들만 출력   values()
print(cabinet.values())
# key, Value 쌍으로 출력    items()
print(cabinet.items())
print(cabinet)

# 모든 값 제거
cabinet.clear()
print(cabinet)
