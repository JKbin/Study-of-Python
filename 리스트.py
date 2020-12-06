# 리스트

subway = ["유재석","조세호","박명수"]
#print(subway)

# append() : 뒤에 삽입
subway.append("하하")
#print(subway)

# insert(n,"b") : n번자리에 "b" 삽입
subway.insert(1,"정형돈")
#print(subway)

# pop() : 뒤에서 부터 제거
subway.pop()    # 하하 제거
#print(subway)
subway.pop()    # 박명수 제거
subway.pop()    # 조세호 제거
#print(subway)

subway.append("유재석")
#print(subway)
#print(subway.count("유재석")) # 2



# 정렬하기 sort()
num_list = [5,1,23,4,6,12]
num_list.sort()     # 오름차순 정렬
#print(num_list)     # [1,4,5,6,12,23]
num_list.sort(reverse=True)     # 내림차순 정렬
#print(num_list)     # [23,12,6,5,4,1]

# 뒤집기 reverse()
num_list.reverse()
#print(num_list)

# 모두 지우기 clear()
num_list.clear()
#print(num_list)

# 다양한 자료형과 함께 사용가능하다.
mix_list = ["장국빈",1, True]
#print(mix_list)

# 리스트 확장 extend()
list1 = [3,4,5,6,12,23]
list2 = ["장국빈","지누시 메이"]
list1.extend(list2)
print(list1)

