# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 :{name}\t 나이: {age}\t",end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)


# profile("Jang",21,"파이썬","자바","C#","C++","jsp")
# profile("Kook",22,"파이썬","자바"," "," "," ")


# 가변인자 : 인자가 몇 개 들어올 지 모를 때 사용
def profile(name, age, *language):
    print(f"이름 :{name}\t 나이: {age}\t",end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("Jang",21,"파이썬","자바","C#","C++","jsp","Node js")
profile("Kook",22,"파이썬","자바")
