NUMBERS = [
    [" _ ", "   ", " _ ", " _ ", "   ", " _ ", " _ ", " _ ", " _ ", " _ "],
    ["| |", "  |", " _|", " _|", "|_|", "|_ ", "|_ ", "  |", "|_|", "|_|"],
    ["|_|", "  |", "|_ ", " _|", "  |", " _|", "|_|", "  |", "|_|", " _|"]
]


def longer(word, times):
    return word[0] + (word[1]*times) + word[2]


def to_longer_lcd(number, timesX, timesY):
    digits = str(number)
    result = ''
    for digit in digits:
        result = result + longer(NUMBERS[0][int(digit)], timesX)
    result = result + '\n'
    for i in range(0, timesY, 1):
        for digit in digits:
            result = result + longer(NUMBERS[1][int(digit)], timesX).replace('_', ' ')
        result = result + '\n'
    for digit in digits:
        result = result + longer(NUMBERS[1][int(digit)], timesX)
    result = result + '\n'
    for i in range(0, timesY, 1):
        for digit in digits:
            result = result + longer(NUMBERS[2][int(digit)], timesX).replace('_', ' ')
        result = result + '\n'
    for digit in digits:
        result = result + longer(NUMBERS[2][int(digit)], timesX)
    return result


def to_lcd(number: int):
    digits = str(number)
    result = ''
    for digit in digits:
        result = result + NUMBERS[0][int(digit)]
    result = result + '\n'
    for digit in digits:
        result = result + NUMBERS[1][int(digit)]
    result = result + '\n'
    for digit in digits:
        result = result + NUMBERS[2][int(digit)]
    return result


def print_number(number):
    print(f'LCD number:\n{number}')


if __name__ == '__main__':
    print_number(to_longer_lcd(1234567890, 5, 2))
