# print("Python", "java",sep=",") #Python,java

# # 문장의 끝 부분을 end값으로 받고 뒤에 있는 값이 연달아서 출력된다.
# print("Python", "java", sep=",", end="?") #Python,java?
# print("무엇이 더 재밌을까요?")


# import sys
# print("Python","Java", file=sys.stdout)
# print("Python","Java", file=sys.stderr)


# ljust(8) : 8칸을 확보하고 왼쪽부터 정렬
# rjust(4) : 4칸을 확보하고 오른쪽부터 정렬
# score = {"수학":0, "영어":50, "코딩":100}
# for subject, score in score.items():
#     #print(subject,score)
#     print(subject.ljust(8), str(score).rjust(4),sep=":")
#     #print(subject, str(score).rjust(4))


# 은행 대기순번표
# 001, 002, 003, ...
# zfill : 3자리를 확보하고 빈 자리는 0으로 채운다.
# for num in range(1,21):
#     #print("대기번호 : " + str(num).zfill(3))
#     print(f"대기번호 : {str(num).zfill(3)}")


# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # 이렇게 입력하면 str값으로 받는다.
print("입력하신 값은 {0}입니다.".format(answer))

