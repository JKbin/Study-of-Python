# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# *표준 체중 : 각 개인의 키에 적당한 체중

#(성별에 따른 공식)
# 남자 : 키(m) x 키(x) x 22
# 여자 : 키(m) x 키(x) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산   > 지역변수 사용
#           * 함수명 : std_weight
#           * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height,gender):
#     weight = 0
#     if gender == 'M':
#         weight = (height*height)*22
#         print("키 {0}cm 남자의 표준 체중은 {1}입니다.".format(height,weight))
#     elif gender == 'F':
#         weight = (height*height)*21
#         print("키 {0}cm 여자의 표준 체중은 {1}입니다.".format(height,weight))
#     return weight

# std_weight(175,'M')
# std_weight(162,'F')


# 풀이
def std_weight(height,gender):  # 키는 m단위(실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175    # cm
gender = "남자"
weight = round(std_weight(height / 100 ,gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))




