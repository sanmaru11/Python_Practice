# 'r' 은 read
# 같은 파일에 있으면 파일명만 쓰고 다른 파일에 있다면 '파일/파일명' 이라고 작성
# f 라는 변수에 저장
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

# strip 공백 제거
print("          abc       def    ".strip()) # 앞뒤 공백 제거
print("   \t    \n   abc       def\n\n\n".strip())
