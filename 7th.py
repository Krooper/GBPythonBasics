"""
Сделать программу расписание - делаем расписание занятий/тренировок или что-то своё.
Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) ,
бесконечный цикл, функции и прочий функционал.
Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать -
вывести, показать, перезаписать, добавить событие в определенный день недели
"""
import time


# Функция для создания файла со словарем расшифровки дней недели
# Существует для удобства пользователя, чтобы вводить номера, как у нас принято
def weekdays_file_creator(file='weekdays.txt'):
    week_days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда',
                 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 0: 'Воскресенье'}
    with open(file, mode='w', encoding='utf-8') as weekdays:
        for key, val in week_days.items():
            weekdays.write('{}:{}\n'.format(key, val))

    return file


# Функция для чтения созданного выше файла
def weekdays_file_reader(file='weekdays.txt'):
    week_days = {}
    with open(file, mode='r', encoding='utf-8') as weekdays:
        for i in weekdays.readlines():
            key, val = i.strip().split(':')
            week_days[key] = val

    return week_days


# Функция для получения дня недели с пользовательского ввода
# Переформатирует полученное число в формат, пригодный для структуры time
def day_getter(inp_day):
    while True:
        try:
            inp_day = int(inp_day)
            if inp_day in range(1, 6):
                time.strptime(f'{inp_day + 1}', '%w')
                inp_day = str(inp_day + 1)
                return inp_day
            elif inp_day == 6:
                time.strptime(f'{0}', '%w')
                inp_day = '0'
                return inp_day
            elif inp_day == 7:
                time.strptime(f'{1}', '%w')
                inp_day = '1'
                return inp_day
            else:
                raise ValueError
        except ValueError:
            print('Нет такого дня недели, попробуйте еще раз!')
            inp_day = input(f'Введите номер дня недели:\n"1" - Понедельник\n"2" - Вторник\n"3" - Среда'
                            f'\n"4" - Четверг\n"5" - Пятница\n"6" - Суббота\n"7" - Воскресенье\n')


# Аналогично для времени в часах и минутах
def time_getter(inp_time):
    try:
        time.strptime(inp_time, '%H:%M')
    except ValueError:
        print('Ввод неверен, попробуйте еще раз!')
        return time_getter(input(f'Введите время в формате ЧЧ:ММ\n'))

    return inp_time


# Функция собирает время и день недели, делает из них строку
# Возвращает эту строку (будет использоваться дальше как ключ другого словаря)
# Вторым элементом кортежа возвращает заполненную этим днем недели и временем структуру time
# Структура будет использоваться в дальнейшем для сравнения
def day_and_time_getter():
    inp_day = day_getter(input(f'Введите номер дня недели:\n"1" - Понедельник\n"2" - Вторник\n"3" - Среда'
                               f'\n"4" - Четверг\n"5" - Пятница\n"6" - Суббота\n"7" - Воскресенье\n'))
    week_days_dict = weekdays_file_reader(weekdays_file_creator())
    inp_time = time_getter(input(f'Введите время в формате ЧЧ:ММ\n'))

    day_and_time_struct = time.strptime(f'{inp_time} {int(inp_day)}', '%H:%M %w')
    week_day_str = week_days_dict[str(day_and_time_struct.tm_wday)]
    time_str = time.strftime("%H:%M", day_and_time_struct)
    return f'{week_day_str}, {time_str}', day_and_time_struct


# Функция для создания пустого расписания
def empty_schedule_generator():
    week_days = list(weekdays_file_reader().values())
    hours = []
    for i in range(0, 24):
        if i < 10:
            hours.append(f'0{i}:00')
        else:
            hours.append(f'{i}:00')
    schedule = {}
    for weekday in week_days:
        for hour in hours:
            schedule[f'{weekday}, {hour}'] = 'пусто'

    return schedule


# Функция для сохранения расписания в файл
# Для простоты каждый раз будем перезаписывать заново
def schedule_file_saver(schedule):
    with open("shedule.txt", mode='w', encoding='utf-8') as schedule_file:
        for key, val in schedule.items():
            schedule_file.write('{}:{}\n'.format(key, val))
    return schedule


# Функция для получения текущего расписания
def get_active_schedule(schedule):
    active_schedule = []
    [active_schedule.append(f'{key} - {value}') for key, value in schedule.items() if
        key.split(", ")[0] not in active_schedule and value != 'пусто']

    with open("active_schedule.txt", mode='w', encoding='utf-8') as active_schedule_file:
        for activity in active_schedule:
            active_schedule_file.write(f'{activity}\n')

    return active_schedule_file.name, active_schedule


# Функция для вывода текущего расписания в консоль
def print_active_schedule(schedule):
    active_schedule_file, active_schedule = get_active_schedule(schedule)
    print(f'Ваше расписание записано в файл {active_schedule_file}')
    print('Вот ваше расписание:')
    for activity in active_schedule:
        print(activity)


# Функция для добавления события в расписание
def add():

    return schedule


# Функция для изменения события в расписании
def rewrite():

    return schedule


# Функция для удаления события из расписания
def delete():

    return schedule


# Функция для выбора действия, которое хочет совершить пользователь
# Является основной функцией - зациклена и имеет возможность выхода
def input_command():
    schedule = empty_schedule_generator()
    schedule_file_saver(schedule)
    while True:
        inp_com = input(f'Введите номер действия:\n"1" - Показать расписание\n'
                        f'"2" - Добавить событие\n"3" - Редактировать событие\n'
                        f'"4" - Удалить событие\n"0" - Выход из программы\n')
        try:
            inp_com = int(inp_com)
            if inp_com == 1:
                print_active_schedule(schedule)
            elif inp_com == 2:
                new_schedule = add()
                schedule = schedule_file_saver(new_schedule)
            elif inp_com == 3:
                new_schedule = rewrite()
                schedule = schedule_file_saver(new_schedule)
            elif inp_com == 4:
                new_schedule = delete()
                schedule = schedule_file_saver(new_schedule)
            elif inp_com == 0:
                quit()
            else:
                raise ValueError
        except ValueError:
            print('Нет такой команды, попробуйте еще раз!')
            return input_command()
