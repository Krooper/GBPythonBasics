"""
Сделать программу расписание - делаем расписание занятий/тренировок или что-то своё.
Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) ,
бесконечный цикл, функции и прочий функционал.
Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать -
вывести, показать, перезаписать, добавить событие в определенный день недели
"""
import time
import os


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
def day_and_time_getter():
    inp_day = day_getter(input(f'Введите номер дня недели:\n"1" - Понедельник\n"2" - Вторник\n"3" - Среда'
                               f'\n"4" - Четверг\n"5" - Пятница\n"6" - Суббота\n"7" - Воскресенье\n'))
    week_days_dict = weekdays_file_reader(weekdays_file_creator())
    inp_time = time_getter(input(f'Введите время в формате ЧЧ:ММ\n'))

    day_and_time_struct = time.strptime(f'{inp_time} {int(inp_day)}', '%H:%M %w')
    week_day_str = week_days_dict[str(day_and_time_struct.tm_wday)]
    time_str = time.strftime("%H:%M", day_and_time_struct)

    return f'{week_day_str}, {time_str}'


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
def save_schedule(schedule):
    with open("schedule.txt", mode='w', encoding='utf-8') as schedule_file:
        for day_and_time, activity in schedule.items():
            schedule_file.write('{} - {}\n'.format(day_and_time, activity))

    return schedule_file.name


# Функция для получения общего расписания из файла
def get_schedule(file='schedule.txt'):
    schedule = {}
    with open(file, mode='r', encoding='utf-8') as schedule_file:
        for i in schedule_file.readlines():
            day_and_time, activity = i.strip().split(' - ')
            schedule[day_and_time] = activity

    return schedule


# Функция для получения текущего расписания из общего
def get_active_schedule_first(schedule):
    active_schedule_lst = []
    [active_schedule_lst.append(f'{key} - {value}') for key, value in schedule.items() if
        key.split(", ")[0] not in active_schedule_lst and value != 'пусто']

    active_schedule = {}
    for event in active_schedule_lst:
        day_and_time, activity = event.strip().split(' - ')
        active_schedule[day_and_time] = activity

    return active_schedule


# Функция для получения текущего расписания из файла
def get_active_schedule():
    active_schedule = {}
    with open('active_schedule.txt', mode='r', encoding='utf-8') as active_schedule_file:
        for i in active_schedule_file.readlines():
            day_and_time, activity = i.strip().split(' - ')
            active_schedule[day_and_time] = activity

    return active_schedule


# Функция для сохранения текущего расписания в файл
def save_active_schedule(active_schedule):
    with open("active_schedule.txt", mode='w', encoding='utf-8') as active_schedule_file:
        for day_and_time, activity in active_schedule.items():
            active_schedule_file.write('{} - {}\n'.format(day_and_time, activity))

    return active_schedule_file.name


# Функция для вывода текущего расписания в консоль
def print_active_schedule():
    active_schedule_file = save_active_schedule(get_active_schedule())
    active_schedule = get_active_schedule()
    print(f'Ваше расписание записано в файл {active_schedule_file}')
    print('Вот ваше расписание:')
    for day_and_time, activity in active_schedule.items():
        print(f'{day_and_time} - {activity}')


# Функция для добавления события в расписание
def add():
    inp_day_and_time = day_and_time_getter()
    active_schedule = get_active_schedule()
    if inp_day_and_time in active_schedule.keys():
        print('Это время уже занято!')
        return
    else:
        activity = input(f'Событие: ')
        active_schedule[inp_day_and_time] = activity
        save_active_schedule(active_schedule)

        schedule = get_schedule()
        schedule[inp_day_and_time] = activity
        save_schedule(schedule)

        print('Успешно!')
    return


# Функция для изменения события в расписании
def rewrite():
    print('Введите день и время для редактирования события')
    inp_day_and_time = day_and_time_getter()
    active_schedule = get_active_schedule()
    if inp_day_and_time in active_schedule.keys():
        activity = input(f'Событие: ')
        active_schedule[inp_day_and_time] = activity
        save_active_schedule(active_schedule)

        schedule = get_schedule()
        schedule[inp_day_and_time] = activity
        save_schedule(schedule)

        print('Успешно!')
        return
    print('Такого события нет!')
    return


# Функция для удаления события из расписания
def delete():
    print('Введите день и время для удаления события')
    inp_day_and_time = day_and_time_getter()
    active_schedule = get_active_schedule()
    if inp_day_and_time in active_schedule.keys():

        active_schedule[inp_day_and_time] = 'пусто'
        save_active_schedule(active_schedule)

        schedule = get_schedule()
        schedule[inp_day_and_time] = 'пусто'
        save_schedule(schedule)

        print('Успешно!')
        return
    print('Такого события нет!')
    return


# Функция для выбора действия, которое хочет совершить пользователь
# Является основной функцией - зациклена и имеет возможность выхода
def input_command():
    weekdays_file_creator()
    if not os.path.exists('active_schedule.txt'):
        save_active_schedule(get_active_schedule_first(get_schedule(save_schedule(empty_schedule_generator()))))

    while True:
        inp_com = input(f'Введите номер действия:\n"1" - Показать расписание\n'
                        f'"2" - Добавить событие\n"3" - Редактировать событие\n'
                        f'"4" - Удалить событие\n"0" - Выход из программы\n')
        try:
            inp_com = int(inp_com)
            if inp_com == 1:
                save_active_schedule(get_active_schedule_first(get_schedule()))
                print_active_schedule()
            elif inp_com == 2:
                add()
            elif inp_com == 3:
                rewrite()
            elif inp_com == 4:
                delete()
            elif inp_com == 0:
                quit()
            else:
                raise ValueError
        except ValueError:
            print('Нет такой команды, попробуйте еще раз!')
            return input_command()


input_command()

