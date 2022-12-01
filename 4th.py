from random import randint
"""
1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
# Для отбора элементов на нечетных индексах можно использовать цикл:
def odds_sum_for(nums):
    sum_odd = 0
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            sum_odd += nums[i]
    return sum_odd


# Для отбора элементов на нечетных индексах использовать генератор с ф-ями enumerate и sum:
def odds_sum_enum(nums):
    return sum([value for key, value in enumerate(nums) if key % 2])


# Список сделаем с помощью генератора:
test_list = [i for i in range(10)]
print(test_list)
# Убедимся, что результаты совпадают:
print(odds_sum_for(test_list))
print(odds_sum_enum(test_list))


"""
2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
"""
# Перенес функцию для проверки на int с прошлого задания
# (будем заполнять двумерный массив с помощью ввода через консоль):
def is_number_and_int(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        print("Вы ввели не число или число не целое! Повторите ввод!")
        return is_number_and_int(input())


def average(arr):
    for i in range(len(arr)):
        row_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
        row_av_sum = row_sum/len(arr[i])
        print(f'Среднее арифметическое {i+1}-й строки: {row_av_sum}')


# Список сделаем с помощью генератора:
a = is_number_and_int(is_number_and_int(input(f'Введите кол-во столбцов: ')))
b = is_number_and_int(is_number_and_int(input(f'Введите кол-во строк: ')))
test_matrix = [[is_number_and_int(input(f'{j+1}-й элемент {i+1}-й строки: ')) for j in range(a)] for i in range(b)]
# Выведем результаты:
average(test_matrix)


"""
3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
"""
def choice_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr


def list_gen():
    arr = []
    for i in range(30):
        arr.append(randint(1, 99))
    return arr


test_list = list_gen()
print(f'Неотсортированный список: {test_list}')
print(f'Отсортированный список: {choice_sort(test_list)}')
