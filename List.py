# 인덱스 (index)
# 변수에 값을 여러개 저장 하고 싶을 때

numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]
# 리스트의 값들을 요소라고 부름

print(numbers)
print(names)

# 인덱싱 (indexing)
# 요소의 위치를 인덱스, 인덱스를 통해 요소를 받아오는걸 인덱싱이라고 함
print(names[1])  # 인덱스는 0부터 시작하기 때문에 혜린이 나옴
print(numbers[1] + numbers[3])
num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)
# print(numbers[6]) 인덱스가 리스트의 범위에서 벗어나 오류가 남
print(numbers[-1]) # 뒤에서 1번째
print(numbers[-2])  # 뒤에서 2번째

# 리스트 슬라이싱 (list slicing)
print(numbers[0:4]) # 인덱스 0부터 3까지 잘라서 출력
print(numbers[2:]) # 2부터 마지막 까지
print(numbers[:3]) # 처음부터 2까지

new_list = numbers[:3] # [2, 3, 5]
print(new_list[2])

numbers[0] = 7 # 7을 0의 자리에 저장
print(numbers)

numbers[0] = numbers[0] + numbers[1]
print(numbers)

