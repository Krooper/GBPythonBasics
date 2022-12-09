"""
В общем, изначально задумка была совсем эпохальная, но понял, что потрачу слишком много времени на
проверку того, правильно ли расставлены корабли (проверка, есть ли на пути у "нового" корабля при расстановке старый,
расположены ли корабли рядом и т.п. что можно было бы сделать через рекурсию).
Поэтому решил этот момент оставить на проверку игрокам (надеемся на честность, как в жизни :) ).
Еще сначала думал сделать каждый корабль определенной длины дочерним классом от родительского класса Ship.
Так бы можно было сделать проверку, сколько кораблей у какого игрока осталось в игре.
В итоге тоже пошел по пути упрощения - просто смотрим, есть ли еще поля, занятые кораблями.
Подытоживая: нет многих проверок, простенький и корявенький (особенно в функции game()) код, корабли можно расположить
только горизонтально, но играть, если игроки не подглядывают, можно :)
Просто дальнейшая работа требовала слишком много времени, которого, к сожалению, не хватает.
В общем, получилось небольшое упражнение на ООП и циклы.
"""
# Функция для процесса игры:
def game():
    Player1 = Player('Миша')
    Player2 = Player('Саша')

    Map1, Map2, Map3, Map4 = game_start(Player1, Player2)

    while True:
        if Map1.loose_check() and Map2.loose_check():
            check1, fire_coord, Map2, Map3 = player_hit(Player1, Map2, Map3)
            Map2.game_coordinates[fire_coord], Map3.empty_coordinates[fire_coord] = 'o', 'o'
            if Map2.loose_check():
                check2, fire_coord, Map1, Map4 = player_hit(Player2, Map1, Map4)
            else:
                break
            Map1.game_coordinates[fire_coord], Map4.empty_coordinates[fire_coord] = 'o', 'o'
        else:
            break


# Функция для инициализации карт для игры:
def game_start(player1, player2):
    Map1 = SeaMap(player1)
    Map2 = SeaMap(player2)

    Map1.empty_coordinates = Map1.set_map_coord()
    Map2.empty_coordinates = Map2.set_map_coord()

    Map1.filled_coordinates = Map1.place_ships(player1)
    Map2.filled_coordinates = Map2.place_ships(player2)

    print(f'{player1.name}, вот твоя карта:')
    print_map(Map1.filled_coordinates)
    Map1.game_coordinates, Map1.filled_coordinates = Map1.coord_check(player1)

    print(f'{player2.name}, вот твоя карта:')
    print_map(Map2.filled_coordinates)
    Map2.game_coordinates, Map2.filled_coordinates = Map2.coord_check(player2)

    Map3 = SeaMap(player1)
    Map4 = SeaMap(player2)
    Map3.empty_coordinates = Map3.set_map_coord()
    Map4.empty_coordinates = Map4.set_map_coord()

    return Map1, Map2, Map3, Map4


# Функция в случае попадания по кораблю:
def player_hit(player, enemy_map, my_enemy_map):
    check, coord = player.fire(enemy_map, my_enemy_map)
    if check:
        enemy_map.game_coordinates[coord] = 'x'
        my_enemy_map.empty_coordinates[coord] = 'x'
        while check and enemy_map.loose_check():
            check, coord = player.fire(enemy_map, my_enemy_map)
            enemy_map.game_coordinates[coord] = 'x'
            my_enemy_map.empty_coordinates[coord] = 'x'
        else:
            quit()

    return check, coord, enemy_map, my_enemy_map


# Функция для заполнения координат кораблями:
def place_ship(player, coords, start_coord, count):
    # Ставим столько 's', сколько надо в зависимости от длины корабля:
    for _ in range(player.ships[count - 1]):
        coords[start_coord] = 's'
        start_coord = f'{start_coord[0]}{int(start_coord[1]) + 1}'
    return coords


# Функция для печати карты:
def print_map(coords):
    coord_x = [chr(j) for j in range(ord('a'), ord('k'))]
    for i in range(len(coord_x)):
        out_str = ''
        for j in range(1, 11):
            elem = f"{coord_x[i]}{j}"
            out_str += f'{coords[elem]}  '
        if out_str is not None:
            print(out_str)


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    # Метод для стрельбы:
    def fire(self, enemy_seamap, field_seamap):
        # Сначала выведем игроку скрытое поле врага:
        print(f'{self.name}, вот поле врага:')
        field_seamap.print_map(field_seamap.empty_coordinates)
        # Он выбирает координату для выстрела:
        fire_coord = input(f'{self.name}, куда будете стрелять: ')
        # Проверка, что координата присутствует на поле и что по ней еще не стреляли:
        while fire_coord not in list(enemy_seamap.game_coordinates.keys()) \
                or enemy_seamap.game_coordinates[fire_coord] == 'o' \
                or enemy_seamap.game_coordinates[fire_coord] == 'x':
            print('Сюда нельзя! Повторите попытку!\n')
            fire_coord = input(f'{self.name}, куда будете стрелять: ')
        # Если там корабль, то попали, если нет корабля, то мимо:
        if enemy_seamap.game_coordinates[fire_coord] == 's':
            print('Попал!')
            return True, fire_coord
        elif enemy_seamap.game_coordinates[fire_coord] == '~':
            print('Мимо!')
            return False, fire_coord


class SeaMap:
    def __init__(self, player):
        self.player = player
        self.empty_coordinates = dict()
        self.filled_coordinates = dict()
        self.game_coordinates = dict()
        self.enemy_coordinates = dict()

    # Создание пустых координат:
    def set_map_coord(self):
        coord_x = [chr(j) for j in range(ord('a'), ord('k'))]
        for i in range(len(coord_x)):
            for j in range(1, 11):
                self.empty_coordinates[coord_x[i] + str(j)] = '~'
        return self.empty_coordinates

    # Метод для расстановки кораблей:
    def place_ships(self, player):
        print(f'{player.name}, расставляй корабли!')
        self.filled_coordinates = self.empty_coordinates
        access_coords = list(self.filled_coordinates.keys())
        for i in range(1, len(player.ships) + 1):
            length = len(access_coords)
            j = 1
            # Обрезаем доступные координаты, чтобы нельзя было, например, поставить 4-х палубный корабль на поле a8:
            while j < len(access_coords):
                el = access_coords[j]
                if str(12 - player.ships[i - 1]) in str(el):
                    access_coords.remove(el)
                    length -= 1
                j += 1

            start_coord = input(f'Расположите {i}-й {player.ships[i - 1]}-палубный корабль: ')
            # Проверяем координату по обрезанному словарю и по наличию корабля на этом поле:
            while start_coord not in access_coords or self.filled_coordinates[start_coord] == 's':
                print('Сюда нельзя! Повторите попытку!\n')
                start_coord = input(f'Расположите {i}-й {player.ships[i - 1]}-палубный корабль: ')

            # Ставим столько 's', сколько надо в зависимости от длины корабля:
            for _ in range(player.ships[i - 1]):
                self.filled_coordinates[start_coord] = 's'
                start_coord = f'{start_coord[0]}{int(start_coord[1]) + 1}'
        return self.filled_coordinates

    # Проверка координат игроков (оставляем это на их совести):
    def coord_check(self, player):
        answer1 = input(f'{player.name}, на поле всё правильно расставлено? (Да/Нет): ')
        if answer1.lower() == 'да':
            self.game_coordinates = self.filled_coordinates
            self.enemy_coordinates = self.empty_coordinates
        elif answer1.lower() == 'нет':
            self.filled_coordinates = self.set_map_coord()
            self.place_ships(player)
            return self.coord_check(player)
        return self.game_coordinates, self.enemy_coordinates

    # Проверка, есть ли еще корабли на поле
    def loose_check(self):
        count = 0
        for coord in list(self.game_coordinates):
            if self.game_coordinates[coord] == 's':
                count += 1
                break
        if count == 0:
            print(f'{self.player.name}, вы проиграли!')
            return False
        return True


game()
