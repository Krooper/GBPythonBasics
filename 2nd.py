def is_number_and_int(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        print("Вы ввели не число или число не целое! Повторите ввод!")
        return is_number_and_int(input())


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
    if list_length == 0:
        return

    # Зполняем список:
    # num_list = []
    # for i in range(int(list_length)):
    #     print(f"Введите {i + 1}-й элемент массива")
    #     num_list.append(is_number_and_int(input()))

    # Далее можно было использовать сортировки и вывести 2 наибольших числа,
    # но это бы значительно повысило сложность (O(N^2) для сортировки пузырьком или O(N log N) для sort()),
    # поэтому решил, что лучше обойтись без сортировки, так как она тут будет избыточна

    # Это, однако, заставляет использовать некоторый костыль, а именно - ограничиваться диапазоном int-ых чисел:
    # max1, max2 = -2147483648, -2147483648
    # for i in range(len(num_list)):
    #     if num_list[i] >= max1 and num_list[i] >= max2:
    #         max2 = max1
    #         max1 = num_list[i]
    #     elif max1 >= num_list[i] >= max2:
    #         max2 = num_list[i]

    # В принципе в целях экономии ресурсов (понижение сложности и отсутсвие списка),
    # можно вообще обойтись без списка и сделать всё в одном цикле:

    max1, max2 = -2147483648, -2147483647
    for i in range(int(list_length)):
        num = is_number_and_int(input(f"Введите {i + 1}-е число: "))
        if num >= max1 and num >= max2:
            max2 = max1
            max1 = num
        elif max1 >= num >= max2:
            max2 = num

    print(f"2 максимальных числа: {max1, max2}")


# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

def salary_bill_calc():
    # Вводим зарплату:
    salary = is_number_and_int(input(f'Введите зарплату: '))

    # Создаем счетчики для купюр:
    count_25, count_10, count_3, count_1 = 0, 0, 0, 0

    # Начинаем считать:
    count_25 = salary // 25
    salary %= 25

    count_10 = salary // 10
    salary %= 10

    count_3 = salary // 3
    salary %= 3

    count_1 = salary // 1
    salary %= 1

    print(f'Минимальное кол-во купюр: {count_25+count_10+count_3+count_1}')
    print(f'Кол-во купюр номиналом 25 руб: {count_25}')
    print(f'Кол-во купюр номиналом 10 руб: {count_10}')
    print(f'Кол-во купюр номиналом 3 руб: {count_3}')
    print(f'Кол-во купюр номиналом 1 руб: {count_1}')


# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо
# упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

def sequence_order():
    # Вводим число:
    num_seq = is_number_and_int(input(f'Введите число: '))

    # Сразу сделаю в одном цикле и без списка:
    for i in range(len(str(num_seq))):
        if i == 0:
            max = num_seq % 10
            num_seq //= 10
        else:
            if max > num_seq % 10:
                max = num_seq % 10
                num_seq //= 10
            else:
                return False
    return True


#nums_interval()
#two_max_nums()
#salary_bill_calc()
if sequence_order():
    print('Да')
else:
    print('Нет')
