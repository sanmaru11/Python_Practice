# 상수 (constant)
# 상수는 이름을 지을 때 대문자를 쓰는 규칙이 있음
# 동작엔 아무런 영향 없고 알아보기 쉽게 하기 위함
# 수정하지 않겠다는 의미

PI = 3.14


# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))