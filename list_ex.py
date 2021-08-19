numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# 리스트 정렬

new_list = sorted(numbers) # 작은숫자부터 정렬
print(new_list)
print(numbers) # 기존의 리스트가 나옴, 기존의 리스트를 건드리지 않음

new_list_2 = sorted(numbers, reverse=True) # 반대로 정렬
print(new_list_2)

print(numbers.sort()) # sort는 아무것도 return 하지 않음 대신 numbers 리스트 자체를 정렬
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
