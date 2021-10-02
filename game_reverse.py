import random


def game_reverse():
    min_number = 1
    max_number = 100
    result = None
    while result != '=':
        number = random.randint(min_number, max_number)
        print(number)
        result = input('= > (Загаданное число больше Вашего) < (загаданное число меньше Вашего)')
        if result == '>':
            min_number = number + 1
        elif result == '<':
            max_number = number - 1

    print('Победа!')


if __name__ == '__main__':
    game_reverse()
