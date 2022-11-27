def is_number_and_int(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Вы ввели не число или число не целое!")
        return False


def is_integer(number):
    if number.isdigit():
        return True
    else:
        print("Вы ввели дробное число!")
        return False


def positive(number):
    if number[0] == '-':
        print("Отрицательное число преобразовано в положительное.")
        return number[1:]
    else:
        return number


## 1) Вводим с клавиатуры целое число X и У.
## Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

def nums_interval():
    lower_num = input(f'Введите начало диапазона: ')
    while not is_number_and_int(lower_num):
        lower_num = input(f'Введите начало диапазона: ')
    lower_num = int(lower_num) + 1

    higher_num = input(f'Введите конец диапазона: ')
    while not is_number_and_int(higher_num):
        higher_num = input(f'Введите начало диапазона: ')
    higher_num = int(higher_num)

    counter = 0
    for num in range(lower_num, higher_num):
        if num % 2 == 0 or num % 3 == 0:
            counter += 1

    print(counter)


nums_interval()