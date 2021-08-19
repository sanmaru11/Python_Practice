# 사전 (dictionary)
# key-value pair
# key: value,

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionary)) # dict 사전 자료형

print(my_dictionary[3]) # key 3 에 있는 값 출력

my_dictionary[9] = 81 # 9라는 key에 81 이라는 값 저장
print(my_dictionary)

"""
리스트와의 차이점 
리스트는 인덱스가 순서대로 0, 1, 2 진행, 정수값이어야 함
사전은 순서 개념이 없음, 사전의 key는 정수가 아니어도 됨
"""

my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}
print(my_family)

# 사전 목록 불러오기
print(my_family.values())
print('이지영' in my_family.values()) # 이지영이라는 값이 사전에 있는지 확인
print('성태호' in my_family.values())

for value in my_family.values():
    print(value)

# 값 대신 key 목록을 가져올 때
print(my_family.keys())

for key in my_family.keys():
    print(key)

# 둘 다 불러올 때
for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)