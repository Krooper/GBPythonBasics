def is_number_and_int(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        print("Вы ввели не число или число не целое! Повторите ввод!")
        return is_number_and_int(input())


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


# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

def nums_interval():
    # Вводим первое число:
    lower_num = is_number_and_int(input(f'Введите начало диапазона: ')) + 1

    # Вводим второе число:
    higher_num = is_number_and_int(input(f'Введите конец диапазона: '))

    # Считаем числа, которые делятся на 2 или 3 без остатка:
    counter = 0
    for num in range(lower_num, higher_num):
        if num % 2 == 0 or num % 3 == 0:
            counter += 1

    print(counter)


# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

def two_max_nums():
    # Вводим длину списка:
    list_length = is_number_and_int(input(f'Введите кол-во чисел: '))

    # Зполняем список:
    num_list = []
    for i in range(int(list_length)):
        print(f"Введите {i + 1}-й элемент массива")
        num_list.append(is_number_and_int(input()))

    # Далее можно было использовать сортировки и вывести 2 наибольших числа,
    # но это бы значительно повысило сложность (O(N^2) для сортировки пузырьком или O(N log N) для sort()),
    # поэтому решил, что лучше обойтись без сортировки, так как она тут будет избыточна

    # Это, однако, заставляет использовать некоторый костыль, а именно - ограничиваться диапазоном int-ых чисел:
    max1 = -2147483648
    max2 = -2147483648
    for i in range(len(num_list)):
        if num_list[i] >= max1 and num_list[i] >= max2:
            max2 = max1
            max1 = num_list[i]
        elif max1 >= num_list[i] >= max2:
            max2 = num_list[i]

    print(max1, max2)







#nums_interval()
two_max_nums()