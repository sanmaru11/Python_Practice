x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)
# 같은 리스트에 x, y 두개의 이름표가 있기 때문에 x, y 는 같은 리스트를 출력함
# y 는 x의 가명(alias) 라고 함

x = [2, 3, 5, 7, 11]
y = list(x)  # list(x)는 리스트를 복사하는 역할
y[2] = 4
print(x)
print(y)