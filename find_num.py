import random
ran = random.randint(1, 20)
i = 0
chance = 6

while i <= (chance-1):
    num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance-i)))
    i += 1
    if num == ran:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i))
        break
    elif num != ran:
        if num > ran:
            print("Down")
        elif num < ran:
            print("Up")
if num != ran:
    print("아쉽습니다. 정답은 {}입니다.".format(ran))
