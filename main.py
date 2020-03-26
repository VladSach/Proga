class EndList:

    def __init__(self, list):
        self.list = list

    def long_word(self):  # находит максимальное
        longest_word = list.index(max(list, key=len))

    def short_word(self):  # находит минимальное
        shortest_word = list.index(min(list, key=len))

    def change_pos(self, longest_word, shortest_word):  # меняет местами
        list[shortest_word], list[longest_word] = list[longest_word], list[shortest_word]

    def __del__(self):
        print('список потерт')


class Line:
    # Инициализирует класс строки, с атрибутом самой этой строки
    def __init__(self, string=''):
        self.line = string

    # Разбивает строку на слова и возвращает массив слов
    def splitting(self):
        return self.line.split()


print("Работу выполнил Саченко Владислав ИП-91 на языке программировании Python")
print("Вариант №22")
print("Заданий рядок слів, які відокремлюються одне від одного будь-якою кількістю пробілів.")
print("Побудувати список відповідних слів. Поміняти місцями найдовше та найкоротше слово цього списку.")
print("Надрукувати початковий і змінений списки.")
print("=================================")


list_first = Line(input('Введите строку: ')).splitting()  # создает массив со словами
print('Начальный список: ', list_first)
list_last = EndList(list_first)
list_last.change_pos(list_last.long_word(), list_last.short_word())
print("Конечный список: ", list_last)
