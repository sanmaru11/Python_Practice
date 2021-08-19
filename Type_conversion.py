"""
형 변환
"""

# int (integer) 정수형 변환
print(int(3.8)) # 소수형을 정수형으로 변환
print(int("2") + int("5")) # 문자형을 정수형으로 변환



# float (floating point) 소수형 변환
print(float(3)) # 정수형을 소수형으로 변환
print(float("1.1") + float("2.5")) # 문자형을 소수형으로 변환

# str (string) 문자형 변환
print(str(3) + str(5)) # 정수형을 문자형으로 변환

age = 7
# print("제 나이는" + age + "살입니다.") -> 오류 str과 int를 연결할 수 없음
print("제 나이는 " + str(age) + "살입니다.") # int형인 age를 문자형으로 바꾸어주어야 함

