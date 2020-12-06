# \n : 줄바꿈
#print("백문이 불여일견 \n백견이 불여일타")

# 저는 "장국빈"입니다.
#print("저는 \"장국빈\"입니다.")
#print("C:\\Users\\JKbin\\Desktop\\Python Practice")

# \r : 커서를 맨 앞으로 이동
#print("Red Apple\rPine")    # PineApple
# \b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")        # RedApple
# \t : tap 역할
#print("Red\tApple")         # Red   Apple




# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#           nav                  + 5        +       1          + !
# 예) 생성된 비밀번호 : nav51!

#a = "http://naver.com"
a = "http://daum.net"
b = a[7:]   #  b = naver.com
c = b.find(".") # c = 5
d = b[:c]       # naver

e = d[:3]   # nav
f = len(d)   # 5
g = d.count("e") # 1
h = '!' # !
print(f"생성된 비밀번호 : {e}{f}{g}{h}")