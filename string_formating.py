"""
문자열 포맷팅
"""

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
# 중괄호로 닫고 .format 뒤에 중괄호에 들어갈 변수 넣기

# 문자열을 변수에 저장하여 사용
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print(date_string.format(year, month, day + 1))

print("저는 {}, {}, {}룰 좋아합니다".format("박지성", "유재석", "빌 게이츠"))
# 순서를 중괄호안에 써주면 순서가 결정됨
print("저는 {1}, {0}, {2}룰 좋아합니다".format("박지성", "유재석", "빌 게이츠"))


num_1 = 1
num_2 = 3

print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1/num_2))
# 소수점 자리를 결정하고싶으면 :.xf를 붙임
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
# 정수형으로 바꾸고 싶으면 :.0f를 사용
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1/num_2))


