numbers = []
# 리스트의 가장 오른쪽에 값을 추가 append
numbers.append(5)
numbers.append(8)
print(numbers)

# 리스트에 값이 몇개가 있는지 확인 len()
print(len(numbers))

numbers_1 = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트의 요소를 지우고 싶을 때 del
del numbers_1[3] # 3번 인덱스 삭제
print(numbers_1)

# 요소를 원하는 위치에 삽임
numbers_1.insert(4, 37) # 4번 인덱스에 37 추가
print(numbers_1)

