#!/usr/bin/env python3

# -*- coding: utf-8 -*-


# Индивидульное задание №3

def decorator(func):

    def wrapper(*args, **kwargs):
        lists = func(*args, **kwargs)
        list_dict = {}

        for idx in range(len(lists[0])):
            list_dict [lists[0][idx]] = lists[1][idx]
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