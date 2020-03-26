class EndList:

    def __init__(self, list):
        self.list = list
        self.longest_word = list.index(max(list, key=len))  # находит максимальное
        self.shortest_word = list.index(min(list, key=len))  # находит минимальное

    def change_pos(self):  # меняет местами
        self.list[self.shortest_word], self.list[self.longest_word] = self.list[self.longest_word], self.list[self.shortest_word]
        return self.list

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
list_last = EndList(list_first).change_pos()
print("Конечный список: ", list_last)

# Вариант без ООП
"""s = input().split()
i = s.index(min(s, key=len))
j = s.index(max(s, key=len))
s[i], s[j] = s[j], s[i]
print(' '.join(s))"""
