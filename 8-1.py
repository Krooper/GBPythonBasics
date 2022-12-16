"""
Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент -
который отвечает за основной продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»
"""


def print_soup(soup_lst):
    for soup in soup_lst:
        soup.show_my_soup()


class Soup:
    def __init__(self, product=None):
        self.product = product

    def show_my_soup(self):
        if self.product is None:
            print('Обычный кипяток')
        else:
            print(f'Суп - {self.product}')


PotatoSoup = Soup('картошка')
OnionSoup = Soup('лук')
ChickenSoup = Soup('курица')
SomeSoup = Soup()
soup_list = [PotatoSoup, OnionSoup, ChickenSoup, SomeSoup]

print_soup(soup_list)
