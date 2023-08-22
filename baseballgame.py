from random import randint


def generate_numbers():
    numbers = [randint(0,9)]
    while len(numbers) != 3 :
        num = randint(0,9)
        if num not in numbers :
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    count = 1

    while count < 4 :
        num = int(input(f"{count}번째 숫자를 입력하세요 :"))
        if num > 9 or num < 0 :
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
        elif num in new_guess :
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else :
            new_guess.append(num)
            count += 1

    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for num_1 in range(0,3) :
        for num_2 in range(0,3) :
            if guesses[num_1] == solution[num_2] and guesses.index(guesses[num_1]) == solution.index(solution[num_2]):
                strike_count += 1
            elif guesses[num_1] == solution[num_2] :
                ball_count += 1


    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
s = 0
while s != 3 :
    guess = take_guess()
    s, b = get_score(guess,ANSWER)
    print(f"{s}S {b}B")
    tries += 1


print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")