"""
3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
"""
# Перенес функцию для проверки на int с прошлого задания
def is_number_and_int(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        print("Вы ввели не число или число не целое! Повторите ввод!")
        return is_number_and_int(input())


# Можно встроенными методами и в одну строку:
def oneline_16th(number_10th):
    print(
        f'Одна строка: \
{hex(number_10th)[2:].upper()}')


# Можно циклом с использованием словаря (к нему быстро обращаться):
def cycles_16th(number_10th):
    dict_16th = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    out_16th = ''
    while number_10th > 0:
        if number_10th % 16 in range(10,16):
            out_16th = str(dict_16th[number_10th % 16]) + out_16th
        else:
            out_16th = str(number_10th % 16) + out_16th
        number_10th //= 16
    print(f'Циклы: {out_16th}')


# Можно тоже со словарем, но рекурсией:
def rec_16th(number_10th, out_16th=''):
    dict_16th = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if number_10th > 0:
        if number_10th % 16 in range(10, 16):
            out_16th = str(dict_16th[number_10th % 16]) + out_16th
        else:
            out_16th = str(number_10th % 16) + out_16th
        return rec_16th(number_10th // 16, out_16th)
    print(f'Рекурсия: {out_16th}')


number_to_convert = is_number_and_int(input(f"Введите число в десятеричной системе счисления: "))
oneline_16th(number_to_convert)
cycles_16th(number_to_convert)
rec_16th(number_to_convert)


"""
3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
"""
# Можно выяснять с помощью функции isdigit(), состоит ли строка только из цифр:
def is_float_isdigit(number):
    if number.isdigit():
        print("Число не дробное!!!")
    else:
        print("Вы ввели дробное число, ура!")


# Можно поискать точку или запятую (разделители могут быть разные):
def is_float_find(number):
    if str(number).find('.') == -1 and str(number).find(',') == -1:
        print("Число не дробное!!!")
    else:
        print("Вы ввели дробное число, ура!")


# Можно используя преобразования и try - except:
def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print("Вы ввели не число!")
        return False


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_float_check(number):
    if is_number and not is_int(number):
        print("Вы ввели дробное число, ура!")
    else:
        print("Число не дробное!!!")


num_to_check = input('Введите число: ')
is_float_isdigit(num_to_check)
is_float_find(num_to_check)
is_float_check(num_to_check)


"""
3.12 Вводим с клавиатуры строку. Необходимо развернуть подстроку между первой и последней буквой "о". 
Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
"""
def o_check(str):
    if str.find("о") == -1:
        print('буква "о" не встречается')
    elif str.find("о") == str.rfind("о"):
        print('буква "о" встречается 1 раз')
    else:
        print(str[str.find("о") + 1:str.rfind("о")])


o_check(input('Введите строку: '))
