# split

my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))  # 문자열이 .을 기준으로 나뉨
print(my_string.split(". ")) # 문자열이 . 을 기준으로 나뉨

full_name = "Kim, Yuna"
print(full_name.split(", "))

print("     \n\n   2   \t  3 \n  5 7 11 \n\n".split())

# 문자형으로 저장됨
numbers = "     \n\n   2   \t  3 \n  5 7 11 \n\n".split()
print(numbers[0] + numbers[1])
print(int(numbers[0]) + int(numbers[1]))