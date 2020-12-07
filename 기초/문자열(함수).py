a = "Python is Amazing"

# lower() : 소문자로 변환
#print(a.lower())
# upper() : 대문자로 변환
#print(a.upper())

# isupper() : 인덱스 자리의 값이 대문자인지 확인해주는 함수
#print(a[0].isupper())   # P > True
#print(a[3].isupper())   # h > False
# islower() : 인덱스 자리의 값이 소문자인지 확인해주는 함수
#print(a[10].islower())   # A > False
#print(a[3].islower())   # h > True

# len() : 문자열의 길이를 알려주는 함수
#print(len(a))       # 17
# replace() : 문자열을 찾아서 바꿔주는 함수
#print(a.replace("Python","Java"))   # Java is Amazing

# index() : 값이 몇번째에 있는지? 만약 값이 없으면 error 발생
#print(a.index("n"))         # 5, 15가 있는 첫번째 값의 index를 찾아준다. 5번째
#print(a.index("n",6))       # 6번째부터 시작해서 n의 index를 찾아준다. 15번째

# find() : index()와 비슷하지만 만약 찾을 문자가 없으면 -1을 return 한다.
# print(a.find("A"))      # 10
# print(a.find("l"))      # -1
# print(a.find("java"))   # -1

# count() : 개수를 반환하는 함수
print(a.count("A"))       # 1
