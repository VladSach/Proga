class ListNode:
    def __init__(self, key, prev=None, _next=None):
        self.key = key
        self.next = _next
        self.prev = prev

        def __del__(self):
            print('узел удален')


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        new = ListNode(key, _next=self.head)
        if self.head:
            self.head.prev = new
        self.head = new

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev

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

list = Line(input('Введите строку: ')).splitting()  # создает массив со словами
print(list)
i = list.index(min(list, key=len))  # находит минимальное
j = list.index(max(list, key=len))  # находит максимальное
list[i], list[j] = list[j], list[i]  # меняет местами

print(list)
