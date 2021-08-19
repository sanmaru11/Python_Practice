"""
for 반복문 / range
"""

# for문이 더 깔끔할 수 있음

my_list = [2, 3, 5, 7, 11]
for number in my_list: # list의 숫자들이 number라는 변수에 들어가며 for문이 실행 됨
    print(number)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

for i in range(1, 101): # range로 리스트를 더 간단히 쓸 수 있음
    print(i)

for i in range(10): # 0~9까지
    print(i)

for i in range(3, 16, 3): # range(start, stop, step) 마지막은 간격
    print(i)
