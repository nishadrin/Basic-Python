# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

before = int(input("Мин. рандомное значение (от): "))
after = int(input("Макс. рандомное значение (до): "))
range_ = int(input("Введите кол-во цифр в списке: "))

lst_gen = [random.randint(before, after) for _ in range(range_)]

lst_gen = [1, 2, 4, 0]

def square_list(list):
    square = [i**2 for i in list]
    return square

print(square_list(lst_gen))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ["apple", "orange", "banana", "pineapple", "kiwi"]
fruit_list2 = ["orange", "apple", "banana", "kiwi"]

fruit_list3 = [i for i in fruit_list1 for j in fruit_list2 if j == i]

print(fruit_list3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

before = int(input("Мин. рандомное значение (от): "))
after = int(input("Макс. рандомное значение (до): "))
range_ = int(input("Введите кол-во цифр в списке: "))

lst_gen = [random.randint(before, after) for _ in range(range_)]

lst_gen = [1, 2, 4, 6, -25, 12]

newlist = [i for i in lst_gen if i > 0 and i % 3 == 0 and i % 4 != 0]

print(newlist)
