import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름":"Jang","나이":28,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file)   # profile에 있는 정보를 file에 저장
profile_file.close()