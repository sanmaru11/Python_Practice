def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 1
    new_guess = []
    while len(new_guess) < 3:
        number = input(str(i) + "번째 숫자를 입력하세요: ")
        if int(number) >= 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            number = input(str(i) + "번째 숫자를 입력하세요: ")
            i += 1
        else:
            if int(number) not in new_guess:
                new_guess.append(int(number))
                i += 1
            else:
                print("중복되는 숫자입니다. 다시 입력하세요.")
                number = input(str(i) + "번째 숫자를 입력하세요: ")
                new_guess.append(int(number))
                i += 1
    return new_guess

print(take_guess())