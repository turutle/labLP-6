#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Индивидульное задание №3 Вводятся два списка (каждый с новой строки) из слов, записанных через пробел. Имеется
# функция, которая преобразовывает эти две строки в два списка слов и возвращает эти
# списки. Определите декоратор для этой функции, который из этих двух списков
# формирует словарь, в котором ключами являются слова из первого списка, а значениями –
# соответствующие элементы из второго списка. Полученный словарь
# должен возвращаться при вызове декоратора. Примените декоратор к первой функции и
# вызовите ее. Результат (словарь) отобразите на экране.

def decorator(func):

    def wrapper(*args, **kwargs):
        lists = func(*args, **kwargs)
        list_dict = dict( zip(lists[0], lists[1]))
        return list_dict
    return wrapper


@decorator
def to_lists(str_1, str_2):
    list_key = list(str_1.split())
    list_val = list(str_2.split())
    return list_key, list_val


if __name__ == "__main__":
    #str_1 = input()
    #str_2 = input()
    str_1 = "key1 key2 key3"
    str_2 = "val1 val2 val3"
    print(to_lists(str_1, str_2))