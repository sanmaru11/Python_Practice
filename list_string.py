alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J']
alphabet_string = 'ABCDEFGHIJ'

# 리스트, 문자열 모두 인덱싱 가능
print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_string[0])
print(alphabet_string[3])

print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_string[0:5])
print(alphabet_string[4:])

# 둘다 덧셈연산 가능
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

# len 함수 사용 가능
my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello world!'
print(len(my_string))

# 리스트는 수정할 수 있지만 문자열은 수정할 수 없음
numbers = [1, 2, 3, 4]
numbers[0] = 'C'
print(numbers)


# name = 'codeit'
# name[0] = 'C'
# print(name)

