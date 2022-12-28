#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = new_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
    for i in new_list:
        if new_list[idx] == 1:
            new_list[idx] = element
    return new_list
