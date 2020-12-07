# import travel.thailand
# trip_to = travel.thailand.ThialndPackage()
# trip_to.detail()

#                               클래스명
# from travel.thailand import ThialndPackage
# trip_to = ThialndPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThialndPackage()
# trip_to.detail()

# 모듈의 위치찾기
import inspect
import random
print(inspect.getfile(random))
#print(inspect.getfile(vietnam))

