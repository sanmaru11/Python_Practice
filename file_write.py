# 'w' 는 덮어쓰기, 'a'는 추가

with open('new_file.txt', 'w', encoding='UTF-8') as f:
    f.write("Hello World!\n")
    f.write("My name is Codeit\n")